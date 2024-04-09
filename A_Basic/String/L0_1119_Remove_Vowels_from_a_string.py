""" https://leetcode.com/problems/remove-vowels-from-a-string/
Given a string `s`, remove the vowels 'a', 'e', 'i', 'o', 'u' from it, and return the new string
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
