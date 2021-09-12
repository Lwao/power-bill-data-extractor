# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 12:07:16 2019

@author: Al Arsalat

pip install xlsxwriter
pip install PyPDF2
pip install tkinter

# pyinstaller .\faturas.py
# pyinstaller -c -F -i ./faul.ico ./main.py
# pyinstaller -c -F -i ./sloth.ico ./main.py
# pyinstaller -c -F "./Images/faul.ico" "./Source code/main.py"
# pyinstaller -c -F "./Images/faul.ico" "./Source code/main.py" --specpath "./Build/" -n PBDE.exe
"""

# importing required modules
#%%
import PyPDF2
import xlsxwriter
import tkinter as tk
from tkinter import filedialog

from init_row_data import init_row_data
from compute_B import compute_B
from compute_A import compute_Ap1, compute_Ap2
from read_page import read_page

# console interface 
#%
print("Power bills data extractor\nver.: 1.1.2, 17/09/2020\nAuthor: Al Arsalat")
input("Press ENTER to begin...")
print("\nProcessing...")
# load files paths
#%
root = tk.Tk()
root.withdraw()
root.call('wm', 'attributes', '.', '-topmost', True)
files = filedialog.askopenfilename(multiple=False) # True to load multiple files
var = root.tk.splitlist(files)
filePaths = []
for f in var:
    filePaths.append(f)
#filePaths

# creating a pdf file object
#%
wdFormatPDF = 17
pdfFileObj = []
pdfReader = []
num_pages = 0
temp_path = ''
for i in range(len(filePaths)):
    temp_path = temp_path + filePaths[i] + " "
temp_path = temp_path[:len(temp_path)-1]
filePaths = [temp_path]
for i in range(len(filePaths)):
    pdfFileObj.append(open(filePaths[i], 'rb'))
    pdfReader.append(PyPDF2.PdfFileReader(pdfFileObj[i]))
    num_pages = num_pages + pdfReader[i].getNumPages()

# creating .xlsx object
#%
findPath = files[len(files)::-1]
findPath = findPath[findPath.find("/"):]
findPath = findPath[len(findPath)::-1]
workbook = xlsxwriter.Workbook(findPath + 'data.xlsx')
worksheet = workbook.add_worksheet('main')
data_dict = init_row_data()
data_headers = list(data_dict.keys())
for itr in range(len(data_headers)): worksheet.write(0, itr, data_headers[itr])

# set loop variables
#%
row = 1
actualPage = 0

# algorithm loop
#%%

while (actualPage<num_pages):
    [text,lines] = read_page(pdfReader,actualPage)

    try:
        ##########################################
        ##########################################
        ##########################################
        ##########################################
        ##########################################
        if(text.find("CLASSIFICAÇÃOB3")>0):
            data = init_row_data()
            data['Classificação'] = 'B3'
            data = compute_B(lines,text,data)
            for i in range(len(list(data))): worksheet.write(row, i, data[list(data)[i]])
            row += 1
            actualPage+=1
        ##########################################
        ##########################################
        ##########################################
        ##########################################
        ##########################################
        if(text.find("CLASSIFICAÇÃOA3")>0):
            data = init_row_data()
            data['Classificação'] = 'A3'
            data = compute_Ap1(lines,text,data)
            # next page           
            [text,lines] = read_page(pdfReader,actualPage+1)
            data = compute_Ap2(lines,text,data)
            for i in range(len(list(data))): worksheet.write(row, i, data[list(data)[i]])
            row += 1
            actualPage+=3
        ##########################################
        ##########################################
        ##########################################
        ##########################################
        ##########################################
        if(text.find("CLASSIFICAÇÃOA4")>0 and text.find("Azul")>0):
            data = init_row_data()
            data['Classificação'] = 'A4A'
            data = compute_Ap1(lines,text,data)
            # next page           
            [text,lines] = read_page(pdfReader,actualPage+1)
            data = compute_Ap2(lines,text,data)
            for i in range(len(list(data))): worksheet.write(row, i, data[list(data)[i]])
            row += 1
            actualPage+=3
        ##########################################
        ##########################################
        ##########################################
        ##########################################
        ##########################################
    
        if(text.find("CLASSIFICAÇÃOA4")>0 and text.find("Verde")>0):
            data = init_row_data()
            data['Classificação'] = 'A4A'
            data = compute_Ap1(lines,text,data)
            # next page           
            [text,lines] = read_page(pdfReader,actualPage+1)
            data = compute_Ap2(lines,text,data)
            for i in range(len(list(data))): worksheet.write(row, i, data[list(data)[i]])
            row += 1
            actualPage+=3
        ##########################################
        ##########################################
        ##########################################
        ##########################################
        ##########################################
    
        if(not ((text.find("CLASSIFICAÇÃOB3")>0) or (text.find("CLASSIFICAÇÃOA3")>0) or (text.find("CLASSIFICAÇÃOA4")>0 and text.find("Verde")>0) or (text.find("CLASSIFICAÇÃOA4")>0 and text.find("Verde")>0))): actualPage+=1
    except:
        print(data['Conta contrato'] + " bill was not correctly identified")
        actualPage+=1

# close files and end routine
#%
workbook.close()
for i in range(len(filePaths)):
    pdfFileObj[i].close()
# console interface
#$
print("\ndata.xlsx file has been successfully saved!")
input("Press ENTER to finish...")