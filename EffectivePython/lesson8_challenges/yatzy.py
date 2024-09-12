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


class Upper(Slot):
    def score(self, dice: list[int], target: int) -> bool:
        if self.value == 0 and not self.blocked:
            total = sum(die for die in dice if die == target)
            if total > 0:
                self._value = total
                return True
        return False


class Matching(Slot):
    def score(self, dice: list[int], matches: int) -> bool:
        if self.value == 0 and not self.blocked:
            sorted_dice = sorted(dice, reverse = True)
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
    def score(self, dice: list[int], target_dice: list) -> bool:
        if self.value == 0 and not self.blocked:
            sorted_dice = sorted(dice)
            if sorted_dice == target_dice:
                self._value = sum(dice)
                return True
        return False


class Ones(Upper):
    def score(self, dice: list[int]) -> bool:
        return super().score(dice, target = 1)


class Twos(Upper):
    def score(self, dice: list[int]) -> bool:
        return super().score(dice, target = 2)


class Threes(Upper):
    def score(self, dice: list[int]) -> bool:
        return super().score(dice, target = 3)


class Fours(Upper):
    def score(self, dice: list[int]) -> bool:
        return super().score(dice, target = 4)


class Fives(Upper):
    def score(self, dice: list[int]) -> bool:
        return super().score(dice, target = 5)


class Sixes(Upper):
    def score(self, dice: list[int]) -> bool:
        return super().score(dice, target = 6)


class Bonus(Slot):
    def verify(self, upper_scores: list[int]) -> bool:
        if self.value == 0 and not self.blocked:
            total_upper = sum(upper_scores)
            if total_upper >= 63:
                self._value = 50
                return True
        return False


class Pair(Matching):
    def score(self, dice: list[int]) -> bool:
        return super().score(dice, matches = 2)


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


class Triple(Matching):
    def score(self, dice: list[int]) -> bool:
        return super().score(dice, matches = 3)


class Quadruple(Matching):
    def score(self, dice: list[int]) -> bool:
        return super().score(dice, matches = 4)


class StraightSmall(Straight):
    def score(self, dice: list[int]) -> bool:
        return super().score(dice, target_dice = [1, 2, 3, 4, 5])


class StraightLarge(Straight):
    def score(self, dice: list[int]) -> bool:
        return super().score(dice, target_dice = [2, 3, 4, 5, 6])


class House(Slot):
    def score(self, dice: list[int]) -> bool:
        if self.value == 0 and not self.blocked:
            sorted_dice = sorted(dice, reverse = True)
            biggest = sorted_dice[0]
            smallest = sorted_dice[1]

            big_count = 0
            small_count = 0
            for index in range(len(sorted_dice)):
                if sorted_dice[index] == biggest:
                    big_count += 1
                if sorted_dice[len(sorted_dice) - 1 - index] == smallest:
                    small_count += 1
            
            if set(big_count, small_count) == set(2, 3):
                self._value = sum(dice)
                return True
        return False


class Chance(Slot):
    def score(self, dice: list[int]) -> bool:
        if self.value == 0 and not self.blocked:
            self._value = sum(dice)
            return True
        return False


class Yatzy(Matching):
    def score(self, dice: list[int]) -> bool:
        if super().score(dice, matches = 5):
            self._value = 50
            return True
        return False


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
    