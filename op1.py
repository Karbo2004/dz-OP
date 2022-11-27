"""
Создайте классы утка и человек. У обоих классов нету свойств, но есть методы крякать и носить одежду.
Утка крякает, а человек имитирует кряканье. Добавьте экземпляры этих классов в список и вызовите в цикле соответствующие методы.
"""
class utka:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print('krya')
    def clothes(self):
        print("????????")

class chel:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print('krkrkrkzkkrzkrzyyayayayya')
    def clothes(self):
        print("nadel shtany")
dutka1 = utka(2)
chel1 = chel(6)
for i in [utka1, chel1]:
    i.sound()
    i.clothes()