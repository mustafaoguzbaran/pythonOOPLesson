#Encapsulation, kapsülleme anlamına gelir. Method'lara veya attribute'lere kısıtlama getirmeye olanak sağlar.

class BankAccount(object):
    def __init__(self, name, money, address):
        self.name = name
        self.money = money
        self.address = address

person1 = BankAccount('Mustafa', 3000, 'Turkey')
person2 = BankAccount('Furkan', 5000, 'Germany')

print(person1.name)
print(person1.money)
print(person1.address)
#Bu, doğru bir şey değil çünkü yaratılan nesne hakkında hassas bilgilere sahip olduk.

person2.money = person2.money + person1.money
person1.money = 0

print("Mustafa Money:", person1.money)
print("Furkan Money: ", person2.money)

#Burada Mustafa'nın parasını Furkan'ın parasına aktarmış olduk. Bu da istenen bir şey değildir.

print("------------------------------- ENCAPSULATION ----------------------")
class BankAccount(object):
    def __init__(self, name, money, address):
        self.name = name #GLOBAL
        self.__money = money #PRIVATE (iki alttan çizgi) sadece class içerisinde private attribute'leri modify
        # edebilmemiz için getter ve setter kullanmamız gerekiyor.
        self.address = address

    def getMoney(self):
        return self.__money

    def setMoney(self, amount):
        self.__money = amount

    def __increaseMoney(self, amount): #private method
        self.__money += amount

person1 = BankAccount('Mustafa', 3000, 'Turkey')
person2 = BankAccount('Furkan', 5000, 'Germany')

print(person1.name)
print(person1.getMoney())
print(person1.address)

person2.money = person2.setMoney(person1.getMoney() + person2.getMoney())
person1.money = 0

print("Mustafa Money:", person1.getMoney())
print("Furkan Money: ", person2.getMoney())

person1.increaseMoney(3000) #private olduğu için hata fırlatacaktır. Private olduğu için bu method class içerisinde
# kullanılır.

print("Mustafa Zamlı Maaş: ", person1.getMoney())