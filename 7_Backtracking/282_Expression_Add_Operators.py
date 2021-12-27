""" L2
TODO: https://leetcode.com/problems/expression-add-operators/discuss/775390/Python3-eval-string
"""
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def fn(i, expr, total, last):
            """Populate ans with expression evaluated to target."""
            if i == len(num): 
                if total == target: ans.append(expr)
            else: 
                for ii in range(i, len(num) if num[i] != "0" else i+1): 
                    val = int(num[i:ii+1])
                    if i == 0: fn(ii+1, num[i:ii+1], val, val)
                    else: 
                        fn(ii+1, expr + "*" + num[i:ii+1], total - last + last * val, last * val)
                        fn(ii+1, expr + "+" + num[i:ii+1], total + val, val)
                        fn(ii+1, expr + "-" + num[i:ii+1], total - val, -val)
                    
        ans = []
        fn(0, "", 0, 0)
        return ans