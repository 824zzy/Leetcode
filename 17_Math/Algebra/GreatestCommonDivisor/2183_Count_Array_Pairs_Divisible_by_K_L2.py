""" https://leetcode.com/problems/count-array-pairs-divisible-by-k/
explanation: 
https://leetcode.com/problems/count-array-pairs-divisible-by-k/discuss/1785027/C%2B%2BPython-Easy-and-Concise-with-Explanation
https://leetcode.com/problems/count-array-pairs-divisible-by-k/discuss/1784721/Count-GCDs

Count all elements greatest common divisor with k.
For each pair (i, j) of divisors, check if i * j % k == 0
"""
class Solution:
    def countPairs(self, A: List[int], k: int) -> int:
        cnt = Counter(math.gcd(a, k) for a in A)
        ans = 0
        for i in cnt:
            for j in cnt:
                if i*j%k==0:
                    if i<j: ans += cnt[i]*cnt[j]
                    elif i==j: ans += cnt[i]*(cnt[i]-1)//2
        return ans