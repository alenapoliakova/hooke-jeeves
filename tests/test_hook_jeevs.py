import pytest

from src.algorithm import HookJeeves


@pytest.mark.timeout(3)
@pytest.mark.parametrize("function,initial_points,delta,epsilon,expected_points,expected_step", [
    # 1. Простая проверка с двумя слагаемыми в степени
    ("x1**2 + x2**2", {"x1": -1, "x2": -1}, 0.5, 0.2, {"x1": 0, "x2": 0}, 0.125),
    # 2. Проверка с выделением коэффициентов у переменных
    ("(x1 - 2)**2 + 3*(x2**2)", {"x1": 0, "x2": -1}, 0.5, 0.2, {"x1": 2, "x2": 0}, 0.125),
    # 3. Тест из примера Кати
    ("(x1+x2)**2 + (x2-1)**2", {"x1": 5, "x2": 6}, 2, 0.2, {"x1": -1, "x2": 1}, 0.125)
])
def test_hook_jeeves(function, initial_points, delta, epsilon, expected_points,
                     expected_step) -> None:
    algo = HookJeeves(function, initial_points, delta, epsilon)
    algo.solve()
    assert algo.current_point == expected_points
    assert algo.current_step == expected_step


@pytest.mark.parametrize("function,initial_points,delta,epsilon,expected_points", [
    # 1. Простая проверка с двумя слагаемыми в степени
    ("x1**2 + x2**2", {"x1": -1, "x2": -1}, 0.5, 0.2, {"x1": -0.5, "x2": -0.5}),
    # 2. Проверка с выделением коэффициентов у переменных
    ("(x1 - 2)**2 + 3*(x2**2)", {"x1": 0, "x2": -1}, 0.5, 0.2, {"x1": 0.5, "x2": -0.5}),
    # 3. Тест из примера Кати
    ("(x1+x2)**2 + (x2-1)**2", {"x1": 5, "x2": 6}, 2, 0.2, {"x1": 3, "x2": 4})
])
def test_explore(function, initial_points, delta, epsilon, expected_points) -> None:
    """Проверка полученных точек после исследовательского поиска."""
    algo = HookJeeves(function, initial_points, delta, epsilon)
    algo.explore()
    assert algo.current_point == expected_points


@pytest.mark.parametrize("function,initial_points,delta,epsilon,expected_points", [
    # 1. Простая проверка с двумя слагаемыми в степени
    ("x1**2 + x2**2", {"x1": -1, "x2": -1}, 0.5, 0.2, {"x1": -1, "x2": -1}),
    # 2. Проверка с выделением коэффициентов у переменных
    ("(x1 - 2)**2 + 3*(x2**2)", {"x1": 0, "x2": -1}, 0.5, 0.2, {"x1": 0, "x2": -1}),
    # 3. Тест из примера Кати
    ("(x1+x2)**2 + (x2-1)**2", {"x1": 5, "x2": 6}, 2, 0.2, {"x1": 5, "x2": 6})
])
def test_pattern_search(function, initial_points, delta, epsilon, expected_points) -> None:
    """Проверка полученных точек после поиска по образцу."""
    algo = HookJeeves(function, initial_points, delta, epsilon)
    algo.pattern_search()
    assert algo.current_point == expected_points
