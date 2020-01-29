import time
import json
from program_execution_module import ProgramExecutionModule
from constraint_generation_module import ConstraintGenerationModule

GLOBAL_KEY = 'DatiConCadenzaMensileInfortuni'

# load all data from file
def read_dataset(input_file):
    R = []
    with open(input_file, 'r') as f:
        for d in json.load(f):
            for t in d[GLOBAL_KEY]:
                R += [t]
    return R


# print a single tuple in a more readable way
def pretty_print_tuple(t):
    for k, v in t.items():
        print('- {}:\t{}'.format(k, v))
    print('')


# write the results on file
def json_dump(output_file, rows):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({GLOBAL_KEY: rows}, f, ensure_ascii=False, indent=4)


# driver function of the program
def main():
    # cli parameters:
    #   - value of k
    #   - input/output file [SMALL|MEDIUM|BIG]
    #   - type of algorithm

    t_start = time.time()
    
    input_file = 'datasets/inail_medium.json'
    output_file = 'datasets/anon_inail.json'
    R = read_dataset(input_file)
    k = 4
    algorithm = 'P-T'
    no_pf = ['Genere', 'Deceduto', 'ModalitaAccadimento', \
             'ConSenzaMezzoTrasporto', 'LuogoAccadimento', \
             'GestioneTariffaria']

    print('--- {} ---\n'.format('K-B Anonimity module'))

    print('{*} Number of Initial Tuples\t\t--\t', len(R), sep='')
    PCBuckets = ProgramExecutionModule(R, k)
    
    R1 = ConstraintGenerationModule(PCBuckets, algorithm, no_pf)
    print('{*} Tuple Released\t\t\t--\t', len(R1), sep='')
    print('{*} Path Coverage\t\t\t--\t', '{0:.5g}'.format(len(R1) / len(PCBuckets) * 100), '%', sep='')
    json_dump(output_file, R1)
    
    t_end = time.time()
    print('{*} Overall Execution Time\t\t--\t', t_end - t_start, ' s', sep='')
    

if __name__ == '__main__':
    main()
