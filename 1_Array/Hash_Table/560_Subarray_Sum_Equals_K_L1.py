class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # TODO: big hash trick
        hash = {}
        sum = 0
        count = 0
        for n in nums:
            sum += n
            if sum == k:
                count += 1
            if sum - k in hash:
                count += hash[sum - k]
            if sum in hash:
                hash[sum] = hash[sum] + 1
            else:
                hash[sum] = 1
        return count