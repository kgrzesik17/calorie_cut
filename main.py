def calculate_weigth(weigth):
    return float(weight) * 0.4535

def calculate_height(height):
    feet = height.split("'")[0]
    inch = height.split("'")[1]
    
    height = float(feet) * 30.48 + float(inch) * 2.54

    return height

def calculate_metabolism(height, weight, age, sex):
    if sex == 'm':
        metabolism = 66.5 + (13.75 * weight) + (5.003 * height) - (6.775 * age)
    else:
        metabolism = 665.1 + (9.563 * weight) + (1.85 * height) - (4.676 * age)

    metabolism = round(metabolism)

    return metabolism

def calculate_calories(metabolism, weight, days, goal):
    goal_difference = weight - goal
    calorie_deficit_overall = goal_difference * 9 * 1000
    calorie_deficit_per_day =  calorie_deficit_overall / days

    diet = metabolism - calorie_deficit_per_day

    print('Your daily metabolism is calculated to be: '+ str(metabolism) + ' calories per day.')
    print('You need to keep a ' + str(calorie_deficit_per_day) + ' calorie deficit per day.')
    print('That means you have to eat no more than ' + str(diet) + ' calories per day for ' + str(days) + ' days to reach your goal.')

units = 0

while units not in ['1', '2']:
    units = input('What unit are you using? [1 - metric, 2 - imperial]: ')

    if units == '1':
        height = float(input('Enter your height in [centimeters]: '))
        weight = float(input('Enter your weight in [kilograms]: '))
        goal = float(input('Enter your goal weight [kilograms]: '))

    else:
        height = float(input('Enter your height in [feet\'inches]: '))
        weight = float(input('Enter your weight in [lbs]: '))
        goal = float(input('Enter your goal weight [lbs]: '))

        height = calculate_height(height)
        weight = calculate_weigth(weight)
        goal = calculate_weigth(goal)

    age = int(input('Enter your age: '))
    sex = input('Enter your sex [M/F]: ').lower()

    days = int(input('Enter in how many days do you want to reach your goal: '))

    metabolism = calculate_metabolism(height, weight, age, sex)

    calculate_calories(metabolism, weight, days, goal)
    