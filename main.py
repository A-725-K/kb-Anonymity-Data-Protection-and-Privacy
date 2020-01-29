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


def json_dump(output_file, rows):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({GLOBAL_KEY: rows}, f, ensure_ascii=False, indent=4)


def main():
    # cli parameters:
    #   - value of k
    #   - input/output file [SMALL|MEDIUM|BIG]
    #   - type of algorithm

    input_file = 'datasets/inail_medium.json'
    output_file = 'datasets/anon_inail.json'
    R = read_dataset(input_file)
    k = 4
    algorithm = 'P-T'
    no_pf = ['Genere', 'Deceduto', 'ModalitaAccadimento', \
             'ConSenzaMezzoTrasporto', 'LuogoAccadimento', \
             'GestioneTariffaria']

    print('--- {} ---\n'.format('K-B Anonimity module'))

    print('{*} Number of initial tuples\t\t--\t', len(R), sep='')
    PCBuckets = ProgramExecutionModule(R, k)
    
    R1 = ConstraintGenerationModule(PCBuckets, algorithm, no_pf)
    print('{*} Path coverage\t\t\t--\t', '{0:.5g}'.format(len(R1) / len(PCBuckets) * 100), '%', sep='')
    json_dump(output_file, R1)
    

if __name__ == '__main__':
    main()
