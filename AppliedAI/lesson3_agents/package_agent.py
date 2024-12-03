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


def remaining_packages(env: Environment) -> int:
    packages_remaining = len([space for row in env.grid
                              for space in row if space == 'package'])
    if env.robot_has_package:
        packages_remaining += 1
    
    return packages_remaining

def run(grid_size: int = 5, loud: bool = False) -> int:
    env = Environment(grid_size)
    bot = ReflexAgent()
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
        if iteration % min(iterations / 100, iterations) == 0 and loud:
            print(iteration)
        results.append(run(grid_size))
    print(f'{iterations=}')
    print(f'{mean(results)=}')
    print(f'{median(results)=}')
    print(f'{max(results)=}')
    print(f'{min(results)=}')

run_repeat(grid_size=4)