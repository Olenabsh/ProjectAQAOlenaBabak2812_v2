new_value = True
false_value = False
#це фун-ї перетворення, базові типи можна між собою перетворювати
# ці фун-ції не перетворюють одні об'єкти на їнші, а створюють копії на основі старих об'єктів.
#бульові значення можна перетворювати в інти
print(int(new_value))
print(int(false_value))
print(bool(1))
print(bool(0))
a = 0
b = bool(3)  #все що більше 1 - це True
print(b)

new_string = 'dnifu'  # перетворення стрінги в булеве значення; все що не пусте - це True;
empty_string = ''
print(bool(new_string))
print(bool(empty_string))

#логічні оператори, оператори порівняння
'''
<
>
<=
>=
== рівність між собою
!=  нерівність між собою
'''
c = 100
d = 200
print(c>d)
print(c<d)
print(c>=d)
print(c<=d)
print(c==d)
print(c!=d)

 #оператор input дозволяє приймати  введених користувачем даних з клавіатури в процесі виконання програми.
 #input завжди повертає стрінгу;
'''
value_to_read = input('print value immediately')
print(value_to_read)

#щоб перетворити - додати догіку з умовними операторами if  та else
value_to_read = input('print value immediately')
if value_to_read.isdigit():
    print(int(value_to_read))
else:
 print('it`s not an integer')
'''
'''
#practis task: знайти модуль - якщо більше 0 - друк, якщо меньше 0 - помножити на -1
test_value = int(input('your number is: ')) #поставивши int (integer) перед input - ми перетворюємо строку на число
if test_value > 0:
 print(test_value)
else:
 print(test_value*(-1))
'''

#task2 число складається з 2 чисел чи більше (ще можна через довжину строки)
'''
numbers = int(input('tell me your number'))
if numbers > 9:
 print("your number has 2 numbers or more")
else:
 print('your number has 1 number')
'''
'''
#логічні оператори
#or -якщо хоч 1 умова виконується
# and -обидві умови виконуються
# not -умова не виконується

value_to_read = int(input('print value immediately'))
if value_to_read>30 or value_to_read<20:
 print('oh ye')

if value_to_read>200 and value_to_read % 20 == 0:  #%20==0 залишок% ділення на 20 = 0,
  print('oh no')
 # умов з if може бути необмежена кількість, але чим більше умов тим складніше опрацювувати

if not value_to_read:
 print('ok')

if not empty_string:     #за допомогою if not можна також зробити перевірку на пусту строку: if not і кидаєш строку для перевірки
    print('oki')
'''
'''
#вкладенсті і elif

str_input = input('go!')

if str_input.startswith('Hello'):
    print('Hello my dear')
elif str_input.isdigit() and not str_input.startswith('2'):
    print('oh I didn`t see you')
elif str_input.startswith('2'):
    print('second')
else:
    print('you typed invalid value')
'''

#метод вкладеності- блоків логіки можна вставляти скільки хочеш
'''
eyes = int(input('how many eyes?'))
legs = int(input('how many legs?'))
if eyes >=8:
    if legs ==8:
        print('spider')
    elif legs ==6:
        print('cockroach')
    else:
        print('underfined creature')
else:
    if eyes == 2 and legs == 4:
        print('defenitly cat')
    else:
        print('horror our comprehension')
'''





