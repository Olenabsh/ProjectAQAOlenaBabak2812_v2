import math
import random


 #Task1
min = random.randint(0, 59)
if min < 15:
    print("Перша чверть години")
elif min < 30:
    print("Друга чверть години")
elif min < 45:
    print("Третя чверть години")
else:
    print("Четверта чверть години")

#Task2

birth_month = int(input('Enter your month of birth: '))

if birth_month in [12, 1, 2]:
    print('Зима - За вікном падав сніг.')
elif birth_month in [3, 4, 5]:
    print('Весна - Все довкола розцвітало')
elif birth_month in [6, 7, 8]:
    print('Літо - Діти насолоджувались літніми канікулами.')
elif birth_month in [9, 10, 11]:
    print('Осінь - Все довкола загоралось яскравими фарбами.')
else:
    print('Некоректне значення для місяця. Будь ласка, введіть число від 1 до 12.')

#Task3

number = random.randint(1, 1000)

print(f"Згенероване число: {number}")

# Перевірити умови діленості на 6
last_digit = number % 10
sum_of_digits = sum(map(int, str(number)))

if last_digit % 2 == 0 and sum_of_digits % 3 == 0:
    print(f"Число {number} ділиться на 6")
else:
    print(f"Число {number} не ділиться на 6")


#Task4

# Вести координати точки
x = float(input("Введіть координату x точки: "))
y = float(input("Введіть координату y точки: "))

# Визначити до якої координатної чверті належить точка
if x == 0 and y == 0:
    print("Точка знаходиться у початку координат")
elif x == 0:
    print("Точка лежить на осі Y")
elif y == 0:
    print("Точка лежить на осі X")
elif x > 0 and y > 0:
    print("Точка належить до першої координатної чверті")
elif x < 0 and y > 0:
    print("Точка належить до другої координатної чверті")
elif x < 0 and y < 0:
    print("Точка належить до третьої координатної чверті")
else:
    print("Точка належить до четвертої координатної чверті")