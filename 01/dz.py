# Напишите программу, удаляющую из текста все слова, содержащие ""абв""

t = "абв"
text = "абв лучше, чем абвгд"
lst = text.split()

new_lst = [x for x in lst if t not in x]
print(new_lst)
