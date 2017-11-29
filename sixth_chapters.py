#字典；Chenyiming-2017-10-25
alien_0 = {'color':'green', 'points':5}

print(alien_0['color'])
print(alien_0['points'])

people_0 = {'name':'bob','age':24}

print(people_0['name'])
print(people_0['age'])

#访问字典中的值
alien_0 = {'color':'green','points':5}

new_points = alien_0['points']
print("You just earned "+str(new_points)+' points.\n')

#添加键—值对
alien_0 = {'color':'green','points':5}

print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#创建一个空字典
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

#修改字典中的值
alien_0 = {'color':'green'}
print("The alien is "+alien_0['color']+'.\n')

alien_0['color'] = 'yellow'
print("The anlien is now "+alien_0['color']+'.\n')

#
alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
alien_0['speed'] = 'fast'
print("Original x-positon: "+str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position']+x_increment
print("New x-position: "+str(alien_0['x_position']))

#由类似对象组成的字典；Chenyiming-2017-10-26
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }

print("Sarah's favorite language is "+
      favorite_languages['sarah'].title()+
      '.\n')
for name,language in favorite_languages.items():
    print(name.title()+"'s favorite language is "+language.title()+'.\n')
#动手试一试
personl_massage_0 = {
    'first_name':'t',
    'last_name':'z',
    'age':23,
    'city':'dg',
    }

print(personl_massage_0['first_name'])
print(personl_massage_0['last_name'])
print(personl_massage_0['age'])
print(personl_massage_0['city'])

favorite_digits = {
    'bob':'520',
    'jack':'521',
    'tom':'1314',
    'tim':'8888',
    'sun':'666',
}

print("Is your favorite digit "+
      favorite_digits['bob']+
      ' ?\n'
      )
print("Is your favorite digit "+
      favorite_digits['jack']+
      ' ?\n'
      )
print("Is your favorite digit "+
      favorite_digits['tom']+
      ' ?\n'
      )
print("Is your favorite digit "+
      favorite_digits['tim']+
      ' ?\n'
      )
print("Is your favorite digit "+
      favorite_digits['sun']+
      ' ?\n'
      )

#Chenyiming-2017-10-27
glossary = {
    'condition_test':'一个值为True或Flase的表达式',
    'section':'处理列表部分元素',
    'tuple':'不可变的列表被称作元组',
    'variable':'存储一个值，与变量相关联的信息',
    'ergodic':'对每个元素执行相同操作',
    }
glossary['indent'] = '缩进4个空格'
glossary['pep8'] = 'python 改进提案'
glossary['blank line'] = '在代码适当位置空行，增加可阅读性'
glossary['list parsing'] = '将for循环和创建新元素的代码合并成一行'
glossary['copy list'] = '通过创建一个包含整个列表的切片，同时省略起始索引和终止索引'

print('\ncondition_test: '+glossary['condition_test']+'.\n'
    '\nsection: '+glossary['section']+'.\n'
    '\ntuple: '+glossary['tuple']+'.\n'
    '\nvariable: '+glossary['variable']+'.\n'
    '\nergodic: '+glossary['ergodic']+'.\n')
for word,meaning in glossary.items():
    print("\nWord: "+word)
    print("meaning: "+meaning)

#遍历字典/遍历字典的所有键—值对、键或者值
#遍历所有键-值对
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
    }
for key,value in user_0.items():
    print("\nKey: "+key)
    print("value: "+value)


#遍历字典中所有的键，使用方法keys()
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }

for name in favorite_languages.keys():
    print('\n'+name.title())
#也可这样写
for name in favorite_languages:
    print(name.title())


favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
for name in favorite_languages.keys():
    if name == 'jen':
        print(name.title()+
              "'s favorite language is "+
              favorite_languages[name].title()+
              '.\n')
    elif name == 'phil':
        print(name.title()+
              "'s favorite language is "+
              favorite_languages[name].title()+
              '.\n'
              )
    else:
        print(name.title()+'\n')

#还可以这样写
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'pyhon',
    }

friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("Hi "+
              name.title()+
              ", I see your favorite language is "+
              favorite_languages[name].title()+
              '.\n'
              )

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }

if 'erin' not in favorite_languages.keys():
    print("Erin,please take our poll!\n")

#按顺序遍历字典中的所有键
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phli':'python',
    }

for name in sorted(favorite_languages.keys()):
    print(name.title()+", thank you for taking the poll.\n")

#遍历字典中的所有值
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phli':'python',
    }

print("The following language have been mentioned:")
for language in favorite_languages.values():
    print(language.title()+'\n')
for language in set(favorite_languages.values()):
    print(language.title())

#动手试一试，Chenyiming——2017-10-28；
river_nation = {
    'nile':'egypt',
    'yellow river':'china',
    'the yangtze river':'china',
    }
for river,nation in river_nation.items():
    print("The "+river.title()+" runs thougt "+nation.title()+'.\n')
for river in river_nation.keys():
    print(river.title()+'\n')
for nation in set(river_nation.values()):
    print(nation.title())

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phli':'python',
    }
people_interview = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phli':'python',
    'bob':'c++',
    'tom':'php'
    }
for name in people_interview.keys():
    if name in favorite_languages.keys():
        print(name.title()+", thank you for joining the survey!\n")
    elif name not in favorite_languages.keys():
        print(name.title()+",please take our poll!\n")

#嵌套，
#字典列表；列表中嵌套字典／字典中嵌套列表／字典中嵌套字典
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)
print(aliens)

#自动生成30个外星人
#创建一个空列表存储生成的外星人
aliens = []

#在此处，使用range()函数来确认循环次数，每循环一次，生成一个外星人；
# 再执行循环部分的aliens.append()语句，向列表末尾添加值。
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")

print("Total number of aliens: "+str(len(aliens)))

#修改前三个外星人的颜色、点数和速度
aliens = []

for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15


for alien in aliens[:5]:
    print(alien)
print("...")

#在字典中存储列表
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
    }

print("You ordered a "+pizza['crust']+"-crust pizza "+
      "with the following topping: "
      )
for topping in pizza['toppings']:
    print("\t"+topping)

favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','hsakell'],
    }

for name,languages in favorite_languages.items():
    if len(languages) > 1:
        print("\n"+name.title()+"'s favorite languages are: ")
    else:
        print("\n"+name.title()+"'s favorite language is: ")
    for language in languages:
        print("\t"+language.title())

#字典中存储字典
users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
        },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
        },
    }

for username,user_info in users.items():
    print("\nUsername: "+username)
    fullname = user_info['first']+" "+user_info['last']
    print("\tFullname: "+fullname.title())
    print("\tLocation: "+user_info['location'].title())


#动手试一试
#列表嵌套字典
people_0 = {
    'first_name':'t',
    'last_name':'z',
    'age':23,
    'location':'dg',
    }
people_1 = {
    'first_name':'ym',
    'last_name':'c',
    'age':24,
    'location':'cd',
    }
people_2 = {
    'first_name':'k',
    'last_name':'t',
    'age':18,
    'location':'am',
    }

people = [people_0,people_1,people_2]#注此处不用引号将字典名引起来
for person in people:
    print(person)
    fullname = person['first_name']+person['last_name']
    print("\tFullname: "+fullname)
    print("\tAge: "+str(person['age']))
    print("\tLocation: "+person['location'])
#列表嵌套字典
dogs = {
    'type':'mammal',
    'master_name':'bob',
    }
cats = {
    'type':'mammal',
    'master_name':'tom',
    }
hamsters = {
    'type':'rodent',
    'master_name':'tony',
    }
parrot = {
    'type':'bird',
    'master_name':'jack'
    }

pets = [dogs,cats,hamsters,parrot]#无引号！
for pet in pets:
    print("\nPets: ")
    print("\tType: "+pet['type'])
    print("\tMaster_name: "+pet['master_name'].title())

#字典嵌套列表
favorite_places = {
    'jack': ['beijing','dalian','qingdao'],
    'bob': ['nanjing','shanghai','suzhou'],
    'tom': ['chengdu'],
    }

for name,places in favorite_places.items():
        if len(places) > 1:
            print("\n"+name.title()+"'s favorite places are: ")
        else:
            print("\n"+name.title()+"'s favorite place is: ")
        for place in places:
            print("\t"+place.title())

favorite_digits = {
    'jack': [123,456,789,0],
    'bob': [520,521,1314],
    'tony': [11111],
    'tim': [8888,66],
    'tom': [666],
    }
for name,digits in favorite_digits.items():
    if len(digits) > 1:
        print("\n"+name.title()+"'s favorite digits are: ")
    else:
        print("\n"+name.title()+"'s favorite digit is:")
    for digit in digits:
        print(digit)
#字典嵌套字典
cities = {
    'beijing': {
        'country': 'china',
        'population': '20 million',
        'fact': 'internationl',
        },
    'paris': {
        'country': 'france',
        'population': '10 million',
        'fact': 'romantic',
        },
    'tokyo': {
        'country': 'japan',
        'population': '15 million',
        'fact': 'science and technology'
        },
    }
cities['new york'] = {
    'country': 'usa',
    'population': '25 million',
    'fact': 'finance',
     'areas': '800 sq km',
    }
for name, cities_info in cities.items():

    if len(cities_info.keys()) > 3:
        print("\tAreas: "+cities_info['areas'])
    print("\nThis is information about the city of "+name.title()+':')
    print("\tCountry: "+cities_info['country'].title())
    print("\tPopulation: "+cities_info['population'])
    print("\tFact: "+cities_info['fact'])