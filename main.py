# Считывание размерности матрицы
def get_matrix_size():
    print("Размерность матрицы (введите f для ввода из файла, k для ввода с клавиатуры:")

    while True:
        input_type = input()
        if input_type == "f":
            print("Данные в файле должны быть в формате <количество_строк количество_столбцов>.")
            while True:
                print("Введите имя файла:")
                file_name = input()
                try:
                    file = open(file_name, 'r')
                    size = list(map(int, file.readline().split()))
                    if len(size) != 2:
                        print("Значения должны быть в формате <количество_строк количество_столбцов>.")
                        continue
                    if size[0] < 1 or size[0] > 20 or size[1] < 1 or size[1] > 20:
                        print("Значения должны быть в промежутке [1,20]")
                        continue
                    return size
                except FileNotFoundError:
                    print("Файл не найден. Попробуйте еще раз.")
                    continue
                except ValueError:
                    print("Некорректные значения. Повторите ввод.")
                    continue
        elif input_type == "k":
            while True:
                print("Введите размерность матрицы в формате <количество_строк количество_столбцов>:")
                try:
                    size_string = input()
                    size = list(map(int, size_string.split()))
                    if len(size) != 2:
                        print("Значения должны быть в формате <количество_строк количество_столбцов>.")
                        continue
                    if size[0] < 1 or size[0] > 20 or size[1] < 1 or size[1] > 20:
                        print("Значения должны быть в промежутке [1,20]")
                        continue
                    return size
                except ValueError:
                    print("Некорректные значения. Повторите ввод.")
                    continue
        else:
            print("Некорректный формат ввода. Повторите еще раз:")


# Считывание элементов матрицы
def get_matrix_values(rows_count, columns_count):
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
                    for row in range(rows_count):
                        elements_string = file.readline().split()
                        if len(elements_string) != columns_count:
                            print("Неправильное количество элементов в строке", row + 1)
                            raise ArithmeticError
                        table.append(list(map(int, elements_string)))
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
                for row in range(rows_count):
                    while True:
                        print("Введите элементы ", row + 1, " строки через пробел:")
                        try:
                            elements_string = input().split()
                            if len(elements_string) != columns_count:
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


def calculate_matrix(table, rows_count, columns_count):
    return table


print("Решение системы методом Гаусса с выбором главного элемента по столбцам.")
matrix_size = get_matrix_size()
print(matrix_size)
matrix = get_matrix_values(matrix_size[0], matrix_size[1])
print(matrix)
calculate_matrix(matrix, matrix_size[0], matrix_size[1])
