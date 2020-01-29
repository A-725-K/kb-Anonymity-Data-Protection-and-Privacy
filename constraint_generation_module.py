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
def NoTupleRepeat(B):
    S = []
    for t in B:
        S += [('Eta', '!=', t['Eta'])]
    return S


# convert the key-string into path (list of path conditions) 
def str2path_condition(s):
    return [make_tuple(t) for t in s.split('|')]


# generate all the constraints based on the algorithm and try to generate a new tuple anonymized
def ConstraintGenerationModule(PCBuckets, alg, no_pf):
    t_start = time.time()
    
    R1 = []
    for pc, B in PCBuckets.items():
        if alg == 'P-F': # same-path, no field repeat
            S = NoFieldRepeat(B, no_pf)
        elif alg == 'P-T': # same-path, no tuple repeat
            S = NoTupleRepeat(B)
        else:
            print('[!!] Algrithm not implemented !')
            exit(1)

        # S = []
        S += str2path_condition(pc)
        row = ConstraintSolverModule(S) # solve the constraints
        if row:
            R1 += [row]
    
    t_end = time.time()
    print('    [*] Constraints Module:\t\t', t_end - t_start, 's')
    
    print('{*} Privacy preservation technique\t--\t', end='')
    if alg == 'P-F':
        print('Same-Path, No Field Repeat')
    elif alg == 'P-T':
        print('Same-Path, No Tuple Repeat')

    return R1
            

