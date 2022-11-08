""" https://leetcode.com/problems/next-greater-element-iv/
learn from lee and guan:
lee: https://leetcode.com/problems/next-greater-element-iv/discuss/2756668/JavaC%2B%2BPython-One-Pass-Stack-Solution-O(n)
guan video explanation: https://www.youtube.com/watch?v=vrNFhKKHkP0
"""
class Solution:
    def secondGreaterElement(self, A: List[int]) -> List[int]:
        # next greater on the right
        stk1 = []
        stk2 = []
        ans = [-1]*len(A)
        for i in range(len(A)):
            while stk2 and A[stk2[-1]]<A[i]:
                ans[stk2.pop()] = A[i]
            
            tmp = []
            while stk1 and A[stk1[-1]]<A[i]:
                tmp.append(stk1.pop())
            stk2.extend(tmp[::-1])
            
            stk1.append(i)
        return ans