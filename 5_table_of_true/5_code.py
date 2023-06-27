from itertools import product

pare = [0, 1]
"""Создаем алфавит. Уже и не помню для чего..."""
alphabet = {'A': pare, 'B': pare, 'C': pare, 'D': pare, 'E': pare, 
            'F': pare, 'G': pare, 'H': pare, 'I': pare, 'J': pare, 
            'K': pare, 'L': pare, 'M': pare, 'N': pare, 'O': pare, 
            'P': pare, 'Q': pare, 'R': pare, 'S': pare, 'T': pare, 'U': pare,
            'V': pare, 'W': pare, 'X': pare, 'Y': pare, 'Z': pare}
"""Ищем во введенном тексте большие буквы и кладем в новый словарь.
   Параллельно буквы найденные кладем в список"""
uses_letters = {}
uses_letters_spis = list()
expr = input()
for i in expr.split():
    if i in alphabet:
        uses_letters[i] = [0, 1]
        if i in uses_letters_spis:
            pass
        else:
            uses_letters_spis.append(i)
    else:
        pass
"""Создаем список всех вариантов значений букв"""
spis = list(product([0, 1], repeat=len(uses_letters)))
"""Записываем первой строкой буквы """
for i in range(len(uses_letters_spis)):
    if i == len(uses_letters_spis) - 1:
        print(uses_letters_spis[i], 'F')
    else:
        print(uses_letters_spis[i], end=' ')
"""Идем по списку вариантов знайчений. В словарь по ключу заносим 
   значения по порядку (для этого счетчик). Потом пробегаем по длине элемента
   списка и выводим на печать, в последнем элементе выдавая значение последней
   буквы и следом значение выражения. Конец."""
count = 0
for i in spis:
    for k in uses_letters:
        uses_letters[k] = i[count]
        count += 1
    for j in range(len(i)):
        if j == len(i) - 1:
            print(f'{i[j]} {int(eval(expr, {}, uses_letters))}')
        else:
            print(i[j], end=' ')
    count = 0