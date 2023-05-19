""" https://leetcode.com/problems/top-k-frequent-elements/
Counter.most_common(K) return [[word_1, frequency_1], [word_2, frequency_2], ..., [word_k, frequency_k]]
"""    
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [w for w, freq in Counter(nums).most_common(k)]

class Solution:
    def topKFrequent(self, A: List[int], topk: int) -> List[int]:
        cnt = Counter(A)
        return [k for k, _ in sorted(cnt.items(), key=lambda x: -x[1])][:topk]