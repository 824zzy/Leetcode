from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        
        longest = 0
        for num in counter:
            if num + 1 in counter:
                longest = max(longest, counter[num]+counter[num+1])
        return longest
                
            