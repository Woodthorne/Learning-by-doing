import os
import random
import string


class Slot:
    def __init__(self) -> None:
        self._value = None
        self._is_blocked = False

    @property
    def value(self) -> int:
        if self.is_blocked or self._value == None:
            return 0
        else:
            return self._value
    
    @property
    def is_blocked(self) -> bool:
        return self._is_blocked

    def block(self) -> bool:
        if self.is_blocked:
            return False
        self._is_blocked = True
        return True
    
    def score(self, dice_values: list[int]) -> bool:
        # Logic for verifying scoring
        return False
    
    def is_scorable(self) -> bool:
        if self.is_blocked:
            return False
        if self.value != 0:
            return False
        return True
    
    def __str__(self) -> str:
        return self.__class__.__name__


class Upper(Slot):
    def score(self, dice_values: list[int], target: int) -> bool:
        if self.value == 0 and not self.is_blocked:
            total = sum(die for die in dice_values if die == target)
            if total > 0:
                self._value = total
                return True
        return False


class Matching(Slot):
    def score(self, dice_values: list[int], matches: int) -> bool:
        if self.value == 0 and not self.is_blocked:
            sorted_dice = sorted(dice_values, reverse = True)
            for index in range(matches - 1, len(sorted_dice)):
                checking_dice = [sorted_dice[index - shift] for shift in range(matches)]
                valid = True
                for die in checking_dice:
                    if checking_dice[0] != die:
                        valid = False
                        break
                if valid:
                    self._value = sum(checking_dice)
                    return True
        return False


class Straight(Slot):
    def score(self, dice_values: list[int], target_dice: list) -> bool:
        if self.value == 0 and not self.is_blocked:
            sorted_dice = sorted(dice_values)
            if sorted_dice == target_dice:
                self._value = sum(dice_values)
                return True
        return False


class Ones(Upper):
    def score(self, dice_values: list[int]) -> bool:
        return super().score(dice_values, target = 1)
    
    def __str__(self) -> str:
        return 'Ettor'


class Twos(Upper):
    def score(self, dice_values: list[int]) -> bool:
        return super().score(dice_values, target = 2)
    
    def __str__(self) -> str:
        return 'Tvåor'


class Threes(Upper):
    def score(self, dice_values: list[int]) -> bool:
        return super().score(dice_values, target = 3)
    
    def __str__(self) -> str:
        return 'Treor'


class Fours(Upper):
    def score(self, dice_values: list[int]) -> bool:
        return super().score(dice_values, target = 4)
    
    def __str__(self) -> str:
        return 'Fyror'


class Fives(Upper):
    def score(self, dice_values: list[int]) -> bool:
        return super().score(dice_values, target = 5)
    
    def __str__(self) -> str:
        return 'Femmor'


class Sixes(Upper):
    def score(self, dice_values: list[int]) -> bool:
        return super().score(dice_values, target = 6)
    
    def __str__(self) -> str:
        return 'Sexor'


class Bonus(Slot):
    def verify(self, upper_scores: list[int]) -> bool:
        if self.value == 0 and not self.is_blocked:
            total_upper = sum(upper_scores)
            if total_upper >= 63:
                self._value = 50
                return True
        return False
    
    def is_scorable(self) -> bool:
        return False

    def __str__(self) -> str:
        return 'Bonus'


class Pair(Matching):
    def score(self, dice_values: list[int]) -> bool:
        return super().score(dice_values, matches = 2)
    
    def __str__(self) -> str:
        return 'Par'


class Pairs(Slot):
    def score(self, dice_values: list[int]) -> bool:
        if self.value == 0 and not self.is_blocked:
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
                self._value = score_1 + score_2
                return True
        return False

    def __str__(self) -> str:
        return 'Två par'


class Triple(Matching):
    def score(self, dice_values: list[int]) -> bool:
        return super().score(dice_values, matches = 3)
    
    def __str__(self) -> str:
        return 'Tretal'


class Quadruple(Matching):
    def score(self, dice_values: list[int]) -> bool:
        return super().score(dice_values, matches = 4)
    
    def __str__(self) -> str:
        return 'Fyrtal'


class StraightSmall(Straight):
    def score(self, dice_values: list[int]) -> bool:
        return super().score(dice_values, target_dice = [1, 2, 3, 4, 5])
    
    def __str__(self) -> str:
        return 'Liten stege'


class StraightLarge(Straight):
    def score(self, dice_values: list[int]) -> bool:
        return super().score(dice_values, target_dice = [2, 3, 4, 5, 6])
    
    def __str__(self) -> str:
        return 'Stor stege'


class House(Slot):
    def score(self, dice_values: list[int]) -> bool:
        if self.value == 0 and not self.is_blocked:
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
                self._value = sum(dice_values)
                return True
        return False
    
    def __str__(self) -> str:
        return 'Kåk'


class Chance(Slot):
    def score(self, dice_values: list[int]) -> bool:
        if self.value == 0 and not self.is_blocked:
            self._value = sum(dice_values)
            return True
        return False
    
    def __str__(self) -> str:
        return 'Chans'


class Yatzy(Matching):
    def score(self, dice_values: list[int]) -> bool:
        if super().score(dice_values, matches = 5):
            self._value = 50
            return True
        return False
    
    def __str__(self) -> str:
        return 'Yatzy'


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.scores = dict(
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
    
    def block_slot(self, slot: str) -> bool:
        return self.scores[slot].block()

    def total_score(self) -> int:
        score = 0
        for slot in self.scores.values():
            score += slot.value
        return score
    
    def is_done(self) -> bool:
        for slot in self.scores.values():
            if slot.is_blocked or slot.value == 0:
                return False
        return True


class Die:
    def __init__(self) -> None:
        self._value = None
        self._is_locked = False
    
    @property
    def value(self) -> int|None:
        return self._value
    
    @property
    def is_locked(self) -> bool:
        return self._is_locked

    def roll(self) -> None:
        if not self.is_locked:
            self._value = random.randint(1, 6)
    
    def toggle_lock(self) -> None:
        self._is_locked = not self._is_locked


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

        # New player Turn
        while not active_player.is_done():
            turn_count += 1
            dice = {char: Die() for char in string.ascii_lowercase[:5]}

            # Player rolls dice
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
                    *[f'{key}: {die.value} - låst' if dice[key].is_locked else f'{key}: {die.value}' for key, die in dice.items() ],
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
            
            # Player chooses how to score
            scored = False
            notification = None
            while not scored:
                opts = [key for key in active_player.scores.keys() if active_player.scores[key].is_scorable()]
                self._print_rows(
                    self._header(
                        f'Tur {turn_count}: {active_player.name}',
                        'Poängsättning'
                    ),
                    notification,
                    f'Tärningar: {" ".join(map(str,[die.value for die in dice.values()]))}',
                    *[f'{index + 1}: {active_player.scores[key]}' for index, key in enumerate(opts)],
                    '0: Stryk ruta istället'
                )
                notification = None
                opt = input('>>> ')
                if opt == '0':
                    while not scored:
                        self._print_rows(
                            self._header(
                                f'Tur {turn_count}: {active_player.name}'
                                'Stryk ruta'
                            ),
                            notification,
                            f'Tärningar: {" ".join(map(str,[die.value for die in dice.values()]))}',
                            *[f'{index + 1}: {active_player.scores[key]}' for index, key in enumerate(opts) ],
                            '0: Fyll i poäng istället'
                        )
                        notification = None
                        opt = input('>>> ')
                        if opt == '0':
                            break
                        elif opt.isnumeric() and 0 <= int(opt) - 1 < len(opts):
                            opt_index = int(opt) - 1
                            scored = active_player.scores[opts[opt_index]].block()
                        if not scored:
                            notification = 'Ogiltigt kommando'
                elif opt.isnumeric() and 0 <= int(opt) - 1 < len(opts):
                    opt_index = int(opt) - 1
                    dice_values = [die.value for die in dice.values()]
                    scored = active_player.scores[opts[opt_index]].score(dice_values)
                else:
                    notification = 'Ogiltigt kommando'
            
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