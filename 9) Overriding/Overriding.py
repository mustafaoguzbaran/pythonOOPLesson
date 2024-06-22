#Overriding: Geçersiz kılma anlamına gelir.

class Animal: #Parent
    def toString(self):
        print("Animal Class")
        
class Monkey(Animal): #Child
    
    def toString(self):
        print("Monkey Class")
        
animal1 = Animal()
animal1.toString()

monkey1 = Monkey()
monkey1.toString() #Monkey sınıfı overriding methodu çağırıyor. Animal ve Monkey sınıflarında da aynı isme sahip methodlar mevcut. Ama çıktı olarak Animal Class ve Monkey Class geliyor. Böylelikle Monkey Class'ı, Animal Class'ındaki toString Methodunu geçersiz kılmış oluyor.