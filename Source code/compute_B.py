#from compute_B3 import *
def compute_B(lines, text, data):
    flag_B3_1 = True
    flag_B3_2 = True
    flag_counter = 0
    flag_counter_day = 0
    zero = False
    
    flags = {'VERDE':text.find('BANDEIRA VERDE'), 'AMARELA':text.find('BANDEIRA AMARELA'), 'VERMELHA':text.find('BANDEIRA VERMELHA')}
    for itr in flags:
        if flags[itr]<0: flag_counter+=1   
        if flag_counter == len(flags): zero = True
    flags = {k: v for k, v in sorted(flags.items(), key=lambda item: item[1])}
    keys_reverse = list(flags.keys())
    keys_direct = list(flags.keys())
    keys_reverse.reverse()
    
    data['Classificação'] = 'B3'
    
    for i in range(len(lines)):
        if(lines[i].find("DATA DA EMISSÃO DA NOTA FISCAL")+1): 
            data['Conta contrato']  = lines[i][lines[i].find('CONTA CONTRATO')+len('CONTA CONTRATO'):lines[i].find('Nº')]
            data['Valor da fatura (R$)'] = float(lines[i][lines[i].find('(R$)')+len('(R$)'):lines[i].find('DATA DA EMI')].replace(".","").replace(",","."))
            data['Data de leitura'] = lines[i][lines[i].find('DATA DA EMISSÃO DA NOTA FISCAL')+len('DATA DA EMISSÃO DA NOTA FISCAL'):lines[i].find('DATA DA APRESENTAÇÃO')]
        if(zero): data['Dias bandeira VERDE'] = 31
        if(lines[i].find("CAT")+1 and not zero):
            try:
                aux = lines[i+1].replace(".","").replace(",",".").split()
                data['Dias bandeira ' + keys_reverse[flag_counter_day]] = int(aux[0])
            except:
                aux = lines[i].replace(".","").replace(",",".").split()
                data['Dias bandeira ' + keys_reverse[flag_counter_day]] = int(aux[len(aux)-1])
                
            flag_counter_day+=1
        if(lines[i].find("Consumo Ativo(kWh)-TE")+1 and not zero and flag_counter<len(flags)):
            aux = lines[i+1].replace(".","").replace(",",".").split()
            data[keys_direct[flag_counter] + ' Consumo ativo (kWh)'] = float(aux[0])
            data[keys_direct[flag_counter] + ' Despesa consumo ativo (R$)'] = float(aux[2])
            flag_counter +=1
        if(lines[i].find("Consumo Ativo(kWh)-TUSD")+1):
            if(flag_B3_1==True):
                #aux = lines[i+1][:lines[i+1].find('0 ')].replace(".","").replace(",",".")
                aux = lines[i+1].replace(".","").replace(",",".").split()
                data['Consumo ativo (kWh)'] = float(aux[0])
                data['Despesa consumo ativo (R$)'] = float(aux[2])
                flag_B3_1 = False
        if(lines[i].find("Federal")+1): data['Tributo (R$)']  = float(lines[i+1][:lines[i+1].find('- ')].replace(".","").replace(",","."))
        #if(lines[i].find("TOTAL A PAGAR(R$)")+1): data['Valor da fatura (R$)']  = float(lines[i][lines[i].find('(R$)')+4:lines[i].find('VE')].replace(".","").replace(",","."))
        #if(lines[i].find("TOTAL A PAGAR")+1): data['Valor da fatura (R$)'] = float(lines[i][lines[i].find('(R$)')+len('(R$)'):lines[i].find('DATA DA EMI')].replace(".","").replace(",","."))
        if(lines[i].find("Excedente(kVARh)")+1):
            if(flag_B3_2):
                aux = lines[i+1].replace(".","").replace(",",".").split()
                data['Consumo reativo excedente (kvarh)'] = float(aux[0])
                data['Despesa consumo reativo excedente (R$)'] = float(aux[2])
                flag_B3_2 = False
    if(data['Dias bandeira VERDE']==-1): data['Dias bandeira VERDE']=0
    if(data['Dias bandeira VERMELHA']==-1): data['Dias bandeira VERMELHA']=0
    if(data['Dias bandeira AMARELA']==-1): data['Dias bandeira AMARELA']=0
    return data