class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        p = [0]*(len(edges)+1)
        s = [1]*(len(edges)+1)
        def find(u):
            while p[u]!=u:
                p[u] = p[p[u]] # point to grandparent
                u = p[u]
            return u
        
        for u, v in edges:
            if p[u]==0: p[u] = u
            if p[v]==0: p[v] = v
            pu, pv = find(u), find(v)
            # Both u and v are already in the tree
            if pu==pv: return [u, v]
            # Union, always merge smaller set(pv) to larger set(pu)
            if s[pv]>s[pu]: u, v = v, u
            p[pv] = pu
            s[pu] += s[pv]
        return []