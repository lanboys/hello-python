class A:
    pass


class B(A):
    pass


def test():
    print(type(bool), type(int), type(list), type(dict), type(set), type(tuple), type(enumerate), type(object))

    print("---------")
    print(type(A()), type(B()), type(A), type(B))
    print(isinstance(A(), A))
    print(type(A()) == A)
    print(isinstance(B(), A))
    print(type(B()) == A)

    print("---------")
    print(issubclass(bool, int))
    print(issubclass(A, object))

    print("---------")
    a, b, c, d = 20, 5.5, True, 4 + 3j
    print(type(a), type(b), type(c), type(d))


if __name__ == '__main__':
    test()
