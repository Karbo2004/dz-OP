"""
Создайте класс который будет устанавливать свойство name и иметь метод
который к имени прибавляет надпись "гений". Создайте еще 1 класс, унаследуйте предыдущий.
Во втором классе вызовите метод класса родителя и добавьте к выводу надпись "но его отчислят если он не будет учить ООП".
Создайте экземпляр второго класса с вашим именем и вызовите метод печатающий всю надпись.
"""
class Genius:
    def __init__(self, name):
        self.name = name

    def write_geniy(self):
        return f'{self.name} гений'

class BUT(Genius):
    def __init__(self, name):
        super().__init__(name)
    def make_object(self):
        obj = Genius(self.name)
        return obj
    def complete(self):
        print(f'{self.make_object().write_geniy()}, но её отчислят если она не будет учить ООП')

def check():
    test = BUT('Oleg')
    test.complete()


check()