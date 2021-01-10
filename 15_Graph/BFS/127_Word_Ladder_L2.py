# Reduce time complexity by ordina
class Solution:
    def ladderLength(self, b: str, e: str, L: List[str]) -> int:
        if e not in L: return 0
        queue = [b]
        masks = defaultdict(list)
        L = set(L)
        step = 1
        while queue:
            for _ in range(len(queue)):
                curr = queue.pop(0)
                for i, c in enumerate(curr):
                    for j in range(26):
                        ordinal = ord('a')+j
                        l = curr[:i]+chr(ordinal)+curr[i+1:]
                        if l in L: 
                            queue.append(l)
                            L.remove(l)
                if e in queue: return step+1
            step += 1
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