"""
Топология сети
Ограничение времени	3 секунды
Ограничение памяти	512Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

Распределённая сеть Александра состоит из n вычислительных узлов, соединённых с помощью помощью  n−1 кабелей.
Каждый кабель соединяет ровно два различных узла, при этом любые два узла соединены кабелем напрямую,
либо через цепочку промежуточных узлов. Александр очень переживает за сохранность данных в системе,
поэтому хочет установить дополнительные жесткие диски на два компьютера-хранилища.
Расстоянием между двумя узлами Александр называет минимальное количество соединений на цепочке от одного узла к другому.
После выбора узлов для установки дополнительных хранилищ, для каждого узла сети Александр определяет ближайшее к нему хранилище.
Ненадёжностью сети он называет максимальное значение этой величины по всем узлам.
Помогите Александру, сообщите, на какие различные компьютеры необходимо установить дополнительные жесткие диски,
чтобы ненадёжность сети была минимальна.

Формат ввода
В первой строке входных данных записано одно целое число n (2≤n≤200000) — количество компьютеров в системе Александра.
Далее в n−1 строках записаны по два целых числа xy(1≤x,y≤n, x≠y) — номера компьютеров, соединенных кабелем.
Формат вывода
В единственной строке выведите номера двух различных выбранных компьютеров.
Если существует несколько решений, удовлетворяющих условию задачи, то выведите любое из них.
"""

"""
Логика решения построена на наблюдениях, в которых потенциальные вершины для хранилищ имеют
глубину(максимальное расстояние до крайних точек) больше чем у центра графа на 2
Однако такое решение не верно
Это практически классическая минимаксная задача размещения, только в интернете решают её для 1 центра, а мы решаем
для двух центров(часто приводят в пример задачу как разместить центры МЧС или Скорой помощи в городе, чтобы сократить
максимальное расстояние до каждого жителя)
Для решения задачи ключевым является алгоритм Дейкстры для поиска самого короткого пути от целевой вершины графа к 
остальным
"""
def dijkstra_algo(computer):
    """
    Алгоритм Дейкстры для поиска минимального пути от целевой вершины графа до всех остальных
    :param computer: На вход принимается один компьютер из пары, которую алгоритм посчитал потенциальной для хранилища
    :return: Функция возвращает список шагов от компьютера-хранилища до всех остальных компьютеров
    """
    steps_from_computer_to_other_computers = []
    visited_computers = []
    MAXWEIGHTVALUE = 200000
    for i in range(total_computers):
        steps_from_computer_to_other_computers.append([])
        visited_computers.append([])
    for x in range(total_computers):
        steps_from_computer_to_other_computers[x] = MAXWEIGHTVALUE
        visited_computers[x] = 1
    steps_from_computer_to_other_computers[computer] = 0
    while True:
        min_value_index = MAXWEIGHTVALUE
        min_weight_to_computer = MAXWEIGHTVALUE
        for x in range(total_computers):
            if visited_computers[x] == 1 and steps_from_computer_to_other_computers[x] < min_weight_to_computer:
                min_weight_to_computer = steps_from_computer_to_other_computers[x]
                min_value_index = x
        if min_value_index != MAXWEIGHTVALUE:
            for x in range(total_computers):
                if connection_matrix[min_value_index][x]:
                    temp_weight = min_weight_to_computer + connection_matrix[min_value_index][x]
                    if temp_weight < steps_from_computer_to_other_computers[x]:
                        steps_from_computer_to_other_computers[x] = temp_weight
            visited_computers[min_value_index] = 0
        if min_value_index == MAXWEIGHTVALUE:
            break

    # print(steps_from_computer_to_other_computers, computer_1+1)
    return steps_from_computer_to_other_computers


def make_matrix():
    """
    Функция создает саму матрицу(двумерный массив), которую мы будем использовать далее
    """
    for x in range(total_computers):
        connection_matrix.append([])
        for y in range(total_computers):
            connection_matrix[x].append(0)


def fill_matrix():
    """
    Функция заполняет матрицу единицами если между парами есть связь
    """
    for _ in range(total_computers - 1):
        connected_pair = input()
        connected_pair = connected_pair.split()
        first_computer = int(connected_pair[0]) - 1
        second_computer = int(connected_pair[1]) - 1
        connection_matrix[first_computer][second_computer] = 1
        connection_matrix[second_computer][first_computer] = 1


def check_all_computers_longest_way():
    """
    Функция просчитывает лямбду/максимальную глубину/длину пути до самой дальней точки
    Точка или точки у которых будет самое маленькое максимальное значение этой длины - будут центрами или центром графа
    Потенциальные хранилища по наблюдениям имеют глубину центра + 2, но видимо это не работает на больших графах
    """
    global max_depth
    depths_list = []
    visited_computers_list = []
    for i in range(total_computers):
        visited_computers_list.append([])
    for i in range(total_computers):
        for x in range(total_computers):
            visited_computers_list[x] = 0
        visited_computers_list[i] = 1
        depth_find_recursion(i, connection_matrix, visited_computers_list, 0)
        depths_list.append([max_depth, i])
        max_depth = 0
    depths_list.sort()
    find_potential_storage(depths_list)


def depth_find_recursion(index, connection_matrix, visited_computers_list, depth):
    """
    Рекурсия для поиска глубины
    :param index: принимает на вход индекс точки, от которой считается глубина
    :param connection_matrix: принимает на вход матрицу соединений
    :param visited_computers_list: принимает на вход уже посещенные компьютеры
    :param depth: принимает на вход глубину поиска, чтобы каждую итерацию увеличивать её
    """
    global max_depth
    for j in range(total_computers):
        if connection_matrix[index][j]:
            if not visited_computers_list[j]:
                visited_computers_list[j] = 1
                depth_find_recursion(j, connection_matrix, visited_computers_list, depth + 1)
    if max_depth < depth:
        max_depth = depth


def find_potential_storage(depths_list):
    """
    Функция ищет вершины графа которые могли бы стать потенциальными хранилищами
    :param depths_list: Функция принимает на вход список глубин для каждой точки
    """
    potential_storage_list = []
    depth = 0
    i = 0
    while depth != 3 and i < len(depths_list) - 1:
        potential_storage_list.append(depths_list[i][1])
        if depths_list[i][0] != depths_list[i + 1][0]:
            depth += 1
        i += 1
    # print(potential_storage_list)
    check_all_pairs_for_reliability(potential_storage_list)


def check_computers_in_list(computer_pairs_list, potential_storages):
    """
    Функция проверяет нет ли зеркальной пары, дабы не выполнять в будущем для неё тяжеловесные вычисления
    :param computer_pairs_list: На вход принимается список пар
    :param potential_storages: На вход принимается пара потенциальных хранилищ
    :return: Функция возвращает True если такая пара уже есть в списке и False если такой пары в списке нет
    """
    for i in range(len(computer_pairs_list)):
        if computer_pairs_list[i][0] == potential_storages[0]:
            if computer_pairs_list[i][1] == potential_storages[1]:
                return True
    return False


def check_all_pairs_for_reliability(potential_storage_list):
    """
    Функция проверяет ненадежность каждого потенциального варианта пар для роли хранилищ
    :param potential_storage_list: На вход принимается список потенциальных пар
    """
    computer_pairs_list = []
    computer_pairs_reliability_dict = {}
    for i in range(len(potential_storage_list)):
        for j in range(len(potential_storage_list)):
            if i == j:
                continue
            first_computer = potential_storage_list[i]
            second_computer = potential_storage_list[j]
            if not check_computers_in_list(computer_pairs_list, [first_computer, second_computer]):
                computer_pairs_list.append([first_computer, second_computer])
                computer_pairs_list.append([second_computer, first_computer])
                first_computer_reliability = dijkstra_algo(first_computer)
                second_computer_reliability = dijkstra_algo(second_computer)
                best_reliability_list = []
                for x in range(len(first_computer_reliability)):
                    if first_computer_reliability[x] < second_computer_reliability[x]:
                        best_reliability_list.append(first_computer_reliability[x])
                    else:
                        best_reliability_list.append(second_computer_reliability[x])
                best_reliability_list.sort()
                # print(f"Для пары выше лучшие пути {best_reliability_list}")
                # print("")
                computer_pairs_reliability_dict[best_reliability_list[len(best_reliability_list) - 1]] = [
                    first_computer + 1, second_computer + 1]
    list_keys = list(computer_pairs_reliability_dict.keys())
    list_keys.sort()
    print(computer_pairs_reliability_dict[list_keys[0]][0], computer_pairs_reliability_dict[list_keys[0]][1])


total_computers = input()
total_computers = int(total_computers)
connection_matrix = []
max_depth = 0
make_matrix()
fill_matrix()
if total_computers == 2:
    print(1, 2)
else:
    check_all_computers_longest_way()
