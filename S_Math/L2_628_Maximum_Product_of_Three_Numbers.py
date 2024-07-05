# O(N)
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1, max2, max3, min1, min2 = (
            float("-inf"),
            float("-inf"),
            float("-inf"),
            float("inf"),
            float("inf"),
        )
        for n in nums:
            if n > max1:
                max1, max2, max3 = n, max1, max2
            elif n > max2:
                max2, max3 = n, max2
            elif n > max3:
                max3 = n

            if n < min1:
                min1, min2 = n, min1
            elif n < min2:
                min2 = n

        return max(max1 * max2 * max3, max1 * min1 * min2)


# O(N*log(N))


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        s = sorted(nums)
        return max(s[-1] * s[-2] * s[-3], s[0] * s[1] * s[-1])
