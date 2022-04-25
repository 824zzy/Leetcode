""" https://leetcode.com/problems/peeking-iterator/
use a cache to store the peek value
"""
class PeekingIterator:
    def __init__(self, iterator):
        self.it = iterator
        self.cache = None

    def peek(self):
        if not self.cache: self.cache = self.it.next()
        return self.cache
        
    def next(self):
        if not self.cache: return self.it.next()
        ans = self.cache
        self.cache = None
        return ans

    def hasNext(self):
        if self.cache: return True
        else: return self.it.hasNext()