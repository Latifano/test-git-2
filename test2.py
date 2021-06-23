"""
Judul : Kalkulator
Deskripsi : Program kalkulator sederhana untuk menjumlah, mengurang, mengali, dan membagi 2 bilangan
"""


class Kalkulator:

    print('\n KALKULATOR SEDERHANA\nPilih Operasi : \n1.Jumlah \n2.Kurang \n3.Kali \n4.Bagi')

    def __init__(self, pilihan, input1, input2):
        self.pilihan = pilihan
        self.input1 = input1
        self.input2 = input2
        self.hasiltambah = self.input1 + self.input2
        self.hasilkurang = self.input1 - self.input2
        self.hasilkali = self.input1 * self.input2
        self.hasilbagi = self.input1 / self.input2

    def info(self):
        if self.pilihan == 1:
            return f'\n{self.input1} + {self.input2} = {self.hasiltambah}\n'
        elif self.pilihan == 2:
            return f'\n{self.input1} - {self.input2} = {self.hasilkurang}\n'
        elif self.pilihan == 3:
            return f'\n{self.input1} * {self.input2} = {self.hasilkali}\n'
        elif self.pilihan == 4:
            return f'\n{self.input1} / {self.input2} = {self.hasilbagi}\n'
        else:
            return f'\nPilihan Operasi cuma 1 - 4 !\n'


inputAngka = Kalkulator(int(input("\nMasukkan pilihan(1/2/3/4) : ")), int(
    input('Masukan Angka Ke-1 : ')), int(input('Masukan Bil Ke-2 : ')))

print(inputAngka.info())
