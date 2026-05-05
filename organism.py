"""
Модуль, содержащий базовый класс Organism и его подклассы.
"""


class Organism:
    """
    Базовый класс, представляющий организм в экосистеме.

    Атрибуты:
        name (str): Имя организма.
        energy (int): Уровень энергии (здоровье).
        age (int): Текущий возраст организма.
        max_age (int): Максимальный возраст организма.
    """

    def __init__(self, name: str, energy: int, max_age: int = 20):
        """
        Инициализация организма.

        Args:
            name (str): Имя организма.
            energy (int): Начальный уровень энергии.
            max_age (int): Максимальный возраст. По умолчанию 20.
        """
        self.name = name
        self.energy = energy
        self.age = 0
        self.max_age = max_age

    def is_alive(self) -> bool:
        """
        Проверяет, жив ли организм.

        Returns:
            bool: True если энергия > 0 и возраст не превышает максимальный.
        """
        return self.energy > 0 and self.age < self.max_age

    def eat(self, amount: int):
        """
        Организм поедает пищу и восстанавливает энергию.

        Args:
            amount (int): Количество восстанавливаемой энергии.
        """
        if self.is_alive():
            self.energy += amount
            print(f"  {self.name} поел(а) и получил(а) {amount} энергии. "
                  f"Энергия: {self.energy}")

    def age_one_day(self):
        """
        Организм стареет на один день, теряя 2 единицы энергии.
        """
        self.age += 1
        self.energy -= 2
        if self.energy < 0:
            self.energy = 0

    def __str__(self) -> str:
        status = "живой" if self.is_alive() else "мёртвый"
        return (f"{self.name} | Энергия: {self.energy} | "
                f"Возраст: {self.age}/{self.max_age} | {status}")


class Herbivore(Organism):
    """
    Травоядное животное. Ест растения, убегает от хищников.

    Наследует: Organism
    """

    def __init__(self, name: str, energy: int = 30):
        super().__init__(name, energy, max_age=15)
        self.type = "herbivore"

    def eat_plant(self, plant):
        """
        Поедает растение, забирая у него энергию.

        Args:
            plant (Plant): Объект растения.
        """
        if plant.is_alive() and self.is_alive():
            stolen = min(15, plant.energy)
            plant.energy -= stolen
            self.energy += stolen
            print(f"  {self.name} съел(а) часть {plant.name}. "
                  f"+{stolen} энергии.")


class Predator(Organism):
    """
    Хищник. Охотится на травоядных.

    Наследует: Organism
    """

    def __init__(self, name: str, energy: int = 50):
        super().__init__(name, energy, max_age=25)
        self.type = "predator"

    def hunt(self, prey: Herbivore):
        """
        Охотится на травоядное.

        Args:
            prey (Herbivore): Жертва охоты.
        """
        if prey.is_alive() and self.is_alive():
            print(f"  {self.name} охотится на {prey.name}!")
            stolen = min(25, prey.energy)
            prey.energy -= stolen
            self.energy += stolen
            if not prey.is_alive():
                print(f"  {prey.name} был(а) съеден(а)!")
            else:
                print(f"  {prey.name} выжил(а). "
                      f"Осталось энергии: {prey.energy}")


class Plant(Organism):
    """
    Растение. Восстанавливает энергию каждый день через фотосинтез.

    Наследует: Organism
    """

    def __init__(self, name: str, energy: int = 40):
        super().__init__(name, energy, max_age=30)
        self.type = "plant"

    def photosynthesize(self):
        """
        Растение восполняет энергию через фотосинтез (+5 в день).
        """
        if self.is_alive():
          self.energy += 5
            print(f"  {self.name} провёл(а) фотосинтез. "
                  f"Энергия: {self.energy}") 





