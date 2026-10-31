def solution(X, Y, D):
    position = X # position = input X
    jump = 0 # jumps start at 0

    while position < Y: # keep looping while position does not reach Y
        position += D # increase position by D
        jump += 1 # add 1 jump to the counter

    return jump
