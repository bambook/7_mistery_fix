# Решатель квадратных уравнений

# описание проекта:

Программа позволяет решать квадратные уравнения

# Как использовать

    это функция расчета корней квадратного уравнения
    см. https://ru.wikipedia.org/wiki/Квадратное_уравнение
    или https://en.wikipedia.org/wiki/Quadratic_equation

    -----------------
    запуск unittest-ов (в отдельном файле):
    python tests.py 

    -----------------
    Примеры ниже, запускать из командной строки:

    python -i quadratic_equation.py

    ----------------------------------------------------------
    >>> import quadratic_equation
    >>> root1, root2 = get_roots(1, -2, 1)
    >>> print('root1 = ', root1)
    root1 =  1.0

    >>> root1, root2 = get_roots(1, 2, -3)
    >>> print('root1 = ', root1)
    root1 =  -3.0
    >>> print('root2 = ', root2)
    root2 =  1.0

    >>> root1, root2 = get_roots(1, -2, 1);
    >>> root1 is not None;
    True
    >>> root2 is None;
    True

    >>> root1, root2 = get_roots(1, 2, 3)
    >>> root1 is None;
    True
    >>> root2 is None;
    True


# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

python -i quadratic_equation.py
или 

python3 -i quadratic_equation.py

запуск unittest-ов:

```bash
python tests.py # может понадобиться вызов python3 вместо python, зависит от настроек операционной системы


```

Запуск на Windows:

python -i quadratic_equation.py

>>> root1, root2 = get_roots(1, -2, 1)
>>> print('root1 = ', root1)

запуск unittest-ов:
python tests.py

подробнее см. примеры выше

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)
