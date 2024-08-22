'''
Är Selection sort också O(n^2)?
Bevisa det praktiskt (dvs tajma koden)
Jämför tiden för Insertion sort och Bubble sort
Är insertion sort snabbare?
Hur mycket snabbare?
Men fortfarande O(n^2)? Eller?
Dvs fyrdubblas tiden om vi dubblar storleken på listan?
'''

from labb2_1 import bubble_sort_players
from labb2_2 import insertion_sort_players
from labb_common import time_team_sorting

if __name__ == '__main__':
    team_sizes = [1000, 2000, 4000, 8000]
    print('___Bubble sort______')
    time_team_sorting(bubble_sort_players, team_sizes)
    print('___Insertion sort___')
    time_team_sorting(insertion_sort_players, team_sizes)