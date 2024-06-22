class Employee(object):

    age = 23
    salary = 2000

    def ageSalaryRatio(self): #Bu bir method
        return self.age / self.salary

def ageSalaryRatio(age, salary): #Bu bir fonksiyon
    return age / salary

employee1 = Employee()
print(employee1.ageSalaryRatio())
print(ageSalaryRatio(25, 2500)) #Class dışında yazılmış fonksiyonun kullanımı.

#Methods vs Function
# Method, self parametresine sahiptir. Self parametresi, class'ın objesini yani class'ı ifade ediyor. Method'lar
# class ierisinde tanımlanır, fonksiyonlar ise class dışında tanımlanır.