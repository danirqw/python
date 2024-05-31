import random
# class Tree:
#     def __init__(self, name:str, height:int, fruits:str):#конструктор
#         self.name = name
#         self.height = height
#         self.fruits = fruits
#     def say_info(self):
#         print(f"я яблоня {self.name} у меня высота {self.height} на мне растут {self.fruits}")
#     def grow_up(self):
#         self.height +=10
#         print(f"дерево {self.name} его высота {self.height}")
# apple_tree = Tree(name="яблоня", height= 400, fruits="яблоки")
# ashberry = Tree(name="рябина", height= 200, fruits="рябник")
# print(apple_tree.name, ashberry.name)
# apple_tree.say_info()
# ashberry.say_info()
# apple_tree.grow_up()


# class Person:
#     def __init__(self, name, surname, age, weight, height):
#         self.name = name
#         self.surname =surname
#         self.age = age
#         self.weight = weight
#         self.height = height
#     def was(self):
#         print(f"меня зовут {self.name}, мне {self.age} лет, мой вес {self.weight} и мой рост{self.height}")
#     def changes(self):
#         self.age += 1
#         self.height += random.randint(1,5)
#         self.weight += random.randint(1,5)
#         print(f"твой персонаж спустя год {self.age} лет  {self.weight} вес {self.height}")
# person_1 = Person(name="danir", surname="gazimov", age=15, weight=51, height=170)
# person_1.was()
# person_1.changes()


# class Table:
#     def __init__(self, material,  age, weight, height):
#         self.weight = weight
#         self.height = height
#         self.age = age
#         self.material = material
#     def say_info(self):
#         print(f"я стол из {self.material} мне {self.age} мой вес {self.weight} мой рост {self.height} ")

# school_table = Table(material="oak", age=4, height=60, weight=20)
# print(school_table.material)
# school_table.say_info()



# class Speach:
#     def decorate(self, what_say):
#         print("-" * (len(what_say) +2))
#         print(f"|{what_say}|")
#         print("-" * (len(what_say) +2))
# text = Speach()
# text.decorate("привет")

# class Father:
#     def __init__( self,name:str, age:int):
#         self.name = name.capitalize()
#         self.age = age
#         self.gender = "мужчина"
#         self.power = 0

#     def swim(self):
#         print(f"{self.name} плавает брассом")

#     def dispute(self):
#         print(f"{self.name} спорит бассом")

#     def chopping(self):
#         self.power += 1
#         print(f"{self.name} срубит дрова. Сила его= {self.power}")
# class Son(Father): #наследие
#     def __init__(self, name: str, age: int, hobby:str):
#         super().__init__(name, age)
#         self.hobby = hobby
#         self.gender ="мальчик"
        
#     def ask_father(self,father:Father):
#         print(f"{self.name} обрптился за помощью к папе {father.name}")
        
#     def hobby(self):
#         print(f"{self.name} занимается хобби: {self.hobby}")
    
#     def dispute(self):
#         super().dispute
#         print(f"{self.name} спорит пискляво")

# papa = Father("олег", age=50)
# papa.swim()
# papa.dispute()
# papa.chopping()
# papa.chopping()

# son = Son("роман", age=18, hobby="програмирование")
# son.swim()
# son.chopping()
# son.dispute()
# son.ask_father(papa)



class Transport:
    def __init__(self, tip, weight, height):
        self.tip = tip
        self.weight = weight
        self.height = height
    def say_info(self):
        print(f"я {self.tip} транспорт мой вес {self.weight} и рост {self.height}")
        
class Moto(Transport):
    def __init__(self, tip, weight, height, wheel):
        super().__init__(tip, weight, height)
        self.wheel = wheel
    def say_info(self):
        print(f"я {self.tip} транспорт мой вес {self.weight} и рост {self.height} и у меня {self.wheel} колеса")
    def collide(self, participant:Transport):
        print(f"{participant.tip} столкнулся с {self.tip}")

car = Transport(tip="легковой", weight=1200, height="средний")
car.say_info()
motobike = Moto(tip="мини легковой", weight=200, height="маленкий", wheel=2)
motobike.say_info()
motobike.collide(car)


        

    