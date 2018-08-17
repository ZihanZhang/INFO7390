import random

# Question1
def question1_math_output():
    ratio = 0.0
    number = 2
    while ratio < 1/2:
        ratio = question1_math(number)
        number = number + 1
        print("Number: " + str(number) + " Ratio: " + str(ratio))

    print(number)    

def question1_math(number):
    no_people = (1 - 1/365)**number
    one_people = 1/365 * (1 - 1/365)**(number - 1) * number
    return 1 - no_people - one_people


# Question2
def question2_simulation_one_round(number):
    dates = []
    for i in range(number):
        dates.append(random.randint(1, 365))

    total = 0
    for i in dates:
        if i == 1:
            total = total + 1

    if total >= 2:
        return True
    else:
        return False

def question2_simulation():
    number = 2
    ratio = 0.0
    while ratio < 1/2:
        true = 0
        false = 0
        for i in range(1000):
            if question2_simulation_one_round(number):
                true = true + 1
            else:
                false = false + 1

        ratio = true / (true + false)
        print(ratio)
        number = number + 1

    print(number)


# Question3
def question3_math():
    return 1/2 * 1/2 * 1/2 * 3

def question3_math_output():
    print(question3_math())


# Question4
def question4_simulation():
    true = 0
    false = 0
    for i in range(1000):
        if question4_simulation_one_round():
            true = true + 1
        else:
            false = false + 1

    ratio = true / (true + false)
    print(ratio)

def question4_simulation_one_round():
    coins = []
    total = 0
    for i in range(3):
        coins.append(random.randint(0, 1))
    for c in coins:
        if c == 1:
            total = total + 1
    if total == 2:
        return True
    else:
        return False

# Question5
def question5_1_math():
    return 1 - 5/6 * 5/6 * 5/6
def question5_1_math_output():
    print(question5_1_math())
def question5_2_math():
    return 1/6 * 5/6 * 5/6 * 3
def question5_2_math_output():
    print(question5_2_math())

# Question6
def question6_1_simulation_one_round():
    dies = []
    for i in range(3):
        dies.append(random.randint(1, 6))
    for d in dies:
        if d == 1:
            return True
    return False

def question6_1_simulation():
    true = 0
    false = 0
    for i in range(1000):
        if question6_1_simulation_one_round():
            true = true + 1
        else:
            false = false + 1
    ratio = true / (true + false)
    print(ratio)

def question6_2_simulation_one_round():
    dies = []
    total = 0
    for i in range(3):
        dies.append(random.randint(1, 6))
    for d in dies:
        if d == 1:
            total = total + 1

    if total == 1:
        return True
    else:
        return False

def question6_2_simulation():
    true = 0
    false = 0
    for i in range(1000):
        if question6_2_simulation_one_round():
            true = true + 1
        else:
            false = false + 1
    ratio = true / (true + false)
    print(ratio)

# Question7
def question7_1_math():
    return 1/4 * 1/3 + (1 - 1/4) * 0.3
def question7_1_math_output():
    print("M: " + str(question7_1_math()))
def question7_2_math():
    return 1/4 * 1/3 + (1 - 1/4) * 0.2
def question7_2_math_output():
    print("I: " + str(question7_2_math()))
def question7_3_math():
    return 1/4 * 1/3 + (1 - 1/4) * 0.5
def question7_3_math_output():
    print("B: " + str(question7_3_math()))


# Question8    
def question8_simulation():
    mtotal = 0
    itotal = 0
    btotal = 0

    for i in range(1000):
        number = 10000
        m = 10000 * (1 - 1/4) * 0.3
        i = 10000 * (1 - 1/4) * 0.2
        b = 10000 * (1 - 1/4) * 0.5

        lazyvoter = int(10000 * 1/4)

        for j in range(lazyvoter):
            if question8_simulation_one_person() == "M":
                m = m + 1
            elif question8_simulation_one_person() == "I":
                i = i + 1
            else:
                b = b + 1

        mtotal = mtotal + m
        itotal = itotal + i
        btotal = btotal + b

    mratio = mtotal / (mtotal + itotal + btotal)
    iratio = itotal / (mtotal + itotal + btotal)
    bratio = btotal / (mtotal + itotal + btotal)

    print("M: " + str(mratio))
    print("I: " + str(iratio))
    print("B: " + str(bratio))

def question8_simulation_one_person():
    vote = random.randint(1, 3)
    if vote == 1:
        return "M"
    elif vote == 2:
        return "I"
    else:
        return "B"
    

# Question9
def question9_math(n, k):
    ratio_stay = 1 / n
    ratio_switch = (n - 1) / n * 1 / (n - k - 1)
    return (ratio_stay, ratio_switch)

def question9_math_output():
    n = 3
    k = 1
    stay, switch = question9_math(n, k)
    print("Stay: " + str(stay))
    print("Switch: " + str(switch))



# Question10
def question10_simulation():
    n = 4
    k = 2
    switch_true = 0
    switch_false = 0
    for i in range(500):
        if question10_simulation_switch_one_round(n, k):
            switch_true = switch_true + 1
        else:
            switch_false = switch_false + 1
    switch_ratio = switch_true / (switch_true + switch_false)

    stay_true = 0
    stay_false = 0
    for i in range(500):
        if question10_simulation_stay_one_round(n, k):
            stay_true = stay_true + 1
        else:
            stay_false = stay_false + 1
    stay_ratio = stay_true / (stay_true + stay_false)

    print("Switch: " + str(switch_ratio))
    print("Stay: " + str(stay_ratio))

def question10_simulation_switch_one_round(n, k):
    doors = [0] * (n - 1)
    doors.append(1)
    first_choice = random.randint(0, n - 1)
    host_choices = []
    for r in range(k):
        for i in range(n):
            if doors[i] == 0 and i != first_choice and i not in host_choices:
                host_choices.append(i)
                break
    second_choice = random.randint(0, n - 1)
    while first_choice == second_choice or second_choice in host_choices:
        second_choice = random.randint(0, n - 1)
    if doors[second_choice] == 0:
        return False
    else:
        return True

def question10_simulation_stay_one_round(n, k):
    doors = [0] * (n - 1)
    doors.append(1)
    first_choice = random.randint(0, n - 1)
    for i in range(n):
        if doors[i] == 0 and i != first_choice:
            host_choice = i
            break
    if doors[first_choice] == 0:
        return False
    else:
        return True
    
    
if __name__ == "__main__":
    # print("Question1:")
    # question1_math_output()
    # print("Question2:")
    # question2_simulation()
    # print("Question3:")
    # question3_math_output()
    # print("Question4:")
    # question4_simulation()
    # print("Question5:")
    # question5_1_math_output()
    # question5_2_math_output()
    # print("Question6:")
    # question6_1_simulation()
    # question6_2_simulation()
    # print("Question7:")
    # question7_1_math_output()
    # question7_2_math_output()
    # question7_3_math_output()
    # print("Question8:")
    # question8_simulation()
    # print("Question9:")
    # question9_math_output()
    print("Question10:")
    question10_simulation()
