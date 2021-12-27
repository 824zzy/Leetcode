""" https://leetcode.com/problems/different-ways-to-add-parentheses/
1. use dic and lambda to simulate operator: ops(input)(x, y)
"""
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        ops = {
            "+": lambda x, y: x+y,
            "-": lambda x, y: x-y,
            "*": lambda x, y: x
        }
        
        def helper(l: int, r: int):
            ans = []
            for i in range(l, r):
                if input[i] in ops:
                    ans += [ops[input[i]](le, ri) for le in helper(l, i) for ri in helper(i+1, r) ]            
            return ans if len(ans)!=0 else [int(input[l:r])]
        
        return help(0, len(input))