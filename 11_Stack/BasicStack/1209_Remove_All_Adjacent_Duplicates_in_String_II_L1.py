# To make it more efficient, use a pair to store the value and the count of each character.
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = [['#', 0]]
        for i, c in enumerate(s):
            if stk[-1][0]==c:
                stk[-1][1] += 1
                if stk[-1][1]==k: stk.pop()
            else: stk.append([c, 1])
        return "".join(c*k for c, k in stk)