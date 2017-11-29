# 文件和异常；chenyiming-2017-11-9
# 读取整个文件；
# （1）数据文件存储在程序文件所在的目录
import json

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# 文件路径；Chenyiming-2017-11-10
# （2）相对文件路径：数据文件存储在程序文件所在目录下的一个文件夹中 斜杠（/）和win系统中使用反斜杠（\）

with open('text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

# （3）绝对文件路径：数据文件存储在计算机中的准确位置
# 将文件路径存储在一个变量中，再将变量传递给函数open()

file_path = "/Users/chenyiming/Downloads/study_python.txt"
with open(file_path) as files_object:
    contents = files_object.read()
    print(contents.rstrip())

# 逐行读取，对文件对象使用for循环
file_path = 'text_files/pi_digits.txt'
with open(file_path) as files_object:
    for line in files_object:
        print(line)

# 创建一个包含文件各行内容的列表
# open()返回的文件对象只能在with代码块内使用
file_path = 'text_files/pi_digits.txt'
with open(file_path) as files_object:
    lines = files_object.readlines()

for line in lines:
    print(line)

# 使用文件中的内容

file_name = 'pi_digits.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()  # 删除每行末尾的换行符

print(pi_string)


#  删除原来位于每行左边的空格：strip()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

#  动手试一试；Chenyiming-2017-11-11

file_name = 'learning_python.txt'
with open(file_name) as file_object_0:
    contents = file_object_0.read()
    print(contents.rstrip())

with open('learning_python.txt') as file_object_1:
    for line in file_object_1:
        print(line)
with open('learning_python.txt') as file_object_2:
    lines = file_object_2.readlines()

for line in lines:
    print(line)

with open('learning_python.txt') as file_object_3:
    lines = file_object_3.readlines()

for line in lines:
    new_learning = line.replace('Python', 'C')
    print(new_learning)

#  写入空文件
file_name_0 = 'programming.txt'  # 注：此处文件programming不存在，函数open()自动创建

with open(file_name, 'w') as file_object_4:
    file_object_4.write('I love programming.')

file_name_1 = 'text_files/le_python.txt'  # 注：此处文件le_python中已存在

with open(file_name_1, 'w') as file_object_5:   # 原文件内容为 I love python
    file_object_5.write("I love programming.")  # Python在返回文件对象前清空该文件

#  写入多行文本，write()函数不会在文本末尾添加换行符，需在添加文本末尾指定换行符
with open('text_files/le_python.txt', 'w') as file_object_6:
    file_object_6.write('I love python.\n')
    file_object_6.write('I love creating new games.\n')

#  附加到文件，以附加模式打开文件 ——'a'
with open('text_files/le_python.txt', 'a') as file_object_7:
    file_object_7.write('I also love finding meaning in large datasets.\n')
    file_object_7.write("I love creating apps that can run in a browser.\n")

#  动手试一试
prompt = "Hello,Please enter your name: "

name = input(prompt)
with open('guest.txt', 'w') as file_object_8:
    file_object_8.write(name.title())

prompt = "Hi guys,Please enter your name: "
while True:
    name = input(prompt)
    if name == 'quit':
        break
    print("Hello, " + name.title() + '.')

    with open('text_files/guest_book.txt', 'a') as file_object_9:
        file_object_9.write(name.title() + '\n')

prompt_0 = "Hi,What is your name: "
prompt_1 = "Hi,Why do you like programming? "

messages = {}

active = True
while active:
    name = input(prompt_0)
    if name == 'quit':
        active = False
        continue

    reason_pro = input(prompt_1)
    if reason_pro == 'quit':
        active = False
        continue

    messages[name] = reason_pro

for name, reason in messages.items():
    with open('text_files/reason_programming.txt', 'a') as file_object_10:
        file_object_10.write(name.title() + ': ')
        file_object_10.write(reason + '\n')

#  异常；Chenyiming-2017-11-12

#  pirnt(5/0) 此行代码会引发异常并创建一个异常对象；0不能被除
#  使用try-except代码块处理异常，让python执行指定操作，同时告诉python发生异常时怎么办

#  使用try-except代码块

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

#  捕获错误后程序继续运行
#  使用异常避免崩溃
#  try-except-else代码块，依赖于try代码块中的代码执行成功的代码都应放在else代码块中

print("Give me two numbers,and I'll divide them.")
print("Enter 'quit' to quit.")

while True:
    f_number = input("First Number: ")
    if f_number == 'quit':
        break
    s_number = input("Second Number: ")
    if s_number == 'quit':
        break
    answer = ''
    try:
        answer = int(f_number) / int(s_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")

    except ValueError:
        print("Enter two numbers!Not a word!")

    else:
        print(answer)

# 处理FileNotFoundError异常
file_name_3 = 'yiming chen.txt'

try:
    with open(file_name_3) as f_object_0:
        contents = f_object_0.read()
except FileNotFoundError:
    msg = "Sorry, the file " + file_name_3 + ' does not exist.'
    print(msg)

# 分析文本，方法split()以空格为分隔符将字符串拆分成多个部分，并将其存储到一个列表中
file_name_4 = 'text_files/division.txt'

try:
    with open(file_name_4) as f_object_1:
        contents = f_object_1.read()
except FileNotFoundError:
    print("Sorry, the file " + file_name_4 + 'does not exist.')

else:
    words_0 = contents.split()
    num_words_0 = len(words_0)
    print("The file " + file_name_4 +
          " has about " + str(num_words_0) + ' words.')

# 分析多个文本


def cou_words(file_name):
    """分析文本，统计文本中有多少个单词"""
    try:
        with open(file_name) as f_object_2:
            contents_ = f_object_2.read()
    except FileNotFoundError:
        print("Sorry, the file " + file_name + " does not exist.")

    else:
        # 计算文件大致包含多少个单词
        words_1 = contents_.split()
        num_words_1 = len(words_1)
        print("The file " + file_name +
              " has about " + str(num_words_1) + ' words')


cou_words('text_files/guest_book.txt')


file_names = ['text_files/division.txt',
              'text_files/reason_programming.txt', 'cym.txt']
for file in file_names:
    cou_words(file)

# 捕获异常后一声不吭（什么都不做）Chenyiming-2017-11-14


def count_words(file_name_):
    """计数一个文档中的文字"""
    try:
        with open(file_name_) as f_object_2:
            contents_1 = f_object_2.read()

    except FileNotFoundError:
        pass

    else:
        words_1 = contents_1.split()
        num_words_1 = len(words_1)
        print(str(num_words_1))


file_name = ['text_files/guest_book.txt', 'chenyiming.txt', 'programming.txt']

for file in file_name:
    count_words(file)

#  动手试一试
print("Please enter two numbers,"
      "and return the sum of the two numbers.")
print("Enter 'quit to quit.")

prompt_2 = 'First Number: '
prompt_3 = 'Second Number: '

while True:

    first_number = input(prompt_2)
    if first_number == 'quit':
        break
    second_number = input(prompt_3)
    if second_number == 'quit':
        break

    try:
        answer = int(first_number) + int(second_number)

    except ValueError:
        print("Enter two numbers! Not a word!")

    else:
        print(str(answer))

# with open('text_files/cats.txt', 'a') as f_object_2:
#     f_object_2.write('xiao\n')
#     f_object_2.write('mack\n')
#     f_object_2.write('jack\n')
#
# with open('text_files/dogs.txt', 'a') as f_object_3:
#     f_object_3.write('black\n')
#     f_object_3.write('white\n')
#     f_object_3.write('handsome\n')


def show_contents(file_n):
    """显示文档中的信息"""
    try:
        with open(file_n) as f_o:
            contents = f_o.read()

    except FileNotFoundError:
        print("The file " + file_n + ' is not found.')
        pass  # 捕获异常后程序不显示错误

    else:
        print(contents)


file_lists = ['text_files/cats.txt', 'text_files/dogs.txt']
for content in file_lists:
    show_contents(content)

try:
    with open('text_files/news.txt') as f_o:
        contents = f_o.read()

except FileNotFoundError:
    print("File Not Found.")

else:
    words = contents.split()
    num_words = len(words)
    print(str(num_words))
    numbers = contents.lower().count('the')
    print(numbers)

# 存储数据-json模块;Chenyiming-2017-11-15
# 模块json能够将简单的python数据结构转存到文件中，并在程序再次运行时加载文件
# 使用json.dump()来存储数据————需要两个参数，一个是要存储的数据，另一个是可用于存储数据的文件对象
# 使用json.load()来将数据读取到内存

file_name = 'text_files/numbers.json'

numbers = [2, 4, 5, 9, 0, 5, 1, 6]
with open(file_name, 'w') as f_obj:
    json.dump(numbers, f_obj)


file_name_ = 'text_files/numbers.json'
with open(file_name_) as f_obj_:
    numbers= json.load(f_obj_)
    print(numbers)
# 保存和读取用户生成的数据
file_name_5 = 'text_files/username.json'

username = input("what is your name: ")
with open(file_name_5, 'w') as f_object:
    json.dump(username, f_object)
    print("We'll remember you when you come back, " + username.title() + '.')

file_name_6 = 'text_files/username.json'
with open(file_name_6) as f_object:
    name = json.load(f_object)
    print("Welcome back, " + name.title() + '.')

# 将上面两个程序合并为一个程序

file_name = 'text_files/user.json'

# 如果以前存储了用户名，就加载它，
# 否则，就提示用户输入用户名并存储它

try:
    with open(file_name) as f_object:
        user = json.load(f_object)

except FileNotFoundError:
    user = input("Hi guys,what is your name: ")
    with open(file_name, 'w') as f_object:
        json.dump(user, f_object)
        print("We'll remember you when you come back, " + user.title() + '!')

else:
    print("Welcome back, " + user.title() + ".")

# 重构
# 将代码划分为一系列完成具体工作的函数，这样的过程就被称为重构
# 重构上面的程序


def greet_user():
    """问候用户，并指出其名字"""
    file_name_7 = 'text_files/user.json'

    try:
        with open(file_name_7) as f_obj_0:
            user_0 = json.load(f_obj_0)

    except FileNotFoundError:
        user_1 = input("What's your name: ")
        with open(file_name_7, 'w') as f_obj_1:
            json.dump(user_1, f_obj_1)
            print("We'll remember you when you comeback, "
                  + user_1.title() + '.')

    else:
        print("Welcome back, " + user_0.title() + '.')


greet_user()

# 上面一个函数仍然完成多个任务，再对其进行重构


def get_sorted_user():
    """如果存储了用户名，就获取它"""
    file_name_8 = 'text_files/user.json'
    try:
        with open(file_name_8) as f_obj_2:
            user_2 = json.load(f_obj_2)

    except FileNotFoundError:
        return None

    else:
        return user_2


def greet_user():
    """向用户问好，并指出其名字"""
    user_ = get_sorted_user()
    if user_:
        print("Welcome back, " + user_.title() + '.')
    else:
        file_name_9 = 'text_files/user.json'
        user_3 = input("What's your name: ")
        with open(file_name_9, 'w') as f_obj_3:
            json.dump(user_3, f_obj_3)
            print("We'll remember you when you come back, " +
                  user_3.title() + '.')


get_sorted_user()
greet_user()

# 上面程序还可进行重构，将没有存储用户名时，提示输入用户名时的代码块写成一个独立的函数


def get_sored_user():
    """如果存储了用户名，获取它"""
    file_name_10 = 'text_files/user.json'
    try:
        with open(file_name_10) as f_obj_4:
            user_4 = json.load(f_obj_4)

    except FileNotFoundError:
        return None

    else:
        return user_4


def get_new_user():
    """提示用户输入用户名，并存储它"""
    file_name_11 = 'text_files/user.json'
    user_5 = input("What's your name: ")
    with open(file_name_11, 'w') as f_obj_5:
        json.dump(user_5, f_obj_5)
        return user_5


def greet_user():
    """向用户问好，并指出其名字"""
    user_ = get_sorted_user()
    if user_:
        print("Welcome back, " + user_.title() + '.')
    else:
        user_6 = get_new_user()
        print("We'll remember you when you come back, " +
              user_6.title().title() + '.')


get_sorted_user()
greet_user()

# 动手试一试
# 10-11
fav_number = input("What's your favorite number: ")
# 存储用户喜欢的数字
with open("text_files/fav_number.json", 'w') as f_obj:
    json.dump(str(fav_number), f_obj)

# 加载文件中的数据
try:
    with open('text_files/fav_number.json') as f_object:
        favorite_number = json.load(f_object)

except FileNotFoundError:
    print("File Not Found.")

else:
    print("I know your favorite number! It's " + str(favorite_number) + '.')

# 10-12
try:
    with open('text_files/fav_number.json') as f_obj:
        favorite_number = json.load(f_obj)

except FileNotFoundError:
    fav_number = input("What is your favorite number: ")
    with open('text_files/fav_number.json', 'w') as f_object:
        json.dump(str(fav_number), f_object)

else:
    print("I know your favorite number! It's " + str(favorite_number) + '.')

# 10-13


def get_sorted_user():
    """如果存储了用户名就获取它"""
    try:
        with open('text_files/user.json') as f_object:
            user = json.load(f_object)
    except FileNotFoundError:
        return None

    else:
        return user


def right_name():
    """询问当前用户，用户名是否正确"""
    user_ = get_sorted_user()

    prompt_ = "Is this " + user_.title() + " your user name?(yes/no) "
    answer_ = input(prompt_)

    return answer_


def get_new_user_():
    """提示用户输入用户名，并存储它"""
    user = input("What is your name: ")

    with open('text_files/user.json', 'w') as f_ob:
        json.dump(user, f_ob)

        return user


def greet_user():
    """向用户问好，并指出其名字"""
    user = get_sorted_user()

    if  user:
        print("Welcome back, " + user.title() + '.')
    else:
        user = get_new_user_()
        print("We'll remember you when you come back, " + user.title() + '.')


get_sorted_user()




