#from compute_A import *
def compute_Ap1(lines, text, data):
    flag_A3_1 = True
    flag_A3_2 = True
    flag_A3_3 = True
    flag_A3_4 = True
    flag_A3_5 = True
    flag_A3_6 = True
    flag_A3_7 = True
    flag_A3_8 = True
    flag_A3_9 = True
    flag_A3_10 = True
    
    flag_A4_1 = True
    flag_A4_2 = True
    flag_A4_3 = True
    
    flag_counter = 0
    zero = False
    
    flags = {'VERDE':text.find('BANDEIRA VERDE'), 'AMARELA':text.find('BANDEIRA AMARELA'), 'VERMELHA':text.find('BANDEIRA VERMELHA')}
    for itr in flags:
        if flags[itr]<0: flag_counter+=1   
        if flag_counter == len(flags): zero = True
    flags = {k: v for k, v in sorted(flags.items(), key=lambda item: item[1])}
    keys_reverse = list(flags.keys())
    keys_direct = list(flags.keys())
    keys_reverse.reverse()
    
    flag_counter_cons_FP = flag_counter
    flag_counter_cons_NP = flag_counter
    
    for i in range(len(lines)):
        if(lines[i].find("DATA DA EMISSÃO DA NOTA FISCAL")+1): 
            data['Conta contrato']  = lines[i][lines[i].find('CONTA CONTRATO')+len('CONTA CONTRATO'):lines[i].find('Nº')]
            data['Valor da fatura (R$)'] = float(lines[i][lines[i].find('(R$)')+len('(R$)'):lines[i].find('DATA DA EMI')].replace(".","").replace(",","."))
            data['Data de leitura'] = lines[i][lines[i].find('DATA DA EMISSÃO DA NOTA FISCAL')+len('DATA DA EMISSÃO DA NOTA FISCAL'):lines[i].find('DATA DA APRESENTAÇÃO')]
        #if(lines[i].find("TOTAL A PAGAR")+1): data['Valor da fatura (R$)'] = float(lines[i][lines[i].find('(R$)')+len('(R$)'):lines[i].find(' DATA')].replace(".","").replace(",","."))
        #if(lines[i].find("TOTAL A PAGAR")+1): data['Valor da fatura (R$)'] = float(lines[i][lines[i].find('(R$)')+len('(R$)'):lines[i].find('DATA DA EMI')].replace(".","").replace(",","."))
        if(lines[i].find("Tributo Federal")+1): data['Tributo (R$)'] = float(lines[i][lines[i].find('Tributo Federal ')+16:lines[i].find('-')].replace(".","").replace(",","."))
        if(lines[i].find("Demanda Ultrapassagem Fora de Ponta(kW)")+1):
            if(flag_A3_1):
                aux = lines[i].replace(".","").replace(",",".").split()
                data['Despesa demanda ultrapassagem FP (R$)'] = float(aux[len(aux)-1])
                data['Demanda ultrapassagem FP (kW)'] = float(aux[len(aux)-3])
                flag_A3_1 = False
        if(lines[i].find("Demanda Ultrapassagem Na Ponta(kW)")+1): ########## not tested 
            if(flag_A3_2):
                aux = lines[i].replace(".","").replace(",",".").split()
                data['Despesa demanda ultrapassagem NP (R$)'] = float(aux[len(aux)-1])
                data['Demanda ultrapassagem NP (kW)'] = float(aux[len(aux)-3])
                flag_A3_2 = False
        if(lines[i].find("Demanda Reativa Exc. Na Ponta(kVAR)")+1):  
            if(flag_A3_3):
                aux = lines[i].replace(".","").replace(",",".").split()
                data['Despesa demanda reativa excedente NP (R$)'] = float(aux[len(aux)-1])
                data['Demanda reativa excedente NP (kvar)'] = float(aux[len(aux)-3])
                flag_A3_3 = False
        if(lines[i].find("Demanda Reativa Exc. Fora de Ponta(kVAR)")+1):  
            if(flag_A3_4):
                aux = lines[i].replace(".","").replace(",",".").split()
                data['Despesa demanda reativa excedente FP (R$)'] = float(aux[len(aux)-1])
                data['Demanda reativa excedente FP (kvar)'] = float(aux[len(aux)-3])
                flag_A3_4 = False        
        if(lines[i].find("Consumo Ativo Na Ponta(kWh)-TUSD")+1):
            if(flag_A3_5):
                aux = lines[i].replace(".","").replace(",",".").split()
                data['Despesa consumo ativo NP (R$)'] = float(aux[len(aux)-1])
                data['Consumo ativo NP (kWh)'] = float(aux[len(aux)-3])
                flag_A3_5 = False   
        if(lines[i].find("Consumo Ativo Fora de Ponta(kWh)-TUSD")+1):
            if(flag_A3_6):
                aux = lines[i].replace(".","").replace(",",".").split()
                data['Despesa consumo ativo FP (R$)'] = float(aux[len(aux)-1])
                data['Consumo ativo FP (kWh)'] = float(aux[len(aux)-3])
                flag_A3_6 = False 
        if(lines[i].find("Consumo Reativo Exc. Na Ponta(kVARh)")+1):
            if(flag_A3_7):
                aux = lines[i].replace(".","").replace(",",".").split()
                data['Despesa consumo reativo excedente NP (R$)'] = float(aux[len(aux)-1])
                #data['Consumo reativo excedente NP (kvarh)'] = float(aux[len(aux)-3])
                flag_A3_7 = False 
        if(lines[i].find("Consumo Reativo Exc. Fora Ponta(kVARh)")+1):
            if(flag_A3_8):
                aux = lines[i].replace(".","").replace(",",".").split()
                data['Despesa consumo reativo excedente FP (R$)'] = float(aux[len(aux)-1])
                #data['Consumo reativo excedente FP (kvarh)'] = float(aux[len(aux)-3])
                flag_A3_8 = False 
        # new
        if(lines[i].find("Demanda Ativa Na Ponta(kW)")+1):
            if(flag_A3_9):
                aux = lines[i].replace(".","").replace(",",".").split()
                data['Despesa demanda ativa NP (R$)'] = float(aux[len(aux)-1])
                data['Demanda ativa NP (kW)'] = float(aux[len(aux)-3])
                flag_A3_9 = False
        if(lines[i].find("Demanda Ativa Fora de Ponta(kW)")+1):
            if(flag_A3_10):
                aux = lines[i].replace(".","").replace(",",".").split()
                data['Despesa demanda ativa FP (R$)'] = float(aux[len(aux)-1])
                data['Demanda ativa FP (kW)'] = float(aux[len(aux)-3])
                flag_A3_10 = False
        # new
        if(lines[i].find("Consumo Ativo Na Ponta(kWh)-TE ")+1 and not zero and flag_counter_cons_NP<len(flags)):
            aux = lines[i].replace(".","").replace(",",".").split()
            data[keys_direct[flag_counter_cons_NP] + ' Consumo ativo NP (kWh)'] = float(aux[len(aux)-3])
            data[keys_direct[flag_counter_cons_NP] + ' Despesa consumo ativo NP (R$)'] = float(aux[len(aux)-1])
            # indicator for compute_A3p2 to ensure wich are the current flags of the bill
            data['Dias bandeira ' + keys_direct[flag_counter_cons_NP]] = text.find('BANDEIRA ' + keys_direct[flag_counter_cons_NP])
            data['Dias bandeira ' + keys_direct[flag_counter_cons_NP]] = text.find('BANDEIRA ' + keys_direct[flag_counter_cons_NP])
            flag_counter_cons_NP +=1
        if(lines[i].find("Consumo Ativo Fora Ponta(kWh)-TE ")+1 and not zero and flag_counter_cons_FP<len(flags)):
            aux = lines[i].replace(".","").replace(",",".").split()
            data[keys_direct[flag_counter_cons_FP] + ' Consumo ativo FP (kWh)'] = float(aux[len(aux)-3])
            data[keys_direct[flag_counter_cons_FP] + ' Despesa consumo ativo FP (R$)'] = float(aux[len(aux)-1])
            # indicator for compute_A3p2 to ensure wich are the current flags of the bill
            data['Dias bandeira ' + keys_direct[flag_counter_cons_FP]] = text.find('BANDEIRA ' + keys_direct[flag_counter_cons_FP])
            data['Dias bandeira ' + keys_direct[flag_counter_cons_FP]] = text.find('BANDEIRA ' + keys_direct[flag_counter_cons_FP])
            flag_counter_cons_FP +=1
        if(lines[i].find("Demanda Ativa Ultrapassagem(kW)")+1):
            if(flag_A4_1):
                aux = lines[i].replace(".","").replace(",",".").split()
                data['Despesa demanda ultrapassagem (R$)'] = float(aux[len(aux)-1])
                data['Demanda ultrapassagem (kW)'] = float(aux[len(aux)-3])
                flag_A4_1 = False
        if(lines[i].find("Demanda Reativa Excedente.(kVAR)")+1):
            if(flag_A4_2):
                aux = lines[i].replace(".","").replace(",",".").split()
                data['Despesa demanda reativa excedente (R$)'] = float(aux[len(aux)-1])
                data['Demanda reativa excedente (kvar)'] = float(aux[len(aux)-3])
                flag_A4_2 = False
        # new
        if(lines[i].find("Demanda Ativa(kW)")+1):
            if(flag_A4_3):
                aux = lines[i].replace(".","").replace(",",".").split()
                data['Despesa demanda ativa (R$)'] = float(aux[len(aux)-1])
                data['Demanda ativa (kW)'] = float(aux[len(aux)-3])
                flag_A4_3 = False
        # new
    return data

def compute_Ap2(lines, text, data):
    flag_A3_9 = True
    flag_A3_10 = True
    flag_A3_11 = True
    flag_A3_12 = True
    flag_A3_13 = True
    flag_A3_14 = True
    
    flag_counter = 0
    flag_counter_day = 0
    zero = False
    
    flags = {'VERDE':data['Dias bandeira VERDE'], 'AMARELA':data['Dias bandeira AMARELA'], 'VERMELHA':data['Dias bandeira VERMELHA']}
    for itr in flags:
        if flags[itr]<0: flag_counter+=1   
        if flag_counter == len(flags): zero = True
    flags = {k: v for k, v in sorted(flags.items(), key=lambda item: item[1])}
    keys_reverse = list(flags.keys())
    keys_reverse.reverse()
    
    for i in range(len(lines)):
        if(zero): data['Dias bandeira VERDE'] = 31
        if(lines[i].find("Dias -")+1 and not zero):
            aux = lines[i].replace(".","").replace(",",".").split()
            data['Dias bandeira ' + keys_reverse[flag_counter_day]] = int(aux[len(aux)-1])
            flag_counter_day+=1
        if(lines[i].find("Fator de Carga")+1):
            aux = lines[i+1].replace(".","").replace(",",".").split("  ")
            data['Fator de carga NP'] = float(aux[0].split()[len(aux[0].split())-1])
            data['Fator de carga FP'] = float(aux[len(aux)-1].split()[len(aux[len(aux)-1].split())-1])
        if(lines[i].find("Demanda NP:")+1):
            aux = lines[i].replace(",",".").split()
            data['Demanda ativa contratada NP (kW)'] = float(aux[len(aux)-1])
        if(lines[i].find("Demanda FP:")+1):
            aux = lines[i].replace(",",".").split()
            data['Demanda ativa contratada FP (kW)'] = float(aux[len(aux)-1])
        if(lines[i].find("Demanda:")+1):
            aux = lines[i].replace(",",".").split()
            data['Demanda ativa contratada (kW)'] = float(aux[len(aux)-1])
        if(lines[i].find("Demanda Máxima Na Ponta")+1):
            if(flag_A3_9):
                aux = lines[i+1].replace(".","").replace(",",".").split()
                data['Demanda máxima NP (kW)'] = float(aux[len(aux)-1])
                flag_A3_9 = False 
        if(lines[i].find("Demanda Máxima Fora de Ponta")+1):
            if(flag_A3_10):
                aux = lines[i+1].replace(".","").replace(",",".").split()
                data['Demanda máxima FP (kW)'] = float(aux[len(aux)-1])
                flag_A3_10 = False 
        if(lines[i].find("Demanda Máxima Corrigida Na Ponta")+1):
            if(flag_A3_11):
                aux = lines[i+1].replace(".","").replace(",",".").split()
                data['Demanda máxima corrigida NP (kW)'] = float(aux[len(aux)-1])
                flag_A3_11 = False 
        if(lines[i].find("Demanda Máxima Corrigida Fora de Ponta")+1):
            if(flag_A3_12):
                aux = lines[i+1].replace(".","").replace(",",".").split()
                data['Demanda máxima corrigida FP (kW)'] = float(aux[len(aux)-1])
                flag_A3_12 = False 
        if(lines[i].find("Consumo Reativo Na Ponta")+1):
            aux = lines[i+1].replace(".","").replace(",",".").split()
            data['Consumo reativo NP (kvarh)'] += float(aux[len(aux)-1])
        if(lines[i].find("Consumo Reativo Fora de Ponta")+1):
            if(data['Classificação'] == 'A3'):
                if(not flag_A3_13 and flag_A3_14):
                    aux = lines[i+1].replace(".","").replace(",",".").split()
                    data['Consumo reativo FP (kvarh)'] += float(aux[len(aux)-1])
                    flag_A3_14 = False
                if(flag_A3_13 and flag_A3_14):
                    aux = lines[i+1].replace(".","").replace(",",".").split()
                    data['Consumo reativo FP (kvarh)'] += float(aux[len(aux)-1][aux[len(aux)-1].find('0000')+len('0000'):])
                    flag_A3_13 = False
            if(data['Classificação'] == 'A4A' or data['Classificação'] == 'A4V'):
                aux = lines[i+1].replace(".","").replace(",",".").split()
                data['Consumo reativo FP (kvarh)'] += float(aux[len(aux)-1])
        if(lines[i].find("Consumo Reativo Excedente Na Ponta")+1):
            aux = lines[i+1].replace(".","").replace(",",".").split()
            data['Consumo reativo excedente NP (kvarh)'] += float(aux[len(aux)-1])
        if(lines[i].find("Consumo Reativo Excedente Fora de Ponta")+1):
            aux = lines[i+1].replace(".","").replace(",",".").split()
            data['Consumo reativo excedente FP (kvarh)'] += float(aux[len(aux)-1])
    if(data['Dias bandeira VERDE']==-1): data['Dias bandeira VERDE']=0
    if(data['Dias bandeira VERMELHA']==-1): data['Dias bandeira VERMELHA']=0
    if(data['Dias bandeira AMARELA']==-1): data['Dias bandeira AMARELA']=0
    return data