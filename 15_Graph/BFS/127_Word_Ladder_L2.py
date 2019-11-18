class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList:
            return 0
        queue = [(beginWord, 1)]
        visited = set()
        wordSet = set(wordList)
        while queue:
            curr, dist = queue.pop(0)
            if curr==endWord:
                return dist
            if curr in visited:
                continue
            for i in range(len(curr)):
                for j in range(0, 26):
                    ordinal = ord('a')+j
                    next_word = curr[0:i]+chr(ordinal)+curr[i+1:]
                    if next_word in wordSet:
                        queue.append((next_word, dist+1))
            visited.add(curr)
        return 0