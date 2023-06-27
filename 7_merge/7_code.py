def merge(x: tuple, y: tuple):
    spisok_1 = list(x)
    spisok_2 = list(y)
    spisok_sort = list()
    i = len(spisok_1)
    j = len(spisok_2)
    while j != 0 and i != 0:
        if spisok_1[0] <= spisok_2[0]:
            spisok_sort.append(spisok_1[0])
            spisok_1.pop(0)
            i -= 1
        else:
            spisok_1[0] > spisok_2[0]
            spisok_sort.append(spisok_2[0])
            spisok_2.pop(0)
            j -= 1
    while i != 0:
        spisok_sort.append(spisok_1[0])
        spisok_1.pop(0)
        i -= 1
    while j != 0:
        spisok_sort.append(spisok_2[0])
        spisok_2.pop(0)
        j -= 1
    x = tuple(spisok_sort)
    return x