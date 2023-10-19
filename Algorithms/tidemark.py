import random

# algorithm used to estimate the number of distinct elements in a stream.
def tidemark(sequence):
    # choose a hash function [n] -> [n] (ax + b mod p) mod n
    # randomly choose a != 0, b < p, p = 2^61 - 1 for simplicity. An actual implementation would not do this.
    p = pow(2,61) - 1
    n = len(sequence)
    a = random.randint(1,n)
    b = random.randint(0,n)

    z = 0
    for i in range(n):
        alpha = sequence[i]
        if zeroes(my_hash(a,b,p,n,alpha)) > z:
            z = zeroes(my_hash(a,b,p,n,alpha))

    return pow(2,z+0.5)

def my_hash(a, b, p, m, x):
    return ((a*x + b) % p) % m

def zeroes(num):
    binary = str(bin(num)[2:])
    count = 0
    for i in range(binary):
        if i == "1":
            count = 0
        else:
            count = count + 1
    return count
