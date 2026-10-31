def solution(A):
    num = 1 # start with the smallest number, 1

    for i in range(len(A)): # loop for the elements in A
        if num in A: # if number is in A, add 1 to number and move on
            num += 1
        else:
            return num # if not in the list, this is the number the question is asking for

    return num
