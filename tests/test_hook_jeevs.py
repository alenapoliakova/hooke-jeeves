import pytest
from src.algorithm import HookJeeves


@pytest.mark.timeout(3)
@pytest.mark.parametrize("function,initial_points,delta,epsilon,expected_points,expected_step", [
    # 1. Простая проверка с двумя слагаемыми в степени
    ("x1**2 + x2**2", {"x1": 5, "x2": 6}, 0.5, 0.2, {"x1": 0, "x2": 0}, 0.125),
    # 2. Простая проверка с наличием слагаемого без степени
    ("x1**3 + x2**3 - 3*x1*x2", {"x1": 5, "x2": 6}, 0.5, 0.2, {"x1": 1, "x2": 1}, 0.125),
    # 3. Проверка с коэффициентами у переменных
    ("x1**3 + 3*x1*x2 - 15*x1 - 12*x2", {"x1": 5, "x2": 6}, 2, 0.2, {"x1": 0.5, "x2": 1}, 0.125),
    # 4. Проверка с выделением коэффициентов у переменных
    ("(x1 - 2)**2 + 3*(x2**2)", {"x1": 5, "x2": 6},0.5, 0.2, {"x1": 2, "x2": 0}, 0.125),
    # 5. Функция Розенброка
    ("(1-x1)**2 + 100*((x2 - x1**2)**2)", {"x1": 5, "x2": 6}, 0.5, 0.2, {"x1": 1, "x2": 1}, 0.125),
])
def test_hook_jeeves(function, initial_points, delta, epsilon, expected_points, expected_step) -> None:
    algo = HookJeeves(function, initial_points, delta, epsilon)
    algo.solve()
    assert algo.current_point == expected_points
    assert algo.current_step == expected_step
