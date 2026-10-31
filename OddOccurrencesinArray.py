def solution(A):
    N = 0 a # output will start with 0
    for i in A: # loop action for A times
        N = N ^ i # XOR the element, will return to 0 if number repeats

    return N
