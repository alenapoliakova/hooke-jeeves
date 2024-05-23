import pytest
from src.algorithm import HookJeeves


@pytest.mark.timeout(3)
@pytest.mark.parametrize("function,initial_points,delta,epsilon,expected_points,expected_step", [
    # 1. Простая проверка с двумя слагаемыми в степени
    ("x1**2 + x2**2", {"x1": -1, "x2": -1}, 0.5, 0.2, {"x1": 0, "x2": 0}, 0.125),
    # 2. Проверка с выделением коэффициентов у переменных
    ("(x1 - 2)**2 + 3*(x2**2)", {"x1": 0, "x2": -1},0.5, 0.2, {"x1": 2, "x2": 0}, 0.125),
    # 3. Тест из примера Кати
    ("(x1+x2)**2 + (x2-1)**2", {"x1": 5, "x2": 6}, 2, 0.2, {"x1": -1, "x2": 1}, 0.125)
])
def test_hook_jeeves(function, initial_points, delta, epsilon, expected_points, expected_step) -> None:
    algo = HookJeeves(function, initial_points, delta, epsilon)
    algo.solve()
    assert algo.current_point == expected_points
    assert algo.current_step == expected_step


def test_explore() -> None:
    algo = HookJeeves("x1**2 + x2**2", {"x1": -1, "x2": -1}, 0.5, 0.2)
    algo.explore()
    assert algo.current_point == {"x1": -0.5, "x2": -0.5}


def test_pattern_search() -> None:
    algo = HookJeeves("x1**2 + x2**2", {"x1": -1, "x2": -1}, 0.5, 0.2)
    algo.pattern_search()
    assert algo.current_point == {"x1": -1, "x2": -1}
