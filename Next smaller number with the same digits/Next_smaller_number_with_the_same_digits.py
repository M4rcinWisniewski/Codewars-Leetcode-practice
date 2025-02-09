# Next smaller number with the same digits
#Please check out the kata on: https://www.codewars.com/kata/5659c6d896bc135c4c00021e/

def next_smaller(n):
    a = list(str(n))
    length = len(a)

    i = length - 2
    while i >= 0 and a[i] <= a[i + 1]:
        i -= 1

    if i == -1:
        return -1

    j = length - 1
    while a[j] >= a[i]:
        j -= 1

    a[i], a[j] = a[j], a[i]


    a = a[:i + 1] + a[i + 1:][::-1]

    next_small = int(''.join(a))

    if next_small >= n or str(next_small)[0] == '0' or len(str(next_small)) < length:
        return -1

    return next_small


print(next_smaller(100))