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
name = input('Введите имя ')

print('Выбор игрока.')
p = randint(1, 2)


if p == 2:
    print('Ходит робот')
    robot = randint(1, 28)
    count += robot
    print (f'У робота {robot}')

while count < candies:
    try:
       input(f'Ходит {name}\n')   
    except SyntaxError:
       pass
    n = randint(1, 28)
    print(f'У вас {n}')
    count += n 
    if count >= candies:
        print(f'Выиграл {name}')
        break
    robot = randint(1, 28)
    count += robot
    print (f'У робота {robot}')
    if count >= candies:
        print('Выиграл Робот')
        break

    print(f'Осталось конфет {candies - count}')
        

        

      