# Python Class


class Calculator:
    """Contoh kelas kalkulator sederhana"""

    def __init__(self, i=12345):  # Constructor
        self.i = i

    def f(self):
        return 'Hello World'

    @classmethod
    def tambah_angka(cls, angka1, angka2):
        return'{} + {} = {}'.format(angka1, angka2, angka1 + angka2)

    @staticmethod  # Static method tidak menerima argument pertama secara implisit, bisa ada tanpa membuat objek dari class
    def kali_angka(angka1, angka2):
        return'{} x {} = {}'.format(angka1, angka2, angka1*angka2)


k = Calculator(i=1024)
print(k.f())
print(k.i)
print(Calculator.f(k))
print(k.tambah_angka(1, 2))
print(k.kali_angka(2, 3))
