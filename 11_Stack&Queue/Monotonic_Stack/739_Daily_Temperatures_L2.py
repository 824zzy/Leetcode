class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stk = []
        ans = [0]*len(T)
        for i, t in enumerate(T):
            while stk and stk[-1][0]<t:
                last_i = stk[-1][1]
                ans[last_i] = i-last_i
                stk.pop()
            stk.append((T[i], i))
    return ans