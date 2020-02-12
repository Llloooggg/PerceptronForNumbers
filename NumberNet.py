import random as rnd
import os

h = 0.24  # Порог

# Считываем матрицу из файла
f = open("Gate.txt")
x = f.readlines()
f.close()
for i in range(7):
    xtext = x[i]
    x[i] = [int(i) for i in xtext.split()]
# Матрица загружена


def training(name):

    weights = [[rnd.uniform(-1.5, 1.5)] * 5 for i in range(7)]
    nu = 0.005
    print("\nТемп обучения:", nu)
    erasquantity = 1000
    print("Количество эпох:", erasquantity)


    for _ in range(erasquantity):
        for i in range(7):
            y = 0
            for j in range(5):
                y += x[i][j] * weights[i][j]
            if y > h:
                y = 1
            else:
                y = 0
            for j in range(5):
                weights[i][j] += (1 - y) * nu * x[i][j]

    # Создаем файл с весами
    f = open(os.path.join(os.path.dirname(__file__))+"/Weights/" + name + ".txt", 'w')
    for i in range(7):
        for j in range (5):
            f.write('%s\n' % weights[i][j])
    f.close()
    # Файл создан

    question = str(input("\nВеса сгенерированы для цифры " + name + "\nПроверить работу? Y/N\n"))
    if question == "Y" or question == "y":
        working()
    elif question != "N" and question != "n":
        print("\n404")


def working():

    count = -1
    success = 0
    weights = [[0.01] * 5 for i in range(7)]
    while count < 10 and success != 7:
        count += 1
        success = 0

        pathcheck = 1
        # Загружаем веса
        if os.path.exists(os.path.join(os.path.dirname(__file__))+"/Weights/" + str(count) + ".txt"):
            f = open(os.path.join(os.path.dirname(__file__))+"/Weights/" + str(count) + ".txt")  # Открытие файла на чтение
            for i in range(7):
                for j in range(5):
                    weights[i][j] = f.readline()
            f.close()
        # Веса загружены

        else:
            pathcheck = 0
        # Веса отсутствуют

        if pathcheck == 1:
            for i in range(7):
                y = 0
                for j in range(5):
                    y += x[i][j] * float(weights[i][j])
                if y > h:
                    success += 1

    if count < 10:
        print("\nУказанное число = " + str(count))
    else:
        print("\nСоответстивий не найдено")


question = int(input("Обучаемся или работаем? 1/2\n"))
if question == 1:
    name = input("\nИзображение извлечено из gate.txt\nВведите цифру в числовом формате:\n")
    training(name)
elif question == 2:
    working()
else:
    print("\n404")

print("Пока")