# Считывание размерности матрицы
def get_matrix_size():
    print("Размерность матрицы (введите f для ввода из файла, k для ввода с клавиатуры:")

    while True:
        input_type = input()
        if input_type == "f":
            print("В файле должно быть целое число от 1 до 20.")
            while True:
                print("Введите имя файла:")
                file_name = input()
                try:
                    file = open(file_name, 'r')
                    size = int(file.readline())
                    if size < 1 or size > 20:
                        print("Значение должно быть в промежутке [1,20]")
                        continue
                    return size
                except FileNotFoundError:
                    print("Файл не найден. Попробуйте еще раз.")
                    continue
                except ValueError:
                    print("Некорректное значение. Повторите ввод.")
                    continue
        elif input_type == "k":
            while True:
                print("Введите целое число от 1 до 20:")
                try:
                    size_string = input()
                    size = int(size_string)
                    if size < 1 or size > 20:
                        print("Значение должно быть в промежутке [1,20]")
                        continue
                    return size
                except ValueError:
                    print("Некорректное значение. Повторите ввод.")
                    continue
        else:
            print("Некорректный формат ввода. Повторите еще раз:")


# Считывание элементов матрицы
def get_matrix_values(size):
    print("Значения матрицы (введите f для ввода из файла, k для ввода с клавиатуры:")

    while True:
        input_type = input()
        if input_type == "f":
            print(
                "Данные в файле должны быть в формате каждая строка матрицы в отдельной строке файла, элементы в строке разделяются пробелами.")
            while True:
                print("Введите имя файла:")
                file_name = input()
                try:
                    file = open(file_name, 'r')
                    table = []
                    for row in range(size):
                        elements_string = file.readline().split()
                        if len(elements_string) != size:
                            print("Неправильное количество элементов в строке", row + 1)
                            raise ArithmeticError
                        table.append(list(map(float, elements_string)))
                    return table
                except FileNotFoundError:
                    print("Файл не найден. Попробуйте еще раз.")
                    continue
                except ValueError:
                    print("Некорректные значения. Повторите ввод.")
                    continue
                except ArithmeticError:
                    continue
        elif input_type == "k":
            while True:
                table = []
                for row in range(size):
                    while True:
                        print("Введите элементы ", row + 1, " строки через пробел:")
                        try:
                            elements_string = input().split()
                            if len(elements_string) != size:
                                print("Неправильное количество элементов в строке")
                                continue
                            table.append(list(map(float, elements_string)))
                            break
                        except ValueError:
                            print("Некорректные значения. Повторите ввод.")
                            continue
                return table
        else:
            print("Некорректный формат ввода. Повторите еще раз:")


def calculate_matrix(table, size):
    return table


def print_matrix(table):
    for row in range(len(table)):
        for x in table[row]:
            print(x, end='   ')
        print('')


def calculate_det(table, size):
    if size == 1:
        return table[0]
    elif size == 2:
        return table[0][0] * table[1][1] - table[0][1] * table[1][0]
    elif size > 2:
        det = 0
        for i in range(size):
            table1 = []
            for row in range(1, size):
                table1.append(table[row][:i] + table[row][i + 1:])
            det += (-1) ** (2 + i) * table[0][i] * calculate_det(table1, size - 1)
        return det


print("Решение системы методом Гаусса с выбором главного элемента по столбцам.")
matrix_size = get_matrix_size()
print("Размерность матрицы - ", matrix_size, "x", matrix_size)
matrix = get_matrix_values(matrix_size)
print_matrix(matrix)
# calculate_matrix(matrix, matrix_size)
print("Определитель матрицы:", calculate_det(matrix, matrix_size))
