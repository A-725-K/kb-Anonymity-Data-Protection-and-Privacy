#!/usr/bin/python3
import json

belfiore_mapping = dict()
ateco_mapping = dict()
gestioni_mapping = dict()

with open('inail_small.json', 'r') as f:
    json_struct = json.load(f)

for t in json_struct['DatiConCadenzaMensileInfortuni']:

	#DataRilevazione
	del t['DataRilevazione']

	#DataProtocollo
	data_array = [int(i) for i in t['DataProtocollo'].split('/')]
	t['DataProtocollo'] = {'Day':data_array[0], 'May':data_array[1],'Year':data_array[2]}
	
	#DataAccadimento
	data_array = [int(i) for i in t['DataAccadimento'].split('/')]
	t['DataAccadimento'] = {'Day':data_array[0], 'May':data_array[1],'Year':data_array[2]}

	#DataMorte
	t['DataMorte'] = 0 if t['DataMorte']==None else 1

	#LuogoAccadimento
	t['LuogoAccadimento'] = int(t['LuogoAccadimento'])

	#IdentificativoInfortunato
	del t['IdentificativoInfortunato']

	#Genere
	t['Genere'] = 0 if t['Genere']=='M' else 1

	#Eta
	t['Eta'] = int(t['Eta'])	

	#LuogoNascita
	if t['LuogoNascita'] in belfiore_mapping:
		t['LuogoNascita'] = belfiore_mapping[t['LuogoNascita']]
	else:
		i = len(belfiore_mapping)
		#print(t['LuogoNascita'], i)			#leggenda
		belfiore_mapping[t['LuogoNascita']] = i
		t['LuogoNascita'] = i

	#ModalitaAccadimento
	t['ModalitaAccadimento'] = 0 if t['ModalitaAccadimento']=='N' else 1
		
	#ConSenzaMezzoTrasporto
	t['ConSenzaMezzoTrasporto'] = 0 if t['ConSenzaMezzoTrasporto']=='N' else 1

	#IdentificativoCaso
	del t['IdentificativoCaso']

	#IdentificativoDatoreLavoro
	del t['IdentificativoDatoreLavoro']

	#PosizioneAssicurativaTerritoriale
	del t['PosizioneAssicurativaTerritoriale']

	#SettoreAttivitaEconomica
	if t['SettoreAttivitaEconomica'] in ateco_mapping:
		t['SettoreAttivitaEconomica'] = ateco_mapping[t['SettoreAttivitaEconomica']]
	else:
		i = len(ateco_mapping)
		#print(t['SettoreAttivitaEconomica'], i)			#leggenda
		ateco_mapping[t['SettoreAttivitaEconomica']] = i
		t['SettoreAttivitaEconomica'] = i

	#Gestione
	if t['Gestione'] in gestioni_mapping:
		t['Gestione'] = gestioni_mapping[t['Gestione']]
	else:
		i = len(gestioni_mapping)
		#print(t['Gestione'], i)			#leggenda
		gestioni_mapping[t['Gestione']] = i
		t['Gestione'] = i

	#GestioneTariffaria
	t['GestioneTariffaria'] = -1 if t['GestioneTariffaria']=='ND' else int(t['GestioneTariffaria'])

	#GrandeGruppoTariffario
	t['GrandeGruppoTariffario'] = -1 if t['GrandeGruppoTariffario']=='ND' else int(t['GrandeGruppoTariffario'])

	#Regione
	t['Regione'] = int(t['Regione'])	
	print(t)

with open('out.json', 'w', encoding='utf-8') as f:
	json.dump(json_struct, f, ensure_ascii=False, indent=4)
