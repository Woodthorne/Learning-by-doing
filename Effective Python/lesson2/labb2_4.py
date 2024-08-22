'''
Verifiera Big O
Bubblesort är O(n^2)
Vad krävs för att bevisa det praktiskt?
Skapa en stor lista, 1000 element (med hjälp av random eller något)
Tajma hur lång tid bubbleSort behöver
Testa med 2000 element - det borde ta 4 gånger mer tid än för 1000
Testa med 4000 element - det borde ta 16 gånger mer tid än för 1000
Testa med 8000 element - det borde ta 64 gånger mer tid än för 1000
'''

from labb2_1 import bubble_sort_players
from labb_common import time_team_sorting

if __name__ == '__main__':
    team_sizes = [1000, 2000, 4000, 8000]
    time_team_sorting(bubble_sort_players, team_sizes)