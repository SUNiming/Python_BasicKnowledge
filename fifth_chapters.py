#if语句;
cars = ['audi','bmw','subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

alphabets = ['ai','bd','ko','jd']

for alphabet in alphabets:
    if alphabet == 'bd':
        print(alphabet.upper())
    else:
        print(alphabet.title())

#检查是否相等时区分大小写
car = 'bmw'

if car == 'bmW':
    print("True\n")

car = 'Bmw'

if car.lower() == 'bmw':#将变量的转为小写，在进行比较
    print("True\n")

requested_topping = 'mushromms'

if requested_topping != 'anchovies':
    print('Hold the anchovies!')
else:
    print("It's right")

age = 18

if age == 18:
    print("\nTrue")
else:
    print("\nFlase")

#检查是否不相等
answer = 17

if answer != 42:
    print("\nThat is not the correct answer.Please try again!")

#检查多个条件
age_0 = 22
age_1 = 18

if (age_0 >= 21) and (age_1 >= 21):#非必须使用括号，使用括号增加可读性,关键字and
    print("\nTrue")
else:
    print("\nFalse")

age_0 = 22
age_1 = 18

if age_0 >= 21 or age_1 >= 21:#关键字or
    print("\nTrue")
else:
    print("\nFalse")

 #检查特定值是否包含在列表中，使用关键字in
requested_topping = ['mushrooms','onions','pineapple']

if requested_topping[0] in requested_topping:
    print("\nTrue")
else:
    print('\nFalse')

requested_topping = ['mushrooms','onions','pineapple']

if 'pepperoni' in requested_topping:
    print("\nTrue")
else:
    print("False\n")

#检查特定值是否不包含在列表中，使用关键字not in
banned_users = ['andrew','carolina','david']
user = 'marie'

if user not in banned_users:
    print(user.title()+",you can post a response if you wish.\n")

#布尔表达式，条件测试的别名，布尔表达式的结果要么为True，要么为Flase，布尔值通常用于记录条件
game_active = True
can_edit = False

#动手试一试
car = 'subaru'
print("Is car == 'subaru'? I predict True")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
if car == 'audi':
    print('True')
else:
    print('False\n')

print("Is car == 'sUbaru'? I predict False.")
print(car == 'sUbaru\n')

car = 'Subaru'

print("\nIs car == 'subaru'? I predict True.")
print(car.lower() == 'subaru')

print("\nIs car != 'subaru'? I predict True.")
print(car != 'subaru')

number = 18

print("\nIs number == 18 ? I predict True.")
if number == 18:
    print('True')
else:
    print("False")
print(number == 18)

print("\nIs number > 19 ? I predict False.")
print(number > 19)

print("\nIs number < 19 ? I predict True.")
print(number < 19)

print("\nIs number < 19 and number > 17? I predict True.")
print(number > 17 and number < 19)

print("\nIs number < 19 or number > 20? I predict True.")
print(number < 19 or number > 20)

word_1 = 'Hello'
word_2 = 'python'

print(word_1 == word_2)
print(word_1 != word_2)
print(word_1.lower() == 'hello')

number_1 = 18
number_2 = 30

print(number_1 == number_2)
print(number_1 != number_2)
print(number_1 > number_2)
print(number_1 < number_2)
print(number_1 >= number_2)
print(number_1 <= number_2)

if number_1 >= 20 and number_2 >= 20:
    print("True")
else:
    print('False')

if number_1 >= 20 or number_2 >= 20:
    print("True")
else:
    print("False")

names = ['bob','jack','sun','tom','tim']

if 'bob' in names:
    print("True")

if "Chen" not in names:
    print("True")
else:
    print("False")

#简单的if语句；Chenyiming——2017-10-24
age = 19

if age >= 18:
    print("You are old enough to vote!\n")
    print("Have you registered to vote yet?\n")
#if-else语句
age = 17

if age >= 18:
    print("You are old enough to vote\n")
    print("Have you registered to vote yet\n")
else:
    print("You are too young to vote\n")
    print("Please register to vote as soon as you turn 18\n")
#if-elif-else语句
age = 12

if age < 4:
    print("Your admission cost is $0.\n")
elif age < 18 :
    print("Your admission cost is $5.\n")
else:
    print("Your admission cost is $10.\n")
#代码风格，简约清新，可以这样写，可以根据需要使用任意数量的elif代码块
age = 18

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("\nYour admission cost is $"+str(price)+'.')

#省略else代码块
age = 65

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("\nYour admission cost is $"+str(price)+'.\n')

#动手试一试
alien_color = 'green'

if alien_color == 'green':
    print("You got 5 points\n")

alien_color = 'red'

if alien_color == 'green':
    print("You got 5 points\n")

#
alien_color = 'green'

if alien_color == 'green':
    print("You got 5 points\n")
else:
    print("You got 10 points\n")

alien_color = 'red'

if alien_color == 'green':
    print("You got 5 points\n")
else:
    print("You got 10 points\n")

#
alien_color = 'red'

if alien_color == 'green':
    print("You got 5 points\n")
elif alien_color == 'yellow':
    print("You got 10 points\n")
else:
    print("You got 15 points\n")
#还可以这样简洁的写
if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
else:
    points = 15
print("You got "+str(points)+' points.\n')

alien_color = 'green'

if alien_color == 'green':
    print("You got 5 points\n")
elif alien_color == 'yellow':
    print("You got 10 points\n")
else:
    print("You got 15 points\n")

alien_color = 'yellow'

if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
else:
    points = 15
print("You got "+str(points)+' points\n')

#
age = 20
if age < 2:
    print("He is a baby\n")
elif age < 4:
    print("He is learning to walk\n")
elif age < 13:
    print("He is a children\n")
elif age <20:
    print("He is a teenager\n")
elif age < 65:
    print("He is a aldut\n")
else:
    print("He is a aged\n")

#
favorite_friuts = ['apple','banana','grape']
if 'pear' in favorite_friuts:
    print("You really like pears.\n")
if 'apple'in favorite_friuts:
    print("You really like apples.\n")
if 'banana' in favorite_friuts:
    print("You really like bananas.\n")
if 'grape' in favorite_friuts:
    print("You really like grapes.\n")
if 'pineapple' in favorite_friuts:
    print("You really like pineapples.\n")

#if语句处理列表；Chenyiming-2017-10-25
requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    print("Adding "+requested_topping+'.\n')

print("Finished making your pizza!\n")

#检查特殊元素
requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry,we are out of green peppers right now.\n")
    else:
        print("Adding "+requested_topping+'.\n')

print("Finished making your pizza!\n")

#确定列表不是空的
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding "+requested_topping+'.\n')
    print("Finished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

#使用多个列表
available_toppings = ['mushrooms','olives','green peppers','pepperoni',
                      'pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding "+requested_topping+'.\n')
    else:
        print("Sorry,we don't have "+requested_topping+'.\n')

print("Finished making your pizza!\n")

#动手试一试
users = ['bob','jack','tim','admin','tom']

for user in users:
    if user == 'admin':
        print("Hello "+user+',would you like to see a status report?\n')
    else:
        print("Hello "+user+",thank you for logging in again.\n")

users = []

if users:
    for user in users:
        if user == 'admin':
            print("Hello "+user+',would you like to see a status report?\n')
        else:
            print("Hello "+user+"thank you for logging in again.\n")
else:
    print("We need to find some users!\n")

current_users = ['bob','admin','chen','xiao','tim']
new_users = ['jack','Bob','Admin','zhang','tony']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("Please enter another user name!\n")
    else:
        print("This user name is not used,you can use it.\n")

digits = list(range(1,10))

for digit in digits:
    if digit == 1:
        print(str(digit)+'st\n')
    elif digit == 2:
        print(str(digit)+'nd\n')
    elif digit == 3:
        print(str(digit)+'rd\n')
    else:
        print(str(digit)+'th\n')



