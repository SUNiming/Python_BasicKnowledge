#操作列表，遍历整个列表；陈一铭——2017-10-20
magicians = ['alice','dacid','carolina']
for magician in magicians:
    print(magician)#缩进4个空格，注for循环后'：'不能忘记
    print(magician.title()+',that was a great trick!')
    print("I can't wait to see your next trick, "+magician.title()+'.\n')
print("Thank you,everyone.That was a great magic show!")




alphabets = ['a','d','e','m']
for alphabet in alphabets:
    print(alphabet)




#动手试一试
humburgers = ['A','C','O','L']
for humburger in humburgers:
    print(humburger)
    print("I like "+humburger+' pizza!\n')
print("I really like pizza!")
friend_humburgers = humburgers[:]
humburgers.append('H')
friend_humburgers.append('T')
print('\nMy favorite humburgers are:')
for humburger in humburgers:
    print(humburger)
print("\nMy friend's favorite humburgers are:")
for friend_humburger in friend_humburgers:
    print(friend_humburger)


animals = ['dog','cat','pig']
for animal in animals:
    print(animal)
    print("A "+animal+" would make a great pet\n")
print("Any of these animals would make a great pet!")


#创建数值列表，使用函数range()
for value in range(1,5):
    print(value)

#使用函数list()将range()函数生成的结果转换为列表
numbers = list(range(1,6))
print(numbers)


#打印1～10内的偶数
even_numbers = list(range(2,11,2))
print(even_numbers)
even_numbers.pop()
print(even_numbers)


#创建一个列表，1～10的平方
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)


squares = []
for value in range(2,11,2):
    squares.append(value**2)
print(squares)

#对数字列表进行简单的统计计算
numbers = list(range(0,100))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
#列表解析：将for循环和创建新元素合并成一行代码，并自动向列表添加新元素
digits = [value+1 for value in range(0,9)]#这里for循环没有冒号！！！
print(digits)



#动手试一试
for value in range(1,21):
    print(value)


digits = [number+0 for number in range(1,1000001)]#生成1～1000000列表digits，列表解析生成列表
#for digit in digits:
    #print(digit)
print(min(digits))
print(max(digits))

#不能使用函数名、关键字作为变量名或列表名！！！
digits = list(range(1,1000001))#使用函数list()生成列表
#for digit in digits:
    #print(digit)
print(max(digits))
print(min(digits))
print(sum(digits))


#生成1～20内的奇数列表，并遍历；陈一铭——2017-10-21
odd_numbers = list(range(1,21,2))
for odd_number in odd_numbers:
    print(odd_number)
print(odd_numbers)



for odd_number in list(range(1,21,2)):
    print(odd_number)


#3的倍数
multiples = []
for value in range(1,11):
    multiple = 3*value
    multiples.append(multiple)
    print(multiple)
print(multiples)
#还可以这样写
multiples = list(range(3,31,3))
for multiple in multiples:
    print(multiple)


#还可以这样写，列表解析
multiples = [value*3 for value in range(1,11)]#注：此处for循环后没有冒号'：'
print(multiples)
#还可以这样写
multiples = []
for value in range(1,11):
    multiples.append(value*3)
print(multiples)


#1~10的立方，并遍历
cubes = []
for value in range(1,11):
    cube = value**3
    cubes.append(cube)
    print(cube)
print(cubes)

#还可以这样写，列表解析
cubes = [value**3 for value in range(1,11)]
print(cubes)




#使用列表的一部分，切片
players = ['Jack','Tony','Tim','Tom','Bob','Xiao','Chen']
print(players[3:5])
print(players[0:3])
print(players[:2])
print(players[5:])
print(players[-2:])

#遍历切片
players = ['Jack','Tony','Tim','Tom','Bob','Xiao','Chen']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player)


#复制列表；陈一铭——2017-10-22
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
my_foods.append('cannoli')
print(my_foods)
friend_foods.append('ice cream')
print(friend_foods)
for my_food in my_foods:
    print(my_food)
for friend_food in friend_foods:
    print(friend_food)



names = ['jack','tim','tom','bob','tony','Chen']
print("The first two items in the list:")
print(names[:2])
print("\nThe items from the middle of the list are:")
print(names[2:4])
print("\nThe last two items in the list are:")
print(names[4:])
for name in names[:2]:
    print(name.title())
others_names = names[:]
others_names.append('Xiao')
print(others_names)


numbers = []
for value in range(1,11):
    number = value**2
    numbers.append(number)
    print(number)

print(numbers)


#元组，定义一个元组来存储矩形的长和宽,用圆括号！！！
dimensions = (200,50)

print(dimensions[0])
print(dimensions[1])#错误语法——dimensions[0]=400,Python指出不能给元组的元素赋值，即修改值
#遍历元组中的值
dimensions = (200,50)
for dimension in dimensions:
    print(dimension)


#修改元组变量,给存储元组的变量赋值，重新定义整个元组
dimensions = (200,50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)


#动手试一试，缩进，空行，行长
    foods = ('A','B','D','K',"H")
    for food in foods:
        print(food)

    foods = ('E','M','D','K','H')
    for food in foods:
       print(food)








































