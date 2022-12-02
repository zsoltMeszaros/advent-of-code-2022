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



# dec_1_puzzle(calories)
# dec_2_puzzle(matches)