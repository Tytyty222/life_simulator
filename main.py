"""
Точка входа в консольный симулятор жизни.
Запускает экосистему с заданными организмами.
"""

from ecosystem import Ecosystem
from organism import Herbivore, Predator, Plant
from utils import print_header, get_simulation_days, ask_yes_no

# Ссылка на репозиторий проекта
REPO_URL = "https://github.com/ТВО_ИМЯ/life_simulator"


def create_default_ecosystem() -> Ecosystem:
    """
    Создаёт экосистему с набором организмов по умолчанию.

    Returns:
        Ecosystem: Готовая экосистема.
    """
    eco = Ecosystem("Лесная экосистема")

    # Добавляем растения
    eco.add_organism(Plant("Дуб", energy=50))
    eco.add_organism(Plant("Берёза", energy=40))
    eco.add_organism(Plant("Трава", energy=30))

    # Добавляем травоядных
    eco.add_organism(Herbivore("Заяц", energy=30))
    eco.add_organism(Herbivore("Олень", energy=40))

    # Добавляем хищников
    eco.add_organism(Predator("Лиса", energy=50))
    eco.add_organism(Predator("Волк", energy=60))

    return eco


def main():
    """
    Основная функция запуска симулятора.
    """
    print_header("КОНСОЛЬНЫЙ СИМУЛЯТОР ЖИЗНИ")
    print(f"  Репозиторий: {REPO_URL}")

    eco = create_default_ecosystem()
    eco.print_status()

    days = get_simulation_days()

    for day in range(days):
        eco.simulate_day()

        # Каждые 5 дней предлагаем подробный статус
        if (day + 1) % 5 == 0:
            if ask_yes_no("\nПоказать подробный статус?"):
                eco.print_status()

        # Проверяем вымирание
        total_alive = sum(
            pop.count() for pop in eco.populations.values()
        )
        if total_alive == 0:
            print("\n💀 Все организмы погибли. Симуляция завершена.")
            break

    print_header("СИМУЛЯЦИЯ ЗАВЕРШЕНА")
    eco.print_status()


if __name__ == "__main__":
    main()
