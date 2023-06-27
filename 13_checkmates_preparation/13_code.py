import numpy as np
 
 
def make_board(n):
    count = 1
    spisok = []
    for i in range(1, n + 1):
        for j in range(1, int((n / 2) + 1)):
            if count % 2 != 0:
                spisok += [1, 0]
            else:
                spisok += [0, 1]
        count += 1
    return np.array(spisok, dtype="int8").reshape(n, n)