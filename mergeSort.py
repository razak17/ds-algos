def merge_me(s1, s2):
    # Merge two sorted python lists s1,s2 into s
    # s1.sort()
    # s2.sort()
    s = [0] * (len(s1) + len(s2))
    i = j = 0
    while i + j < len(s):
        if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
            s[i + j] = s1[i]
            i += 1
        else:
            s[i + j] = s2[j]
            j += 1
    return s

# print(merge_me([2,3,5,7,11], [8,6,4,2]))


def merge(s1, s2, s):
    # Merge two sorted python lists s1,s2 into s
    i = j = 0
    while i + j < len(s):
        if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
            s[i + j] = s1[i]
            i += 1
        else:
            s[i + j] = s2[j]
            j += 1
    return s

def merge_sort(s):
    n = len(s)
    if n < 2:
        return
    # divide
    mid = n // 2
    s1 = s[0:mid]
    s2 = s[mid:n]
    # conquer
    merge_sort(s1)
    merge_sort(s2)
    # merge results
    return merge(s1,s2,s)

print(merge_sort([3,5,1,7,9,2,4,8,6,11]))


