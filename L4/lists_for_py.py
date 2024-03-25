'''
#трохи з другої домашки
a = 12
b = str(a/6)
c = b.split('.')
if c[1] == '0':
    print('congrats')
else:
    print('disspointment')

 '''
#lists
# Списки - впорядкований набір даних, складається з логічних елементів; відноситься до послідовностей, за властивостями нагадує строки
#Особливості:
# може зберігати будь яку інформацію, але вона обов'яково має бути між собою пов'язана;
# може зберігати різні типи даних, але це маєть бути однотипні дані;
# частіше за все, в назві відображається що це - які дані
# позначається в квадратних дужках [] або list()
# порядковий номер елементів в списку починається з 0
# назви прийнято писати в множині
# оголошення списку (2 варіанти створення) :
#first_list = []
#second_list = list()
'''
cool_fruit = 'watermelon'
fruits = ['apple', 'banana', cool_fruit, 'watermelon', 'cherry', 'watermelon']
print(fruits)
print(type(fruits))
print(id(fruits))
print(len(fruits))
print(fruits[2])   #показує третій елемент в списку
print(fruits[-1])   #показує останній (ДОДАНИЙ) елемент в списку незележно від кількості
print(fruits.index('watermelon', 4)) #шукає з ліва на право і відображає тільки перше входженя (індекс першого знайденого ел-та, всі інші ні)
     #в дужках через кому, можна вказати індекс(номер) елемента з якого (від якого) починати пошук

fruits.append('lemon')  #додавання елемента в список, додається останнім в списку
print(fruits)
print(fruits[-1])  #підтримує індексацію, -1 це завжди останній
fruits.pop()  #видаляє останній елемент в списку
fruits.pop(3) #видаляє за індексом, якщо є назва - знайти індекс, потім видалити за індексом
print(fruits)
del fruits[1] # не рекомдується використувати в пайтон, (видаляє об'єкти за неочивидною чергою, за якою ви очікуєте)
print(fruits)
fruits.clear()  # видалення всього списку
print(fruits)

#відсортуйте список (співбесіда)
first_list = [4,8,9,5,19,14,16,13,17]
print(sorted(first_list))
print(sorted(first_list, reverse=True)) #сортує в зворотньому порядку
print(first_list[4:])  #діапазони індексів -можемо обрати з якого ел-ту відображати список
print(first_list[:4])  #діапазони індексів -можемо обрати до якого ел-ту показувати список
second_list = first_list[:4]  #можемо зробити частину списку іншій змінній
print(second_list)
print(first_list[2:5])
first_list.extend(second_list) #змінні "перший список" змінюється, включає в себе другий список - згідно значення
print(first_list)    #[4, 8, 9, 5, 9, 4, 6, 3, 7, 4, 8, 9, 5]

#цикл for дає мождивість оперативно повторювати ті чи інші дії;
# задати елемент (значення) де саме і що ми хочемо робити;
for element in first_list:
    print(element*2)   #кожен елемент з першого списку помножиться на 2 (але езультат буде виведений в стовбчик)

third_list = []
for element in first_list:
    third_list.append(element*2) #команда  .append щось додає
print(third_list)   #виведе результат помножений на 2 у вигляді списку


third_list = []
for element in first_list:
    third_list.append(element*2)
#через відступ/табуляцію перед print кожен елемент буде доданий в третій список помножений на 2 у вигляді додавання кожного елементу покроково
    print(third_list)

fourth_list = first_list+second_list
print(fourth_list)

a = [1,2,3,4]  #створюючи змінну, ми робимо пряме посилання на комірочку пам'яті, т.я. б=а - списки зміняться одночасно
b = a
a.append(5)
b.append(6)
print(a)
print(b)
# розділитт списки:
c = a.copy() #метод .copy буквально копіює дані змінної і засовує їх в іншу змінну, тепер у них різні айдішники
c.pop()
print(a)
print(c)

e = [1,2]
d = [4,5]
f = e + d
e.pop()
print(f)
e.extend(d)
d.pop()
print(e)
r = list(e) #теж створює нову копію
print(r)
e.pop()
print(r)
print(id(e))
print(id(r))
#для співбесіди:змінювальні/незмінювальні типи даних, мутабельні/немутабельні (приблизно на 55хвилині)
'''

first_list = [2,5,6,6,6,7,8,9] #можемо порахувати скільки конкретних елементів в списку
print(first_list.count(6))
first_list.reverse() #reverse як і сорт - модифікує сам список, відображення в зворотньому порядку [9, 8, 7, 6, 6, 6, 5, 2];
                     #якщо записувати в іншу змінну отримаємо none -> print(first_list.reverse()) ;
print(first_list)
#кортежі - це незмінний список
# #відрізняється способом запису, після створення не має можливості модифікувати - тобто не можемо додавати елемет за допомогою методів;
# використовується в функціях - списки записуються у вигляді таплов;
# ;
first_tuple = (4,5,6,7,8)
print(first_tuple[0])

#цикли -ними можна проходить будь-які послідовності, викоритсовується коли треба повторити якусь дію 1 раз і більше
#основна задача - повторюванні дії;
# цикл for - команди (в тілі циклу) виконуються до тих пір, поки параметр циклу не набуде всіх
# значень що місться в об'єкті, в даному випадку це first_list і ми для кожого елементу проходимось
# по ньому(тобто дивимось надовжину цього списку і по айдішнікам буквально проходимо) ;

element_list = []
for element in first_list:
    if element > 7:
        element_list.append(element)
    #element = element**2
    #print(element)
print(element_list)

#цикл while - блок команд буде виконуватись до тих пір поки умова існує;
#цикл while складається з зарезервованого слова  while та умови, тому блок кода нижче виконується нна кожній ітерації;
#якщо умова не правдива від  початку, блок коду не виконається жодного разу
# i = 10
# while i<50:
#     print(i)
#     i += 10
#коли умова перестане бути правдивою(і стане більше 50) ми вийдемо з циклу - щоб вийти з циклу, треба змінювати значення змінної в середені циклу i += 10;
#якщо змінювати і не в ціклі, ми отримаємо безкінечниий цикл:
#while True:
#     print('Іnfinitе loop')
# є можливість вийти з циклу примусово, незалежно від  умови, для цього використовують break:
#while True:
#     answer = input('Enter yes or no')
#     if answer == 'no':
#         break
#цикл буде присити ввести дані, поки користувач не введе НІ, тоді цикл перерветься;

#while True:                         #т.я. True не змінеться, то цей цикл буде працювати нескіченно, тому варто задати умову,
                                    # наприклад, скільки раз проходити цикл
#    print('help me in stuck in the infinit loop')
counter = 0
while counter<2:
    print('help me in stuck in the infinit loop')
    counter+=1

#спеціальні слова: continue - перехід до наступної ітерації, і ті строки коди що знаходяться після continue,
# на поточній ітерації не виконуються:
# random_num = random.randint(1, 5)    #метод .randint генерує випадкове число в заданому діапазані;
#while True:
#     num = int(input("Guess the number form 1 to 5: "))
#     if num != random_num:
#         print("Try again...")
#         continue
#     print("Congrats!"), random_num)
#     break
#  цикл  if буде виконтуватись завдяки continue поки користувач не вгадає згенероване число, після чого ми вийдем з циклу завдяки  break;

# цикл пройшов по кожному елементу (букві), якщо цей елемент дорівнював 0 - використовувся continue
# continue - починає наступну ітерацію, ігноруючи тіло цикла що йде за ним, тобто все що після continue ігнорується і ми заходимо
# на наступні літеру, в даному випадку ми проігнорували всі "о",
for element in "hello world":
    if element == 'o':
        continue
    print(element)

while counter<20:
    counter += 1         #або додати на самому початку додаєм каунтер, тоді буде змінуватитьякщо треба щоб щось змінилося, то і тут додаєм каунтер
    if counter%2 == 1:
        #counter += 1   #якщо треба щоб щось змінилося, то і тут додаєм каунтер
        continue
    counter += 1
    print(counter)

while counter<30:
    counter += 1         #або додати на самому початку додаєм каунтер, тоді буде змінуватитьякщо треба щоб щось змінилося, то і тут додаєм каунтер
    if counter%2 == 1:
        print('about to break')
        break
    print(counter)
#continue та break можемо комбінувати в середені ціклу з логікою,
# на цьому побудований while - для задання логічної умови за допомогою спец.слів згідно поставленої задачі

for i in 'hello_word':
    if i == "f":
        print("this string have other letters")
        break
    else:
        print(i)
else:
    print("this string have any A letters")

#task 1

entered = 0
while True:
    new_entred = input('Enter your number or sum: ')
    if new_entred == 'sum':
        print(entered)
        break
    elif new_entred.isdigit():
        entered += int(new_entred)
    else:
        print('Not a number')

#task1.2
entered = 0
while True:
    new_entred = input('Enter your number or sum: ')
    if new_entred == 'sum':
        print(entered)
        break
    elif new_entred.startswith('-') and new_entred[1:].isnumeric() or new_entred.isnumeric():
        entered += int(new_entred)
    else:
        print('Not a number')


