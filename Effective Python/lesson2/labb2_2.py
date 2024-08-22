'''
Implementera Insertion Sort enligt pseudokod/dans så man kan
sortera på en property (ex namn)
'''

from labb_common import HockeyPlayer, TeamRecruiter, show_team_numbers

def insertion_sort_players(team: list[HockeyPlayer]) -> None:
    for index in range(1, len(team)):
        if team[index].number < team[index - 1].number:
            # print(team[index].number)
            for left_index in range(index, -1, -1):
                if team[left_index].number < team[index].number:
                    team.insert(left_index + 1, team.pop(index))
                    break
                elif left_index == 0:
                    team.insert(0, team.pop(index))
        # show_team_numbers(team)
            

if __name__ == '__main__':
    recruiter = TeamRecruiter()
    team = recruiter.make_team(size = 10)
    show_team_numbers(team)
    insertion_sort_players(team)
    show_team_numbers(team)