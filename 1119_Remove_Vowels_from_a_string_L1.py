""" Premium member problem
Given a string `s`, remove the vowels 'a', 'e', 'i', 'o', 'u' from it, and return the new string

hint: hash set is a little bit faster.
"""


class Solution:
    def removeVowels(self, S: str) -> None:
        s = set()
        s.add('a')
        s.add('e')
        s.add('i')
        s.add('o')
        s.add('u')

        result = ''
        for c in S:
            if not s.contains(c):
                result.append(c)
        
        return result

            
    