from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.is_word = False
    
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur_n = self.root
        for w in word:
            cur_n = cur_n.child[w]
        cur_n.is_word = True
        
    def search(self, word: str) -> bool:
        cur_n = self.root
        self.ans = False
        def dfs(node, word):
            if not word:
                if node.is_word:
                    self.ans = True
                return
            if word[0]=='.':
                for n in node.child.values():
                    dfs(n, word[1:])
            else:
                node = node.child[word[0]]
                if not node:
                    return
                dfs(node, word[1:])
        dfs(cur_n, word)
        return self.ans