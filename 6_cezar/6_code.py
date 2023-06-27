line_1 = ''
sdvig = int(input())
with open('public.txt', encoding='UTF-8') as file_in:
    line = file_in.read()
stroka_A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * abs(sdvig)
stroka_a = 'abcdefghijklmnopqrstuvwxyz' * abs(sdvig)
for i in line:
    if i in stroka_A:
        line_1 += stroka_A[stroka_A.index(i) + 52 + sdvig]
    elif i in stroka_a:
        line_1 += stroka_a[stroka_a.index(i) + 52 + sdvig]
    else:
        line_1 += i

with open('private.txt', 'w', encoding='UTF-8') as file_out:
    file_out.writelines(line_1)