import math

#Task1
first_name = '       olena   '
last_name = 'babak   '
full_name = first_name+' '+last_name

print(full_name.strip().capitalize())
print('\t'+first_name.strip().capitalize()+' '+'\n'+'\t'+last_name.strip().capitalize())

print(full_name.upper())
print(full_name.lower())
print(full_name.title())

#Task2: Створіть програму для обчислення довжини кола та площі круга за введеним радіусом.
# (Використати функцію pi модуля math) Радіус задайте в змінній. Вивести отримані результати,
# використовуючи f-string

radius = 24
length_of_circle = 2*math.pi*radius
area_of_circle = math.pi*radius**2
print(f'Довжина кола становить {round(length_of_circle, 2)}')
print(f'Площа круга становить  {round(area_of_circle, 2)}')

#Task3:
# Створіть змінну що містить поточний курс долара
# Створіть нову змінну що конвертує 1000 гривень в долар
# Заокругліть отримане значення до двох знаків після коми
# Виведіть результат за допомогою форматування (“Поточний курс складає: значення”).

current_rate = 37.56842
amount_uah = 1000
amount_usd = amount_uah/current_rate
print(f'Поточний курс складає: {round(amount_usd, 2)}')



