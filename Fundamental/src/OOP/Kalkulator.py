class Kalkulator:


    def __init__(self, nilai=0):
        self.nilai = nilai

    def tambahAngka(self, angka1, angka2):
        self.nilai = angka1 + angka2
        if self.nilai > 9:
            print('Kalkulator sederhana melebihi batas angka: {}'.format(self.nilai))
        return '{} + {} = {}'.format(angka1, angka2, self.nilai)


class KalkulatorKali(Kalkulator):
    """Inheritance"""

    def kaliAngka(self, angka1, angka2):
        self.nilai = angka1*angka2
        return '{} x {} = {}'.format(angka1, angka2, self.nilai)

    def tambahAngka(self, angka1, angka2):  # Override
        self.nilai = angka1 + angka2
        return'{} + {} = {}'.format(angka1, angka2, self.nilai)


class KalkulatorTambah(Kalkulator):
    """Inheritance"""

    def tambahAngka(self, angka1, angka2):
        if angka1 + angka2 <= 9:
            super().tambahAngka(angka1, angka2)
        else:
            self.nilai = angka1 + angka2
        return '{} + {} = {}'.format(angka1, angka2, self.nilai)


kk = KalkulatorKali()
a = kk.kaliAngka(2, 3)
print(a)

b = kk.tambahAngka(5, 6)
print(b)

kt = KalkulatorTambah()
c = kt.tambahAngka(2, 6)
print(c)