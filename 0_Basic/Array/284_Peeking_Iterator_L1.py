""" https://leetcode.com/problems/peeking-iterator/
use a buffer to store the peek value
"""
class PeekingIterator:
    def __init__(self, iterator):
        self.it = iterator
        self.buff = None

        
    def peek(self):
        if self.buff: return self.buff
        else:
            self.buff = self.it.next()
            return self.buff
        

    def next(self):
        if self.buff:
            ans = self.buff
            self.buff = None
            return ans
        else: return self.it.next()

        
    def hasNext(self):
        if self.buff: return True
        else: return self.it.hasNext()