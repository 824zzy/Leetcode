class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a, b = s[:len(s)/2], s[len(s)/2:]
        V = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        cnt_a, cnt_b = 0, 0
        for i in range(len(a)):
            if a[i] in V: cnt_a += 1
            if b[i] in V: cnt_b += 1
        return cnt_a==cnt_b