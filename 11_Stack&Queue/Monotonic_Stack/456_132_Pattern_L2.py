class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        k = float('-inf')
        s = []
        for n in nums[::-1]:
            if n<k:
                return True
            while s and s[-1]<n:
                k = s.pop()
            s.append(n)
        return False