""" https://leetcode.com/problems/apply-discount-to-prices/
format floats by {:.2f}
"""
class Solution:
    def discountPrices(self, A: str, discount: int) -> str:
        ans = []
        for s in A.split():
            if s[0]=='$' and s[1:].isnumeric():
                x = int(s[1:])
                x *= (100-discount)/100
                ans.append("$"+'{:.2f}'.format(x))
            else: ans.append(s)
        return ' '.join(ans)