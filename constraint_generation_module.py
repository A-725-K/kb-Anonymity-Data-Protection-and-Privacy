def NoFieldRepeat(B, no_pf):
    S = []
    for t in B:
        for k, v in t.items():
            if k not in no_pf:
                S += [(k, '!=', v)]                
    return S


def NoTupleRepeat(B):
    S = []
    for t in B:
        S += [('Eta', '!=', t['Eta'])]
    return S


def str2path_condition(s):
    from ast import literal_eval as make_tuple
    return [make_tuple(t) for t in s.split('|')]


def ConstraintGenerationModule(PCBuckets, alg, no_pf):

    for pc, B in PCBuckets.items():
        if alg == 'P-F':
            S = NoFieldRepeat(B, no_pf)
        elif alg == 'P-T':
            S = NoTupleRepeat(B)
        else:
            print("Algritmo non implementato")
            exit(1)
        S += str2path_condition(pc)
        print(S)
        break  