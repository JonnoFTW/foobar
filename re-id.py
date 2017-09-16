from math import sqrt
def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n %2 == 0:
        return False
    for i in range(3, int(sqrt(n))+2, 2):
        if n % i == 0:
            return False
    return True
def answer(n):
    s = "2"
    # keep adding primes to the string until its length is at least n + 5
    i = 3
    while len(s) < n + 5:
        if isPrime(i):
            s += str(i)
        i += 2
    return s[n:n+5]

if __name__ == "__main__":
    for i in range(100):
        print(answer(i))
    # print(answer(0))
    # print(answer(3))
    # print(answer(4))
    # print(answer(5))
