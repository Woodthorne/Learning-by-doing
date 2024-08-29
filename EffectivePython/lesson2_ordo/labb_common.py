import random
from timeit import default_timer

class HockeyPlayer:
    def __init__(self, name: str, number: int) -> None:
        self.name = name
        self.number = number
        self.wearing_folk_dress = False


class TeamRecruiter:
    def __init__(self) -> None:
        self.given_names = ['Börje',
                            'Nicklas',
                            'Jenni',
                            'Peter',
                            'Henrik',
                            'Pernilla',
                            'Mats',
                            'Henrik',
                            'Daniel',
                            'Tommy'
                            ]
        self.surnames = ['Salming',
                         'Lidström',
                         'Asserholt',
                         'Forsberg',
                         'Lundqvist',
                         'Winberg',
                         'Sundin',
                         'Zetterberg',
                         'Alfredsson',
                         'Salo'
                         ]

    def make_team(self,
                  size: int = 6,
                  ordered: bool = False
                  ) -> list[HockeyPlayer]:
        team: list[HockeyPlayer] = []
        for num in range(size):
            name = random.choice(self.given_names) + ' '
            name += random.choice(self.surnames)
            team.append(HockeyPlayer(name = name, number = num))
        
        if not ordered:
            random.shuffle(team)
        
        return team
    
def show_team_numbers(team: list[HockeyPlayer]):
    print([player.number for player in team])

def doubling_array(entries: int = 4, initial: int = 1000) -> list[int]:
    values = [initial]
    for _ in range(entries - 1):
        values.append(2 * values[-1])
    return values

def time_team_sorting(func, sizes: list[int]):
    recruiter = TeamRecruiter()
    teams = [recruiter.make_team(size) for size in sizes]

    times: list[float] = []
    for index in range(len(teams)):
        start_time = default_timer()
        func(teams[index])
        stop_time = default_timer()
        elapsed_time = stop_time - start_time
        message = f'[Team {sizes[index]}] Time elapsed: {"{0:.2f}".format(elapsed_time)} seconds'
        if index != 0:
            message += f', change: x{"{0:.2f}".format(elapsed_time / times[index - 1])}'
        print(message)
        times.append(elapsed_time)
