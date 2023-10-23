""" https://leetcode.com/problems/flatten-nested-list-iterator/
dfs on a special data structure
"""
class NestedIterator:
    def __init__(self, A):
        self.A = []
        def dfs(node):
            for n in node:
                if n.isInteger(): self.A.append(n.getInteger())
                else: dfs(n.getList())      
        dfs(A)
        
    
    def next(self) -> int:
        return self.A.pop(0)
        
    
    def hasNext(self) -> bool:
        return len(self.A)>0