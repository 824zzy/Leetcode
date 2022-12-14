""" https://leetcode.com/problems/design-memory-allocator/description/
since n<=1000, just brute force using two pointers
"""
class Allocator:
    def __init__(self, n: int):
        self.A = [0]*n

    def allocate(self, size: int, mID: int) -> int:
        cnt = 0
        for i, x in enumerate(self.A):
            if x: cnt = 0
            else:
                cnt += 1
                if cnt==size:
                    self.A[i-size+1:i+1] = [mID]*size
                    return i-size+1
        return -1

    def free(self, mID: int) -> int:
        ans = 0
        for i in range(len(self.A)):
            if self.A[i]==mID:
                self.A[i] = 0
                ans += 1
        return ans
