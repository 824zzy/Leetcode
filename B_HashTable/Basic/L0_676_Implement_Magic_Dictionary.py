""" https://leetcode.com/problems/implement-magic-dictionary/
Since 1 <= dictionary.length <= 100 and 1 <= dictionary[i].length <= 100, and at most 100 calls will be made to search.
so forget about trie. Just use a hash table.

Time complexity: O(100*m*n), where m is the length of the dictionary, n is the length of the search word.
"""


class MagicDictionary:
    def __init__(self):
        self.mp = defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        for w in dictionary:
            self.mp[len(w)].append(w)

    def search(self, searchWord: str) -> bool:
        for w in self.mp[len(searchWord)]:
            cnt = 0
            if w == searchWord:
                continue
            for c1, c2 in zip(w, searchWord):
                if c1 != c2:
                    cnt += 1
                if cnt > 1:
                    continue
            if cnt == 1:
                return True
        return False
