import random


class Agent:
    def __init__(self, strategy: str):
        self.score = 0
        self.strategy = strategy
    
    def get_fingers(self) -> int:
        match self.strategy.split('/'):
            case ['random']:
                return random.randint(1, 2)
            case [num, _]:
                return 1 if random.random() < float(num) / 100 else 2


def run_morra(
        odd_strat: str = 'random',
        even_strat: str = 'random',
        iterations: int = 10
) -> None:
    for strat in [odd_strat, even_strat]:
        if strat == 'random':
            continue
        assert len(strat.split('/')) == 2, 'Strategy needs to be "random" or format "XX/YY".'
        assert strat.split('/')[0].isnumeric() and strat.split('/')[1].isnumeric(), 'Both sides of divider needs to be numeric in strategy.'
        assert float(strat.split('/')[0]) + float(strat.split('/')[1]) == 100, 'Both numbers needs to add up to 100 in strategy.'

    agent_o = Agent(odd_strat)
    agent_e = Agent(even_strat)
    for _ in range(iterations):
        fingers = sum([agent_o.get_fingers(), agent_e.get_fingers()])
        if fingers % 2 == 0:
            agent_o.score -= fingers
            agent_e.score += fingers
        else:
            agent_o.score += fingers
            agent_e.score -= fingers
    
    print(f'Results after {iterations} iterations:')
    print(f'Agent O: {agent_o.score} points')
    print(f'Agent E: {agent_e.score} points')


if __name__ == '__main__':
    run_morra(odd_strat = '70/30', even_strat='random')