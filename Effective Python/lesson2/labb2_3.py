'''
Implementera Selection Sort enligt pseudokod/dans så man kan
sortera på en property (ex namn)
'''

from labb_common import HockeyPlayer, TeamRecruiter, show_team_numbers

def selection_sort_players(team: list[HockeyPlayer]) -> None:
    for index in range(len(team)):
        smallest_index = index
        for player_index in range(index, len(team)):
            if team[smallest_index].number > team[player_index].number:
                smallest_index = player_index
                # print(team[smallest_index].number)
        team.insert(index, team.pop(smallest_index))
        # show_team_numbers(team)

if __name__ == '__main__':
    recruiter = TeamRecruiter()
    team = recruiter.make_team(size = 10)
    show_team_numbers(team)
    selection_sort_players(team)
    show_team_numbers(team)