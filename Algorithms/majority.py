# return an element that occurs > m/2 times if it exists.
def majority(sequence):
    alpha = sequence[0]
    counter = 0
    for i in range(1, len(sequence)):
        if counter == 0:
            alpha = sequence[i]
            counter = 1
        elif sequence[i] == alpha:
            counter = counter + 1
        else:
            counter = counter - 1
    return alpha

#verify output of the majority algorithm with a second pass.
def majority_second_pass(sequence, alpha):
    count = 0
    for i in sequence():
        if i == alpha:
            count = count + 1
    return count > len(sequence) / 2