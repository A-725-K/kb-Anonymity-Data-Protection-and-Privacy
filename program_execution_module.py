def path_conditions2str(lst):
    return ''.join([str(i) for i in lst])


def delete_small_buckets(buckets, k):
    for pc, B in buckets.items():
        if len(B) < k:
            print('Unsatisfiable case, too few tuples for this path: {}'.format(pc)) # str2path_conditions
            del buckets[pc]


def ProgramExecutionModule(R, k):
    PCBuckets = {}
   
    for t in R:
        pc = []
        #P_test(t, pc)
        key_bucket = path_conditions2str(pc)
        try:
            PCBuckets[key_bucket] += [t]
        except KeyError as ke:
            PCBuckets[key_bucket] = [t]

    delete_small_buckets(PCBuckets, k)
    return PCBuckets
