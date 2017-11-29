#  函数；Chenyiming-2017-10-31
#  定义函数，使用关键字def

def greet_user():
    """显示简单的问候语"""
    print("Hello!")

greet_user()

# 向函数传递信息
def greet_user(username):
    """显示简单的问候语"""
    print("\nHello, "+username.title()+'!')


greet_user('chen')

#  动手试一试；Chenyiming-2017-11-1


def display_message():
    """显示简单的说明语句"""
    print("\nI'm learning the function")


display_message()

#
def favorite_book(title):
    """显示我最喜欢的书"""
    print("\nOne of my favorite books is "+title.title())


favorite_book('python')

#传递实参
# 位置实参，注：位置实参的顺序很重要，必须实参顺序与形参相同

def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + '.')
    print("My " + animal_type + "'s name is " + pet_name.title() + '.')


describe_pet('hamster', 'harry')
describe_pet('dog', 'bob')  # 调用函数多次

#  关键字实参，由变量名和值组成，是传递给函数的名称-值对

def describe_pets(animal_tpye, pet_name):
    """显示宠物信息"""
    print("\nI have a " + animal_tpye + '.')
    print("My " + animal_tpye + "'s name is " + pet_name.title())


describe_pet(animal_type='hamster',pet_name='harry')


#  默认值

def describe_pet(pet_name, animal_type='dog'):
    """显示宠物信息"""
    print("\nI have a " + animal_type + '.')
    print("My " + animal_type + "'s name is " + pet_name.title() + '.')


describe_pet(pet_name='harry')
describe_pet('willie')
describe_pet(animal_type='bird',pet_name='fly')

#  等效的函数调用


def describe_pet(pet_name, animal_type='dog'):
    """显示宠物信息"""
    print("\nI have a " + animal_type + '.')
    print("My " + animal_type + "'s name is " + pet_name.title())


describe_pet('jack', 'cat')  #位置实参
describe_pet(pet_name='bob', animal_type='pig')  # 关键字实参
describe_pet(animal_type='pig',pet_name='bob')  # 关键字实参，顺序无关紧要
describe_pet('tom')  # 使用形参默认值／位置实参
describe_pet(pet_name='tim')  # 使用形参默认值／关键字实参

#  动手试一试

def make_shirt(size, message='sport'):
    """显示T恤信息"""
    print("\nI have a T-shirt printed with " +
          message + ", and the size is " +
          size.title() + '.')


make_shirt('l', 'fun')
make_shirt(message='happy', size='xl')
make_shirt('s')
make_shirt(size='m')


def make_shirt(size='l', message='python'):
    """显示T恤信息"""
    print("\nI love " + message.title() +
          ", and t-shirt size is " +
          size.title() + '.')


make_shirt()
make_shirt(size='m')
make_shirt(message='sport')
make_shirt(message='happy', size='s')
make_shirt('xll', 'sun')


def describe_city(city_name,nation='china'):
    """显示城市信息"""
    print(city_name.title() + " is in " + nation.title() + '.\n')


describe_city('chengdu')
describe_city(city_name='shenzhen')
describe_city('new york', 'usa')

#  返回值

def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

name = get_formatted_name(first_name='yiming', last_name='chen')
print(name)

#  让实参可选；Chenyiming-2017-11-2
#  一个人名，如果提供中间名，这样写：


def get_formatted_name(first_name, middle_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()


name = get_formatted_name('yi', 'ming', 'chen')
print(name)

#  错误示例：
#  name = get_formatted_name(first_name='yiming',last_name='chen')
#  print(name)  #函数调用传递实参错误，缺少一个实参

#  让中间名可选，可将形参middle_name的默认值指定为空字符串


def get_formatted_name(first_name,last_name,middle_name=''):
    """返回整洁的姓名"""
    if middle_name:  # python将非空字符串解读为True
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name

    return full_name.title()

name = get_formatted_name(first_name='yi',middle_name='ming',last_name='chen')
print(name)  # 注：位置实参 传递实参时 注意实参顺序与形参对应

sun = get_formatted_name(first_name='yiming',last_name='chen')
print(sun)

#  返回字典


def bulid_person(first_name,last_name):
    """返回一个字典，其中包含一个人的信息"""
    person = {'first':first_name, 'last':last_name}
    return person


name = bulid_person(first_name='yiming', last_name='chen')
print(name)

#  扩展上面的程序，使其有可选项


def bulid_person(first_name, last_name, middle_name='',
                 age='',  career='',  location=''):
    """返回一个字典，其中包含一个人的信息"""
    person = {'first':first_name, 'last':last_name}

    if middle_name:
        person['middle'] = middle_name
    if age:
        person['age'] = age
    if career:
        person['career'] = career
    if location:                           # 运行多个代码块，使用一系列的if语句；
                                           # 运行一个代码块使用if-elif-else
        person['location'] = location
    return person

people = bulid_person(first_name='yiming', last_name='chen',
                      location='chengdu', age='18')
print(people)


#
def bulid_person(first_name,last_name,age=''):
    """返回一个字典，其中包含一个人的信息"""
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person

people = bulid_person('yiming','chen')
print(people)

people = bulid_person(first_name='yiming',last_name='chen',age='18')
print(people)

#
def bulid_color_list(color_0,color_1='',color_2='',color_3=''):
    """返回一个列表，包含各种颜色信息"""
    colors = [color_0]
    if color_1:
        colors.append(color_1)
    if color_2:
        colors.append(color_2)
    if color_3:
        colors.append(color_3)
    return colors

color_list = bulid_color_list('green','red','whiht','black')
print(color_list)


#  结合使用函数和while循环

def get_formatted_name(first_name,last_name,middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name

    return full_name.title()

while True:
    print("\nPlease tell me your name: ")
    print("enter 'quit' at any time to quit.")
    f_name = input("First name: ")
    if f_name == 'quit':
        break
    l_name = input("Last name: ")
    if l_name == 'quit':
            break

    question = input("Do you have middle name:(yes/no)")
    if question == 'yes':
        m_name = input("Middle name:")
        formatted_name = get_formatted_name(f_name, l_name,m_name)
        print("Hello, " + formatted_name + '.')
    elif question == 'no':
        formatted_name = get_formatted_name(f_name,l_name)
        print("Hello, "+formatted_name+'.')

#  动手试一试

def city_country(city,country):
    """显示城市信息"""
    city_message = city.title() + ', ' + country.title() + '.'
    return city_message

city_0 = city_country('beijing','china')
print(city_0)

city_1 = city_country('new york','usa')
print(city_1)

city_2 = city_country(city='tokyo',country='japan')
print(city_2)

def make_album(singer_name,album_name,numbers_songs=''):
    """返回一个字典，包含音乐专辑信息"""
    album_message = {'singer_name':singer_name,'album_name':album_name}
    if numbers_songs:
        album_message['numbers_songs'] = numbers_songs

    return album_message

album_message_0 = make_album('jay chou','s_m_i')
print(album_message_0)

album_message_1 = make_album(singer_name='jay chou',
                             album_name="i'm busy",numbers_songs='10')
print(album_message_1)

#  动手试一试；Chenyiming-2017-11-3

def make_album(singer_name,album_name):
    """返回一个字典，显示音乐专辑信息"""
    album_message = {'singer_name':singer_name,'album_name':album_name}
    return album_message

prompt_0 = "\nHello,who is your favorite singer? "
prompt_1 = "Do you konw the name one of these albums?"

while True:                 #此处使用break退出循环
    s_name = input(prompt_0)
    if s_name == 'quit':
        break

    a_name = input(prompt_1)
    if a_name == 'quit':
        break

    album_message_0 = make_album(s_name,a_name)
    print(album_message_0)


#  向函数传递列表

def greet_users(names):
    """向列表中的每位用户发出简单问候"""
    for name in names:
        greet_message = "Hello, " + name.title() + '!'
        print(greet_message)

usernames = ['bob','jack','tony']
greet_users(usernames)


#  在函数中修改列表

def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        #模拟根据设计制作3D打印模型的过程
        print("Printing model: "+current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示所有打印好的模型"""
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)


#  动手试一试

def show_magicians(magicians):
    """显示列表中的每位魔术师"""
    for magician in magicians:
        print(magician.title())

magicians_list = ['bob','jack','tom','tim','tony']
show_magicians(magicians_list)

#
def show_magicians(magicians):
    """显示列表中的每位魔术师"""
    for magician in magicians:
        print(magician.title())

def make_great(modify_magicians,modified_magicians):
    """对列表进行修改，在每个名字前加上其他信息"""
    while modify_magicians:
        words = 'the Great'
        current_magician = words + ' ' + modify_magicians.pop()
        modified_magicians.append(current_magician)
    return modified_magicians

magicians_list = ['bob','jack','tom']
modified_magicians = []

copy_magicians_list = make_great(magicians_list[:],modified_magicians)  #  此处使用列表副本，可保留原列表
show_magicians(copy_magicians_list)                                     #  使用返回值
show_magicians(magicians_list)                                          #  确认是原来列表，函数没有修改列表

make_great(magicians_list,modified_magicians)         #  在上面代码运行后，此处
show_magicians(modified_magicians)                    #  modified_magicians列表中已有元素，所有此处运行有6个值


#  传递任意数量的实参
#  不知道函数要接受多少个实参
def make_pizza(*toppings):            #'*'——星号让python创建一个名为toppings的空元组，并将值封装到元组中
    """打印顾客点的所有配料"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')


def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print('\t-' + topping)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')


#  结合使用位置实参和任意数量实参
#  让函数接受不同类型的实参，将函数定义中的能够接纳任意数量的形参放在最后

def make_pizza(size,*toppins):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings: ")
    for toppin in toppins:
        print('\t-' + toppin)

make_pizza('16','pepperoni')
make_pizza('12','mushrooms','green peppers', 'extra cheese')

#  使用任意数量的关键字实参；Chenyiming-2017-11-4

def build_profile(first,last,**user_info):  #  两个星号（**）让python创建一个名为user_info的空字典
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('yiming','chen',
                             loaction='chengdu',age='18',field='computer')
print(user_profile)

#  动手试一试

def make_sandwich(*toppings):
    """打印顾客所点的配料"""
    print("\nMaking a sandwich with the following toppings: ")
    for topping in toppings:
        print('-' + topping)

make_sandwich('apple')
make_sandwich('banana','butter','pear')
make_sandwich('apple','butter','pear','banana','grape')

def build_profile(first,last,**my_info):
    """创建一个字典，包含个人的信息"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key ,value in my_info.items():
        profile[key] = value
    return profile

my_profile = build_profile('yiming','chen',
                           school='CNU',location='chengdu',
                           age='18',field='computer')
print(my_profile)

def make_car(maker, model, **car_info):
    """创建一个字典，包含汽车的信息"""
    cars = {}
    cars['manufacturer'] = maker
    cars['vision'] = model
    for key, value in car_info.items():
        cars[key] = value

    return cars

cars_info = make_car('mazda', 'outback', color='white', tow_package=True)
print(cars_info)

#  将函数存储在模块中或着叫独立文件中，可将模块导入主程序中，
#  见function_module_eighth_chapters
