def find_brute(aList, target):
    """Return the lowest index of aList at which target begins"""
    n, m = len(aList), len(target)
    # print(n)
    # print(m)
    for i in range(n - m + 1):
        k = 0
        while k < m and aList[i + k] == target[k]:
            k += 1
        if k == m:
            return i
    return -1

# print(find_brute("curfuffle", "f"))
# print(find_brute("abacaabaccabacabaabb", "abacab"))


def find_boyer_moore(T, P):
    """Return the lowest index of aList at which target begins"""
    n, m = len(T), len(P)
    if m == 0: return 0
    last = {}
    for k in range(m):
        last[P[k]] = k
    # align end of pattern (m - 1) index of text
    i = n - 1
    k = m - 1
    while i < n:
        if T[i] == P[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(T[i], -1)
            i +=m - min(k, j + 1)
            k = m - 1
    return -1

print(find_brute("curfuffle", "ff"))
print(find_brute("abacaabaccabacabaabb", "abacab"))

def find_kmp(T, P):
    n, m = len(T), len(P)
    if m == 0: return 0
    fail = compute_kmp_fail(P)
    j = 0
    k = 0
    while j < n:
        if T[j] == P[k]:
            if k == m - 1:
                return j - m + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k - 1]
        else:
            j += 1
    return -1

def compute_kmp_fail(P):
        """Utility that compares and returns KMP 'fail' list."""
        m = len(P)
        fail = [0] * m
        j = 1
        k = 0
        while j < m:
            if P[j] == P[k]:
                fail[j] = k + 1
                j += 1
                k += 1
            elif k > 0:
                k = fail[k - 1]
            else:
                j += 1
        return fail

# print(find_kmp("curfuffle", "ff"))
# print(compute_kmp_fail("curfuffle"))
# print(compute_kmp_fail("abacaabaccabacabaabb"))
# print(find_kmp("abacaabaccabacabaabb", "abacab"))


