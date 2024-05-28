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

    def explore(self) -> None:
        """
        Метод для выполнения исследующего поиска (первый этап).
        :return: None
        """
        self.initial_point = copy.copy(self.current_point)
        current_value = self.function.subs(self.current_point)
        for point in self.current_point:
            candidate_point = copy.copy(self.current_point)
            candidate_point[point] += self.current_step
            candidate_value = self.function.subs(candidate_point)
            if candidate_value <= current_value:
                self.current_point = candidate_point
            else:
                candidate_point[point] -= 2 * self.current_step
                candidate_value = self.function.subs(candidate_point)
                if candidate_value <= current_value:
                    self.current_point = candidate_point

    def pattern_search(self) -> None:
        """
        Метод для выполнения поиска по образцу (второй этап).
        :return: None
        """
        lambda_idx = 1
        initial_value = self.function.subs(self.current_point)
        candidate_value, previous_candidate, previous_point, candidate_point = None, None, None, None
        while True:
            previous_point = candidate_point
            # нахождение координат точек
            candidate_point = {}
            for point in self.current_point:
                candidate_point[point] = self.current_point[point] + lambda_idx * (self.current_point[point] - self.initial_point[point])

            # вычисление значения функции
            previous_candidate = candidate_value
            candidate_value = self.function.subs(candidate_point)
            print(f"-->{previous_candidate=} {candidate_value=} > {previous_candidate=}: {candidate_point=}")
            if previous_candidate is None and candidate_value >= initial_value:
                # проверяем условие окончания алгоритма
                if self.current_step > self.epsilon:
                    # уменьшаем приращение в 2 раза
                    self.current_step = self.current_step / 2
            if previous_candidate is not None and candidate_value >= previous_candidate:
                self.current_point = previous_point
                break
            lambda_idx += 1

    def solve(self) -> None:
        """
        Метод для выполнения итераций алгоритма до достижения критерия останова.
        :return: None
        """
        while self.current_step >= self.epsilon:
            self.explore()
            self.pattern_search()


if __name__ == "__main__":
    algo = HookJeeves("(x1 + x2) ^ 2 + (x2 - 1) ^ 2", {"x1": 5, "x2": 6}, 2, 0.2)
    algo.solve()
    print(f"{algo.current_point=} {algo.current_step}")
