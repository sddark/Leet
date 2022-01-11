def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

print(cons(3, 4))