def solution(A):
    num = 1 # 1 is the smallest number that could be missing
    while num in A:
        num += 1 # is the number is within the list, add 1 to check the next

    return num
