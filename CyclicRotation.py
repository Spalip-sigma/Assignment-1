def solution(A, K):
    N = len(A) # how many elements are in A

    if N == 0: # is nothing is in A then ignore it
        return A
    else:
        for i in range(K): # repate the following actions K times
            last = A.pop() # remove the last element, then save it
            A.insert(0, last) # insert the last element at the front

    return A
