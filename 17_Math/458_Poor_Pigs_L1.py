class Solution:
    def poorPigs(self, b: int, D: int, T: int) -> int:
        base = 0
        while (T/D+1)**base<b:
            base += 1
        return base