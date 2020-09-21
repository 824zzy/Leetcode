class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        for size in range(1, len(arr)+1, 2):
            for i in range(0, len(arr)):
                if i+size<=len(arr):
                    ans += sum(arr[i:i+size])
        return ans