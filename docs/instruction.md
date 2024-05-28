# Инструкция по запуску алгоритма Хука-Дживса и интерфейса

## Требования

- Python 3.11
- Зависимости из файла requirements.txt

## Установка и запуск

- **Шаг 1**: Установка Python 3.11

Если у вас еще не установлен Python 3.11, скачайте и установите его с официального сайта [python.org](https://www.python.org/).

- **Шаг 2**: Установка зависимостей

Создайте виртуальное окружение и установите необходимые зависимости:

    # Создание виртуального окружения
    python3.11 -m venv venv
    
    # Активация виртуального окружения
    # Для Windows
    venv\Scripts\activate
    # Для Unix или MacOS
    source venv/bin/activate
    
    # Установка зависимостей
    pip install -r requirements.txt

- **Шаг 3**: Запуск алгоритма

Для запуска алгоритма Хука-Дживса выполните следующую команду:

    python algowithm.py

- **Шаг 4**: Запуск графического интерфейса

Для запуска графического интерфейса выполните следующую команду:

    python interface_layout.py