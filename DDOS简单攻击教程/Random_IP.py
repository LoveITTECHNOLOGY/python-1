import random


def Random_Section():
    section = random.randint(1, 254)
    return section


def Random_IP():
    IP = str(Random_Section()) + '.' + str(Random_Section()) + '.' + str(Random_Section()) + '.' + str(Random_Section())
    return IP


if __name__ == '__main__':
    print(Random_IP())
