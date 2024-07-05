""" https://leetcode.com/problems/count-collisions-on-a-road/
"""


class Solution:
    def countCollisions(self, A: str) -> int:
        stk = []
        ans = 0
        for x in A:
            while stk and (
                (stk[-1] == "R" and x == "L")
                or (stk[-1] == "R" and x == "S")
                or (stk[-1] == "S" and x == "L")
            ):
                if stk[-1] == "R" and x == "L":
                    ans += 2
                elif (stk[-1] == "R" and x == "S") or (stk[-1] == "S" and x == "L"):
                    ans += 1
                stk.pop()
                # staying after collision
                x = "S"
            stk.append(x)
        return ans
