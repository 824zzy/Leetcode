class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList:
            return 0
        queue = [(beginWord, 1)]
        seen = set()
        wordSet = set(wordList)
        while queue:
            curr, dist = queue.pop(0)
            if curr==endWord:
                return dist
            if curr in seen:
                continue
            for i in range(len(curr)):
                for j in range(0, 26):
                    ordinal = ord('a')+j
                    next_word = curr[0:i]+chr(ordinal)+curr[i+1:]
                    if next_word in wordSet:
                        queue.append((next_word, dist+1))
            seen.add(curr)
        return 0
    
# Reduce time complexity by defaultdict
class Solution:
    def ladderLength(self, b: str, e: str, L: List[str]) -> int:
        if e not in L: return 0
        queue = [b]
        masks = defaultdict(list)
        for w in L:
            for i, c in enumerate(w):
                masks[w[:i]+'*'+w[i+1:]].append(w)
        L = set(L)
        step = 1
        while queue:
            for _ in range(len(queue)):
                curr = queue.pop(0)
                if curr in L: L.remove(curr)
                for i, c in enumerate(curr):
                    m = curr[:i]+'*'+curr[i+1:]
                    queue.extend(masks[m])
                    del masks[m]
                if e in queue: return step+1
            step += 1
        return 0