from math import sqrt


def get_roots(a, b, c):

    '''
    engl: This function is implementing Quadratic equation
    https://en.wikipedia.org/wiki/Quadratic_equation
    examples is below, launch from command line:
    python -i quadratic_equation.py

    launch doctest's:
    python -m doctest quadratic_equation.py -v

    launch unittest's (they are in other file):
    python tests.py 
    ----------------------------------------------------------
    rus: это функция расчета корней квадратного уравнения
    https://ru.wikipedia.org/wiki/Квадратное_уравнение
    Примеры ниже, запускать из командной строки

    python -i quadratic_equation.py

    запуск doctest-ов:
    python -m doctest quadratic_equation.py -v

    запуск unittest-ов (в отдельном файле):
    python tests.py 

    ----------------------------------------------------------
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

    '''

    discriminant = (b ** 2) - (4 * a * c)

    if discriminant == 0:
        root1 = (-b - sqrt(discriminant)) / (2 * a)

        return root1, None

    elif discriminant < 0:
        return None, None

    elif discriminant > 0:
        root1 = (-b - sqrt(discriminant)) / (2 * a)
        root2 = (-b + sqrt(discriminant)) / (2 * a)
        return root1, root2


