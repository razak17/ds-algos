""" Implementation of merge-sort using a basic queue

"""

# from linkedQueue import LinkedQueue as lq


def merge(s1, s2, s):
    while len(s1) != 0 and len(s2) != 0:
        if s1[0] < s2[0]:
            s.append(s1.pop(0))
        else:
            s.append(s2.pop(0))
    while len(s1) != 0:
        s.append(s1.pop(0))
    while len(s2) != 0:
        s.append(s2.pop(0))
    return s


def merge_sort(s):
    n = len(s)
    if n < 2:
        return
    #divide
    s1 = []
    s2 = []
    # move first n // 2 elements to s1
    while len(s1) < n // 2:
        s1.append(s.pop())
    # move the rest to s2
    while len(s) != 0:
        s2.append(s.pop())
    # conquer (with recursion)
    merge_sort(s1)
    merge_sort(s2)
    # merge results
    return merge(s1, s2, s)
    

print(merge_sort([2,4,6,8,1,3,5,7,9]))
print(merge_sort([3,5,1,7,9,2,4,8,6,11]))
