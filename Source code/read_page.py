#from read_page import *
def read_page(pdfReader,actualPage):
    # transcribe .pdf text to variable
    pageObj = pdfReader[0].getPage(actualPage)  #always read from the first file
    text = pageObj.extractText()
    disp_text = text
    lines = ['dont', 'panic']

    # convert str into list based in break points
    # continues while disp_text it's not empty and when lines receive repeted str
    while(len(disp_text)>0 and lines[len(lines)-1]!=lines[len(lines)-2]):
        lines.append(disp_text[:disp_text.find('\n')])
        disp_text = disp_text[disp_text.find('\n')+1:]
    lines = lines[2:len(lines)]
    
    return text, lines
