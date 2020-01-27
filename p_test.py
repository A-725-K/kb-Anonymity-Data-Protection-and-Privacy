#!/usr/bin/python3

def P_test(t, pc):
	
	##########
	# TEST 1 #
	##########
	
	#LUOGO NASCITA
	if t['LuogoNascita'] == -1:
		pc += [('LuogoNascita', '==', -1)]

	elif t['LuogoNascita'] != 0:
		pc += [('LuogoNascita', '!=', 0)]

		#DATA ACCADIMENTO
		if t['DataAccadimento']['Month'] == 10:
			pc += [('DataAccadimento_Month', '==', 10)]

		elif t['DataAccadimento']['Month'] == 11:
			pc += [('DataAccadimento_Month', '==', 11)]

		else:
			pc += [('DataAccadimento_Month', '==', 12)]

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
		pc += [('LuogoNascita', '==', 0)]

	##########
	# TEST 2 #
	##########

	#SETTORE ATTIVITA' ECONOMICA MACRO
	if t['SettoreAttivitaEconomica']['Macro'] == 2:
		pc += [('SettoreAttivitaEconomica_Macro', '==', 2)]

		#GESTIONE
		if t['Gestione'] == 0:
			pc += [('Gestione', '==', 0)]
		elif t['Gestione'] == 1:
			pc += [('Gestione', '==', 1)]
		else
			pc += [('Gestione', '==', 2)]

	else:
		pc += [('SettoreAttivitaEconomica_Macro', '!=', 2)]
	
	##########
	# TEST 3 #
	##########

	#ETA
	if t['Eta'] <= 30:
			pc += [('Eta', '<=', 30)]

	elif  t['Eta'] > 30 and t['DataAccadimento']['Month'] <= 45:
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
	
	#DATA PROTOCOLLO
	if t['DataProtocollo']['Month'] == 12:		
		pc += [('DataProtocollo_Month', '==', 12)
		#GRANDE GRUPPO TARIFFARIO
		if t['GrandeGruppoTariffario'] == 4:
			pc += [('GrandeGruppoTariffario', '==', 4)
		elif t['GrandeGruppoTariffario'] == 6:
			pc += [('GrandeGruppoTariffario', '==', 6)
		elif t['GrandeGruppoTariffario'] == 8:
			pc += [('GrandeGruppoTariffario', '==', 8)
		elif t['GrandeGruppoTariffario'] == 9:
			pc += [('GrandeGruppoTariffario', '==', 9)
		else
			pc += [('GrandeGruppoTariffario', '!=', 4)
			pc += [('GrandeGruppoTariffario', '!=', 6)
			pc += [('GrandeGruppoTariffario', '!=', 8)
			pc += [('GrandeGruppoTariffario', '!=', 9)
	else:
		pc += [('DataProtocollo_Month', '!=', 12)
	
		

	

	



