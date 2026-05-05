"""
Вспомогательные утилиты для симулятора.
"""


def print_header(title: str):
    """
    Выводит красивый заголовок в консоль.

    Args:
        title (str): Текст заголовка.
    """
    border = "=" * 45
    print(f"\n{border}")
    print(f"  {title}")
    print(f"{border}")


def get_simulation_days() -> int:
    """
    Запрашивает у пользователя количество дней симуляции.

    Returns:
        int: Количество дней (от 1 до 100).
    """
    while True:
        try:
            days = int(input("\nСколько дней симулировать? (1-100): "))
            if 1 <= days <= 100:
                return days
            print("  Введите число от 1 до 100.")
        except ValueError:
            print("  Ошибка: введите целое число.")


def ask_yes_no(question: str) -> bool:
    """
    Задаёт пользователю вопрос с ответом да/нет.

    Args:
        question (str): Текст вопроса.

    Returns:
        bool: True если ответ 'да', False если 'нет'.
    """
    while True:
        answer = input(f"{question} (да/нет): ").strip().lower()
        if answer in ("да", "д", "yes", "y"):
            return True
        if answer in ("нет", "н", "no", "n"):
            return False
        print("  Введите 'да' или 'нет'.")
