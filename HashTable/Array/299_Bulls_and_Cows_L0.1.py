from collections import Counter
class Solution(object):
    def getHint(self, secret, guess):
        countA = 0
        for i, j in zip(secret, guess):
            if i==j:
                countA += 1
        
        cntS = Counter(secret)
        cntG = Counter(guess)
        countB = sum((cntS&cntG).values())
        
        return str(countA)+'A'+str(countB-countA)+'B'