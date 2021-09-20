class Solution:
    def thousandSeparator(self, n: int) -> str:
        rev_s = list(str(n))[::-1]
        ans = []
        for i in range(len(rev_s)):
            if i%3==0 and i!=0:
                ans.append('.')
            ans.append(rev_s[i])
        return ''.join(reversed(ans))