import copy

from sympy import sympify


class HookJeeves:
    """
    Реализация алгоритма Хук-Дживс для оптимизации функций.

    Attributes:
        expression: Строка, содержащая математическое выражение, представляющее оптимизируемую функцию.
        initial_point: Начальная точка поиска, заданная в виде словаря с координатами.
        initial_step: Начальный размер шага для исследующего поиска.
        epsilon: Значение, определяющее критерий останова - минимальный размер шага.
    """

    def __init__(self, expression: str, initial_point: dict[str, int | float],
                 initial_step: int | float, epsilon: int | float) -> None:
        """
        Инициализация объекта алгоритма Хук-Дживс.
        :param expression: Строка, содержащая математическое выражение, представляющее оптимизируемую функцию.
        :param initial_point: Начальная точка поиска, заданная в виде словаря с координатами.
        :param initial_step: Начальный размер шага для исследующего поиска.
        :param epsilon: Значение, определяющее критерий останова - минимальный размер шага.
        :return: None
        """
        self.initial_point = copy.copy(initial_point)
        self.current_point = initial_point
        self.current_step = initial_step
        self.function = sympify(expression)
        self.epsilon = epsilon

    def explore(self, current_point: dict[str, int | float], current_step: int | float) -> dict[str, int | float]:
        """
        Метод для выполнения исследующего поиска (первый этап).
        :param current_point: Текущая точка поиска, заданная в виде словаря с координатами.
        :param current_step: Текущий размер шага для исследующего поиска.
        :return: Новая точка после исследующего поиска.
        """
        current_value = self.function.subs(current_point)
        for point in current_point:
            candidate_point = copy.copy(current_point)
            candidate_point[point] += current_step
            candidate_value = self.function.subs(candidate_point)
            if candidate_value <= current_value:
                current_point = candidate_point
            else:
                candidate_point[point] -= 2 * current_step
                candidate_value = self.function.subs(candidate_point)
                if candidate_value <= current_value:
                    current_point = candidate_point
        return current_point

    def pattern_search(self, current_point: dict[str, int | float], initial_point: dict[str, int | float]) -> dict[str, int | float]:
        """
        Метод для выполнения поиска по образцу (второй этап).
        :param current_point: Текущая точка поиска, заданная в виде словаря с координатами.
        :param initial_point: Начальная точка поиска, заданная в виде словаря с координатами.
        :return: Новая точка после поиска по образцу.
        """
        lambda_idx = 1
        initial_value = self.function.subs(current_point)
        candidate_value, previous_candidate, previous_point, candidate_point = None, None, None, None
        while True:
            previous_point = candidate_point
            # нахождение координат точек
            candidate_point = {}
            for point in current_point:
                candidate_point[point] = current_point[point] + lambda_idx * (current_point[point] - initial_point[point])

            # вычисление значения функции
            previous_candidate = candidate_value
            candidate_value = self.function.subs(candidate_point)
            if previous_candidate is None and candidate_value >= initial_value:
                # проверяем условие окончания алгоритма
                if self.current_step > self.epsilon:
                    # уменьшаем приращение в 2 раза
                    self.current_step = self.current_step / 2
            if previous_candidate is not None and candidate_value >= previous_candidate:
                return previous_point
            lambda_idx += 1

    def solve(self) -> None:
        """
        Метод для выполнения итераций алгоритма до достижения критерия останова.
        :return: None
        """
        while self.current_step >= self.epsilon:
            self.initial_point = copy.copy(self.current_point)
            self.current_point = self.explore(self.current_point, self.current_step)
            self.current_point = self.pattern_search(self.current_point, self.initial_point)


if __name__ == "__main__":
    algo = HookJeeves("(x1 + x2) ^ 2 + (x2 - 1) ^ 2", {"x1": 5, "x2": 6}, 2, 0.2)
    algo.solve()
    print(f"{algo.current_point=} {algo.current_step}")
