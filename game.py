import time

import keyboard
from const import *


class Tamagucci:
    def __init__(self, name="Person_name", health=100, eat=140, type="REAL"):
        self.name = name
        self.age = 0
        self.health = health
        self.type = type
        self.is_living = True
        self.sleep = MAX_SLEEP
        self.eat = eat
        self.happiness = 100

    def eating(self):
        if self.eat < EAT:
            self.eat += 10
            print("Спасибо за вкусняшку")
        else:
            print('Я не хочу кушать')

    def life(self):
        if self.health <= 0:
            self.is_living = False
        if self.eat <= 5:
            print("Я умираю от голода, покорми меня")
            self.eat = 0
        if self.happiness <= MAX_HAPPINESS // 2:
            print("Скучно...")
        if self.eat <= 5:
            print("Я умираю от голода, покорми меня")
            self.eat = 0
        else:
            self.eat -= 5 * 2 if self.happiness <= MAX_HAPPINESS // 5 else 1
        if self.sleep <= 2:
            print("Я умираю от усталости, давай поспим")
            self.sleep = 0
        else:
            self.sleep -= 2 * 2 if self.happiness <= MAX_HAPPINESS // 5 else 1
        if self.eat <= 0 or self.sleep == 0:
            self.health -= 10 if self.health > 0 else 0
        self.happiness -= 2

    def __str__(self):
        return f"Информация о {self.name}\nЗдоровье {self.health}\nСон {self.sleep}\nЕда {self.eat}\nСчастье {self.happiness}"

    def walk(self):
        print("Ура идем гулять")
        print("Зажми CTRL, чтобы пойти домой")
        while True:
            if keyboard.is_pressed("ctrl"):
                print("Ну ладно, пошли домой")
                break
            self.happiness += 10 if self.happiness <= MAX_HAPPINESS else 0
            time.sleep(2)

    def play(self):
        print("Играем")
        print("Зажми CTRL, чтобы закончить игру")
        while True:
            if keyboard.is_pressed("ctrl"):
                print("Хорошо поиграли")
                break
            self.happiness += 15 if self.happiness <= MAX_HAPPINESS else 0
            time.sleep(2)

    def sleeping(self):
        if CREATURE[0].sleep == MAX_SLEEP:
            print("Я не хочу спать")
        else:
            print("Зажми CTRL, чтобы пробудить меня")
            while True:
                print("Zzz...")
                if keyboard.is_pressed("ctrl"):
                    print("Почти выспался")
                    break
                if self.sleep >= MAX_SLEEP:
                    self.sleep = MAX_SLEEP
                    print("Я выспался")
                    break
                self.sleep += 10
                time.sleep(2)

    def ability(self):
        print("У меня есть способность, но я ее пока не получил(")


class Unreal(Tamagucci):
    def __init__(self, name="Person_name", health=150, eat=140):
        super().__init__(name, health, eat, "MAGIC")

    def do_magic(self):
        print("Я могу все")


class Real(Tamagucci):
    def __init__(self, name="Person_name", health=100, eat=140):
        super().__init__(name, health, eat)


class Dragon(Unreal):
    def __init__(self, name="Person_name"):
        super().__init__(name)
        self.magic = 100

    def do_magic(self):
        if self.magic >= 10:
            print("Пых, и нет")
            self.magic -= 10
        else:
            print("У меня нет маны!")

    def ability(self):
        print('Я умею сжигать')


class Cat(Real):
    def __init__(self, name="Person_name"):
        super().__init__(name)

    def ability(self):
        print("Мур")


class Dog(Real):
    def __init__(self, name="Person_name"):
        super().__init__(name)

    def ability(self):
        print("ГАВ")

