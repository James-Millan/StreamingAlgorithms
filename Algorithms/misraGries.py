# returns a set A, of size k - 1 contain all elements that occur with frequency > m/k.
# if k - 1 elements that satisfy this criterion don't exist, some elements in this set may not be frequent elements.
def misra_gries(sequence, k):
    A = {}
    for i in range(len(sequence)):
        if sequence[i] in A:
            A[i] = A[i] + 1
        else:
            if len(A) < k - 1:
                A[sequence[i]] = 1
            else:
                B = A.copy()
                for j in A:
                    B[j] = A[j] - 1
                    if B[j] == 0:
                        B.pop(j)
                A = B.copy()
        return A


