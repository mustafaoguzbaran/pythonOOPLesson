from abc import ABC, abstractmethod
#Abstract Classes: Soyut sınıflar olarakta adlandırılır. Child class'lar için şablon görevi görürler ve kullanılacak ortak fonksiyonları kendi içlerinde tutarlar.

class Animal(ABC): #super class. İlk Kural: Abstract class'tan hiç bir şekilde obje yaratamam.
    @abstractmethod #Animal class'ımızı abstract class yaptık.
    def walk(self): pass
    
    @abstractmethod
    def run(self): pass

#İkinci kural: abstract class'ta yazılan methodlar child class'ta da kullanılmak zorundadır.
class Bird(Animal): #child class
    def __init__(self):
        print("Bird")
        
    def walk(self):
        print("walk ")
        
    def run(self):
        print("run")
    
    
bird1 = Bird()

#Kullanılma sebebi: Aslında abstract class'lar şablondur. Bir şablon yaratılır ve kullanılacak class'larda nerede hangi fonksiyon kullanılacağı belli olmuş oluyor.