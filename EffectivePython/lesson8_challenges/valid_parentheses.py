class Solution:
    def isValid(sefl, s: str) -> bool:
        active_brackets = []
        closing = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for char in s:
            if char in ['(', '{', '[']:
                active_brackets.append(char)
            else:
                if active_brackets and closing[char] == active_brackets[-1]:
                    active_brackets.pop()
                else:
                    return False
        return not active_brackets