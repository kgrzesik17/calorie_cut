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

units = 0

while units not in ['1', '2']:
    units = input('What unit are you using? [1 - metric, 2 - imperial]: ')

    if units == '1':
        height = float(input('Enter your height in [centimeters]: '))
        weight = float(input('Enter your weight in [kilograms]: '))
        goal = input('Enter how much weight do you want to lose [kilograms]')

    else:
        height = float(input('Enter your height in [feet\'inches]: '))
        weight = float(input('Enter your weight in [lbs]: '))
        goal = input('Enter how much weight do you want to lose [lbs]: ')

        height = calculate_height(height)
        weight = calculate_weigth(weight)

    age = int(input('Enter your age: '))
    sex = input('Enter your sex [M/F]: ').lower()

    days = input('Enter in how many days do you want to reach your goal: ')

    metabolism = calculate_metabolism(height, weight, age, sex)
    