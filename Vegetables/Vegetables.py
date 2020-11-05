import Module
class Vegetables():
    is_fresh = "Yes"
    number = int(input("Сколько у тебя овощей? "))

    def value(self, value = number):
        self.value = value
    
    def eat(self):
        if self.value > 0:
            self.value -= 1
            print('Съедена 1 шт!')
        else:
            print("В магаз!")
    
    def res(self):
        if self.value > 0:
            print('Осталось ' + str(self.value))
        else:
            print("У вас не осталось овощей!")

class Korneplodi(Vegetables):
    size = 'small'
    name = 'potato'

    def __init__(self):
        print('Экземпляр класса Корнеплодные создан!')

class Plodovie(Vegetables):
    colour = 'red'
    name = 'tomato'

    def __init__(self):
        print("Экземпляр класса Плодовые создан!")

class Listovie(Vegetables):
    smell = 'strong'
    name = 'cabbage'

    def __init__(self):
        print("Экземпляр класса Листовые создан!")

K = Korneplodi()
print(K.name)
K.value()
K.eat()
K.res()

#Vegetables.fresh = "No"
#Vegetables.colour = "Red"
#setattr(Vegetables,"ves",2)
#delattr(Vegetables, "ves")
#print(Vegetables.__dict__)