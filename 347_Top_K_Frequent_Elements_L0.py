""" Counter.most_common(K) return
[[word_1, frequency_1], [word_2, frequency_2], ..., [word_k, frequency_k]]
"""    

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [w for w, freq in Counter(nums).most_common(k)]