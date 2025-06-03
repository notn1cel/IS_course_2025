import numpy as np

def uniform_intervals(a, b, n):
    """1. создает numpy массив - равномерное разбиение интервала от a до b на n отрезков."""
    return np.linspace(a, b, n)


def cyclic123_array(n):
    """2. Генерирует numpy массив длины 3𝑛 , заполненный циклически числами 1, 2, 3, 1, 2, 3, 1...."""
    return np.tile([1, 2, 3], n)

def first_n_odd_number(n):
    """3. Создает массив первых n нечетных целых чисел"""
    return np.arange(1, n*2, 2)

def zeros_array_with_border(n):
    m = np.ones((n, n))
    m[1:-1, 1:-1] = 0
    """4. Создает массив нулей размера n x n с "рамкой" из единиц по краям."""

    return m

def chess_board(n):
    m = np.zeros((n, n))
    m[1::2, 1::2] = 1
    m[::2, ::2] = 1
    """5. Создаёт массив n x n с шахматной доской из нулей и единиц"""
    return m

def matrix_with_sum_index(n):
    m = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            m[i][j] += i+j
    """6. Создаёт 𝑛 × 𝑛  матрицу с (𝑖,𝑗)-элементами равным 𝑖+𝑗."""
    return m

def cos_sin_as_two_rows(a, b, dx):
    m = np.arange(a, b, dx)
    co = np.cos(m)
    si = np.sin(m)
    """7. Вычислите $cos(x)$ и $sin(x)$ на интервале [a, b) с шагом dx, 
    а затем объедините оба массива чисел как строки в один массив. """
    return np.array([co, si])

def compute_mean_rowssum_columnssum(A):
    """8. Для numpy массива A вычисляет среднее всех элементов, сумму строк и сумму столбцов."""
    return np.mean(A), np.sum(A, axis=0), np.sum(A, axis=1)

def sort_array_by_column(A, j):
    """ 9. Сортирует строки numpy массива A по j-му столбцу в порядке возрастания."""
    return A[np.argsort(A[:, j])]

def compute_integral(a, b, f, dx, method):
    """10. Считает определённый интеграл функции f на отрезке [a, b] с шагом dx 3-мя методами: """
    if method == 'rectangular': # - методом прямоугольника
        return np.sum(f(np.arange(a, b, dx))) * dx
    elif method == 'trapezoidal': # - методом трапеций
        return np.sum((f(np.arange(a, b, dx)) + f(np.arange(a + dx, b + dx/2, dx))) * dx / 2)
    elif method == 'simpson': # методом Симпсона
        return np.sum((f(np.arange(a, b, dx))
                       + 4*f(np.arange(a + dx/2, b + dx/2, dx))
                       + f(np.arange(a + dx, b + dx/2, dx))) * dx/6)
    pass