# itertoools.accumulate
class Solution:
    def runningSum(self, A):
        return list(itertools.accumulate(A))

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans, S = [], 0
        for n in nums:
            S += n
            ans.append(S)
        return ans