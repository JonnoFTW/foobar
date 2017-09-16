from __future__ import print_function
from fractions import Fraction as F
from copy import deepcopy


def mat_mul(a, b):
    dim = len(a)
    temp = [[0 for _ in range(dim)] for _ in range(dim)]
    for i in range(dim):
        temp[i] = [0 for _ in range(dim)]
        for j in range(dim):
            s = 0
            for l in range(dim):
                s += a[i][l] * b[l][j]
            temp[i][j] = s
    return temp


def mat_pow(m, pow):
    result = deepcopy(m)
    for n in range(pow):
        result = mat_mul(result, m)
    return result
    # dim = len(m)
    # out = [[1 if i == j else 0 for j in range(dim)] for i in range(dim)]
    # temp = [[0 for _ in range(dim)] for _ in range(dim)]
    # for p in range(pow):
    #     for row in range(dim):
    #         for col in range(dim):
    #             temp[row][col] = 0
    #             for k in range(dim):
    #                 temp[row][col] += m[row][k] * m[k][col]
    #     for i in range(dim):
    #         for j in range(dim):
    #             out[i][j] = temp[i][j]
    #
    # return out


def mat_id(dim):
    return [[1 if i == j else 0 for j in range(dim)] for i in range(dim)]


def mat_diff(a, b, dim):
    out = [[0 for _ in range(dim)] for _ in range(dim)]
    for i in range(dim):
        for j in range(dim):
            out[i][j] = a[i][j] - b[i][j]
    return out


def mat_disp(mat):
    for row in mat:
        print(row)
    print()

mid = mat_id(3)
mat_disp(mid)
P = [[F(1, 2), F(1, 2), F(0),    F(0)],
     [F(0),    F(1, 2), F(1, 2), F(0)],
     [F(1, 2), F(0),    F(0),    F(1, 2)],
     [F(0),    F(0),    F(0),    F(1)]]
R =
mat_disp(P)

mat_disp(mat_diff(mid, P, len(mid)))
print()

def answer(m):
    # model as a markov chain
    frac_m = []
    terminal = []
    for s, row in enumerate(m):
        denom = sum(row)
        if denom == 0:
            terminal.append(s)
            frac_m.append([F(0) for _ in row])
        else:
            frac_m.append([F(i, denom) for i in row])
    for row in frac_m:
        print(row)
    print()
    for row in mat_pow(frac_m, 5):
        print(row)

    print()


# https://www.youtube.com/watch?v=cP3c2PJ4UHg

"""
Write a function answer(m) that takes an array of array of nonnegative ints representing how many times that state has 
gone to the next state and return an array of ints for each terminal state giving the exact probabilities of each
terminal state, represented as the numerator for each state, then the denominator for all of them at the end and in 
simplest form. The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in, there is a
path from that state to a terminal state. That is, the processing will always eventually end in a stable state. 
The ore starts in state 0. The denominator will fit within a signed 32-bit integer during the calculation, as long 
as the fraction is simplified regularly.

and then workingand For example, consider the matrix m:
[
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]
So, we can consider different paths to terminal states, such as:
s0 -> s1 -> s3
s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
s0 -> s1 -> s0 -> s5
Tracing the probabilities of each, we find that
s2 has probability 0
s3 has probability 3/14
s4 has probability 1/7
s5 has probability 9/14
So, putting that together, and making a common denominator, gives an answer in the form of
[s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
[0, 3, 2, 9, 14].
"""
if __name__ == "__main__":
    print(answer([
        [0, 1, 0, 0, 0, 1],  # s0, the initial state, goes to s1 and s5 with equal probability
        [4, 0, 0, 3, 2, 0],  # s1 can become s0, s3, or s4, but with different probabilities
        [0, 0, 0, 0, 0, 0],  # s2 is terminal, and unreachable (never observed in practice)
        [0, 0, 0, 0, 0, 0],  # s3 is terminal
        [0, 0, 0, 0, 0, 0],  # s4 is terminal
        [0, 0, 0, 0, 0, 0],  # s5 is terminal
    ]))
    # print(answer([
    #     [0, 2, 1, 0, 0],
    #     [0, 0, 0, 3, 4],
    #     [0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0]
    # ]))
    # print(answer([
    #     [0, 1, 0, 0, 0, 1],
    #     [4, 0, 0, 3, 2, 0],
    #     [0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0]]
    # ))
