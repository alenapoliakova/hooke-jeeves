import random
import tkinter as tk
from tkinter import scrolledtext

from src.algorithm import HookJeeves


class Application(tk.Tk):
    """Графическое приложение для решения уравнений с использованием алгоритма Хука-Дживса."""

    def __init__(self) -> None:
        """Инициализация главного окна приложения."""
        super().__init__()
        self.title("The Hooke-Jeeves")
        self.configure(bg='#fafafa')
        self.geometry('600x500')
        self.resizable(width=False, height=False)

        self.create_widgets()

    def create_widgets(self) -> None:
        """Создание всех виджетов для приложения."""
        self.create_title()
        self.create_display()
        self.create_equation_input()
        self.create_accuracy_input()
        self.create_buttons()

    def create_title(self) -> None:
        """Создание заголовка с названием приложения и команды."""
        title_frame = tk.Frame(self, bg='green', height=50)
        title_frame.pack(fill='x')
        tk.Label(
            title_frame,
            text='Coded and Designed by Malinnik team',
            background='green',
            foreground='white',
            width=60
        ).pack(side='left', padx=10)
        tk.Label(
            title_frame,
            text='Алгоритм Хука-Дживса',
            background='green',
            foreground='white',
            font=('Helvetica', 20)
        ).pack(side='left')

    def create_display(self) -> None:
        """Создание области для отображения решения."""
        self.display = scrolledtext.ScrolledText(self, bg="white")
        self.display.place(x=20, y=60, width=560, height=300)
        self.display.insert(tk.INSERT, 'Решение: ' + '\n')

    def create_equation_input(self) -> None:
        """Создание поля ввода для уравнения."""
        tk.Label(
            self,
            text='Введите уравнение:',
            background='white',
            foreground='black'
        ).place(x=20, y=380)
        self.entry_equation = tk.Entry(self, bg='white', width=40)
        self.entry_equation.place(x=140, y=382)

    def create_accuracy_input(self) -> None:
        """Создание поля ввода для желаемой точности."""
        tk.Label(
            self,
            text='Введите точность:',
            background='white',
            foreground='black'
        ).place(x=20, y=410)
        self.entry_accuracy = tk.Entry(self, bg='white', width=40)
        self.entry_accuracy.place(x=140, y=410)

    def create_buttons(self) -> None:
        """Создание кнопок начала и остановки, а также отображения ответа."""
        start_button = tk.Button(
            self,
            text='Начать',
            bg='green',
            foreground='white',
            command=self.start_click
        )
        start_button.place(x=20, y=445, width=110, height=30)

        stop_button = tk.Button(
            self,
            text='Остановить',
            bg='red',
            foreground='white',
            command=self.stop_click
        )
        stop_button.place(x=140, y=445, width=110, height=30)

        tk.Label(
            self,
            text='Ответ:',
            background='white smoke',
            foreground='black'
        ).place(x=300, y=450)
        self.answer_entry = tk.Entry(self, bg='white', width=37)
        self.answer_entry.place(x=345, y=450)

    def start_click(self) -> None:
        """Обработчик события нажатия кнопки 'Начать' для запуска алгоритма Хука-Дживса."""
        initial_point = {"x1": random.randint(1, 10), "x2": random.randint(1, 10)}
        algo = HookJeeves(self.entry_equation.get(), initial_point, 2,  # type: ignore
                          float(self.entry_accuracy.get()))
        algo.solve()
        self.display.insert(tk.INSERT, f"{algo.current_point=} {algo.current_step}")
        self.answer_entry.insert(tk.INSERT, f"{algo.current_point=} {algo.current_step}")

    def stop_click(self) -> None:
        """Обработчик события нажатия кнопки 'Остановить' для очистки дисплея."""
        self.display.delete(1.0, tk.END)
        self.display.insert(tk.INSERT, 'Решение: ' + '\n')


if __name__ == "__main__":
    app = Application()
    app.mainloop()
