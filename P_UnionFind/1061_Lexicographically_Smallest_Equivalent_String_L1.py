""" https://leetcode.com/problems/lexicographically-smallest-equivalent-string/
Find groups of equivalent characters.
The tricky part is maintaining the minimal group index during the union operation.
"""
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        A = list(range(26))
        
        def find(x):
            if A[x]!=x: A[x] = find(A[x])
            return A[x]
        
        def union(x, y):
            _x, _y = find(x), find(y)
            if _x<_y: _x, _y = _y, _x
            A[_x] = _y
            
        for x, y in zip(s1, s2):
            union(ord(x)-97, ord(y)-97)
            
        return ''.join([chr(find(ord(c)-97)+97) for c in baseStr])