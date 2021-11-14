""" Google
"""
class Solution:
    def detectCapital(self, word:str) -> bool:
        if word.isupper() or word.islower():
            return True
        elif word[0].isupper() and word[1:].islower():
            return True
        return False
    
    
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cap = [0 for _ in range(len(word))]
        for i in range(len(word)):
            if word[i].isupper():
                cap[i] = 1
            else:
                cap[i] = 0
        
        if cap.count(1)==len(word) or cap.count(1)==0:
            return True
        elif cap.count(1)==1 and word[0].isupper():
            return True
        else:
            return False