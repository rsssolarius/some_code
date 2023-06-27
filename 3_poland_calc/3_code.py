stroka = input()
spisok = stroka.split()
s = 0
counter = 0
spisok_new = []
for i in range(len(spisok)):
    if '*' in spisok[i]:
        s = int(spisok_new[counter - 2]) * int(spisok_new[counter - 1])
        del spisok_new[-1]
        del spisok_new[-1]
        spisok_new.append(str(s))
        counter -= 1
        s = 0
    elif '-' in spisok[i]:
        s = int(spisok_new[counter - 2]) - int(spisok_new[counter - 1])
        del spisok_new[-1]
        del spisok_new[-1]
        spisok_new.append(str(s))
        counter -= 1
        s = 0
    elif '+' in spisok[i]:
        s = int(spisok_new[counter - 2]) + int(spisok_new[counter - 1])
        del spisok_new[-1]
        del spisok_new[-1]
        spisok_new.append(str(s))
        counter -= 1
        s = 0
    elif '/' in spisok[i]:
        s = int(spisok_new[counter - 2]) / int(spisok_new[counter - 1])
        del spisok_new[-1]
        del spisok_new[-1]
        spisok_new.append(str(s))
        counter -= 1
        s = 0
    else:
        spisok_new.append(spisok[i])
        counter += 1
print(spisok_new[0])