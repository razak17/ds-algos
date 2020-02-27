import random
def quick_select(s, k):
    """Return the kth smallest element of list S, for k from 1 to len(S)."""
    if len(s) == 1:
        return s[0]
    pivot = random.choice(s)
    L = [x for x in s if x < pivot]
    E = [x for x in s if x == pivot]
    G = [x for x in s if x > pivot]

    if k <= len(L):
        return quick_select(L, k)
    elif k <= len(L) + len(E):
        return pivot
    else:
        j = k - len(L) - len(E)
        return quick_select(G, j)

print(quick_select([4,3,9,5,2], 1))
