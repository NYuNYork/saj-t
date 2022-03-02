import re 
import copy


class Gyerek_osztaly:
    def __init__(self, nev, szul_ev, nem, magassag, suly):
        self.nev = nev
        self.szul_ev = int(szul_ev)
        self.magassag = int(magassag)
        self.suly = int(suly)
        self.nem = nem

def gyerek_lista():

    gyerek = []

    n = int(input('add meg hány gyerektet akarsz bevinni: '))
    nb = 0
    no = 1

    print('add meg a gyerek adatait')
    while n != nb:
        print(f'add meg az {no}. gyereket')
        a = input('neve: ')
        b = int(input('születési év: '))
        c = input('neme: ')
        d = int(input('magassága: '))
        e = int(input('súlya: '))
        gyerek.append(Gyerek_osztaly(a, b, c, d, e))
        no += 1
        nb += 1
    return gyerek

def arány(gyerek):
    f = 0
    n = 0
    for gy in gyerek:
        if gy.nem == 'férfi':
            f += 1
        if gy.nem == 'nő':
            n += 1
    b = f/n
    return b

def legidősebb_gyerek(gyerek):
    mini = 0
    for i in range(0, len(gyerek)):
        if gyerek [i].szul_ev < gyerek[mini].szul_ev:
            mini = i
            return gyerek[mini].nev

# def bmi(gyerek):
#     BMI =[]
#     for gy in gyerek:
#         while len(BMI) != len(gyerek):
#             r = gy.suly/(gy.magassag/100) 
#             BMI.append(Gyerek_osztaly(r))
#     return BMI

def átlagmagasság(gyerek):
    for i in gyerek:
        b = ([i].magassag)/len(gyerek)
        return b

