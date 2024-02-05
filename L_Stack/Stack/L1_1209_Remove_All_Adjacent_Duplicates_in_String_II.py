""" https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
store characters along with their continuous count in stack for efficiency
 
Time: O(n)
"""

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []
        for c in s:
            if stk:
                # push c
                if stk[-1][0]==c:
                    stk[-1][1] += 1
                else:
                    stk.append([c, 1])
                # pop k duplicate
                if stk[-1][1]==k:
                    stk.pop()
            else:
                stk.append([c, 1])
        return ''.join(k*v for k, v in stk)