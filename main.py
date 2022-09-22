from game import *
from threading import Thread
import time


def life():
    while CREATURE[0].is_living:
        CREATURE[0].life()
        time.sleep(5)
    print("Вы не смогли уследить за своим персонажем, он умер((")
    exit(0)


def main_game():
    if len(CREATURE) == 0:
        new_game()
    while CREATURE[0].is_living:
        print("Выбирите действие:")
        print("1: Покормить")
        print("2: Уложить спать")
        print("3: Поиграть")
        print("4: Погулять")
        print("5: Вывести информацию")
        print("6: Суперспособность")
        if CREATURE[0].type == "MAGIC":
            print("7: Магия")
        try:
            n = int(input())
            if not CREATURE[0].is_living:
                break
        except ValueError:
            print("Повторите ввод")
        if n in ACTIONS.keys():
            try:
                getattr(CREATURE[0], ACTIONS[n])() if n != 5 else print(CREATURE[0])
            except AttributeError:
                print("Я так не умею, введи снова")
        else:
            print("Я так не умею, введи снова")
    print("Вы не смогли уследить за своим персонажем, он умер((")


def new_game() -> bool:
    print("Выбирите персонажа: \nЧтобы выбрать дракона введите '0' \nЧтобы выбрать кошку введите '1' \nЧтобы выбрать собаку введите '2'")
    n = False
    while not n:
        s = int(input())
        if s in [0, 1, 2]:
            print("Введите имя персонажа:")
            s1 = input()
            if s == 0:
                CREATURE.append(Dragon(s1))
                return True
            elif s == 1:
                CREATURE.append(Cat(s1))
                return True
            elif s == 2:
                CREATURE.append(Dog(s1))
                return True
            else:
                print("Повторите ввод")


if __name__ == "__main__":
    if new_game():
        Thread(target=main_game).start()
        Thread(target=life).start()
