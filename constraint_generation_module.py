import time
from ast import literal_eval as make_tuple
from constraint_solver_module import ConstraintSolverModule


# every value in the released dataset is has not appeared in any raw data point
def NoFieldRepeat(B, no_pf):
    S = []
    for t in B:
        for k, v in t.items():
            if k not in no_pf:
                S += [(k, '!=', v)]               
    return S


# every released tuple is distinguishable
def NoTupleRepeat(B, field_pt):
    S = []
    for t in B:
        S += [(field_pt, '!=', t[field_pt])]
    return S


# convert the key-string into path (list of path conditions) 
def str2path_condition(s):
    return [make_tuple(t) for t in s.split('|')]


# generate all the constraints based on the algorithm and try to generate a new tuple anonymized
def ConstraintGenerationModule(PCBuckets, alg, config_file, no_pf=None, field_pt=None):
    t_start = time.time()
    
    R1 = []
    for pc, B in PCBuckets.items():
        if alg == 'P-F': # same-path, no field repeat
            if no_pf:
                S = NoFieldRepeat(B, no_pf)
            else:
                print('[!!] You must specify P-F attributes to exclude !')
                exit(1)
        elif alg == 'P-T': # same-path, no tuple repeat
            if field_pt:
                S = NoTupleRepeat(B, field_pt)
            else:
                print('[!!] You must specify P-T attribute !')
                exit(1)
        else:
            print('[!!] Algorithm not implemented !')
            exit(1)

        # S = []
        S += str2path_condition(pc)
        row = ConstraintSolverModule(S, config_file) # solve the constraints
        if row:
            R1 += [row]
    
    t_end = time.time()
    print('    [*] Constraints Module:\t\t', t_end - t_start, 's')
    
    print('{*} Privacy Preservation Technique\t--\t', end='')
    if alg == 'P-F':
        print('Same-Path, No Field Repeat')
    elif alg == 'P-T':
        print('Same-Path, No Tuple Repeat')

    return R1
            

