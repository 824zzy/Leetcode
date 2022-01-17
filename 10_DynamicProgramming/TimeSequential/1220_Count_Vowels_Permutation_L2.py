""" https://leetcode.com/problems/count-vowels-permutation/
Hash table dp using a,e,i,o,u as key and cumulative sum as value.
"""
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        @cache
        def fn(n, c):
            """Return count of n vowels starting with c."""
            if n == 1: return 1
            if c == "a": return fn(n-1, "e")
            elif c == "e": return fn(n-1, "a") + fn(n-1, "i")
            elif c == "i": return fn(n-1, "a") + fn(n-1, "e") + fn(n-1, "o") + fn(n-1, "u")
            elif c == "o": return fn(n-1, "i") + fn(n-1, "u")
            else: return fn(n-1, "a")
            
        return sum(fn(n, c) for c in "aeiou")%(10**9+7)
    
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