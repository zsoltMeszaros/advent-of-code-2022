import pprint
from data import (
    calories, matches, rucksacks, pairs, orders, datastream, lines, forest
)



def dec_1_puzzle(calories):

    maxes = [0, 0, 0] #contains the 3 biggest calories
    current_max = 0
    for calorie in calories.splitlines():
        if calorie == "":
            if min(maxes) < current_max:
                maxes[maxes.index(min(maxes))] = current_max
                current_max = 0
            else:
                current_max = 0
        else:
            calorie = int(calorie)
            current_max += calorie

    print("calories:", sum(maxes))


def dec_2_puzzle(matches):

    first_half_result = 0
    second_half_result = 0

    for match in matches.splitlines():
        enemy_hand, my_hand = match.split()

        enemy_hand_value = {
            "A": 1, #rock
            "B": 2, #paper
            "C": 3, #scissors
        }[enemy_hand]
        my_hand_value = {
            "X": 1, #rock
            "Y": 2, #paper
            "Z": 3, #scissors
        }[my_hand]

        if enemy_hand_value == my_hand_value:
            first_half_result += 3 + my_hand_value
        elif (enemy_hand_value == my_hand_value-1) or (enemy_hand_value == 3 and my_hand_value == 1):
            first_half_result += 6 + my_hand_value
        else:
            first_half_result += my_hand_value

        hand_exchange_values = [0, 1, 2, 3, 1, 2]

        if my_hand_value == 2:
            second_half_result += 3 + enemy_hand_value
        elif my_hand_value == 1:
            second_half_result += hand_exchange_values[enemy_hand_value+2]
        else:
            second_half_result += 6 + hand_exchange_values[enemy_hand_value+1]
        
    print("first half result:", first_half_result)
    print("second half result:", second_half_result)


def dec_3_puzzle(rucksacks):
    rucksacks = rucksacks.splitlines()

    def get_rucksack_value(rucksack):
        result = []
        for letter in rucksack:
            if letter.isupper():
                result.append(int(ord(letter)) - 38)
            else:
                result.append(int(ord(letter)) - 96)
        return result


    def first_half():
        result = 0
        for rucksack in rucksacks:
            left, right = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
            left_list = set(get_rucksack_value(left))
            right_list = set(get_rucksack_value(right))
        
            if (left_list & right_list):
                result += (left_list & right_list).pop()
        print(result)
    

    def second_half():
        result = 0
        for i in range(len(rucksacks)//3):
            print(i*3)
            a, b, c = rucksacks[i*3], rucksacks[i*3+1], rucksacks[i*3+2]
            a, b, c = set(get_rucksack_value(a)), set(get_rucksack_value(b)), set(get_rucksack_value(c))

            result += (set(a) & set(b) & set(c)).pop()
        print(result)
        
    first_half()
    second_half()


def dec_4_puzzle(pairs):
    pairs = pairs.splitlines()

    def first_half():
        result_counter = 0
        for pair in pairs:
            first, second = pair.split(",")
            first, second = first.split("-"), second.split("-")

            if int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1]):
                result_counter += 1
            elif int(first[0]) >= int(second[0]) and int(first[1]) <= int(second[1]):
                result_counter += 1
        print(result_counter)


    def second_half():
        result_counter = 0
        print(len(pairs))
        for pair in pairs:
            first, second = pair.split(",")
            first, second = first.split("-"), second.split("-")

            if int(first[0]) > int(second[1]):
                result_counter += 1
            elif int(first[1]) < int(second[0]):
                result_counter += 1
        print(result_counter)


    first_half()
    second_half()


def dec_5_puzzle(orders):
    base = [
        ["D", "B", "J", "V"],
        ["P", "V", "B", "W", "R", "D", "F"],
        ["R", "G", "F", "L", "D", "C", "W", "Q"],
        ["W", "J", "P", "M", "L", "N", "D", "B"],
        ["H", "N", "B", "P", "C", "S", "Q"],
        ["R", "D", "B", "S", "N", "G"],
        ["Z", "B", "P", "M", "Q", "F", "S", "H"],
        ["W", "L", "F"],
        ["S", "V", "F", "M", "R"],
    ]

    orders = orders.splitlines()


    def first_half():
        for order in orders:
            order = order.replace("move", "")
            move, temp = order.split("from")
            start, end = temp.split("to")
            move, start, end = int(move), int(start)-1, int(end)-1

            for _ in range(move):
                base[end].append(base[start][-1])
                del base[start][-1]


    def second_half():
        for order in orders:
            order = order.replace("move", "")
            move, temp = order.split("from")
            start, end = temp.split("to")
            move, start, end = int(move), int(start)-1, int(end)-1

            base[end] += base[start][0-move:]
            del base[start][0-move:]


    # first_half()
    # second_half()
    pprint.pprint(base)


def dec_6_puzzle(datastream):
    def first_half():
        for i in range(len(datastream)-4):
            if len(set(list(datastream[i:i+4]))) == 4:
                print(i+4)
                return
    
    def second_half():
        for i in range(len(datastream)-4):
            if len(set(list(datastream[i:i+14]))) == 14:
                print(i+14)
                return

    first_half()
    second_half()


def dec_7_puzzle(lines):
    lines = lines.splitlines()
    folders = {}


    to_count = False
    current_key = ""
    for line in lines:
        line = line.split()
        if to_count and line[1] == "ls":
            continue
        if to_count:
            if line[0] == "dir":
                continue
            if line[0].isnumeric():
                folders[current_key] += int(line[0])
            else:
                to_count = False
        else:
            if line[1] == "cd" and line[2] not in ["..", "/"]:
                folders[line[2]] = 0
                current_key = line[2]
                to_count = True

    to_count = False
    for i in range(10):
        for line in lines:
            line = line.split()
            if to_count and line[1] == "ls":
                continue
            if to_count:
                if line[0].isnumeric():
                    continue
                if line[0] == "dir":
                    if line[1] in folders.keys():
                        folders[current_key] += folders[line[1]]
                else:
                    to_count = False
            else:
                if line[1] == "cd" and line[2] not in ["..", "/"]:
                    current_key = line[2]
                    to_count = True


    print(folders)
    result = 0
    for value in folders.values():
        if value <= 100000:
            result += value
    print(result)


def dec_8_puzzle(forest):
    forest = forest.splitlines()

    forest_grid = []

    for line in forest:
        forest_grid.append([int(i) for i in list(line)])

    vertical_forest_grid = [*map(list,zip(*forest_grid))]

    result = len(forest_grid)*2 + len(vertical_forest_grid[0])*2 - 4

    for i in range(1, len(forest_grid)-1):
        print(forest_grid[i])
        print(vertical_forest_grid[i])
        for j in range(1, len(forest_grid[i])-1):
            if forest_grid == 0:
                continue
            # print("choices:")
            # print(sorted(forest_grid[i][:j])[-1], forest_grid[i][j])
            # print(sorted(forest_grid[i][j+1:])[-1], forest_grid[i][j])
            # print(sorted(vertical_forest_grid[i][:j])[-1], forest_grid[i][j])
            # print(sorted(vertical_forest_grid[i][j+1:])[-1], forest_grid[i][j])
            # print("chosen:")
            # return
            if sorted(forest_grid[i][:j])[-1] < forest_grid[i][j]:
                # print(forest_grid[i][:j], forest_grid[i][j])
                result += 1
                # print("increment")
                continue
            elif sorted(forest_grid[i][j+1:])[-1] < forest_grid[i][j]:
                # print(forest_grid[i][j+1:], forest_grid[i][j])
                result += 1
                # print("increment")
                continue
            elif sorted(vertical_forest_grid[i][:j])[-1] < vertical_forest_grid[i][j]:
                # print(vertical_forest_grid[i][:j], forest_grid[i][j])
                result += 1
                # print("increment")
                continue
            elif sorted(vertical_forest_grid[i][j+1:])[-1] < vertical_forest_grid[i][j]:
                # print(vertical_forest_grid[i][j+1:], forest_grid[i][j])
                result += 1
                # print("increment")
                continue

    
    print(result)


# dec_1_puzzle(calories)
# dec_2_puzzle(matches)
# dec_3_puzzle(rucksacks)
# dec_4_puzzle(pairs)
# dec_5_puzzle(orders)
# dec_6_puzzle(datastream)
# dec_7_puzzle(lines)
dec_8_puzzle(forest)