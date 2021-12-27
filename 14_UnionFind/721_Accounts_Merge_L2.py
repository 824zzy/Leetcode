""" https://leetcode.com/problems/accounts-merge/
Use two hash table for mapping email to index and name,
then find groups by union find
"""
class DSU:
    def __init__(self, n):
        self.p = [i for i in range(n)]

    def find(self, x):
        if self.p[x]!=x: self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)
        
class Solution:
    def accountsMerge(self, A: List[List[str]]) -> List[List[str]]:
        emails = []
        for a in A:
            for e in a[1:]:
                if e not in emails: emails.append(e)
        M1 = {a: i for i, a in enumerate(emails)} # email: index
        
        M2 = {} # email: name
        for a in A:
            for e in a[1:]:
                M2[e] = a[0]   
                                                    
        dsu = DSU(len(emails))
        for a in A:
            for i in range(2, len(a)):
                dsu.union(M1[a[1]], M1[a[i]])
        
        groups = defaultdict(list)
        for e in emails: groups[dsu.find(M1[e])].append(e)
            
        ans = []
        for v in groups.values():
            ans.append([M2[v[0]]]+sorted(v))
        return ans