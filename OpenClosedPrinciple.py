import math

class BangunDatar:

    def luas():
        pass

class Persegi(BangunDatar):

    def __init__(self, panjang):
        self.panjang = panjang

    def luas(self):
        return pow(self.panjang, 2)

class Lingkaran(Interface):

    def __init__(self, radius):
        self.radius = radius

    def luas(self):
        return math.pi * pow(self.radius, 2)

class Kalkulasi:

    def __init__(self, *args):
        self.bangunDatar = args

    def calculate(self):
        listLuas = []
        for objek in self.bangunDatar:
              if isinstance(objek, BangunDatar):
                luas = objek.luas()
                listLuas.append(luas)
                continue

        raise Exception("This Object (",object,") Not Implementation of BangunDatar")


    def output(self):
        return self.calculate()