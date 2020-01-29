#!/usr/bin/python3

def P_test(t, pc):
    test_1(t, pc)
    test_2(t, pc)
    test_3(t, pc)
    test_4(t, pc)

##########
# TEST 1 #
##########

def test_1(t, pc):      
    #LUOGO NASCITA
    if t['LuogoNascita'] == 0:
        pc += [('LuogoNascita', '==', 0)]
        #DATA ACCADIMENTO
        if 20191001 <= t['DataAccadimento'] <= 20191031:
            pc += [('DataAccadimento', '<=', 20191031)]
            pc += [('DataAccadimento', '>=', 20191001)]
        
        elif 20191101 <= t['DataAccadimento'] <= 20191130:
            pc += [('DataAccadimento', '<=', 20191130)]
            pc += [('DataAccadimento', '>=', 20191101)]

        else:
            pc += [('DataAccadimento', '<=', 20191231)]
            pc += [('DataAccadimento', '>=', 20191201)]

        #GENERE
        if t['Genere'] == 0:
            pc += [('Genere', '==', 0)]

        else:
            pc += [('Genere', '==', 1)]
            
        #DECEDUTO 
        if t['Deceduto'] == 0:
            pc += [('Deceduto', '==', 0)]

        else:
            pc += [('Deceduto', '==', 1)]	

    else:
        pc += [('LuogoNascita', '!=', 0)]


##########
# TEST 2 #
##########

def test_2(t, pc):
    #SETTORE ATTIVITA' ECONOMICA MACRO
    if t['SettoreAttivitaEconomica_Macro'] == 2:
        pc += [('SettoreAttivitaEconomica_Macro', '==', 2)]

        #GESTIONE
        if t['Gestione'] == 0:
            pc += [('Gestione', '==', 0)]

        elif t['Gestione'] == 1:
            pc += [('Gestione', '==', 1)]

        else:
            pc += [('Gestione', '==', 2)]

    else:
        pc += [('SettoreAttivitaEconomica_Macro', '!=', 2)]


##########
# TEST 3 #
##########

def test_3(t, pc):
    #ETA
    if t['Eta'] <= 30:
        pc += [('Eta', '<=', 30)]

    elif  t['Eta'] > 30 and t['Eta'] <= 45:
        pc += [('Eta', '>', 30)]
        pc += [('Eta', '<=', 45)]

    else:
        pc += [('Eta', '>', 45)]

    #MODALITA ACCADIMENTO
    if t['ModalitaAccadimento'] == 0:
        pc += [('ModalitaAccadimento', '==', 0)]

        #CON SENZA MEZZO DI TRASPORTO
        if t['ConSenzaMezzoTrasporto'] == 0:
            pc += [('ConSenzaMezzoTrasporto', '==', 0)]
        
        else:
            pc += [('ConSenzaMezzoTrasporto', '==', 1)]

    else:
        pc += [('ModalitaAccadimento', '==', 1)]


##########
# TEST 4 #
##########

def test_4(t, pc):      
    #DATA PROTOCOLLO
    if 20191201 <= t['DataProtocollo'] <= 20191231:		
        pc += [('DataProtocollo', '<=', 20191231)]
        pc += [('DataProtocollo', '>=', 20191201)]
        
        #GRANDE GRUPPO TARIFFARIO
        if t['GrandeGruppoTariffario'] == 4:
            pc += [('GrandeGruppoTariffario', '==', 4)]

        elif t['GrandeGruppoTariffario'] == 6:
            pc += [('GrandeGruppoTariffario', '==', 6)]

        elif t['GrandeGruppoTariffario'] == 8:
            pc += [('GrandeGruppoTariffario', '==', 8)]

        elif t['GrandeGruppoTariffario'] == 9:
            pc += [('GrandeGruppoTariffario', '==', 9)]

        else:
            pc += [('GrandeGruppoTariffario', '!=', 4)]
            pc += [('GrandeGruppoTariffario', '!=', 6)]
            pc += [('GrandeGruppoTariffario', '!=', 8)]
            pc += [('GrandeGruppoTariffario', '!=', 9)]

    else:
        pc += [('DataProtocollo', '<', 20191201)]
	
