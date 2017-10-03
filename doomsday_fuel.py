from fractions import Fraction as F, gcd
from copy import deepcopy


def mat_mul(a, b):
    aRows = len(a)
    aColumns = len(a[0])
    bColumns = len(b[0])
    temp = [[0 for _ in range(bColumns)] for _ in range(aRows)]
    for i in range(aRows):
        for j in range(bColumns):
            for k in range(aColumns):
                temp[i][j] += a[i][k] * b[k][j]
    return temp


def mat_pow(m, pow):
    result = deepcopy(m)
    for n in range(pow):
        result = mat_mul(result, m)
    return result


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


def mat_zero(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]


def mat_inv_js(m):

    dim = len(m)
    I = mat_id(dim)
    C = deepcopy(m)
    for i in range(dim):
        e = C[i][i]
        if e == 0:
            for ii in range(dim):
                if C[ii][i] != 0:
                    for j in range(dim):
                        C[i][j], C[ii][j] = C[ii][j], C[i][j]
                        I[i][j], I[ii][j] = I[ii][j], I[i][j]
                    break
            e = C[i][i]
            if e == 0:
                return
        for j in range(dim):
            C[i][j] = C[i][j] / e
            I[i][j] = I[i][j] / e
        for ii in range(dim):
            if ii == i:
                continue
            e = C[ii][i]
            for j in range(dim):
                C[ii][j] -= e * C[i][j]
                I[ii][j] -= e * I[i][j]
    return I


def answer(m):
    # model as a markov chain
    # transient states can be exited
    # absorbing cannot
    if len(m) == 1:
        return [1,1]
    t_states = []
    transient_states = []
    absorbing_states = []

    a_states = []

    for s, row in enumerate(m):
        denom = sum(row)
        if denom == 0:
            # state is absorbing
            a_states.append([F(1) if s == i else F(0) for i in row])
            absorbing_states.append(s)
        else:
            # state is transient
            t_states.append([F(i, denom) for i in row])
            transient_states.append(s)
    # Q = probability of going from transient to transient
    Q = [[f for idx, f in enumerate(t) if idx not in absorbing_states] for t in t_states]
    R = [[f for idx, f in enumerate(t) if idx not in transient_states] for t in t_states]
    t = len(t_states)
    r = len(a_states)

    # make a new array with transient in top left, prob of ending in absorbing at top right
    # zeros bottom left, id bottom right

    I_t = mat_id(t)
    I_minus_Q = mat_diff(I_t, Q, t)
    N = mat_inv_js(I_minus_Q)
    B = mat_mul(N, R)

    max_denom = reduce(gcd, B[0]).denominator

    fracs = map(lambda x: max_denom / x.denominator * x.numerator, B[0])
    return fracs + [max_denom]


"""
READ THIS:

https://math.dartmouth.edu//archive/m20x06/public_html/Lecture14.pdf

AND THIS:

https://en.wikipedia.org/wiki/Absorbing_Markov_chain


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
        [0, 2, 1, 0, 0],
        [0, 0, 0, 3, 4],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]))

    print(answer([
        [0, 1, 0, 0, 0, 1],  # s0, the initial state, goes to s1 and s5 with equal probability
        [4, 0, 0, 3, 2, 0],  # s1 can become s0, s3, or s4, but with different probabilities
        [0, 0, 0, 0, 0, 0],  # s2 is terminal, and unreachable (never observed in practice)
        [0, 0, 0, 0, 0, 0],  # s3 is terminal
        [0, 0, 0, 0, 0, 0],  # s4 is terminal
        [0, 0, 0, 0, 0, 0],  # s5 is terminal
    ]))
    print(answer([
        [1, 0, 1, 1, 0, 5,0],
        [0, 1, 1, 0, 0, 0,0],
        [0, 0, 0, 1, 0, 0,0],
        [0, 0, 0, 0, 0, 0,0],
        [0, 0, 0, 0, 0, 0,1],
        [0, 0, 0, 0, 0, 0,0],
        [0, 0, 0, 0, 0, 0, 0],
    ]))
    print(answer([
        [0,0],
    ]))
