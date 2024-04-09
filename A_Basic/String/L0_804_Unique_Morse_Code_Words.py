""" https://leetcode.com/problems/unique-morse-code-words/
transform word into morse code and check the length of the seen set
"""


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mp = {chr(i + 97): x for i,
              x in enumerate([".-",
                              "-...",
                              "-.-.",
                              "-..",
                              ".",
                              "..-.",
                              "--.",
                              "....",
                              "..",
                              ".---",
                              "-.-",
                              ".-..",
                              "--",
                              "-.",
                              "---",
                              ".--.",
                              "--.-",
                              ".-.",
                              "...",
                              "-",
                              "..-",
                              "...-",
                              ".--",
                              "-..-",
                              "-.--",
                              "--.."])}
        seen = set()
        for w in words:
            morse = ''.join([mp[c] for c in w])
            seen.add(morse)
        return len(seen)
