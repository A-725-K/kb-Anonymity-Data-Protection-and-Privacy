from p_test import P_test

def path_conditions2str(lst):
    return '|'.join([str(i) for i in lst])


def delete_small_buckets(buckets, k):
    to_delete = []
    for pc, B in buckets.items():
        if len(B) < k:
            #print('Unsatisfiable case, too few tuples for this path: {}'.format(len(B))) # str2path_conditions
            to_delete += [pc]

    for short_pc in to_delete:
        del buckets[short_pc]



def ProgramExecutionModule(R, k):
    PCBuckets = {}
    
    for t in R:
        pc = []
        P_test(t, pc)
        key_bucket = path_conditions2str(pc)
        try:
            PCBuckets[key_bucket] += [t]
        except KeyError as ke:
            PCBuckets[key_bucket] = [t]

    n_paths = len(PCBuckets)
    print('Number of different paths', n_paths)
    delete_small_buckets(PCBuckets, k)
    print('Number of paths removed', n_paths-len(PCBuckets))
    return PCBuckets
