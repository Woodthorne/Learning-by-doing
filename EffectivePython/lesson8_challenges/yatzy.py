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
        self._ui = Interface()
    
    def run(self) -> None:
        notification = None
        while True:
            self._print_rows(
                self._header('Huvudmeny'),
                notification,
                '1. Nytt spel',
                '0. Avsluta'
            )
            # self._ui.print_menu(
            #     header = 'YATZY',
            #     description = notification,
            #     options = ['Nytt spel'],
            #     escape = 'Avsluta'
            # )
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
        # options = ['Lägg till spelare']
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
            # if len(self.players) != 0:
            #     listing = [player.name for player in self.players]
            #     for command in ['Ta bort spelare', 'Börja spelet']:
            #         if command not in options:
            #             options.append(command)
            # else:
            #     listing = None
            #     for command in ['Ta bort spelare', 'Börja spelet']:
            #         if command in options:
            #             options.remove(command)
            # self._ui.print_menu(
            #     header = 'Starta nytt spel',
            #     description = notification,
            #     listing = listing,
            #     options = options,
            #     escape = 'Tillbaka till huvudmeny'
            # )
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
            # self._ui.print_menu(
            #     header = 'Lägg till spelare',
            #     listing = [
            #         'Skriv namn på spelare',
            #         '0. Tillbaka till nytt spel'
            #     ]
            # )
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
            # self._ui.print_menu(
            #     header = 'Ta bort spelare',
            #     description = notification + 'Välj spelare att ta bort',
            #     options = [player.name for player in self.players],
            #     escape = 'Tillbaka till nytt spel' 
            # )
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
                # header = f'Tur {turn_count}: {active_player.name}'
                # listing = []
                # for char, die in dice.items():
                #     row = f'{char}. {die.value}'
                #     if die.is_locked:
                #         row += ' - låst'
                #     listing.append(row)
                # description = 'Välj tärning att låsa eller låsa upp innan nästa tärningsslag.'
                # self._ui.print_menu(
                #     header = header + f' - Slag {rolls}/3',
                #     description = description,
                #     listing = listing,
                #     options = ['Slå tärningarna'],
                #     escape = 'Spara resultat' 
                # )
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
                # dice_values = [die.value for die in dice.values()]
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
                # description = 'Tärningar:'
                # for num in dice_values:
                #     description += f' {num}'
                # options = []
                # opts = []
                # for slot_key in active_player.scores.keys():
                #     slot = active_player.scores[slot_key]
                #     if slot.is_scorable():
                #         options.append(str(slot))
                #         opts.append(slot_key)
                # self._ui.print_menu(
                #     header = header + ' - Poängsättning',
                #     description = description,
                #     options = options,
                #     escape = 'Stryk ruta istället'
                # )
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
                        # options = []
                        # opts = []
                        # for slot_key in active_player.scores.keys():
                        #     slot = active_player.scores[slot_key]
                        #     if slot.is_scorable():
                        #         options.append(str(slot))
                        #         opts.append(slot_key)
                        # self._ui.print_menu(
                        #     header = header + ' - Stryk ruta',
                        #     options = options,
                        #     escape = 'Fyll i poäng istället'
                        # )
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
            # self._ui.print_menu(
            #     header = 'Spelet är slut',
            #     description = f'{winner.name} har vunnit spelet med {winner.total_score()}',
            #     listing = [f'{player.name}: {player.total_score()}' for player in self.players],
            #     escape = 'Tillbaka till huvudmenyn'
            # )
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

class Interface:
    def print_menu(
            self,
            header: str,
            menu_width: int = 6,
            description: str = None,
            listing: list[str] = None,
            options: list[str] = None,
            escape: str = None
        ) -> None:
        '''
        Prints a bordered menu. Can contain description, lists, and options.
        
        header: Header of the menu.
        
        menu_width: Optional int. Specifies the minimum width of the menu.
            Defaults to 6 characters.

        description: Optional string. Wraps the string so that it fits within the
            width of the menu borders.
        
        listing: Optional list of strings. Produces unnumbered list.
        
        options: Optional list of option strings. Will get numbered starting
            at 1.
        
        escape: Optional string. Adds option "0." at the bottom of options.
            Useful for escaping option.
        
        
        '''
        if len(header) > 2:
            menu_width += len(header) - 2
        if listing:
            for item in listing:
                if len(item) + 4 > menu_width:
                    menu_width = len(item) + 4
        if options:
            for item in options:
                if len(item) + 7 > menu_width:
                    menu_width = len(item) + 7
        if escape and len(escape) + 7 > menu_width:
            menu_width = len(escape) + 7
        content_width = menu_width - 4

        self._new_screen()
        print(f'=={header}{"=" * (content_width - len(header))}==')
        option_num = 0
        if description:
            if len(description) <= content_width:
                padding = content_width - len(description)
                print(f'| {description}{" " * padding} |')
            else:
                split_description = description.split(' ')
                while split_description:
                    current_row = ''
                    while split_description and len(current_row) \
                                                + len(split_description[0]) \
                                                + 1 \
                                                    <= content_width:
                        current_row += ' ' + split_description.pop(0)
                    padding = content_width - len(current_row)
                    print(f'| {current_row}{" " * padding} |')
            print('=' * menu_width)
        
        if listing:
            for item in listing:
                padding = content_width - len(item)
                print(f'| {item}{" " * padding} |')
            print('=' * menu_width)

        if options:
            for item in options:
                option_num += 1
                padding = content_width - len(item) - 3
                print(f'| {option_num}. {item}{" " * padding} |')
        if escape:
            padding = content_width - len(escape) - 2
            print(f'| 0. {escape}{" " * padding}|')
        if options or escape:
            print('=' * menu_width)

    def _string_wrap(self, string: str, max_width: int) -> str:
        '''
        Rudimentary string wrapper which takes a string and maximum width and
        splits the rows at the blank space preceding a width-breaching word.
        '''
        if len(string) <= max_width:
            return string
        split_string = string.split(' ')
        new_string_list = []
        while split_string:
            current_row = []
            while split_string and len(current_row) \
                                    + len(str(current_row)) \
                                    + len(split_string[0]) \
                                    <= max_width:
                current_row.append(split_string.pop(0))
            new_string_list.append(" ".join(current_row))
        new_string = '\n'.join(new_string_list)
        return new_string

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