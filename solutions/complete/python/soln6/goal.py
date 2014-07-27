from functools import partial
def f(times, letters=None):
    if letters:
        return 'g'+('o'*times)+letters
    return partial(f, times+1)
g=partial(f, 0)

if __name__ == '__main__':
    print(g('al'))
    print(g()('al'))
    print(g()()('al'))
    print(g()()()()()('al'))
