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
from labb2_3 import selection_sort_players
from labb_common import doubling_array, time_team_sorting

if __name__ == '__main__':
    team_sizes = doubling_array(entries = 6, initial = 1000)
    print('___Selection sort___')
    time_team_sorting(selection_sort_players, team_sizes)
    print('___Bubble sort______')
    time_team_sorting(bubble_sort_players, team_sizes)
    print('___Insertion sort___')
    time_team_sorting(insertion_sort_players, team_sizes)