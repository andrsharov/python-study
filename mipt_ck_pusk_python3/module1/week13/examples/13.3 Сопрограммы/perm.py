def permutations(s, i=0, a=''):
    if i == len(s):
        yield a
        return

    for c in s:
        if c not in a:
            yield from permutations(s, i + 1, a + c)


print(list(permutations('abc')))
