# Radix sort is a sort of distribution, also known as “bucket sort” or “bin sort”. As the name suggests, it is the distribution of the elements to be sorted by the key information. To some “bucket”, in order to achieve the role of sorting, radix sorting is a sort of stability, the time complexity O (nlog (r) m), where r is the cardinal number, and m for the heap In some cases, the radix sorting method is more efficient than other stability sequencing methods.


import math


def radix_sort(lists, radix=10):
    k = int(math.ceil(math.log(max(lists), radix)))
    bucket = [[] for i in range(radix)]
    for i in range(1, k+1):
        for j in lists:
            bucket[j/(radix**(i-1)) % (radix**i)].append(j)
        del lists[:]
        for z in bucket:
            lists += z
            del z[:]
    return lists
