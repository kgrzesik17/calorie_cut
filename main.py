def calculate_weigth(weigth):
    return weight * 0.4535

def calculate_height(height):
    pass

units = 0

while units not in [1, 2]:
    units = input('What unit are you using? [1 - metric, 2 - imperial]')

    if units == 1:
        height = input('Enter your height in [centimeters]: ')
        weigth = input('Enter your weight in [kilograms]: ')
    else:
        height = input('Enter your height in [feet\'inches]')
        weight = input('Enter your weight in [lbs]')
    
def main(height, weight):
