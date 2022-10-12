# Задача №41: Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
#  Пример:
# На сжатие входные данные: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Выходные данные:          12W1B12W3B24W1B14W


# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

code_text = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
lst = []
coding = ''

for i in range(len(code_text)): 
    if code_text[i] not in lst:
        lst.append(code_text[i])

for j in range(len(lst)):
    count = 0
    for u in range(len(code_text)):
        if lst[j] == code_text[u]:
            count += 1 
    coding = coding + str(count) + lst[j]      

print(coding)
