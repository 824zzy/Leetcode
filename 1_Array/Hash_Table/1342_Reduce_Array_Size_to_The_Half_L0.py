from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        l, thres, ans = len(arr), len(arr)//2, 0
        cnt = Counter(arr)
        sortA = sorted(cnt.items(), key=lambda i:i[1], reverse=True)
        for i in sortA:
            ans += 1
            if l-i[1]<=thres:
                return ans
            else:
                l -= i[1]