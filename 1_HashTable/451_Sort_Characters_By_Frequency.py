""" L0: https://leetcode.com/problems/sort-characters-by-frequency/
count frequency and sort the counter.
"""
# most_common()
class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s).most_common()
        return "".join([k*v for k, v in cnt])

# lambda sort
class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = sorted(Counter(s).items(), key=lambda x: -x[1])
        return "".join([k*v for k, v in cnt])