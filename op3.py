from datetime import date

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def ptintname(self):
        print(self.name, self.age)

    @classmethod
    def classmethod(cls, year):
        return Person("oleg", date.today().year - year)

    @staticmethod
    def staticmethod(age):
        if age < 18:
            return "net"
        else:
            return "da"


oleg = (Person.classmethod(2004))
print(oleg.name)
print(oleg.age)
print(oleg.staticmethod(18))