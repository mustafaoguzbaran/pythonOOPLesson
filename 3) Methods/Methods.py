class Square(object):
    edge = 5 #karenin bir kenarı
    area = 0 #s1.area şeklinde çağırıldığında nesnenin yaratılmış olduğu memory adresini getirir.
    def area(self): #Bu self ifadesi class'a ait attributes'leri kullanmaya olanak tanır.
        return self.edge * self.edge #Buradaki self yukarıdaki objeyi ifade etmiş oluyor. Obje de Class'ın içerisinde
        # yaratılmış olan attribute'leri, behaviour'ları ifade ediyor. Yani kısacası self ifadesi Class içerisindeki
        # tüm attribute'leri, behaviour'ları ifade ederek class içerisinde bunları kullanmamıza olanak tanıyor.

s1 = Square()

print(s1)
print(s1.edge)
print((s1.area))
print(s1.area())