import pandas
import matplotlib.pyplot as plt
import numpy as np
import json

def ds(s=18720, e=20160):
    '''Возвращает датасет из скоростей ветра с рядка s в табл до рядка e'''

    data = pandas.read_csv('dsc_fc_summed_spectra_2016_v01.csv',
    delimiter = ',', parse_dates=[0], na_values='0',
    header = None)

    date = "2016-07-01" # Без взякого смысла
    print(f"data: {date}")

    dataset = []
    ##### шпаргалка #####
    #18720
    #20159 #1439

    #20160
    #21599 #1439
    ######################

    i = 0
    batch = [] # список ветров за 3 часа
    for row in range(s, e): # перебираем рядки
        i += 1 # счётчик для того чтобы понять когда 3 часа прошли (180 циклов)
        for j in range(4, 53): # перебираем столбци
            v = str(data[j][row])
            if v != 'nan': # игнорируем nan
                batch.append(float(v))
        if i == 180: # когда прошло 3 часа
            i = 0
            print(len(batch))
            '''нейронке надо чтобы массивы были одинаковой длинны, а кол-во nan разное везде.
            Но в тех днях которые я вытягиваю - в каждом 3х часовом промежутке минимум 3400 значений.
            Крч я сделал все списки одинаковой длинны, чтобы нейронка не ныла'''
            dataset.append(batch[:3400])
            batch = []

    return dataset

def kp(s=0, e=8): # возвращает датасет планетарных индексов
    dataset = []
    with open('kp.txt', "r") as f:
        for line in f.readlines()[s:e]: # срез. Чтобы брать нужные елементы(с 0 по 8 или с 8 по 16)
            dataset.append(int(float(line.split(" ")[8])*10))
    return dataset
