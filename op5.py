"""
Создайте класс SpaceObject у которого будут свойство размер.
Создайте 2 класса Star и Planet которые будут наследовать SpaceObject. В классе Star добавьте свойство яркость
и метод светить в котором будет выводится на экран с какой яркостью светит звезда.
Классу Planet добавьте свойства население и прирост за год и метод который будет печатать население через переданное
ему количество лет.
"""
class SpaceObject:
    def __init__(self, size):
        self.size = size

class Star(SpaceObject):
    def __init__(self, size, brightness):
        super().__init__(size)
        self.brightness = brightness
    def shine(self):
        print(f'яркость: {self.brightness}')

class Planet(SpaceObject):
    def __init__(self, size, population, increasement):
        super().__init__(size)
        self.population = population
        self.increasement = increasement
    def population_in_years(self, years):
        print(f'спустя {years} лет населения составит{self.population + self.increasement * years} человек')

star = Star(100, 200)
star.shine()
planet = Planet(500, 1000, 200)
planet.population_in_years(5)

star = Star(50, 100)
star.shine()
planet = Planet(100, 1000, 10)
planet.population_in_years(5)