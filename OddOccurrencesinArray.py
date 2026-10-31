def solution(A):
    N = 0
    for i in A:
        N = N ^ i

    return N
