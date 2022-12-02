from data import calories, matches

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
