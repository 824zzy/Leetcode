""" L1:
One pass to count suffix sum of shifts.
One pass to shift letters in string S
"""
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        prefix = 0
        new_shifts = []
        for c in shifts[::-1]:
            prefix += c
            new_shifts.append(prefix%26)
        new_shifts = new_shifts[::-1]
        ans = []
        for i, c in enumerate(s):
            ans.append(chr((ord(c)-97+new_shifts[i])%26+97))
        return ''.join(ans)