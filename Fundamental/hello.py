import sys

def world():
    print('Hello, World!')


nama = "Audie"


class Student:
    def __init__(self, name, kelas):
        self.name = name
        self.kelas = kelas

    def learn(self):
        print(self.name + " sedang belajar di kelas " + self.kelas)


for a in sys.path:
    print(a + "\n")