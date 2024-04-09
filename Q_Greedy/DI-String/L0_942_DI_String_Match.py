""" https://leetcode.com/problems/construct-smallest-number-from-di-string/
Greedily pop the smallest/largest number from the stack to the answer.
Or use lee's template
"""
# greedily pop the smallest/largest number from the stack to the answer


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        ans, s = [], [i for i in range(len(S) + 1)]
        for c in S:
            if c == 'I':
                ans.append(s.pop(0))
            else:
                ans.append(s.pop())
        ans.append(s.pop())
        return ans

# lee's template


class Solution:
    def diStringMatch(self, A: str) -> List[int]:
        ans = []
        stk = []
        for i, c in enumerate(A + 'I'):
            stk.append(str(i))
            if c == 'I':
                ans += stk[::-1]
                stk = []
        return ans
