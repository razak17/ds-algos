import collections
def hash_code(s):
    mask = (1 << 32) - 1
    h = 0
    for character in s:
        h = (h << 5 & mask) | (h >> 27)
        h += ord(character)
    return h

print(hash_code("x"))

print(hash(5))
print(hash(5.0))