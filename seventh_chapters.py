#用户输入和 while循环；Chenyiming-2017-10-29
message = input("Tell me something,and I will repeat it back to you: ")
print(message)
#编写清晰的程序
name = input("Please enter your name: ")
print("Hello, "+name.title()+".")
#提示超过一行，可将提示存储在一个变量中，再将该变量传递给函数input()
prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("Hello, "+name.title()+'!')

#int()函数将数字的字符串表示转换为数值表示

height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")


prompt = "\nWelcome to this bar!"
prompt +="\nHow old are you? "

age = input(prompt)
age = int(age)

if age >= 18 and age < 70:
    print("\nWelcome to this bar,have a good time!")
elif age >= 70:
    print("\nYou should go to the park!")
else:
    print("\nYou are too young to enter!")

#求模运算符%，两个数相除只会返回余数，判断一个数是奇数还是偶数
number = input("\nEnter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number "+str(number)+' is even.')
else:
    print("\nThe number "+str(number)+' is odd.')

#在python2.7中使用函数raw_input()来提示用户输入，也将输入解读为字符串。
#动手试一试
cars = input("\nWhat kind of car do you want to rent? ")
print("\nLet me see if I can find you a "+cars.title()+'.')

number_people = input("\nHow many people have dinner? ")
number_people = int(number_people)

if number_people > 8:
    print("\nNo empty table for "+str(number_people)+" people.")
else:
    print("\nEmpty tables to accommodate "+str(number_people)+" people.")

number = input("\nPlease enter a number: ")
number = int(number)

if number % 10 == 0:
    print("\nThe number "+str(number)+" is an integer multiple of 10.")
else:
    print("\nThe number "+str(number)+" isn't an integer multiple of 10.")


#while循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number = current_number + 1  #也可写做current_number += 1

#让用户选择何时退出
prompt = '\nTell me something,and I will repeat it back to you: '
prompt += "\nEnter 'quit' to end the program. "

message = " "
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)


#使用标志；Chenyiming-2017-10-30；
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

#使用break退出循环
prompt = "Please enter the name of a city you have visited: "
prompt += "\nEnter 'quit' when you are finished."

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("\nI'd love to go to "+city.title()+'.\n')

#在循环中使用continue，返回到循环开头，并根据条件测试结果决定是否继续执行循环
#将1～10中的奇数打印出来
current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

#避免无限循环
#x = 1
#while x < 5:
#   print(x)

#动手试一试
prompt = "\nPlease input a series of pizza ingredients you need: "

active = True
while active:
    ingredient = input(prompt)
    if ingredient == 'quit':
        active = False
    else:
        print("\nWe'll add "+ingredient+" ingredient to pizza.")


prompt = "How old are you? "
prompt += "\nAnd tell you how much the movies costs."

active = True  #这里使用标志，判断程序是否处于活动状态

while active:
    age = input(prompt)
    if age == 'quit':
        active = False
        print("\nThank you for using*_*")
    elif int(age) < 3:
        print("\nThe moive fare is $0.")
    elif int(age) <= 12:
        print("\nThe movie fare is $10.")
    elif int(age) > 12:
        print("\nThe movie fare is $15.")

#在while循环中使用条件测试
prompt = "\nPlease input a series of pizza ingredients you need: "

ingredient = ''
while ingredient != 'quit':
    ingredient = input(prompt)
    if ingredient != 'quit':
        print("\nWe'll add "+ingredient+" ingredient to pizza.")

#使用break退出循环
prompt = "\nHow old are you? "
prompt += "\nAnd tell you how much the movie costs."
price = 0

while True:
    age = input(prompt)
    if age == 'quit':
        print("\nThanks for using!")
        break
    elif int(age) < 3:
        price = 0
    elif int(age) <= 12:
        price = 10
    elif int(age) > 12:
        price = 15
    print("\nThe movie fare is $"+str(price)+'.')

#在while循环中使用条件测试
prompt = "\nHow old are youuu 😄? "
prompt += "\nAnd tell you how much the moive costs."

age = ''
while age != 'quit':
    age = input(prompt)
    if age == 'quit':
        print("\nThanks for using ^_^")
    elif int(age) < 3:
        print("\nThe movie fare is $0..")
    elif int(age) <= 12:
        print("\nThe movie fare is $10..")
    elif int(age) > 12:
        print("\nThe movie fare is $15..")

#在列表之间移动元素
#首先创建一个待验证的用户列表
#和一个用户存储已验证用户的空列表

unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("\nVertifying user: "+current_user)
    confirmed_users.append(current_user)

print("\nThe following users have benn confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user)

#删除包含特定值的所有列表元素
pets = ['cat','dog','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)