"""
В классе Hero из предыдущего занятия добавьте приватное свойство rank.
Создайте геттер, сеттер и делиттер чтобы можно было получить звание героя, установить звание "Победитель арены"
в случае победы героя в битве и удалить ранк в случае поражения.
"""
class Hero:
    def __init__(self, health, power, rank):
        self.health = health
        self.power = power
        self.__rank = rank

    def set_rank(self, rank):
        self.__rank = rank

    def get_rank(self):
        return self.__rank

    def del_rank(self):
        del self.__rank

    def fight(self, enemy):
        while self.power > 0:
            enemy.health -= 5
            self.power -= 10
        if enemy.health < 0:
            self.set_rank('Победитель арены')
            print(self.get_rank())
        else:
            self.del_rank()
            print('вы потеряли ранг')

hero1 = Hero(300, 1000,)
hero2 = Hero(1000, 1000,)
hero1.fight(hero2)