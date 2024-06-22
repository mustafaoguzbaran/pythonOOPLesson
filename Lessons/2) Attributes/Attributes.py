class Footballer():
    #Futbolcuların ismi, soyismi, yaşı, göz rengi gibi özellikleri olabilir.
    # Attribute; özellik,
    # nitelik anlamına gelir.
    name = "Mustafa Oğuz"
    surname = "BARAN"
    age = 23
    eyeColor = "brown"

footballer1 = Footballer()
print(footballer1) #Objenin yaratıldığı bilgisini ve memory'deki adresini verir.
print(footballer1.name) #Class içerisinde set edilen name bilgisini getirir.
print(footballer1.surname) #Class içerisinde set edilen surname bilgisini getirir.
print(footballer1.age) #Class içerisinde set edilen age bilgisini getirir.
print(footballer1.eyeColor) #Class içerisinde set edilen göz rengi bilgisini getirir.

footballer1.name = "Furkan"
footballer1.surname = "Yaşar"

print(footballer1) #Objenin yaratıldığı bilgisini ve memory'deki adresini verir.
print(footballer1.name) #Class içerisinde set edilen name bilgisini getirir.
print(footballer1.surname) #Class içerisinde set edilen surname bilgisini getirir.
print(footballer1.age) #Class içerisinde set edilen age bilgisini getirir.
print(footballer1.eyeColor) #Class içerisinde set edilen göz rengi bilgisini getirir.

#Yukarıda görüldüğü üzere futbolcu ismi ve soyismini değiştirebiliyoruz. (Bu yazılım standartlarında hoş karşılanan
# bir durum değildir.) Memory'deki adrese baktığımız zaman her iki
# memory bilgisinin de aynı olduğu görülecektir.