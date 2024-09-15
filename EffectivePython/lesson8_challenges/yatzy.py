import os
import random
import string


class Slot:
    def __init__(self) -> None:
        self._points = None

    @property
    def points(self) -> int:
        if self.is_scorable():
            return 0
        else:
            return self._points
    
    @points.setter
    def points(self, new_value: int) -> bool:
        if self.is_scorable():
            self._points = new_value
            return True
        return False
    
    def get_score(self, dice_values: list[int]) -> int|None:
        # Logic for verifying scoring
        if self.is_scorable():
            return 0
        return None
    
    def is_scorable(self) -> bool:
        if self._points == None:
            return True
        return False
    
    def __str__(self) -> str:
        return self.__class__.__name__


class Upper(Slot):
    def get_score(self, dice_values: list[int], target: int) -> bool:
        if self.is_scorable():
            return sum(die for die in dice_values if die == target)
        return None


class Matching(Slot):
    def get_score(self, dice_values: list[int], matches: int) -> bool:
        if self.is_scorable():
            sorted_dice = sorted(dice_values, reverse = True)
            for index in range(matches - 1, len(sorted_dice)):
                checking_dice = [sorted_dice[index - shift] for shift in range(matches)]
                valid = True
                for die in checking_dice:
                    if checking_dice[0] != die:
                        valid = False
                        break
                if valid:
                    return sum(checking_dice)
            return 0
        return None


class Straight(Slot):
    def get_score(self, dice_values: list[int], target_dice: list) -> bool:
        if self.is_scorable():
            sorted_dice = sorted(dice_values)
            if sorted_dice == target_dice:
                return sum(dice_values)
            return 0
        return None


class Ones(Upper):
    def get_score(self, dice_values: list[int]) -> bool:
        return super().get_score(dice_values, target = 1)
    
    def __str__(self) -> str:
        return 'Ettor'


class Twos(Upper):
    def get_score(self, dice_values: list[int]) -> bool:
        return super().get_score(dice_values, target = 2)
    
    def __str__(self) -> str:
        return 'Tvåor'


class Threes(Upper):
    def get_score(self, dice_values: list[int]) -> bool:
        return super().get_score(dice_values, target = 3)
    
    def __str__(self) -> str:
        return 'Treor'


class Fours(Upper):
    def get_score(self, dice_values: list[int]) -> bool:
        return super().get_score(dice_values, target = 4)
    
    def __str__(self) -> str:
        return 'Fyror'


class Fives(Upper):
    def get_score(self, dice_values: list[int]) -> bool:
        return super().get_score(dice_values, target = 5)
    
    def __str__(self) -> str:
        return 'Femmor'


class Sixes(Upper):
    def get_score(self, dice_values: list[int]) -> bool:
        return super().get_score(dice_values, target = 6)
    
    def __str__(self) -> str:
        return 'Sexor'


class Bonus(Slot):
    @property
    def points(self) -> int:
        if self._points == None:
            return 0
        else:
            return self._points

    def verify(self, upper_scores: list[int]) -> None:
        if self._points == None:
            total_upper = sum(upper_scores)
            if total_upper >= 63:
                self._points = 50
    
    def is_scorable(self) -> bool:
        return None

    def __str__(self) -> str:
        return 'Bonus'


class Pair(Matching):
    def get_score(self, dice_values: list[int]) -> bool:
        return super().get_score(dice_values, matches = 2)
    
    def __str__(self) -> str:
        return 'Par'


class Pairs(Slot):
    def get_score(self, dice_values: list[int]) -> bool:
        if self.is_scorable():
            sorted_dice = sorted(dice_values, reverse = True)
            scored = None
            score_1 = None
            score_2 = None
            for index in range(1, len(sorted_dice)):
                die_1 = sorted_dice[index]
                die_2 = sorted_dice[index - 1]
                if die_1 == die_2:
                    if not scored:
                        score_1 = die_1 + die_2
                        scored = [index, index - 1]
                    elif index not in scored and index - 1 not in scored:
                        score_2 = die_1 + die_2
            if score_1 and score_2:
                return score_1 + score_2
            return 0
        return None

    def __str__(self) -> str:
        return 'Två par'


class Triple(Matching):
    def get_score(self, dice_values: list[int]) -> bool:
        return super().get_score(dice_values, matches = 3)
    
    def __str__(self) -> str:
        return 'Tretal'


class Quadruple(Matching):
    def get_score(self, dice_values: list[int]) -> bool:
        return super().get_score(dice_values, matches = 4)
    
    def __str__(self) -> str:
        return 'Fyrtal'


class StraightSmall(Straight):
    def get_score(self, dice_values: list[int]) -> bool:
        return super().get_score(dice_values, target_dice = [1, 2, 3, 4, 5])
    
    def __str__(self) -> str:
        return 'Liten stege'


class StraightLarge(Straight):
    def get_score(self, dice_values: list[int]) -> bool:
        return super().get_score(dice_values, target_dice = [2, 3, 4, 5, 6])
    
    def __str__(self) -> str:
        return 'Stor stege'


class House(Slot):
    def get_score(self, dice_values: list[int]) -> bool:
        if self.is_scorable():
            sorted_dice = sorted(dice_values, reverse = True)
            biggest = sorted_dice[0]
            smallest = sorted_dice[1]

            big_count = 0
            small_count = 0
            for index in range(len(sorted_dice)):
                if sorted_dice[index] == biggest:
                    big_count += 1
                if sorted_dice[len(sorted_dice) - 1 - index] == smallest:
                    small_count += 1
            
            if {big_count, small_count} == {2, 3}:
                return sum(dice_values)
            return 0
        return None
    
    def __str__(self) -> str:
        return 'Kåk'


class Chance(Slot):
    def get_score(self, dice_values: list[int]) -> bool:
        if self.is_scorable():
            return sum(dice_values)
        return None
    
    def __str__(self) -> str:
        return 'Chans'


class Yatzy(Matching):
    def get_score(self, dice_values: list[int]) -> bool:
        if super().get_score(dice_values, matches = 5):
            return 50
        return None
    
    def __str__(self) -> str:
        return 'Yatzy'


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.scores: dict[str, Slot|Bonus] = dict(
            ones = Ones(),
            twos = Twos(),
            threes = Threes(),
            fours = Fours(),
            fives = Fives(),
            sixes = Sixes(),
            bonus = Bonus(),

            pair = Pair(),
            pairs = Pairs(),
            triple = Triple(),
            quadruple = Quadruple(),
            straight = StraightSmall(),
            Straight = StraightLarge(),
            house = House(),
            chance = Chance(),
            yatzy = Yatzy(),
        )

    def total_score(self) -> int:
        get_score = 0
        for slot in self.scores.values():
            get_score += slot.points
        return get_score
    
    def is_done(self) -> bool:
        for slot in self.scores.values():
            if slot.is_scorable():
                return False
        return True


class Die:
    def __init__(self) -> None:
        self._points = None
        self._is_locked = False
    
    @property
    def points(self) -> int|None:
        return self._points
    
    @property
    def is_locked(self) -> bool:
        return self._is_locked

    def roll(self) -> None:
        if not self.is_locked:
            self._points = random.randint(1, 6)
    
    def toggle_lock(self) -> None:
        self._is_locked = not self._is_locked
    
    def display(self) -> list[str]:
        rows: list[str] = [' _____ ']
        
        if self.points == 1:
            rows.append('|     |')
        elif self.points in [2, 3]:
            rows.append('|*    |')
        else:
            rows.append('|*   *|')
        
        if self.points in [1, 3, 5]:
            rows.append('|  *  |')
        elif self.points in [2, 4]:
            rows.append('|     |')
        else:
            rows.append('|*   *|')
        
        if self.points == 1:
            rows.append('|     |')
        elif self.points in [2, 3]:
            rows.append('|    *|')
        else:
            rows.append('|*   *|')
        
        rows.append(' \u203E\u203E\u203E\u203E\u203E ')

        return rows


class Game:
    def __init__(self) -> None:
        self.players: list[Player] = []
    
    def run(self) -> None:
        notification = None
        while True:
            self._print_rows(
                self._header('Huvudmeny'),
                notification,
                '1. Nytt spel',
                '0. Avsluta'
            )
            notification = ''
            opt = input('>>> ')
            if opt == '0':
                quit()
            elif opt == '1':
                self._setup_game()
            else:
                notification = 'Ogiltigt kommando'

    def _setup_game(self) -> None:
        notification = None
        while True:
            self._print_rows(
                self._header('Nytt spel'),
                notification,
                'Spelare:' if (self.players) else None,
                *[f' - {player.name}' for player in self.players],
                '1. Lägg till spelare',
                '2. Ta bort spelare' if len(self.players) != 0 else None,
                '3. Börja spelet' if len(self.players) != 0 else None,
                '0. Tillbaka till huvudmeny'
            )
            notification = None
            opt = input('>>> ')
            if opt == '0':
                self.players = []
                return
            elif opt == '1':
                self._add_player()
            elif opt == '2' and len(self.players) != 0:
                self._remove_player()
            elif opt == '3' and len(self.players) != 0:
                self._play_game()
                return
            else:
                notification = 'Ogiltigt kommando'
    
    def _add_player(self) -> None:
        notification = None
        while True:
            self._print_rows(
                self._header(
                    'Nytt spel',
                    'Lägg till spelare'
                ),
                notification,
                'Skriv namn på spelare',
                '0. Avbryt'
            )
            notification = None
            opt = input('>>> ')
            if opt == '0':
                return
            else:
                if opt in [player.name for player in self.players]:
                    notification = 'Namn upptaget'
                    continue
                while True:
                    confirm = input(f'Använd spelarnamn {opt}? (j/n)').lower()
                    if confirm == 'j':
                        self.players.append(Player(opt))
                        return
                    elif confirm == 'n':
                        break
                    else:
                        print('Ogiltigt kommando')

    def _remove_player(self) -> None:
        notification = None
        while True:
            self._print_rows(
                self._header(
                    'Nytt spel',
                    'Ta bort spelare'
                ),
                notification,
                [player.name for player in self.players],
                'Skriv namn på spelaren du vill ta bort',
                '0. Avbryt'
            )
            notification = None
            opt = input('>>> ')
            if opt == '0':
                return
            elif opt in [player.name for player in self.players]:
                for index, player in enumerate(self.players):
                    if player.name == opt:
                        self.players.pop(index)
                        if len(self.players) == 0:
                            return
                        break
            else:
                notification = 'Ingen spelare har det namnet'

    def _play_game(self) -> None:
        random.shuffle(self.players)
        turn_count = 0
        active_player_index = -1
        active_player = self.players[active_player_index]

        ### New player Turn
        while not active_player.is_done():
            turn_count += 1
            dice = {char: Die() for char in string.ascii_lowercase[:5]}

            ### Player rolls dice
            for die in dice.values():
                die.roll()
            rolls = 1
            notification = None
            while rolls < 3:
                self._print_rows(
                    self._header(
                        f'Tur {turn_count}: {active_player.name}',
                        f'Slag {rolls}/3'
                    ),
                    notification,
                    'Välj tärning att låsa eller låsa upp innan nästa tärningsslag',
                    *self._display_dice([die for die in dice.values()], show_locks = True),
                    '1. Slå olåsta tärningarna',
                    '0. Gå till poängsättning'
                )
                notification = None
                opt = input('>>> ').lower()
                if opt == '0':
                    break
                elif opt == '1':
                    for die in dice.values():
                        die.roll()
                    rolls += 1
                elif opt in dice.keys():
                    dice[opt].toggle_lock()
                else:
                    notification = 'Ogiltigt kommando'
            
            ### Player chooses how to score points
            self._score_points(
                player = active_player,
                dice = list(dice.values()),
                turn = turn_count
            )
            
            active_player_index = (active_player_index + 1) % len(self.players)
            active_player = self.players[active_player_index]
        
        # Game end
        self.players.sort(key = lambda x: x.total_score())
        winner = self.players[-1]
        while True:
            self._print_rows(
                self._header('Spelslut'),
                f'{winner.name} har vunnit spelet med {winner.total_score()}',
                '### Slutranking ###',
                *[f'{index + 1} - {player.name}: {player.total_score()}' for index, player in enumerate(self.players)],
                '0: Tillbaka till huvudmenyn'
            )
            while True:
                opt = input('>>> ')
                if opt == '0':
                    return
                else:
                    print('Ogiltigt kommando')
    
    def _score_points(
            self,
            player: Player,
            dice: list[Die],
            turn: int
    ) -> None:
        dice.sort(key= lambda die: die.points)
        dice_values = sorted([die.points for die in dice])
        options: list[str] = []
        opts: dict[str, str] = {}
        scores: dict[str, int] = {}
        for index, key in enumerate(player.scores.keys()):
            opt_key = str(index + 1)
            slot = player.scores[key]
            if slot.is_scorable():
                opts[opt_key] = key
                scores[opt_key] = slot.get_score(dice_values)
                options.append(f'{opt_key}: {slot} ({scores[opt_key]})')
            else:
                options.append(f'   {slot} {slot.points}')
        
        notification = None
        scored = False
        while not scored:
            opts = {str(index + 1): key for index, key in enumerate(player.scores.keys()) if player.scores[key].is_scorable()}
            self._print_rows(
                self._header(
                    f'Tur {turn}: {player.name}',
                    'Poängsättning'
                ),
                notification,
                *self._display_dice(dice),
                # f'Tärningar: {" ".join(map(str,[die for die in dice_values]))}',
                *options
            )
            notification = None
            opt = input('>>> ')
            if opt in opts.keys():
                slot_key = opts[opt]
                score = scores[opt]
                scored = player.scores[slot_key].points = score
                if scored and issubclass(player.scores[slot_key].__class__, Upper):
                    upper_scores = [player.scores[key].points for key in player.scores.keys() if issubclass(player.scores[key].__class__, Upper)]
                    player.scores['bonus'].verify(upper_scores)
            else:
                notification = 'Ogiltigt kommando'
        return
    
    def _print_rows(self, *rows: str) -> None:
        self._new_screen()
        for row in rows:
            if row != None:
                print(row)

    def _header(self, *messages: str) -> str:
        header = '### YATZY'
        for message in messages:
            header += f' - {message}'
        header += ' ###'
        return header
    
    def _display_dice(self, dice: list[Die], show_locks = False):
        dice_rows = zip(*[die.display() for die in dice])
        dice_rows = ['  '.join(row) for row in dice_rows]
        dice_rows = [' ' + row for row in dice_rows]
        dice_rows.insert(0, ''.join([f'    {char}    ' for char in string.ascii_lowercase[:len(dice)]]))
        if show_locks:
            dice_rows.append(''.join([f'  låst   ' if die.is_locked else '         ' for die in dice]))
        return dice_rows
    
    def _new_screen(self):
        '''
        Clears the screen, for windows and unix
        '''
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')


if __name__ == '__main__':
    game = Game()
    game.run()