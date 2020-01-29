import json
from program_execution_module import ProgramExecutionModule
from constraint_generation_module import ConstraintGenerationModule
GLOBAL_KEY = 'DatiConCadenzaMensileInfortuni'


def read_dataset(input_file):
    R = []
    with open(input_file, 'r') as f:
        for d in json.load(f):
            for t in d[GLOBAL_KEY]:
                R += [t]
    return R


def pretty_print_tuple(t):
    for k, v in t.items():
        print('- {}:\t{}'.format(k, v))
    print('')

def json_dump(rows):
    with open('inail_anon.json', 'w', encoding='utf-8') as f:
        json.dump({"DatiConCadenzaMensileInfortuni":rows}, f, ensure_ascii=False, indent=4)

def main():
    # cli parameters:
    #   - value of k
    #   - input file [SMALL|MEDIUM|BIG]
    #   - type of algorithm

    input_file = 'datasets/inail_big.json'
    R = read_dataset(input_file)
    k = 1
    no_pf = ['Genere', 'Deceduto', 'ModalitaAccadimento', \
             'ConSenzaMezzoTrasporto', 'LuogoAccadimento', \
             'GestioneTariffaria']

    print('The dataset contains', len(R), 'tuples')
    PCBuckets = ProgramExecutionModule(R, k)
    
    R1 = ConstraintGenerationModule(PCBuckets, 'P-T', no_pf)
    print(len(PCBuckets))
    print(len(R1))
    print('Path coverage:', len(R1)/len(PCBuckets)*100, '%')
    json_dump(R1)
    

if __name__ == '__main__':
    main()
