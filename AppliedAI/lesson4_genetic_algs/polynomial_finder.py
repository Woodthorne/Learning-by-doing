import random
from pathlib import Path
from statistics import mean
from typing import Callable

import numpy as np
import plotly.express as px
import plotly.graph_objs as go


class Individual:
    def __init__(self, chromosome: list[float], x: np.ndarray, y: np.ndarray) -> None:
        self.chromosome = chromosome
        self.x = x
        self.y = y
    
        self.fitness = self.calc_fitness()
    
    def procreate(self, mate: 'Individual') -> 'Individual':
        new_chromosome = []
        for gene_1, gene_2 in zip(self.chromosome, mate.chromosome):
            probability = random.random()
            # if probability < 0.45:
            #     new_chromosome.append(gene_1)
            # elif probability < 0.9:
            #     new_chromosome.append(gene_2)
            if probability < 0.7:
                new_chromosome.append(mean([gene_1, gene_2]))
            elif probability < 0.8:
                new_chromosome.append(mutated_gene())
            else:
                new_chromosome.append(0)
        
        return Individual(new_chromosome, self.x, self.y)
    
    def get_polynomial(self) -> Callable:
        components = [exponent_coefficient for exponent_coefficient
                      in enumerate(reversed(self.chromosome))]
        return lambda x: sum([c * exponentiation(x, e) for e, c in components])

    def calc_fitness(self) -> float:
        vfunc = np.vectorize(self.get_polynomial())
        distances = abs(self.y - vfunc(self.x))
        return int(sum(distances))
        
    def __str__(self) -> str:
        return '[ ' + (' '.join([f'{num:.2f}' for num in self.chromosome])) + ' ]'

def math_cache(func: Callable):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@math_cache
def exponentiation(base: int|float, exponent: int|float) -> float:
    return base ** exponent

def mutated_gene(floor: int = -10, ceiling: int = 10) -> float:
    return random.uniform(floor, ceiling)

def random_genome(length: int) -> list[float]:
    return [mutated_gene(-1, 1) for _ in range(length)]

def find_polynomial(
        x: np.ndarray,
        y: np.ndarray,
        terms: int,
        population_size: int,
        generation_limit: int = 5000
) -> None:
    found = False
    current_fitness_score = terms
    generations_since_change = 0

    generation = 1
    population = [
        Individual(random_genome(terms), x, y)
        for _ in range(population_size)
    ]

    while not found:
        if generations_since_change > generation_limit:
            break
        
        generation += 1

        population.sort(key = lambda x: x.fitness)

        if population[0].fitness <= 0:
            found = True
            break

        survivor_size = population_size // 10
        new_generation = population[:survivor_size]
        
        parent_size = population_size // 2
        while len(new_generation) < population_size:
            parent_1 = random.choice(population[:parent_size])
            parent_2 = random.choice(population[:parent_size])
            child = parent_1.procreate(parent_2)
            new_generation.append(child)
        
        population = new_generation

        if current_fitness_score > population[0].fitness:
            current_fitness_score = population[0].fitness
            generations_since_change = 0
        else:
            generations_since_change += 1
        
        if generation % (generation_limit // 20) == 0:
            message = f'Generation: {generation}, '
            message += f'Candidate: {population[0]}, '
            message += f'Fitness: {population[0].fitness}'
            print(message)
    
    if found:
        message = f'Found result: '
    else:
        message = f'Final result: '
    message += f'Generation: {generation}, '
    message += f'Candidate: {population[0]}, '
    message += f'Fitness: {population[0].fitness}'
    print(message)

    func = population[0].get_polynomial()
    vfunc = np.vectorize(func)

    fig = px.scatter(x=x, y=x)
    trace = go.Scatter(x=x, y=vfunc(x), name='Found polynomial')
    fig.add_trace(trace)
    fig.show()

if __name__ == '__main__':
    POPULATION = 100
    TERMS = 11

    dir_path = Path('AppliedAI/lesson4_genetic_algs')
    file_name = 'polynomial_data_demo3.csv'
    file_path = dir_path / file_name

    data = np.genfromtxt(file_path, delimiter=',', names=True)

    find_polynomial(
        x = data['x'],
        y = data['y'],
        terms = TERMS,
        population_size = POPULATION
    )