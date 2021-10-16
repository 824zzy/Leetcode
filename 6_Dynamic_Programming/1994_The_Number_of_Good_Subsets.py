""" L4: https://leetcode.com/problems/the-number-of-good-subsets/
https://leetcode.com/problems/the-number-of-good-subsets/discuss/1444213/Python-DP-solution
Sorry I am stupid.

dp+math+bitmask
"""
class Solution:
    def numberOfGoodSubsets(self, A: List[int]) -> int:
        mod = 10 ** 9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # n<30
        dp = [1] + [0] * (1 << 10) # len(primes)==10
        count = Counter(A)
        for a in count:
            if a == 1: continue # special case
            if a % 4 == 0 or a % 9 == 0 or a == 25: continue # 2*2, 3*3, 5*5 are bad
            # Find prime factors and represent in bitmask
            # Bitmask === a set of primes where primes[i] is included if bitmask[i] == 1.
            mask = sum([1 << i for i, p in enumerate(primes) if a % p == 0])
            # Iterate through all possible sets of primes
            for i in range(1 << 10): 
                # Skip if there is any common set bits/prime (becomes invalid subset)
                if i & mask: continue
                dp[i | mask] = (dp[i | mask] + count[a] * dp[i]) % mod
        return (1 << count[1]) * (sum(dp) - 1) % mod