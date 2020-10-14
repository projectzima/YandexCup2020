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
Логика решения построена на делении графа на 3 части, сначала надвое центром(или двумя центрами), затем
равноудаленными от центра и от крайних точек графа вершинами. Итого мы имеем что то вроде 0---1---1---1---0  где 1 это
вершина-делитель. В нечетном графе хранилищами становятся какие-нибудь соседи крайних делителей. Итого перед алгоритмом 
Дейкстры мы имеем список пар индексов потенциальных хранилищ, для которых мы просчитываем ненадежность. Это позволяет
не проводить огромных вычислений двигаясь в стороны от центра, а сразу вычислять ненадежность из нужных вершин
Это практически классическая минимаксная задача размещения, только в интернете решают её для 1 центра, а мы решаем
для двух центров(часто приводят в пример задачу как разместить центры МЧС или Скорой помощи в городе, чтобы сократить
максимальное расстояние до каждого жителя)
Для решения задачи ключевым является алгоритм Дейкстры для поиска самого короткого пути от целевой вершины графа к 
остальным
"""


def dijkstra_algo(computer):
    # print("Запустили dijkstra_algo")
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
    # print("Запустили check_all_computers_longest_way")
    """
    Функция просчитывает лямбду/максимальную глубину/длину пути до самой дальней точки
    Точка или точки у которых будет самое маленькое максимальное значение этой длины - будут центрами или центром графа
    Потенциальные хранилища находятся на расстоянии половины длины от центра до крайней точки с округлением вниз,
    То есть если длина от центра до крайней точки равна 5, новый делитель графа будет на расстоянии 2 шагов от центра
    """
    global max_depth
    global all_steps_list
    depths_list = []
    for i in range(total_computers):
        steps_from_computer_to_other_computers = dijkstra_algo(i)
        all_steps_list.append(steps_from_computer_to_other_computers)
    max_steps = 200000
    counter = 0
    for steps_list in all_steps_list:
        if max(steps_list) < max_steps:
            max_steps = max(steps_list)
            depths_list.append([max_steps, counter])
        elif max(steps_list) == max_steps:
            depths_list.append([max_steps, counter])
        counter += 1
    depths_list.sort()
    # print(depths_list)
    find_potential_storage(depths_list)


def other_centres_finder_recursion(center_index, connection_matrix, visited_computers_list, distance_to_other_centres,
                                   depth):
    # print("Запустили other_centres_finder_recursion")
    global other_centres_indexes_list
    if depth == distance_to_other_centres:
        other_centres_indexes_list.append(center_index)
        return
    for j in range(total_computers):
        if connection_matrix[center_index][j]:
            if not visited_computers_list[j]:
                visited_computers_list[j] = 1
                other_centres_finder_recursion(j, connection_matrix, visited_computers_list, distance_to_other_centres,
                                               depth + 1)


def find_potential_storage(depths_list):
    # print("Запустили find_potential_storage")
    """
    Функция ищет вершины графа которые могли бы стать потенциальными хранилищами
    Логика такая, что мы берем одну или две вершины
    Потом мы делим граф на три части, крайние делители будут потенциальными хранилищами, для которых мы дополнительно
    добавляем в список все соседние к делителям вершины(они тоже могут быть потенциальными хранилищами)
    В итоге мы получаем список индексов потенциальных хранилищ, и не тратим огромные ресурсы каким бы большим не был граф
    :param depths_list: Функция принимает на вход список глубин для каждой точки
    """
    DEPTH = 1
    global other_centres_indexes_list
    if int(depths_list[0][0]) != (depths_list[1][0]):
        centres_list = [depths_list[0]]
    else:
        centres_list = [depths_list[0], depths_list[1]]
    visited_computers_list = []
    distance_to_other_centres = int(depths_list[0][0]) // 2
    for i in range(total_computers):
        visited_computers_list.append([])
    for i in centres_list:
        for x in range(total_computers):
            visited_computers_list[x] = 0
        visited_computers_list[i[1]] = 1
        other_centres_finder_recursion(i[1], connection_matrix, visited_computers_list, distance_to_other_centres, 0)
    # print(other_centres_indexes_list)
    # print(centres_list)
    other_centres_for_indexation = []
    other_centres_for_indexation.extend(other_centres_indexes_list)
    for i in other_centres_for_indexation:
        for x in range(total_computers):
            visited_computers_list[x] = 0
        visited_computers_list[i] = 1
        other_centres_finder_recursion(i, connection_matrix, visited_computers_list, DEPTH, 0)
    # print(other_centres_indexes_list)
    other_centres_indexes_set = set(other_centres_indexes_list)
    other_centres_indexes_list = list(other_centres_indexes_set)
    # print(other_centres_indexes_list)
    check_all_pairs_for_reliability(other_centres_indexes_list)


def check_all_pairs_for_reliability(potential_storage_list):
    # print("Запустили check_all_pairs_for_reliability")
    """
    Функция проверяет ненадежность каждого потенциального варианта пар для роли хранилищ
    :param potential_storage_list: На вход принимается список потенциальных пар
    """
    computer_pairs_reliability_dict = {}
    for i in range(len(potential_storage_list)):
        for j in range(len(potential_storage_list)):
            if i == j:
                continue
            first_computer = potential_storage_list[i]
            second_computer = potential_storage_list[j]
            first_computer_reliability = all_steps_list[first_computer]
            second_computer_reliability = all_steps_list[second_computer]
            best_reliability_list = []
            for x in range(len(first_computer_reliability)):
                if first_computer_reliability[x] < second_computer_reliability[x]:
                    best_reliability_list.append(first_computer_reliability[x])
                else:
                    best_reliability_list.append(second_computer_reliability[x])
            best_reliability_list.sort()
            # print(f"Для пары{first_computer},{second_computer} лучшие пути {best_reliability_list}")
            # print("")
            computer_pairs_reliability_dict[best_reliability_list[len(best_reliability_list) - 1]] = [
                first_computer + 1, second_computer + 1]
    list_keys = list(computer_pairs_reliability_dict.keys())
    list_keys.sort()
    print(computer_pairs_reliability_dict[list_keys[0]][0], computer_pairs_reliability_dict[list_keys[0]][1])


total_computers = input()
total_computers = int(total_computers)
connection_matrix = []
all_steps_list = []
other_centres_indexes_list = []
max_depth = 0
make_matrix()
fill_matrix()
if total_computers == 2:
    print(1, 2)
else:
    check_all_computers_longest_way()
