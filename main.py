from program_execution_module import ProgramExecutionModule
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
    #for r in R:
    #    pretty_print(r)
    print('The dataset contains', len(R), 'tuples')
    PCBuckets = ProgramExecutionModule(R, k)
    
    print(PCBuckets)

if __name__ == '__main__':
    main()
