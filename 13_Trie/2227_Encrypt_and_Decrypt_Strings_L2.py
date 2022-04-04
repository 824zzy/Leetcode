""" https://leetcode.com/problems/encrypt-and-decrypt-strings/
trie + back tracking: pruning and pruning again
"""
class Trie:
    def __init__(self):
        self.trie = {}
        
    def insert(self, word: str) -> None:
        node = self.trie
        for c in word:
            if c not in node: node[c] = {}
            node = node[c]
        node['#'] = word

    def search(self, word: str) -> bool:
        node = self.trie
        for c in word:
            if c not in node: return False
            node = node[c]
        return '#' in node
    
    
class Encrypter:
    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.mp = {k: v for k, v in zip(keys, values)}
        self.mp2 = defaultdict(set)
        for k, v in zip(keys, values):
            self.mp2[v].add(k)
            
        self.T = Trie()
        for d in set(dictionary):
            self.T.insert(d)

    def encrypt(self, word1: str) -> str:
        ans = ''
        for c in word1:
            ans += self.mp[c]
        return ans

    def decrypt(self, word2: str) -> int:
        self.ans = 0
        stk = []
        def dfs(i, node):
            if i==len(word2): 
                if '#' in node:
                    self.ans += 1
                    return 
            for c in self.mp2[word2[i:i+2]]:
                if c in node:
                    stk.append(c)
                    dfs(i+2, node[c])
                    stk.pop()
                    
        node = self.T.trie
        dfs(0, node)
        return self.ans