from src.algorithm import HookJeeves


def test_hook_jeeves() -> None:
    """Простой тест алгоритма."""
    # Инициализация объекта алгоритма
    algo = HookJeeves("(x1 + x2) ** 2 + (x2 - 1) ** 2",
                      {"x1": 5, "x2": 6}, 2, 0.2)
    # Выполнение алгоритма
    algo.solve()
    # Проверка полученного результата
    assert algo.current_point == {'x1': -1.0, 'x2': 1.0}
    assert algo.current_step == 0.125
