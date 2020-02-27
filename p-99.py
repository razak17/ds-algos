def factors(n):
    factor_list = []
    for i in range(1, int(n*0.5) + 1):
        if n % i == 0:
            factor_list.append(i)
    return factor_list

print(factors(100))

cache = {}
def fib(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    else:
        result = fib(n - 1) + fib(n - 2)
        cache[n] = result
        return result
print(fib(5))












def preorder_label(T, p, d, path):
    label = '.'.join(str(j + 1) for j in path)
    print(2*d*' ' + label, p.element())
    path.append(0)
    for c in T.chidren(p):
        preorder_label(T, c, d + 1, path)
        path[-1] += 1
    path.pop()

