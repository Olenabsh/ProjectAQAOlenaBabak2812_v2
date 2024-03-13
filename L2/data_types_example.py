import math
import random


a = 'hdigk'  #str
b = 1    #int
f = 2.5  #float
g = True  #bool

c = id(b)
print(c)
print(id(b))
e = 21
print(id(e))
print(type(b))

person_name = 'John'
simple_int = 4
second_int = 6
print(simple_int+second_int)
third_int = simple_int+second_int
print(third_int)

print(second_int-1)
print(second_int*5)
print(second_int/2)
print(3**3)
print(2+3*4)
print((2+6)*4)
print(9/4)
print(9//4)
print(11%4)
print(2+2.75)

'''
1. ** (возведение в квадрат или степень)  
2. * , /, // (до цілого числа), %  (до цілого числа)
3. +, -,
'''
new_value = 2+5.11
print(new_value)
small_number = 1.0
smaller_number = 0.00000001
print(0.2+0.1)
first = 2.56987452136
print(round(first, 4))  #ф-ція "round" дозволяє заокруглювати число до певної к-ті знаків після коми
print(dir(math))  #ф-ція dir викликає бібліотеку - опис доступних методів
print(math.pi)     #звертаємося до бібліотеки math (після імпортування) і після крапки вибираємо доступні методи
print(math.cos(0))
print(dir(random))
print(random.randint(2, 7))  #бере рандомний інтежер з вказаного інтервалу
print(random.randrange(15))      #бере рандомний інтежер з вказаного інтервалу від 0 до вказаного числа
print(random.choice(['black', 'white', 'red', 'green']))   #рандомний вибір одного з варіантів
                            # ['black', 'white', 'red', 'green'] в квадратних дужках створюється список
new_string = 'duhvoidj'
new_string2 = "h"
new_string3 = 'f'
new_string4 = "I know him"
new_string5 = 'this is called "Sunday"'
new_string6 = "I know\" him"   #слеш вліво і спецсимвол екранують
print(dir('a'))
message = 'i`m a small message'
print(message.title())
print(message.capitalize())
print(message.upper())
print(message.lower())
first_name = 'Olena'
last_name = 'Babak'
full_name = first_name+last_name  #поєднання 2 строк
print(full_name)
full_name = first_name+' '+last_name  #додати (+) пробіл між словами - (' ') = пробіл між одинарними лапками
print(full_name)
full_name = '\t'+first_name+' '+last_name  #додати табуляцію '\t'
print(full_name)
print('students:\nOlha \nNina') # \n - строка почнеться з нової строчки
print('a python')        #строки чутливі до реєстру
print('A Python')
print('python            '.rstrip())  #видаляє пробіли зправа
print('           python'.lstrip())  #видаляє пробіли зліва
print('         python       '.strip()) #видаляє пробіли зправа i зліва
py_string_example = 'python is a very bad bad bad language'
print('python is very bad language'.replace('bad', 'good'))
print(py_string_example.replace('bad', 'good', 2))
                                            #заміна одного слова на інше + кількість повторення дії
print('bad' in py_string_example) # in дозволяє перевірити наявність елементу в послідовності true or false (= bool значення)
print('good' in py_string_example)
print(type(py_string_example))
print(py_string_example.islower())
print(py_string_example.isupper())
print(py_string_example.startswith('python'))
print(py_string_example.endswith('land'))
print(first_name.isalpha())   #чи складається тільки з літер
one = '1'
print(one.isdigit())
spacial_symbols = '\n\t'
print(spacial_symbols.isspace())
print(spacial_symbols.isprintable())
print(py_string_example.islower(), py_string_example.isspace()) #можна через кому перевірити декілька умов
print(py_string_example.capitalize().startswith('python'))
print(py_string_example.count('bad'))
print(py_string_example.index('bad')) #вказує місце всередені последовності (рахує від 0)але тільки перше входження якщо слово вказане не правильне - виникає помилка
print(py_string_example.find('bat'))  #знаходить місце всередені последовності (рахує від 0) якщо слово вказане не правильно - виставляє -1
print(len(py_string_example))           #точна довжинна строчки
splitted_string = py_string_example.split()
print(splitted_string)                   #розділяє, використовуючи пробіл, всю строку по словам
splitted_string = py_string_example.split('a') #пробіл на початку і в кінці змінює значення
print(splitted_string)
splitted_string = py_string_example.split('very') #ділить стрінгу кожен раз, коли зустрічає значення до кінця;
print(splitted_string)
splitted_string = py_string_example.split('very', 2)  # можна обмежити кількість розділення, поставивши потрібне число
print(splitted_string)
lines_example = 'a\n b\n c'
print(lines_example.splitlines())
print(py_string_example[7]) #виводить елемент згідно індексу , який нам потрібен
print(py_string_example[10:20]) #виводить елементи з по  згідно індексу , який нам потрібен

food = 'Pizza'
cost = 150
str_cost = str(cost)
print('your '+food+' cost is '+str(cost))
print('Your % cost % hryvnias' % (cost, cost))
print('thanks for this{}, here`s your {}'.format(food, cost))
print(f'Happily, I went home with my{food}, and without my{cost} hryvnias')
