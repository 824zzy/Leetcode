""" https://leetcode.com/problems/text-justification/
complex simulation
"""
from header import *


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def process(line):
            words = line.split()
            if len(words) == 1:
                return words[0] + " " * (maxWidth - len(words[0]))
            ans = [words[0]]
            for i in range(1, len(words)):
                ans.append("")
                ans.append(words[i])
            width = maxWidth - sum(len(w) for w in words)
            i = 0
            while width > 0:
                if i & 1:
                    ans[i % (len(ans) - 1)] += " "
                    width -= 1
                i += 1
            return "".join(ans)

        def process_last(line):
            return line + " " * (maxWidth - len(line))

        ans = []
        line = words[0]
        for i in range(1, len(words)):
            w = words[i]
            if len(line) + len(w) + 1 <= maxWidth:
                line += " " + w
            else:
                ans.append(process(line))
                line = w
        ans.append(process_last(line))
        return ans


"""
["This", "is", "an", "example", "of", "text", "justification."]
16
["What","must","be","acknowledgment","shall","be"]
16
["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
20
["Listen","to","many,","speak","to","a","few."]
6
"""
