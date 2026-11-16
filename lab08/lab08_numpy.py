import numpy as np


import numpy as np


# Задание 1

hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("Задание 1")
print("hours:", hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)
print("line:", line)
print("zeros:", zeros)
print("unknown_table:\n", unknown_table)
print("identity:\n", identity)


# Задание 2

print("\nЗадание 2")
print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2-5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("В обратном порядке:", hours[::-1])


# Задание 3

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18]
])

print("\nЗадание 3")
print("shape:", temperatures.shape)
print("ndim:", temperatures.ndim)
print("size:", temperatures.size)
print("Вторая строка, третий столбец:", temperatures[1, 2])
print("Первая строка:", temperatures[0, :])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:\n", temperatures[:2, 1:])
print("Центральный фрагмент:\n", temperatures[:2, 1:3])


# Задание 4

matrix = np.arange(1, 26).reshape(5, 5)

print("\nЗадание 4")

fragment = matrix[:3, :]
print("Первые три строки:\n", fragment)
print("shape:", fragment.shape)

fragment = matrix[-2:, :]
print("Последние две строки:\n", fragment)
print("shape:", fragment.shape)

fragment = matrix[:, :2]
print("Первые два столбца:\n", fragment)
print("shape:", fragment.shape)

fragment = matrix[1:4, 2:5]
print("Фрагмент строк 1-3 и столбцов 2-4:\n", fragment)
print("shape:", fragment.shape)

fragment = matrix[-2:, -2:]
print("Правый нижний блок 2x2:\n", fragment)
print("shape:", fragment.shape)


# Задание 5

vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1

print("\nЗадание 5")
print("changed_hours:", changed_hours)
print("Исходный hours:", hours)

# copy() создаёт независимую копию массива,
# поэтому изменения не затрагивают исходный hours.

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100

print("Изменённая матрица:\n", changed_matrix)
print("Исходная матрица:\n", matrix)


# Задание 6

numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print("\nЗадание 6")
print("numbers:\n", numbers)
print("Форма numbers:", numbers.shape)
print("table:\n", table)
print("Форма table:", table.shape)
print("transposed:\n", transposed)
print("Форма transposed:", transposed.shape)

# reshape(3, 4) работает, потому что 3 * 4 = 12,
# то есть количество элементов не меняется.
# reshape(5, 3) вызовет ошибку, потому что 5 * 3 = 15,
# а в исходном массиве только 12 элементов.

