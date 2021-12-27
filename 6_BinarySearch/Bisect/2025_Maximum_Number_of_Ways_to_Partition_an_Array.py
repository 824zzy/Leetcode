""" L3: https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/discuss/1499024/Python3-binary-search
use prefix and locations to find any prefix sum equals to half of nums sum.
TODO: figure out bisect part
"""
class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        prefix = [0]
        loc = defaultdict(list)
        for i, x in enumerate(nums): 
            prefix.append(prefix[-1] + x)
            if i < len(nums)-1: loc[prefix[-1]].append(i)
        
        ans = 0 
        if prefix[-1] % 2 == 0: ans = len(loc[prefix[-1]//2]) # unchanged 
        
        total = prefix[-1]
        for i, x in enumerate(nums): 
            cnt = 0 
            diff = k - x
            target = total + diff 
            if target % 2 == 0: 
                target //= 2
                cnt += bisect_left(loc[target], i)
                cnt += len(loc[target-diff]) - bisect_left(loc[target-diff], i)
            ans = max(ans, cnt)
        return ans 

# TODO: https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/discuss/1499026/Short-Python-solution-Compute-prefix-sums%3A-O(n)
class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        prefix_sums = list(accumulate(nums))
        total_sum = prefix_sums[-1]
        best = 0
        if total_sum % 2 == 0:
            best = prefix_sums[:-1].count(total_sum // 2)  # If no change

        after_counts = Counter(total_sum - 2 * prefix_sum
                               for prefix_sum in prefix_sums[:-1])
        before_counts = Counter()

        best = max(best, after_counts[k - nums[0]])  # If we change first num

        for prefix, x in zip(prefix_sums, nums[1:]):
            gap = total_sum - 2 * prefix
            after_counts[gap] -= 1
            before_counts[gap] += 1

            best = max(best, after_counts[k - x] + before_counts[x - k])

        return best