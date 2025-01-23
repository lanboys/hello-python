def test():
    a = dict()
    print(dict, type(dict), type(a))

    a[2] = 3
    a[4] = 5
    a["b"] = 9
    a['c'] = "3"
    print(a)

    b = dict(one=1, two=2, three=3)
    print(b)

    c = {"2": 3, "4": 5, "b": 5, "c": "3"}
    print(c)
    print(c["b"])

    d = dict(c)
    print(d)

    del d['c']  # 删除键 'c'
    print(d)

    d.clear()  # 清空字典
    print(d)

    e = {'a': c}
    print(e)

    f = e['a']
    del f['c']
    print(f)

    print("c" in f)
    print("b" in f)

    print("-------")
    print(str(f))


if __name__ == '__main__':
    test()
