from itertools import tee, zip_longest, chain

def pairwise_offset(sequence, fillvalue="*", offset=1):
    it1, it2 = tee(sequence,2)
    print(it1,it2)
    return zip_longest(it1,chain(fillvalue * offset, it2), fillvalue=fillvalue)
    
pairwise_offset(['a','b','c'], '*',  1)