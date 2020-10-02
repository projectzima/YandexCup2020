massive_size = input()
massive_size = massive_size.split()
massive_a_size = int(massive_size[0])
massive_b_size = int(massive_size[1])
massive_a = input()
massive_a = massive_a.split()
massive_b = input()
massive_b = massive_b.split()
global matrix
total_summ = 0


def check_for_equal():
    strings_unique = set(massive_a)  # СЕТ уникальных строк в массиве а(строки)
    columns_unique = set(massive_b)  # СЕТ уникальных строк в массива б(столбцы)
    if len(strings_unique) == 1 and len(columns_unique) == 1:  # Если длина обоих сетов равна 1, значит все значения равны
        default = int(massive_a[0]) * (10 ** 9) + int(massive_b[0])  # Дефолтное значение ячейки
        total_summ = (default * len(massive_a)) + (default * (len(massive_b) - 1))  # Считаем сумму всей таблицы
        return total_summ, True
    else:
        return 0, False


def find_index_for_max_values(massive, index):  # доделать
    max_value = massive[int(index)]
    list_of_max_values = []
    for i in range(len(massive)):
        if massive[i] == max_value:
            list_of_max_values.append(i)
    return list_of_max_values


def find_max_summ():
    global total_summ
    StopRow = massive_a.index(max(massive_a))
    StopColumn = massive_b.index(max(massive_b))
    vecIndexStopRow = find_index_for_max_values(massive_a, StopRow)
    i = 0
    j = 0
    for step in range(len(vecIndexStopRow)):
        StopRow = vecIndexStopRow[step]
        while i != StopRow:
            total_summ += int(massive_a[i]) * 10 ** 9 + int(massive_b[j])
            i += 1
        while j != StopColumn:
            total_summ += int(massive_a[i]) * 10 ** 9 + int(massive_b[j])
            j += 1
    if StopColumn == j and StopRow == i:
        while j != len(massive_b):
            total_summ += int(massive_a[i]) * 10 ** 9 + int(massive_b[j])
            j += 1
        j -= 1
        i += 1
        while i != len(massive_a):
            total_summ += int(massive_a[i]) * 10 ** 9 + int(massive_b[j])
            i += 1
        return


def run():
    total_summ_from_equal, equal = check_for_equal()
    if equal:
        print(total_summ_from_equal)
        return
    else:
        find_max_summ()
    print(total_summ)


run()
