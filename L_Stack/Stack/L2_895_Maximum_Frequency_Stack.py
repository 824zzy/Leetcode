""" https://leetcode.com/problems/maximum-frequency-stack/
build a stack using:
1. defaultdict(list) to save frequency as key and val list as values. 
2. Counter to save frequency of each element
3. maxF as maximal frequency
"""
class FreqStack:
    def __init__(self):
        self.stk = defaultdict(list)
        self.freq = Counter()
        self.maxF = 0
        
    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.maxF = max(self.maxF, self.freq[val])
        self.stk[self.freq[val]].append(val)

    def pop(self) -> int:
        x = self.stk[self.maxF].pop()
        self.freq[x] -= 1
        if not self.stk[self.maxF]: self.maxF -= 1
        return x