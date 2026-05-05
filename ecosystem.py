"""
Модуль экосистемы — управляет всеми организмами и симуляцией.
"""

from organism import Organism, Herbivore, Predator, Plant


class Population:
    """
    Класс, представляющий популяцию однотипных организмов.

    Атрибуты:
        species_name (str): Название вида.
        members (list): Список организмов в популяции.
    """

    def __init__(self, species_name: str):
        """
        Args:
            species_name (str): Название вида популяции.
        """
        self.species_name = species_name
        self.members = []

    def add_member(self, organism: Organism):
        """
        Добавляет организм в популяцию.

        Args:
            organism (Organism): Организм для добавления.
        """
        self.members.append(organism)

    def get_alive(self) -> list:
        """
        Возвращает список живых членов популяции.

        Returns:
            list: Живые организмы.
        """
        return [m for m in self.members if m.is_alive()]

    def count(self) -> int:
        """
        Возвращает количество живых особей.

        Returns:
            int: Число живых членов популяции.
        """
        return len(self.get_alive())

    def __str__(self) -> str:
        return f"Популяция '{self.species_name}': {self.count()} живых особей"


class Ecosystem:
    """
    Класс экосистемы, управляющий всеми организмами и симуляцией.

    Атрибуты:
        name (str): Название экосистемы.
        day (int): Текущий день симуляции.
        organisms (list): Все организмы в экосистеме.
        populations (dict): Словарь популяций по типу.
    """

    def __init__(self, name: str = "Лесная экосистема"):
        """
        Args:
            name (str): Название экосистемы.
        """
        self.name = name
        self.day = 0
        self.organisms = []
        self.populations = {
            "plants": Population("Растения"),
            "herbivores": Population("Травоядные"),
            "predators": Population("Хищники"),
        }

    def add_organism(self, organism: Organism):
        """
        Добавляет организм в экосистему и соответствующую популяцию.

        Args:
            organism (Organism): Организм для добавления.
        """
        self.organisms.append(organism)

        if isinstance(organism, Plant):
            self.populations["plants"].add_member(organism)
        elif isinstance(organism, Predator):
            self.populations["predators"].add_member(organism)
        elif isinstance(organism, Herbivore):
            self.populations["herbivores"].add_member(organism)

    def simulate_day(self):
        """
        Симулирует один день жизни экосистемы:
        - Растения фотосинтезируют
        - Травоядные едят растения
        - Хищники охотятся
        - Все организмы стареют
        """
        self.day += 1
        print(f"\n{'='*45}")
        print(f"  ДЕНЬ {self.day} — {self.name}")
        print(f"{'='*45}")

        # 1. Растения фотосинтезируют
        print("\n🌿 Фотосинтез растений:")
        for plant in self.populations["plants"].get_alive():
            plant.photosynthesize()

        # 2. Травоядные едят растения
        plants_alive = self.populations["plants"].get_alive()
        print("\n🐇 Травоядные ищут пищу:")
        for herb in self.populations["herbivores"].get_alive():
            if plants_alive:
                herb.eat_plant(plants_alive[0])
            else:
                herb.energy -= 5
                print(f"  {herb.name} не нашёл(ла) пищи. -5 энергии.")

        # 3. Хищники охотятся
        herbivores_alive = self.populations["herbivores"].get_alive()
        print("\n🦊 Хищники охотятся:")
        for pred in self.populations["predators"].get_alive():
            if herbivores_alive:
                pred.hunt(herbivores_alive[0])
            else:
                pred.energy -= 8
                print(f"  {pred.name} не нашёл(ла) добычи. -8 энергии.")

        # 4.Все организмы стареют
        for org in self.organisms:
            if org.is_alive():
                org.age_one_day()

        # 5. Итог дня
        self._print_daily_summary()

    def _print_daily_summary(self):
        """
        Выводит сводку по итогам дня.
        """
        print(f"\n📊 Итог дня {self.day}:")
        for pop in self.populations.values():
            print(f"  {pop}")

    def print_status(self):
        """
        Выводит подробный статус всех организмов.
        """
        print(f"\n{'='*45}")
        print(f"  СТАТУС ЭКОСИСТЕМЫ — День {self.day}")
        print(f"{'='*45}")
        for org in self.organisms:
            icon = "✅" if org.is_alive() else "💀"
            print(f"  {icon} {org}")
