""" https://leetcode.com/problems/asteroid-collision/
A variance of monotonic stack, in this problem the "monotonic" is no collision
"""
# elegant implementation
class Solution:
    def asteroidCollision(self, A: List[int]) -> List[int]:
        stk = []
        for x in A:
            # stk has collision
            while stk and (stk[-1]>0 and x<0): 
                y = stk.pop()
                if -x<y: x = y
                elif -x==y: x = 0
            # if x still has mass
            if x: stk.append(x) 
        return stk
    

# ugly implementation
class Solution:
    def asteroidCollision(self, A: List[int]) -> List[int]:
        stk = []
        for x in A:
            ma = x
            while stk and (stk[-1]>0 and x<0):
                if abs(x)==abs(stk[-1]): 
                    ma = 0
                    stk.pop()
                    break
                ma = max([x, stk.pop()], key=abs)
                x = ma
            if ma: stk.append(ma)
        return stk