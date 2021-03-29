"""
The order of digits is the key to solve problem.
"""
class Solution:
    def originalDigits(self, s: str) -> str:
        D = ["zero","two","four","six","eight","one","three","five","seven","nine"]
        I = [0,2,4,6,8,1,3,5,7,9]
        M = [(Counter(d), str(i)) for d, i in zip(D, I)]
        cnt = Counter(s)
        ans = ''
        while M:
            while cnt|M[0][0]==cnt:
                ans += M[0][1]
                cnt -= M[0][0]
            M.pop(0)
        return "".join(sorted(ans))