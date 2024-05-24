import pytest
from src.algorithm import HookJeeves


@pytest.mark.timeout(3)
@pytest.mark.parametrize("function,initial_points,delta,epsilon,explore_points,pattern_search_points,expected_points,expected_step", [
    # 1. Простая проверка с двумя слагаемыми в степени
    ("x1**2 + x2**2", {"x1": -1, "x2": -1}, 0.5, 0.2, {"x1": -0.5, "x2": -0.5}, {"x1": -1, "x2": -1}, {"x1": 0, "x2": 0}, 0.125),
    # 2. Проверка с выделением коэффициентов у переменных
    ("(x1 - 2)**2 + 3*(x2**2)", {"x1": 0, "x2": -1},0.5, 0.2, {"x1": -0.5, "x2": -0.5}, {"x1": -1, "x2": -1}, {"x1": 2, "x2": 0}, 0.125),
    # 3. Тест из примера Кати
    ("(x1+x2)**2 + (x2-1)**2", {"x1": 5, "x2": 6}, 2, 0.2, {"x1": -0.5, "x2": -0.5}, {"x1": -1, "x2": -1}, {"x1": -1, "x2": 1}, 0.125)
])

#Тест на правильность выполнения
def test_hook_jeeves(function,initial_points,delta,epsilon,expected_points,expected_step) -> None:
    algo = HookJeeves(function, initial_points, delta, epsilon)
    algo.solve()
    assert algo.current_point == expected_points
    assert algo.current_step == expected_step

#Проверка полученных точек после исследовательного поиска
def test_explore(function,initial_points,delta,epsilon,explore_point,pattern_search_point,expected_points,expected_step) -> None:
    algo = HookJeeves(function, initial_points, delta, epsilon)
    algo.explore()
    assert algo.current_point == explore_points

#Проверка полученных точек после поиска по шаблону
def test_pattern_search(function,initial_points,delta,epsilon,explore_point,pattern_search_point,expected_points,expected_step) -> None:
    algo = HookJeeves(function, initial_points, delta, epsilon)
    algo.pattern_search()
    assert algo.current_point == pattern_search_points
