""" L1: https://leetcode.com/problems/implement-magic-dictionary/submissions/
TODO: wrong answer
https://leetcode.com/problems/implement-magic-dictionary/discuss/896442/Python3-trie
"""
class MagicDictionary:

    def __init__(self):
        self.root = {} # root of trie 

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary: 
            node = self.root
            for c in word: node = node.setdefault(c, {})
            node["#"] = word # sentinel 

    def search(self, searchWord: str) -> bool:
        
        def fn(node, i, chg=False): 
            """Return True if it is possible to change one character."""
            if not node: return False 
            if i == len(searchWord): return node.get("#") and chg
            return fn(node.get(searchWord[i]), i+1, True) if chg else any(fn(node[c], i+1, c != searchWord[i]) for c in node if c != "#")  
        
        return fn(self.root, 0)