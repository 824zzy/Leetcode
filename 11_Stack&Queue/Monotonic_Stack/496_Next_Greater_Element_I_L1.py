class Solution:
    def nextGreaterElement(self, A: List[int], B: List[int]) -> List[int]:
        stk, ans = [], []
        mp = {}
        for b in B:
            while stk and stk[-1]<b:
                mp[stk.pop()] = b
            stk.append(b)

        for a in A:
            if a in mp: ans.append(mp[a])
            else: ans.append(-1)
        return ans