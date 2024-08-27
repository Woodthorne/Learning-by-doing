import string
from timeit import default_timer

class Car:
    def __init__(self, plate: str, brand: str = '', fuel: str = '') -> None:
        self.plate = plate
        self.brand = brand
        self.fuel = fuel

def generate_cars(mode: str = 'list'):
    '''
    mode is either 'list', 'dict' or 'split'
    '''

    LETTERS = list(string.ascii_uppercase)
    DIGITS = list(string.digits)
    
    if mode == 'list':
        cars: list[Car] = []
    elif mode == 'dict':
        cars: dict[str, Car] = {}
    elif mode == 'split':
        cars: dict[str, Car] = {}

    for char1 in LETTERS:
        if mode == 'split':
            cars[char1] = []

        for char2 in LETTERS:
            for char3 in LETTERS:
                for char4 in DIGITS:
                    for char5 in DIGITS:
                        for char6 in DIGITS:
                            plate = char1 + char2 + char3 + char4 + char5 + char6
                            car = Car(plate)

                            if mode == 'list':
                                cars.append(car)
                            if mode == 'dict':
                                cars[car.plate] = car
                            if mode == 'split':
                                cars[char1].append(car)
    return cars

def generate_and_time(mode: type = list):
    t_start = default_timer()
    cars = generate_cars(mode = mode)
    t_end = default_timer()
    print('Time passed during generation:', t_end - t_start)
    return cars