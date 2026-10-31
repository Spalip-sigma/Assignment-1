def solution(X, Y, D):
    position = X
    jump = 0

    while position < Y:
        position += D
        jump += 1

    return jump
