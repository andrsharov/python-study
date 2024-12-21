def gen():
    try:
        yield 1
        yield 2
        yield 3
    except GeneratorExit:
        print('GeneratorExit')
    finally:
        print('Finally')


g = gen()
print(next(g))
print(next(g))
