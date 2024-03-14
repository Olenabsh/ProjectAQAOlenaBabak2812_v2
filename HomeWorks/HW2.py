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

#Task3fffff
lif birth_month in [9, 10, 11]:
    print('Осінь - Все довкола загоралось яскравими фарбами.')
else:
    print('Некоректне значення для місяця. Будь ласка
