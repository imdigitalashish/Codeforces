import sys

def read():
    s = 0
    w = 1
    ch = sys.stdin.read(1)
    while not ('0' <= ch <= '9'):
        if ch == '-':
            w = -1
        ch = sys.stdin.read(1)
    while '0' <= ch <= '9':
        s = (s << 1) + (s << 3) + (ord(ch) ^ 48)
        ch = sys.stdin.read(1)
    return s * w

def F(x, n):
    while n > 0:
        if x == 0:
            return x
        x = (x >> 1)
        n -= 1
    return x

def C(x, n):
    while n > 0:
        if x <= 1:
            return x
        x = ((x + 1) >> 1)
        n -= 1
    return x

t = read()
while t > 0:
    x = read()
    n = read()
    m = read()
    print(f"{F(C(x, m), n)} {C(F(x, n), m)}")
    t -= 1
