#Polymorphism: Türkçesi çok şekillilik ya da çok biçimlilik anlamlarına gelir. Parent Class'ta kullanılan bir methodu child class'larda da farklı bir şekilde kullanılıyorsa polymorphism yapılmış oluyor. Ayrıca polymorphism ile birlikte overriding'te yapılmış olur.

class Employee: #Parent Class
    
    def raisee(self):
        raseRate = 0.1
        print(100 + 100 * raseRate)
    
class ComputerEngineer(Employee): #Child Class
    
    def raisee(self):
        raiseRate = 0.2 #raseRate farklı olduğundan dolayı bu konsepte de polymorphism denir.
        print(100 + 100 * raiseRate)
    
class EEE(Employee): #Child Class
    def raisee(self):
        raiseRate = 0.3
        print(100 + 100 * raiseRate)
    
employee1 = Employee()

ce = ComputerEngineer()

eee = EEE()