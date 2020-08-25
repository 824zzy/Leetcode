from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return [w for w, freq in sorted(Counter(words).most_common(), key=lambda t: (-t[1], t[0]))][:k]
