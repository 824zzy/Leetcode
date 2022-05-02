""" https://leetcode.com/problems/k-divisible-elements-subarrays/
save all the valid subarrays in trie and count
Time: O(n^2)
"""
class Trie:
    def __init__(self, A):
        self.trie = {}
        self.A = A
        
    def insert(self, i, k, p):
        node = self.trie
        ans = 0
        while k>-1 and i<len(self.A):
            if self.A[i]%p==0 and (k:=k-1)==-1: 
                break
            
            if self.A[i] not in node:
                node[self.A[i]] = {}
                ans += 1
            node = node[self.A[i]]
            i += 1
        return ans

    
    
class Solution:
    def countDistinct(self, A: List[int], k: int, p: int) -> int:
        ans = 0
        trie = Trie(A)
        for i in range(len(A)):
            ans += trie.insert(i, k, p)
        return ans