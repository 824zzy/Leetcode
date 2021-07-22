""" L0
Note that string deepcopy is necessary.
TODO: add probability solution
"""
class Solution:
    def __init__(self, nums: List[int]):
        self.L = nums
        
    def reset(self) -> List[int]:
        return self.L

    def shuffle(self) -> List[int]:
        tmp = copy.deepcopy(self.L)
        random.shuffle(tmp)
        return tmp