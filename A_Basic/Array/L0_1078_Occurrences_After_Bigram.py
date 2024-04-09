class Solution(object):
    def findOcurrences(self, text, first, second):
        text = text.split(' ')
        # print(text)
        ans = []
        for i in range(len(text) - 2):
            if text[i] == first and text[i + 1] == second:
                ans.append(text[i + 2])
        return ans
