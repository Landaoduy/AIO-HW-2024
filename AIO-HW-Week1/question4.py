# Question 4:

def giai_thua(n):

    if n < 0:
        raise ValueError('n must be larger than 0')

    elif n == 0:
        return 1

    else:
        s = 1
        for i in range(1, n+1):
            s = s*i
        return s


def sin(x, n):

    approx_sin = sum(((-1)**i) * (x**(2*i+1)) / giai_thua(2*i+1)
                     for i in range(n))

    print(
        f"The approximate value of sin with x = {x} and n = {n} is: {approx_sin} ")


def cos(x, n):

    approx_cos = sum(((-1)**i) * (x**(2*i)) / giai_thua(2*i) for i in range(n))

    print(
        f"The approximate value of cos with x = {x} and n = {n} is: {approx_cos} ")


def sinh(x, n):

    approx_sinh = sum(x**(2*i+1) / giai_thua(2*i+1) for i in range(n))

    print(
        f"The approximate value of sinh with x = {x} and n = {n} is: {approx_sinh}")


def cosh(x, n):

    approx_cosh = sum(x**(2*i) / giai_thua(2*i) for i in range(n))

    print(
        f"The approximate value of cosh with x = {x} and n = {n} is: {approx_cosh}")
