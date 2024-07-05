""" L1: simulate preorder traversal
annoying corner case
"""


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        S = preorder.split(",")
        stk = []
        for i, c in enumerate(S):
            while len(stk) > 1 and stk[-1] == "#" and c == "#":
                stk.pop()
                stk.pop()
            # corner cases like "1,#,#,#,#"
            if stk == ["#"] and i != len(S) - 1:
                return False
            stk.append(c)
        return stk == ["#"]
