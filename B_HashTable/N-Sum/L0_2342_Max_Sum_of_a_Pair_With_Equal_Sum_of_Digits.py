""" https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/
"""
# two-sum like solution
class Solution:
    def maximumSum(self, A: List[int]) -> int:
        seen = defaultdict(int)
        ans = -1
        for x in A:
            sm = sum(int(c) for c in str(x))
            if sm in seen:
                ans = max(ans, x+seen[sm])
                seen[sm] = max(x, seen[sm])
            else: seen[sm] = x
        return ans

# straight forward solution: sort the hash table and find the max two sum
class Solution:
    def maximumSum(self, A: List[int]) -> int:
        mp = defaultdict(list)
        for x in A:
            mp[sum([int(c) for c in str(x)])].append(x)
        
        ans = -1
        for k, v in mp.items():
            if len(v)>=2:
                vv = sorted(v, reverse=True)
                ans = max(ans, vv[0]+vv[1])
        return ans
            
            
        
""" 54 -1 973
[18,43,36,13,7]
[10,12,19,14]
[229,398,269,317,420,464,491,218,439,153,482,169,411,93,147,50,347,210,251,366,401]
"""