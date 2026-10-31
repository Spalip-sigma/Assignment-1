def solution(A, K):
    N = len(A)

    if N == 0:
        return A
    else:
        for i in range(K):
            last = A.pop()
            A.insert(0, last)

    return A
