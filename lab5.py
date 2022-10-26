import numpy as np
import pandas as pd
import csv
import numpy
emotion = input("""
    Максимальный и средний возраст пациентов с установленным диабетом. -> Нажмите 1
    Параметры с максимальной корреляцией между собой, значение корреляции. -> Нажмите 2
    Доля бездетных среди пациентов с неустановленным диабетом. -> Нажмите 3
    Максимальная концентрация глюкозы у пациентов старше 50 лет. -> Нажмите 4
    Средний возраст пациентов с диастолическим давлением выше 80 -> Нажмите 5
    Список пациентов старше 60 с уровнем инсулина выше среднего, отсортированный по
    возрастанию столбца Возраст. -> Нажмите 6
    Список записей с нулевыми значениями хотя бы одного параметра (за исключением
    первого и последнего столбцов). -> Нажмите 7
""")
if emotion == "1":
    mass =[]
    coup = 0
    kol = 0
    sum = 0
    with open('prima-indians-diabetes.csv',) as File:
        reader = csv.reader(File)
        for row in reader:
            if row[8] == "1":
                kol += 1
                mass.append(row[7])
                sum += int(row[7])
        avg = round(sum/kol)
        print("Максимальный возраст пациентов с установленным диабетом. = " + max(mass))
        print(f"Cредний возраст пациентов с установленным диабетом. = {avg}")
elif emotion == "2":
    path = 'prima-indians-diabetes.csv'
    data_frame = pd.read_csv(path, sep=',', header=None)
    diabets_array = [row for row in data_frame.values if int(row[8]) == 1]
    diabets = pd.DataFrame(data=diabets_array)
    print(f"Параметры с макс корреляцией: {diabets.corr()}")
elif emotion == "3":
    persons = 0
    nodiabet = 0
    with open('prima-indians-diabetes.csv', newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            persons += 1
            if row[8] == "0" and row[0] == "0":
                nodiabet += 1
        result = nodiabet * 100 / persons
        print(f"Доля бездетных среди пациентов с неустановленным диабетом. = {round(result)}%")
elif emotion == "4":
    mass = []
    with open('prima-indians-diabetes.csv', newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            if row[7] > "50":
                mass.append(row[1])
        print(f"Максимальная концентрация глюкозы у пациентов старше 50 лет. = {max(mass)}")
elif emotion == "5":
    persons = 0
    davlenie = 0
    with open('prima-indians-diabetes.csv', newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            if row[2] > "80":
                persons += 1
                davlenie += int(row[7])
        print(f"Средний возраст пациентов с диастолическим давлением выше 80 = {round(davlenie/persons)}")
elif emotion == "6":
    path = 'prima-indians-diabetes.csv'
    data_frame = pd.read_csv(path, sep=',', header=None)
    # Диабетики
    diabets_array = [row for row in data_frame.values if int(row[8]) == 1]
    diabets = pd.DataFrame(data=diabets_array)
    avg_insulin = diabets[4].mean()
    task6 = pd.DataFrame([row for row in data_frame.values if row[7] > 60 and row[4] > avg_insulin])
    task6 = task6.sort_values(by=7)
    print(
        f"Список пациентов старше 60 с уровнем инсулина выше среднего, отсортированный по возрастанию столбца возраста:\n{task6}")
elif emotion == "7":
    with open('prima-indians-diabetes.csv', newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            first = row.pop(0)
            last = row.pop(7)
            if "0" in row:
                row.insert(0,first)
                row.insert(8,last)
                print(row)
        print( "Список записей с нулевыми значениями хотя бы одного параметра (за исключением первого и последнего столбцов)")
else: print("Такой команды не существует")