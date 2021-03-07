class Trie:
    def __init__(self):
        self.trie = {}
        
    def insert(self, word: str) -> None:
        tmp = self.trie
        for c in word:
            if c not in tmp:
                tmp[c] = {}
            tmp = tmp[c]
        tmp['#'] = '#'
    
    def search(self, word: str) -> bool:
        tmp = self.trie
        for c in word:
            if c not in tmp:
                return False
            tmp = tmp[c]
        return '#' in tmp
        
        

    def startsWith(self, prefix: str) -> bool:
        tmp = self.trie
        for c in prefix:
            if c not in tmp:
                return False
            tmp = tmp[c]
        return True