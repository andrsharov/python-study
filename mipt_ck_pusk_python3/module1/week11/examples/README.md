# Пример работы с pytest

## Подготовка

```bash
pip install -r requirements.txt
```

## Описание файлов

* main.py — основной модуль программы. Задача — протестировать функции first_function() и second_function(). Обратите внимание на импортируемые объекты.
* include/my_module.py — модуль, из которого импортируется функция get_lucky_number() и класс DataProvider.
* tests/test_*.py — код для pytest, демонстрирующий использование мок-объекта и фикстуры.

## Использование

1. Запуск тестов: просто выполнить pytest в директории проекта.

2. Создание отчета о покрытии:

```bash
pytest --cov --cov-report=html:cov_report
```

Отчет появится в директории cov_report.
