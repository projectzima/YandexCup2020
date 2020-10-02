total_targets = input()


def slicer():
    target = input()
    target = target.split()
    if target[0] == "0":
        x = int(target[2])
        y = int(target[3])
        center_point = [x, y]
        list_of_points.append(center_point)
    elif target[0] == "1":
        x_point = (int(target[1]) + int(target[3]) + int(target[5]) + int(target[7])) / 4
        y_point = (int(target[2]) + int(target[4]) + int(target[6]) + int(target[8])) / 4
        center_point = [x_point, y_point]
        list_of_points.append(center_point)


list_of_points = []
for _ in range(int(total_targets)):
    slicer()


sorted_x = sorted(list_of_points)
lowest_coordinate = sorted_x[0]
highest_coordinate = sorted_x[(len(sorted_x) - 1)]
error = False
for point in sorted_x:
    if lowest_coordinate[0] < point[0]:
        break
    elif lowest_coordinate[1] > point[1]:
        lowest_coordinate[1] = point[1]

for point in sorted_x:
    if highest_coordinate[0] > point[0]:
        break
    elif highest_coordinate[1] < point[1]:
        highest_coordinate[1] = point[1]

for point in sorted_x:
    first = point[0] - lowest_coordinate[0]
    second = highest_coordinate[0] - lowest_coordinate[0]
    third = point[1] - lowest_coordinate[1]
    fourth = highest_coordinate[1] - lowest_coordinate[1]
    if first == 0:
        first = 1
    if second == 0:
        second = 1
    if third == 0:
        third = 1
    if fourth == 0:
        fourth = 1

    if first / second != third / fourth:
        print("No")
        error = True
        break

if error is False:
    print("Yes")





