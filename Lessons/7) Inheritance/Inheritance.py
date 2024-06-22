#Inheritance: Kalıtım ya da miras anlamına gelir. Inheritance, daha önce yazılmış bir class'ın attribute'lerini veya methodlarını kullanarak yeni bir class yaratmaktır. Yani daha önce yazılmış class'ın attribute'leri ya da methodları kullanılacaksa sonraki class'ta bunları kullanmaya gerek yok. Yani bir önceki class'taki methodlar veya attribute'leri kullanılabilir hale getirir.

#Child Class: parent class'ın attribute'lerini veya methodlarını kullanabilen class'tır. Child class'a parent class'tan türetilmiş class'ta denebilir.

#Parent Cass
class Animal:
    def __init__(self):
        print("Animal is created.")

    def toString(self):
        print("animal")

    def walk(self):
        print("animal walk")

#Child Class
class Monkey(Animal):
    def __init__(self):
        super().__init__() #Animal class'ın init'i kullanılabilir hale gelmiş oluyor.
        print("Monkey is created.")

    def toString(self):
        print("Monkey")

    def climb(self):
        print("Monkey can climb")

monkey1 = Monkey()
monkey1.toString()
monkey1.walk() #Animal class'ından almış olduk.
monkey1.climb()
