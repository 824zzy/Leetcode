""" L1
"""


class Solution:
    def replaceWords(self, D: List[str], S: str) -> str:
        trie = {}
        ans = []

        def insert(word):
            node = trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['#'] = word

        def search(word):
            node = trie
            for c in word:
                if c not in node:
                    return False
                node = node[c]
                if '#' in node:
                    return node['#']

        for d in D:
            insert(d)
        for s in S.split():
            m = search(s)
            if m:
                ans.append(m)
            else:
                ans.append(s)
        return ' '.join(ans)
