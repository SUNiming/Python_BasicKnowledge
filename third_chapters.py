#第三章列表；陈一铭——2017-10-18
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)

#访问列表元素
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[2])
print(bicycles[-1])


#使用列表中的值
bicycles = ['trek','cannondale','redline','specialized']
message = "My favorite bicycle is a "+bicycles[2].title()+'.'
print(message)


#创建一个列表存储朋友姓名，并打印
names = ['Bob','Tim','Jack','Xiao']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[0]+',How are you?')
print(names[1]+',How are you?')
print(names[2]+',How are you?')
print(names[3]+',How are you?')


# 交通工具
transportation = ['bicyle','atuo','motorcycle','aircraft','ship']
message = 'I would like to own a '
print(message+transportation[0])
print(message+transportation[1])
print(message+transportation[2])
print(message+transportation[3])
print(message+transportation[4])


#修改列表元素
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles[-1] = 'yadi'
print(motorcycles)


#向列表中添加新元素,方法append()向列表末尾添加元素
motorcycles = ['honda','yamaha','suzuki']
motorcycles.append('ducati')
print(motorcycles)

#创建一个空列表，使用方法append()向其添加元素
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)


#在列表中任意位置添加元素
motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)
motorcycles.insert(1,'yadi')
print(motorcycles)


#从列表中删除元素（知道元素位置），使用del语句
motorcycles = ['honda','yamaha','suzuki']
del motorcycles[1]
print(motorcycles)



#使用方法pop()删除列表末尾元素，并后续依旧可以使用该弹出的值
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

#最后购买的摩托(假设是按购买时间存储的)
motorcycles = ['honda','yamaha','suzuki']
last_motorcycle = motorcycles.pop()
print("The last motorcycle I owned was a "+last_motorcycle.title()+'.')

#使用方法pop()删除列表中任意位置的元素，需指定元素索引
motorcycles = ['honda','yamaha','suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a '+first_owned.title()+'.')


#不确定元素索引时，只知道元素值时，使用方法remove()
motorcycles = ['honda','yamaha','suzuki']
motorcycles.remove('yamaha')
print(motorcycles)

#方法remove()删除某值后，可继续使用该值，注：方法remove()只删除第一个指定的值；陈一铭——2017-10-19
motorcycles = ['honda','yamaha','suzuki','ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print('A '+too_expensive.title()+' is too expensive for me!')


#动手试一试
invitaion_name = ['Bob','Jack',"Tim",'Tom']
print(invitaion_name)


invitaion_name = ['Bob','Jack','Tim','Tom']
poped_invitation_name = invitaion_name.pop(2)
print(invitaion_name)
print(poped_invitation_name+" can't attend this party.")




invitaion_name = ['Bob','Jack','Tim',"Tom"]
invitaion_name[2] = 'Xiao'
print(invitaion_name)
print('Hi '+invitaion_name[0]+' ,Welcome to this party!')
print('Hi '+invitaion_name[1]+' ,Welcome to this party!')
print("Hi "+invitaion_name[2]+' ,Welcome to this party!')
print('Hi '+invitaion_name[3]+' ,Welcome to this party!')
print("It's nice to find a bigger table!")


# 添加嘉宾
invitaion_name = ['Bob','Jack','Tim','Tom']
invitaion_name.insert(0,'Xiao')
invitaion_name.insert(2,'Chen')
invitaion_name.append('Zhang')
print(invitaion_name)
print("Hi "+invitaion_name[0]+' ,Welcome to this party!')
print('Hi '+invitaion_name[1]+' ,Welcome to this party!')
print('...')
print('There are '+str(len(invitaion_name))+' peopel.')
print("Sorry,I can only choose two guests to attend!")

#缩减名单
invitaion_name = ['Bob','Jack','Tim','Tom']
poped_invitation_name = invitaion_name.pop()
print('Sorry '+poped_invitation_name+',I can only choose two guests to attend!')
poped_invitation_name = invitaion_name.pop(0)
print('Sorry '+poped_invitation_name+',I can only choose two gusest to attend!')
print('Hi '+invitaion_name[0]+',Welcome to this party!')
print("Hi "+invitaion_name[1]+',Welcome to this party!')
print(invitaion_name)
del invitaion_name[0]#注：此时列表中共Jack和Tim，索引为【0】和【1】，当使用del删除Jack后，Tim的索引变为【0】
#print(invitaion_name)
#print(len(invitaion_name))解决由逻辑引起的索引错误
del invitaion_name[0]
print(invitaion_name)




#组织列表，列表元素按一定顺序排列
cars = ['bmw','audi','toyota','subaru']
cars.sort()#方法sort()永久性排序，按字母顺序排列
print(cars)
cars.sort(reverse=True)#向方法sort传递参数reverse=True，可按照字母顺序相反的顺序排列列表元素
print(cars)


cars = ['bmw','audi','toyota','subaru']
print('Here is original list:')
print(cars)
print('\nHere is the sorted list:')
print(sorted(cars))#使用函数sorted()临时对列表进行排序
print('\nHere is the original list:')
print(cars)

cars = ['bmw','audi','toyota','subaru']
print(sorted(cars,reverse=True))#向函数传递参数reverse=True，列表按字母相反的顺序显示
print(cars)




names = ['chen','zhang','he','li','sun','wang']
names.sort()
print(names)
names.sort(reverse=True)
print(names)


alphabet = ['d','a','e','n','x']
print(sorted(alphabet,reverse=True))
print(sorted(alphabet))
print(alphabet)


#倒着打印列表，使用方法reverse()
cars =['bmw','audi','toyota','subaru']
cars.reverse()
print(cars)#注：在打印变量car时并使用方法可以这样写：print(car.title()),而在打印列表时只能这样写：cars.reverse()/print(cars)

#确定列表的长度，使用函数len()
cars = ['bmw','audi','toyota','subaru']
print(len(cars))



#动手试一试
place = ['beijing','shanghai','xizang','sanya','hongkong']
print(place)
print(sorted(place))
print(place)
print(sorted(place,reverse=True))
print(place)
place.reverse()
print(place)
place.reverse()
print(place)
place.sort()
print(place)
place.sort(reverse=True)
print(place)




alphabet = ['w','e','c','o','b','z']
print(sorted(alphabet))
print(sorted(alphabet,reverse=True))
print(len(alphabet))
print(alphabet)
print('There are '+str(len(alphabet))+' words')#函数str()/len()/sorted()








