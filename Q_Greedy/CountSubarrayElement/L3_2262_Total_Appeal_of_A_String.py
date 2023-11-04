""" https://leetcode.com/problems/total-appeal-of-a-string/
Similar to /Q_Greedy/CountSubarrayElement/828_Count_Unique_Characters_of_All_Substrings_of_a_Given_String_L3.py

Iterative element instead of the whole array.

1. From A to Z, find all the indexes of every characters
2. Given ...XXXA[XXAXX]AXX.., the answer of j should be (A[j]-A[i])*(A[k]-A[j])
               i   j   k
"""
class Solution:
    def appealSum(self, s: str) -> int:
        mp = [[-1] for _ in range(26)]
        n = len(s)
        for i, c in enumerate(s):
            mp[ord(c)-97].append(i)
        for i in range(26):
            mp[i].append(n)
            
        ans = 0
        for x in mp:
            for i in range(1, len(x)-1):
                ans += (x[i]-x[i-1])*(n-x[i])
        return ans
    

""" https://leetcode.com/problems/total-appeal-of-a-string/
from lee: https://leetcode.com/problems/total-appeal-of-a-string/discuss/1996390/JavaC%2B%2BPython-Easy-and-Concise-with-Explanation
record the increment using hash table, check the example below
"""
class Solution:
    def appealSum(self, s: str) -> int:
        ans = 0
        sm = 0
        last = {}
        for i, c in enumerate(s):
            sm += i-last.get(c, -1)
            ans += sm
            last[c] = i
        return ans

"""
abbca
[a]
 1
abbca
 [b]
[ab]
2 1
abbca
  [b]
 [bb]
[abb]
2 1 1
.......
"""