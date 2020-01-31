import time
import json
import argparse
from kb_anonymization import program_execution_module as pem
from kb_anonymization import constraint_generation_module as cgm

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


# check arguments from command line
def check_cli_args():
    # cli parameters:
    #   - value of k
    #   - input/output file [SMALL|MEDIUM|BIG]
    #   - type of algorithm
    #   - range constraint file

    args_parser = argparse.ArgumentParser(description='Implementation of K-B Anonimity to anonymize data for testing purpose')
    required_args = args_parser.add_argument_group('required arguments')
    required_args.add_argument('-i', '--input-file', help='path of json input dataset', required=True)
    required_args.add_argument('-o', '--output-file', help='path of anonymzed dataset', required=True)
    required_args.add_argument('-a', '--algorithm', help='choose one between P-F and P-T', required=True)
    required_args.add_argument('-k', help='degree of anonimity', type=int, required=True)
    required_args.add_argument('-c', '--config-file', help='path of range constraints file', required=True)
    args = args_parser.parse_args()
    return args.input_file, args.output_file, args.k, args.algorithm, args.config_file


# driver function of the program
def main():
    # get algorithm parameters from user
    input_file, output_file, k, algorithm, config_file = check_cli_args()

    t_start = time.time()

    # field to exclude in no-field repeat algorithm
    no_pf = ['Genere', 'Deceduto', 'ModalitaAccadimento', \
             'ConSenzaMezzoTrasporto', 'LuogoAccadimento', \
             'GestioneTariffaria']

    R = read_dataset(input_file)
    print('--- {} ---\n'.format('K-B Anonimity module'))

    print('{*} Number of Initial Tuples\t\t--\t', len(R), sep='')
    PCBuckets, n_paths = pem.ProgramExecutionModule(R, k)
    
    if algorithm == 'P-F':
        R1 = cgm.ConstraintGenerationModule(PCBuckets, algorithm, config_file, no_pf=no_pf)
    elif algorithm == 'P-T':
        R1 = cgm.ConstraintGenerationModule(PCBuckets, algorithm, config_file, field_pt='Eta')
    print('{*} Tuple Released\t\t\t--\t', len(R1), sep='')
    print('{*} Path Coverage\t\t\t--\t', '{0:.5g}'.format(len(R1) / n_paths * 100), '%', sep='')
    json_dump(output_file, R1)
    
    t_end = time.time()
    print('{*} Overall Execution Time\t\t--\t', t_end - t_start, ' s', sep='')
    

if __name__ == '__main__':
    main()
