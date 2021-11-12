# L0: classical stack problem
class Solution:
    def evalRPN(self, T: List[str]) -> int:
        s = []
        for t in T:
            if t not in "+-*/": s.append(t)
            else:
                r = s.pop()
                l = s.pop()
                s.append(str(int(eval(l+t+r))))
        return s[0]