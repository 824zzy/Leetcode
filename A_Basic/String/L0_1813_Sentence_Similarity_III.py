""" https://leetcode.com/problems/sentence-similarity-iii/
brute force simulation
"""


class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        s1 = s1.split()
        s2 = s2.split()
        if len(s1) < len(s2):
            s1, s2 = s2, s1

        for i in range(len(s1)):
            for j in range(i, len(s1) + 1):
                rm = s1[:i] + s1[j:]
                if rm == s2:
                    return True
        return False


"""
"My name is Haley"
"My Haley"
"of"
"A lot of words"
"Eating right now"
"Eating"
"Ogn WtWj HneS"
"Ogn WtWj HneS"
"""
