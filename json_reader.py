#!/usr/bin/python3
import json

OUTPUT_FILES = ['datasets/inail_small.json', 'datasets/inail_medium.json', 'datasets/inail_big.json']
INPUT_FILES = ['datasets/inail_small_orig.json', 'datasets/inail_medium_orig.json', 'datasets/inail_big_orig.json']

belfiore_mapping = dict()
gestioni_mapping = dict()


def split_date(t, param):
    data_array = [i for i in t[param].split('/')]
    t[param] = int(data_array[2]+data_array[1]+data_array[0])


def mapping_ateco(t, param):
    if t[param] == 'ND':
        t[param] = {'Macro': -1, 'Micro': -1}
        return

    ateco_array = t[param].split(' ')
    t[param] = {'Macro': ord(ateco_array[0]) - ord('A'), 'Micro': int(ateco_array[1])}


def mapping2int(t, param, d):
    if t[param] in d:
        t[param] = d[t[param]]
    else:
        if t[param] == 'ND':
            print(t)
        i = -1 if t[param] == 'ND' else len(d)
        d[t[param]] = i
        t[param] = i


def print_legenda(d, out_file, header):    
    with open(out_file, 'w') as f:
        f.write('***** {} ******\n'.format(header))
        for k, v in d.items():
            f.write('{}:\t{}\n'.format(k, v))

#########
# START #
#########
file_idx = 0
for INPUT_FILE in INPUT_FILES:
    with open(INPUT_FILE, 'r') as f:
        json_arr = json.load(f)
        for js in json_arr:
            for t in js['DatiConCadenzaMensileInfortuni']:
                # DataRilevazione
                del t['DataRilevazione']

                # DataProtocollo
                split_date(t, 'DataProtocollo')
                    
                # DataAccadimento
                split_date(t, 'DataAccadimento') 
                    
                # DataMorte
                t['Deceduto'] = 0 if t['DataMorte'] == None else 1
                del t['DataMorte']

                # LuogoAccadimento
                t['LuogoAccadimento'] = int(t['LuogoAccadimento'])

                # IdentificativoInfortunato
                del t['IdentificativoInfortunato']

                # Genere
                t['Genere'] = 0 if t['Genere'] == 'M' else 1

                # Eta
                t['Eta'] = int(t['Eta'])	

                # LuogoNascita
                mapping2int(t, 'LuogoNascita', belfiore_mapping)

                # ModalitaAccadimento
                t['ModalitaAccadimento'] = 0 if t['ModalitaAccadimento'] == 'N' else 1
                    
                # ConSenzaMezzoTrasporto
                t['ConSenzaMezzoTrasporto'] = 0 if t['ConSenzaMezzoTrasporto'] == 'N' else 1

                # IdentificativoCaso
                del t['IdentificativoCaso']

                # IdentificativoDatoreLavoro
                del t['IdentificativoDatoreLavoro']

                # PosizioneAssicurativaTerritoriale
                del t['PosizioneAssicurativaTerritoriale']

                # SettoreAttivitaEconomica
                mapping_ateco(t, 'SettoreAttivitaEconomica')

                # Gestione
                mapping2int(t, 'Gestione', gestioni_mapping)

                # GestioneTariffaria
                t['GestioneTariffaria'] = -1 if t['GestioneTariffaria'] == 'ND' else int(t['GestioneTariffaria'])
                
                # GrandeGruppoTariffario
                t['GrandeGruppoTariffario'] = -1 if t['GrandeGruppoTariffario'] == 'ND' else int(t['GrandeGruppoTariffario'])

                # Regione
                del t['Regione'] # only ligurian accidents

            with open(OUTPUT_FILES[file_idx], 'w', encoding='utf-8') as f:
                json.dump(json_arr, f, ensure_ascii=False, indent=4)
    file_idx += 1

# print the legendas of dictionaries
print_legenda(belfiore_mapping, 'mappings/belfiore.txt', 'Legenda Indice Belfiore')
print_legenda(gestioni_mapping, 'mappings/gestioni.txt', 'Legenda Gestioni')
