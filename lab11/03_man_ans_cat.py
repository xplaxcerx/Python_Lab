from random import randint

from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def kat_food(self):
        cprint('{} купил еду коту'.format(self.name), color='yellow')
        self.house.cat_food += 50     
        self.house.money -= 50

    def clean(self):
        cprint('{} убрался в доме'.format(self.name), color='blue')
        self.fullness -= 20
        self.house.durt -= 100

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 1350
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')


    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.cat_food < 10:
            self.kat_food()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif self.house.durt >= 100:
            self.clean()
        else:
            self.watch_MTV()

class Kat:
    def __init__(self, name):
        self.fullness_k = 50
        self.house = None  
        self.name = name

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness_k)
    
    def pick_up_kat(self,house):
        self.house = house
        self.fullness_k -= 10
        cprint('{} Подобрали домой'.format(self.name), color='cyan')

    def sleep(self):
        cprint('{} спал'.format(self.name), color='cyan')
        self.fullness_k -= 10

    def eat_k(self):
        if self.house.cat_food >= 10:
            cprint('{} ел'.format(self.name), color='cyan')
            self.fullness_k += 20
            self.house.cat_food -= 10   
        else:
            cprint('{} нет еды'.format(self.name), color='red')
    def wallpaper(self):
        cprint('{} драл обои'.format(self.name), color='cyan')
        self.fullness_k -= 10
        self.house.durt += 5

    def act(self):
        if self.fullness_k <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness_k < 20:
            self.eat_k()
        elif dice <= 3:
            self.sleep()
        else:
            self.wallpaper()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.cat_food = 0
        self.durt = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, кошачьей еды осталось {}, грязи осталось {}'.format(
            self.food, self.money, self.cat_food, self.durt)


citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни'),
]

kats = [
    Kat(name='Бисквитик'),
    Kat(name='Рулетик'),
    Kat(name='Жирулька'),
]

my_sweet_home = House()
for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)
for kat in kats:
    kat.pick_up_kat(house=my_sweet_home)

for day in range(1, 36):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        citisen.act()
    for kat in kats:
        kat.act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    for kat in kats:
        print(kat)
    print(my_sweet_home)





