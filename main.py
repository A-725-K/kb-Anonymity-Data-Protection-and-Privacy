from program_execution_module import ProgramExecutionModule
from constraint_generation_module import ConstraintGenerationModule
GLOBAL_KEY = 'DatiConCadenzaMensileInfortuni'


def read_dataset(input_file):
    import json
    R = []
    with open(input_file, 'r') as f:
        for d in json.load(f):
            for t in d[GLOBAL_KEY]:
                R += [t]
    return R


def pretty_print(t):
    for k, v in t.items():
        print('- {}:\t{}'.format(k, v))
    print('')
    

def main():
    # cli parameters:
    #   - value of k
    #   - input file [SMALL|MEDIUM|BIG]
    #   - type of algorithm

    input_file = 'datasets/inail_small.json'
    R = read_dataset(input_file)
    k = 5
    no_pf = ['Genere', 'Deceduto', 'ModalitaAccadimento', 'ConSenzaMezzoTrasporto']
    #for r in R:
    #    pretty_print(r)
    print('The dataset contains', len(R), 'tuples')
    PCBuckets = ProgramExecutionModule(R, k)
    ConstraintGenerationModule(PCBuckets, 'P-F', no_pf)
    #print(PCBuckets)

if __name__ == '__main__':
    main()
