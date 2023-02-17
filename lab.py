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
                        if len(elements_string) != size + 1:
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
                            if len(elements_string) != size + 1:
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


# Приведение матрицы к треугольному виду с выбором главного элемента по столбцу
def matrix_to_triangle(table, size):
    k = 0
    for column in range(size - 1):
        max_el = 0
        max_row = column
        for row in range(column, size):
            if abs(table[row][column]) > max_el:
                max_el = abs(table[row][column])
                max_row = row
        if max_row != column:
            k += 1
            table1 = table[max_row]
            table[max_row] = table[column]
            table[column] = table1
        for row in range(column + 1, size):
            if table[row][column] != 0:
                x = -(table[row][column] / table[column][column])
                table1 = [y * x for y in table[column]]
                for i in range(column, size + 1):
                    table[row][i] = round(table1[i] + table[row][i], 5)
        print("Выбор главного элемента по", column + 1, "столбцу")
        print_matrix(table)
        print()
    return table, k


# Вычисление вектора неувязок
def calculate_hitch(table, size, x_table):
    r_table = []
    for row in range(size):
        sum_el = 0
        for el_index in range(size):
            sum_el += x_table[el_index] * table[row][el_index]
        r_table.append(round(sum_el - table[row][-1], 5))
        if abs(r_table[row]) == 0:
            r_table[row] = abs(r_table[row])
    print("Вектор неувязок:", r_table)


def calculate_det(table, size, k):
    det = (-1)**k
    for i in range(size):
        det *= table[i][i]
    return det

# Решение СЛАУ
def calculate_matrix(table, size):
    table1 = table.copy()
    table, replace_count = matrix_to_triangle(table, size)
    print("\nОпределитель треугольной матрицы: ", round(calculate_det(table, size, replace_count), 5), "\n")
    print("Треугольная матрица")
    print_matrix(table)
    print()
    x_table = [0 for i in range(size)]

    for row in range(size - 1, -1, -1):
        sum = table[row][-1]
        for i in range(row + 1, size):
            sum -= table[row][i] * x_table[i]
        x_table[row] = round(sum / table[row][row], 5)
        if abs(x_table[row]) == 0:
            x_table[row] = abs(x_table[row])
    print("Вектор неизвестных:", x_table)
    calculate_hitch(table1, size, x_table)


# Вывод матрицы в консоль
def print_matrix(table):
    for row in range(len(table)):
        for x in table[row]:
            print('%.5f' % x, end='   ')
        print()


# Вычисление определителя
def calculate_det_by_definition(table, size):
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
            det += (-1) ** (2 + i) * table[0][i] * calculate_det_by_definition(table1, size - 1)
        return round(det, 5)


print("Решение системы методом Гаусса с выбором главного элемента по столбцам.")
matrix_size = get_matrix_size()
print("Размерность матрицы - ", matrix_size, "x", matrix_size)
matrix = get_matrix_values(matrix_size)
print("\nВведенная матрица")
print_matrix(matrix)
det = calculate_det_by_definition(matrix, matrix_size)
print("\nОпределитель матрицы:", det, "\n")
if det == 0:
    print("Система не имеет решений, т.к. определитель равен нулю.")
else:
    calculate_matrix(matrix, matrix_size)
