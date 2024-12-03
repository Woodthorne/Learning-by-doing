import random
from statistics import mean, median

from package_manager import Environment


class ReflexAgent:
    def get_action(self, percept: dict[str, str|bool]) -> str:
        match percept:
            case {'current_cell': 'charger', 'battery': 'low'}:
                return 'charge'
            case {'battery': 'low'}:
                return random.choice(['left', 'up'])
            case {'current_cell': 'dock', 'has_package': True}:
                return 'deliver'
            case {'current_cell': 'package', 'has_package': False}:
                return 'pick up'
            case {'has_package': True}:
                return random.choice(['right', 'down'])
            case _:
                return random.choice(['left', 'right', 'up', 'down'])
            
class GPSReflexAgent:
    def __init__(self, grid_size: int) -> None:
        self.grid_size = grid_size

    def get_action(self, percept: dict[str, str|bool]) -> str:
        match percept:
            case {'current_cell': 'charger', 'battery': 'low'}:
                return 'charge'
            case {'battery': 'low'}:
                if percept['y'] == 0:
                    return 'up'
                else:
                    return 'left'
            case {'current_cell': 'dock', 'has_package': True}:
                return 'deliver'
            case {'current_cell': 'package', 'has_package': False}:
                return 'pick up'
            case {'has_package': True}:
                if percept['y'] == self.grid_size - 1:
                    return 'down'
                else:
                    return 'right'
            case _:
                options = ['left', 'right', 'up', 'down']
                if percept['x'] == 0:
                    options.remove('up')
                elif percept['x'] == self.grid_size - 1:
                    options.remove('down')
                if percept['y'] == 0:
                    options.remove('left')
                elif percept['y'] == self.grid_size - 1:
                    options.remove('right')
                return random.choice(options)


def remaining_packages(env: Environment) -> int:
    packages_remaining = len([space for row in env.grid
                              for space in row if space == 'package'])
    if env.robot_has_package:
        packages_remaining += 1
    
    return packages_remaining

def run(grid_size: int = 5, loud: bool = False) -> int:
    env = Environment(grid_size)
    bot = ReflexAgent()
    bot = GPSReflexAgent(grid_size)
    step = 0
    if loud:
        print('=== Startläge ===')
        print(env)
    while remaining_packages(env) > 0:
        percept = env.get_percept()
        action = bot.get_action(percept)
        env.perform_action(action)
        
        step += 1
        
        if loud:
            print(f'=== Steg {step} ===')
            print(env, f'{remaining_packages(env)=}')

    if loud:
        print('=== Alla paket levererade ===')
    return step

def run_repeat(iterations: int = 1_000, grid_size: int = 5, loud: bool = False) -> None:
    results = []
    for iteration in range(iterations):
        if iteration % (iterations / min(100, iterations)) == 0 and loud:
            print(iteration)
        results.append(run(grid_size, loud))
    print(f'{iterations=}')
    print(f'{mean(results)=}')
    print(f'{median(results)=}')
    print(f'{max(results)=}')
    print(f'{min(results)=}')

run_repeat(grid_size=4, loud=False, iterations=10_000)