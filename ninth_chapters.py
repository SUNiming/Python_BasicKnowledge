#  类
#  创建Dog()类；chenyiming-2017-11-5


class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")

#  python2.7中创建类：class ClassName(object):
#  根据类创建实例
#  访问实例的属性，句点表示法


my_dog = Dog('bob', 3)  # 根据类创建实例，类中方法__init__()未显式包含return语句，
#  但python自动返回一个实例，存储在变量my_dog 中
print("\nMy dog's name is " + my_dog.name.title() + '.')
print("My dog is " + str(my_dog.age) + " years old.")

#  调用类中的方法，使用句点表示法
my_dog.sit()
my_dog.roll_over()

#  创建多个实例
your_dog = Dog('tony', 2)
his_dog = Dog('jack', 6)

print("\nYour dog's name is " + your_dog.name.title() + '.')
print("Your dog is " + str(your_dog.age) + 'years old.')
your_dog.sit()
your_dog.roll_over()

print("\nHis dog's name is " + his_dog.name.title() + '.')
print("His dog is " + str(his_dog.age) + "years old.")
his_dog.sit()
his_dog.roll_over()

#  动手试一试


class Restaurant:
    """模拟餐馆"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """简单描述餐馆信息"""
        print("\nThe name of the restaurant is " +
              self.restaurant_name.title() + '.')
        print("The cuisine of the restaurant is " +
              self.cuisine_type.title() + '.')

    def open_restaurant(self):
        """餐馆正在营业中"""
        print("The restaurant is in business. ")


restaurant_0 = Restaurant('cym', 'sichuan food')

print(restaurant_0.restaurant_name.title())
print(restaurant_0.cuisine_type.title())

restaurant_0.describe_restaurant()
restaurant_0.open_restaurant()

restaurant_1 = Restaurant('ym', 'gd food')
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant('m', 'hn food')
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant('sun', 'hotpot')
restaurant_3.describe_restaurant()

#  动手试一试；Chenyiming-2017-11-6


class User:
    """模拟用户"""
    def __init__(self, first_name, last_name, age, location, career):
        """初始化属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.career = career

    def describe_user(self):
        """显示用户的信息"""
        print("\nUsers information is as follows: ")
        print('\t-Full_name: ' + self.first_name.title() +
              ' ' + self.last_name.title() + '.')
        print("\t-Age: " + str(self.age))
        print("\t-Location: " + self.location.title())
        print("\t-Career: " + self.career.title())

    def greet_user(self):
        """向用户打招呼"""
        print("Hello, " + self.first_name.title() +
              ' ' + self.last_name.title() + '!')


user_0 = User('yiming', 'chen', 18, 'cheng du', 'student')
user_1 = User('sun', 'c', 19, 'guang yuan', 'worker')
user_2 = User('tony', 'm', 20, 'hk', 'teacher')

user_0.describe_user()
user_0.greet_user()

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()


class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 给属性指定默认值，就无需包含为它提供初始值的形参

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = '\n' + str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer! ")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer! ")


my_new_car = Car('audi', 'a4', 2017)
print('\n' + my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#  修改属性的值
#  (1)通过实例进行修改属性的值

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#  (2)通过方法修改属性的值
#  在Car类中添加一个新的方法update_odometer()

my_new_car.update_odometer(28)  # 通过实例调用方法update_odometer()修改属性值
my_new_car.read_odometer()

#  (3)通过方法对属性的值进行递增
#  在Car类中添加一个新的方法increment_odometer()

my_used_car = Car('mazda', 'outback', 2016)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(111110)
my_used_car.read_odometer()

my_used_car.increment_odometer(5550)
my_used_car.read_odometer()

#  动手试一试


class Restaurant:
    """模拟餐馆"""
    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """显示餐馆的简单信息"""
        print("\nThe name of the restaurant is " +
              self.restaurant_name.title() + '.')
        print("The cuisine of the restaurant is " +
              self.cuisine_type.title() + '.')

    def open_restaurant(self):
        """餐馆正在营业"""
        print("The restaurant is in business. ")

    def show_dining(self):
        """显示就餐人数信息"""
        print("There were " + str(self.number_served) +
              " people in the restaurant who had eaten.")

    def set_number_served(self, person_number):
        """将就过餐的人数设置为指定的人数"""
        if person_number >= 0:
            self.number_served = person_number
        else:
            print("Illegal Input!")

    def increment_number_served(self, person):
        """将人数增加指定人数"""
        if person >= 0:
            self.number_served += person
        else:
            print("Illegal Input!")


restaurant_4 = Restaurant('sun.c', 'sh food')

restaurant_4.describe_restaurant()
restaurant_4.show_dining()  # 此时属性值为默认值

restaurant_4.number_served = 10  # 通过实例直接访问属性修改其值
restaurant_4.show_dining()

restaurant_4.set_number_served(60)  # 通过定义新的方法来修改属性的值
restaurant_4.show_dining()

restaurant_4.increment_number_served(10)  # 通过方法对属性的值进行递增
restaurant_4.show_dining()


class User():
    """模拟用户"""
    def __init__(self, first_name, last_name, age, location, career):
        """初始化属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.career = career
        self.login_attempts = 0

    def describe_user(self):
        """显示用户信息摘要"""
        print("\nUsers is information as follows: ")
        print("\t-Full Name: " + self.first_name.title() +
              self.last_name.title() + '.')
        print("\t-Age: " + str(self.age))
        print("\t-Location: " + self.location.title())
        print("\tCareer: " + self.career.title())

    def greet_user(self):
        """向用户打招呼"""
        print("Hello, " + self.first_name.title() +
              self.last_name.title() + '!')

    def increment_login_attempts(self):
        """将登陆尝试次数增加1次数"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """将尝试登陆次数重置为0"""
        self.login_attempts = 0


user_3 = User('ym', 'c', 18, 'cheng du', 'student')

user_3.increment_login_attempts()
print(user_3.login_attempts)

user_3.increment_login_attempts()
print(user_3.login_attempts)

user_3.increment_login_attempts()
print(user_3.login_attempts)

user_3.reset_login_attempts()
print(user_3.login_attempts)

#  继承;Chenyiming-2017-11-7
#  子类的方法__init__()


class Car:
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + 'miles on it')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            return self.odometer_reading
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
print(my_tesla.update_odometer(1000))

#  Python2.7中的继承,函数super需要两个实参：子类名和对象self，将父类和子类关联起来
# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super(ElectricCar, self).__init__(make, model, year)

#  给子类定义属性和方法


class ElectricCar(Car):
    """电动汽车独特之处"""
    def __init__(self, make, model, year):
        """初始化父类属性，在初始化特有属性"""
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kwh battery.")


my_tesla_1 = ElectricCar('tesla', 'model s', 2017)
print(my_tesla_1.get_descriptive_name())
my_tesla_1.describe_battery()

#  重写父类的方法，在子类中定义一个方法，与父类方法同名，
#  python会不考虑父类的方法，而使用子类中定义的同名方法
#  若Car类中有方法fill_gas_tank(),在电动汽车中没有油箱，则重写父类的方法，如下：


class ElectricCar(Car):
    """电动汽车独特之处"""
    def __init__(self, make, model, year):
        """初始化父类属性，再初始化特有属性"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """电动车没有油箱"""
        print("This car doesn't need a gas tank.")


#  将实例用作属性；Chenyiming-2017-11-8
#  将电池作为一个类，其实例用作ElectricCar类的一个属性

class Battery():
    """模拟汽车电池"""
    def __init__(self, battery_size=70):
        """初始化电池属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    def get_range(self):
        """打印一条消息，指出电池的续航里程"""
        if self.battery_size == 70:
            range_ = 240
        elif self.battery_size == 85:
            range_ = 270

        message = "This car can go approximately " + str(range_)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """检查电池容量"""
        if self.battery_size != 85:
            self.battery_size = 85


my_tesla_2 = ElectricCar('tesla', 'model p90d', 2017)
print(my_tesla_2.get_descriptive_name())

my_tesla_2.battery.describe_battery()
my_tesla_2.battery.get_range()

my_tesla_3 = ElectricCar('tesla', 'model p90d', 2016)
my_tesla_3.battery.get_range()

my_tesla_3.battery.upgrade_battery()
my_tesla_3.battery.get_range()

#  动手试一试


class Restaurant():
    """模拟餐馆"""
    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """描述餐馆的信息"""
        print("\nThe name of the restaurant is " +
              self.restaurant_name.title() + '.')
        print("The cuisine of the restaurant is " +
              self.cuisine_type.title() + '.')

    def open_restaurant(self):
        """餐馆正在营业"""
        print("The restaurant is in business.")


class IceCreamStand(Restaurant):
    """冰淇淋小店的特殊之处"""
    def __init__(self, restaurant_name, cuisine_type, various_icecream):
        """初始化父类属性"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = various_icecream

    def show_various_icecream(self):
        """显示各种各样的冰淇淋"""
        print("The taste of ice cream is as follows: ")
        for flavor in self.flavors:
            print("\t-" + flavor.title())


serveral_icecream = ['sweet', 'buttery', 'chocolates']
flavors_0 = IceCreamStand('ice', 'western food', serveral_icecream)

flavors_0.describe_restaurant()
flavors_0.show_various_icecream()


class User():
    """模拟用户"""
    def __init__(self, first_name, last_name, age, location, career):
        """初始化描述用户的属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.career = career

    def describe_user(self):
        """简单描述用户信息"""
        print("\nUsers information is as follows: ")
        print("\t-Full Name: " + self.first_name.title() + ' ' +
              self.last_name.title())
        print("\t-Age: " + str(self.age))
        print("\t-Location: " + self.location)
        print("\t-Career: " + self.career)

    def greet_user(self):
        """向用户打招呼"""
        print("Hello, " + self.first_name.title() +
              ' ' + self.last_name.title())


class Admin(User):
    """特殊用户——管理员"""
    def __init__(self, first_name, last_name, age, location, career, freedom):
        """初始化父类属性"""
        super().__init__(first_name, last_name, age, location, career)
        self.privileges = freedom

    def show_privileges(self):
        """显示特权信息"""
        print("Privileges are as follows: ")
        for privilege in self.privileges:
            print('\t-' + privilege)


liberty = ['can add post', 'can delete post', 'can ban user']
user_4 = Admin('yiming', 'chen', 18, 'cheng du', 'student', liberty)

user_4.describe_user()
user_4.greet_user()
user_4.show_privileges()


class Privileges():
    """模拟管理员特权"""
    def __init__(self, privileges):
        """初始化属性"""
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges are as follows: ")
        for privilege in self.privileges:
            print("\t-" + privilege)


class Admin(User):
    """模拟特殊用户——管理员"""
    def __init__(self, first_name, last_name,
                 age, location, career, freedom_1):
        """初始化父类属性"""
        super().__init__(first_name, last_name, age, location, career)
        self.privileges = Privileges(freedom_1)


freedom_ = ['can add post', 'can delete post', 'can ban user']
admin_user_0 = Admin('yiming', 'chen', 18, 'cheng du', 'student', freedom_)

admin_user_0.privileges.show_privileges()

#  导入类，见class_module_ninth_chapters

