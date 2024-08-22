'''
Skapa en lista med objekt (bäst med HockeyPlayer men ta något
annat om du vill)

Implementera en Bubble Sort enligt pseudokod/dans så man kan
sortera på en property (ex namn)
'''

from labb_common import HockeyPlayer, TeamRecruiter, show_team_numbers

def bubble_sort_players(team: list[HockeyPlayer]) -> None:
    for loop in range(len(team)):
        for index in range(1, len(team) - loop):
            if team[index].number < team[index - 1].number:
                team[index], team[index - 1] = team[index - 1], team[index]
            # show_team_numbers(team)
        # show_team_numbers(team)

if __name__ == '__main__':
    recruiter = TeamRecruiter()
    team = recruiter.make_team(size = 10)
    show_team_numbers(team)
    bubble_sort_players(team)
    show_team_numbers(team)