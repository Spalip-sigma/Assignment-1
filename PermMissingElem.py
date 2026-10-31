def solution(A):
    num = 1

    for i in range(len(A)):
        if num in A:
            num += 1
        else:
            return num

    return num
