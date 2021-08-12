# L1: from Amazon, sort str as dict's key
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = defaultdict(list)
        for w in strs:
            anag[''.join(sorted(w))].append(w)
        return [v for v in anag.values()]