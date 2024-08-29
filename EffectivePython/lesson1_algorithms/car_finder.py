from timeit import default_timer

from cars import Car, generate_and_time


def get_car(plate: str,
            all_cars: list[Car]|dict[str, Car]|dict[str,list[Car]],
            mode: str = 'list'):
    if mode == 'list':
        for car in all_cars:
            if car.plate == plate:
                return car
    elif mode == 'dict':
        try:
            return all_cars[plate]
        except:
            pass
    elif mode == 'split':
        try:
            for car in all_cars[plate[0]]:
                if car.plate == plate:
                    return car
        except:
            pass
    return None

def main():
    mode = 'split'          # Set to 'list', 'dict' or 'split'
    cars = generate_and_time(mode)

    while True:
        plate = input('Input licence plate: ').upper()
        if plate == 'Q':
            break
        
        t_start = default_timer()
        car = get_car(plate, cars, mode)
        t_end = default_timer()
        print('Time passed during search:', t_end - t_start)
        
        if car:
            print('Car found!')
        else:
            print('No car with that license plate.')

if __name__ == '__main__':
    main()