from random import randint as roll_die

class Slot:
    def __init__(self) -> None:
        self._value = None
        self.blocked = False

    @property
    def value(self) -> int:
        if self.blocked or self._value == None:
            return 0
        else:
            return self._value
    
    def score(self, dice: list[int]) -> bool:
        # Logic for verifying scoring
        pass

class Ones(Slot):
    def __init__(self) -> None:
        super().__init__()
    
    def score(self, dice: list[int]) -> bool:
        if self.value == 0:
            total = sum(die for die in dice if die == 1)
            if total > 0:
                self._value = total
                return True
        return False





# class Player:
#     def __init__(self, name: str) -> None:
#         self.name = name
#         self.scores = dict(
#             ones = None,
#             twos = None,
#             threes = None,
#             fours = None,
#             fives = None,
#             sixes = None,
#             bonus = None,

#             pair = None,
#             pairs = None,
#             triple = None,
#             quadruple = None,
#             straight = None,
#             Straight = None,
#             house = None,
#             chance = None,
#             yatzy = None,
#         )

#     def block_slot(self, slot: str) -> bool:
#         if not self.scores[slot]:
#             self.scores[slot] = 'blocked'
#             return True
#         return False
    
#     def get_total_score(self) -> int:
#         slots = [
#             'ones', 'twos', 'threes', 'fours',
#             'fives', 'sixes', 'bonus', 'pair',
#             'pairs', 'triple', 'quadruple', 'straight',
#             'Straight', 'house', 'chance', 'yatzy'
#         ]
#         total_score = 0
#         for slot in slots:
#             slot_score = self.scores[slot]
#             if type(slot_score) == int:
#                 total_score += slot_score
        
#         return total_score
    
#     def verify_bonus(self) -> None:
#         requirements = [
#             'ones', 'twos', 'threes',
#             'fours', 'fives', 'sixes'
#         ]
#         bonus_possible = True
#         for slot in requirements:
#             if not self.scores[slot]:
#                 bonus_possible = False
#         if bonus_possible:
#             total_upper = sum(self.scores[slot] for slot in requirements)
#             if total_upper < 63:
#                 self.scores['bonus'] = 'blocked'
#             else:
#                 self.scores['bonus'] = 50
