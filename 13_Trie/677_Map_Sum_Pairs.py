""" L0: https://leetcode.com/problems/map-sum-pairs/
trie+dfs
"""
class MapSum:
    def __init__(self):
        self.trie = {}

    def insert(self, key: str, val: int) -> None:
        cur = self.trie
        for k in key:
            if k not in cur: 
                cur[k] = {}
            cur = cur[k]
        cur['#'] = val

    def sum(self, prefix: str) -> int:
        cur = self.trie
        for p in prefix:
            if p in cur: cur = cur[p]
            else: return 0
        self.ans = 0
        self.dfs(cur)
        return self.ans
        
    def dfs(self, node):
        if '#' in node: self.ans += node['#']
            
        for k, v in node.items():
            if k!='#': self.dfs(node[k])