class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count = s.count('a')
        b_count = 0
        s_count = [a_count+b_count]
        for c in s:
            if c=='a':
                a_count -= 1
            else:
                b_count += 1
            s_count.append(a_count+b_count)
        return min(s_count)