def minus(s, e):
    return minus(s-2, e) + minus(s-5, e) if s > e else s == e


print(minus(23, 2))
