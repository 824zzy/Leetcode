""" https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
 store characters along with their continuous count in stack for efficiency
 
 Time: O(n)
"""
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = [['#', 0]]
        for i, c in enumerate(s):
            if stk[-1][0]==c:
                stk[-1][1] += 1
                if stk[-1][1]==k: stk.pop()
            else: stk.append([c, 1])
        return "".join(c*k for c, k in stk)