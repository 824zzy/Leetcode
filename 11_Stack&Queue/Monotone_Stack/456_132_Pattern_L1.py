class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        k = float('-inf')
        s = []
        for i in nums[::-1]:
            if i<k:
                return True
            while s and s[-1]<i:
                k = s.pop()
            s.append(i)
        return False