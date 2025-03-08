def calculate_weigth(weigth):
    return float(weight) * 0.4535

def calculate_height(height):
    feet = height.split("'")[0]
    inch = height.split("'")[1]
    
    height = float(feet) * 30.48 + float(inch) * 2.54

    return height

units = 0

while units not in [1, 2]:
    units = input('What unit are you using? [1 - metric, 2 - imperial]: ')

    if units == 1:
        height = input('Enter your height in [centimeters]: ')
        weigth = input('Enter your weight in [kilograms]: ')
    else:
        height = input('Enter your height in [feet\'inches]: ')
        weight = input('Enter your weight in [lbs]: ')

        height = calculate_height(height)
        weight = calculate_weigth(weight)
    
def main(height, weight):
    pass