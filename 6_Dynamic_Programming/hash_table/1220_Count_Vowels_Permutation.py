""" L1
Hash table dp using a,e,i,o,u as key and cumulative sum as value.
"""
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
        for _ in range(n-1):
            a = dp['e']
            e = dp['a'] + dp['i']
            i = dp['a'] + dp['e'] + dp['o'] + dp['u']
            o = dp['i'] + dp['u']
            u = dp['a']
            dp['a'], dp['e'], dp['i'], dp['o'], dp['u'] = a, e, i, o, u
        return sum(dp.values())%(10**9+7)