from random import randint as roll_die

class Slot:
    def __init__(self) -> None:
        self._value = None
        self._blocked = False

    @property
    def value(self) -> int:
        if self.blocked or self._value == None:
            return 0
        else:
            return self._value
    
    @property
    def blocked(self) -> bool:
        return self._blocked

    def block(self) -> bool:
        if self.blocked:
            return False
        else:
            self._blocked = True
            return True
    
    def score(self, dice: list[int]) -> bool:
        # Logic for verifying scoring
        return False


class Ones(Slot):    
    def score(self, dice: list[int]) -> bool:
        if self.value == 0 and not self.blocked:
            total = sum(die for die in dice if die == 1)
            if total > 0:
                self._value = total
                return True
        return False


class Twos(Slot):
    def score(self, dice: list[int]) -> bool:
        if self.value == 0 and not self.blocked:
            total = sum(die for die in dice if die == 2)
            if total > 0:
                self._value = total
                return True
        return False


class Threes(Slot):
    def score(self, dice: list[int]) -> bool:
        if self.value == 0 and not self.blocked:
            total = sum(die for die in dice if die == 3)
            if total > 0:
                self._value = total
                return True
        return False


class Fours(Slot):
    def score(self, dice: list[int]) -> bool:
        if self.value == 0 and not self.blocked:
            total = sum(die for die in dice if die == 4)
            if total > 0:
                self._value = total
                return True
        return False


class Fives(Slot):
    def score(self, dice: list[int]) -> bool:
        if self.value == 0 and not self.blocked:
            total = sum(die for die in dice if die == 5)
            if total > 0:
                self._value = total
                return True
        return False


class Sixes(Slot):
    def score(self, dice: list[int]) -> bool:
        if self.value == 0 and not self.blocked:
            total = sum(die for die in dice if die == 6)
            if total > 0:
                self._value = total
                return True
        return False


class Bonus(Slot):
    def verify(self, upper_scores: list[int]) -> bool:
        if self.value == 0 and not self.blocked:
            total_upper = sum(upper_scores)
            if total_upper >= 63:
                self._value = 50
                return True
        return False


class Pair(Slot):
    def score(self, dice: list[int]) -> bool:
        if self.value == 0 and not self.blocked:
            sorted_dice = sorted(dice, reverse = True)
            for index in range(1, len(sorted_dice)):
                die_1 = sorted_dice[index]
                die_2 = sorted_dice[index - 1]
                if die_1 == die_2:
                    self._value = die_1 + die_2
                    return True
        return False


class Pairs(Slot):
    def score(self, dice: list[int]) -> bool:
        if self.value == 0 and not self.blocked:
            sorted_dice = sorted(dice, reverse = True)
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
    
#     