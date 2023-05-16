import random


def ch(bc):
    bc = bc[::-1]
    if bc != b:
        za = bc[:3] + '1'
        zb = bc[:3] + '0'
        zc = '0' + bc[:3]
        zd = '1' + bc[:3]
        ze = bc[1:] + '1'
        zf = bc[1:] + '0'
        zg = '0' + bc[1:]
        zh = '1' + bc[1:]
        if za or zb or zc or zd or ze or zf or zg or zh:
            print('\33[1m(b) Reversed and matched')
        else:
            ch(bc)
    else:
        print('\33[1m(b) Reversed and matched')


def ss_r(ab):
    x = random.randint(1, 2)
    if x == 1:
        y = ab[:3]
        print(y)
    if x == 2:
        y = ab[1:]
        print(y)
    z = y[::-1]
    return z


a = '11101'
b = '11111'

print('The binary values are a={} and b={}'.format(a, b))
a1 = ss_r(a)
print('\33[1m(a) The reversed substring is: {}'.format(a1))
a2 = ch(a)
print(a[1:])
print(random.randint(1,2))