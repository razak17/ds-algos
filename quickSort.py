def quick_sort(s):
    n = len(s)
    if n < 2:
        return
    # divide
    p = s[0]
    L = []
    E = []
    G = []
    for i in range(len(s)):
        while len(s) != 0:
            if s[i] < p:
                L.append(s.pop(0))
            elif p < s[i]:
                G.append(s.pop(0))
            else:
                E.append(s.pop(0))
        
    # conquer (recursion)
    quick_sort(L)
    quick_sort(G)

    # concatenate results
    while len(L) != 0:
        s.append(L.pop(0))
    while len(E) != 0:
        s.append(E.pop(0))
    while len(G) != 0:
        s.append(G.pop(0))
    return s

print(quick_sort([3,5,1,99,44,66,22,33,7,9,2,4,8,6,11]))

print(sorted('green'))

colors = [ 'red' , 'green' , 'blue' , 'cyan' , 'magenta' , 'yellow' ]
print(colors.sort(key=len))
print(sorted(colors, key=len))
print(sorted(colors, key=len, reverse=True))


