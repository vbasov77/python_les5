# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 
# 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота

from random import randint

candies = 2021
count = 0
lst = []
name = input('Введите имя ')
lst.append(name)
lst.append('Робот')

print('Выбор игрока...')
p = randint(1, 2)


def player(nam):
    print(f'Ходит {nam}...')
    number = randint(1, 28)
    print (f'У {nam}а {number}')
    return number


if p == 2:
    num = player(lst[1])
    candies -= num
    print(f'Осталось конфет {candies}')

while candies > 0:
    while True:
        num = int(input(f'{name} введите от 1 до 28\n'))
        try:
            if 0 < num <= 28:
               break
     
            else: print('Неверное число')
        except ValueError:
            print('Число должно быть от 1 до 28')
    
    candies -= num
    if candies <= 0:
        print(f'Выиграл {lst[0]}')
        break
    print(f'Осталось конфет {candies}')
    num_2 = player(lst[1])
    candies -= num_2
    if candies <= 0:
        print(f'Выиграл {lst[1]}')
        break
    print(f'Осталось конфет {candies}')

        

        

      