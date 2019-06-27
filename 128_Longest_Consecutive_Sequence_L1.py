class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d, ans = {}, 0

        for n in nums:
            if n not in d:
                l = d.get(n-1, 0)
                r = d.get(n+1, 0)
                lens = l + r + 1
                
                ans = max(ans, lens)

                d[n-1] = d[n] = d[n+1] = lens
                
        return ans
                
        


""" [4, 1, 3, 2]
{4: 1}
{4: 1, 1: 1}
{4: 2, 1: 1, 3: 2}
{4: 4, 1: 4, 3: 2, 2: 4}

1 2 3 4
      1
1
  2 2 2
4 4 4
"""