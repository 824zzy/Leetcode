""" a little trival string problem
"""
class Solution:
    def countAndSay(self, n: int) -> str:
        answer = '1'
        for i in range(1, n):
            temp = ''
            last = answer[0]
            freq = 0
            
            
            for elem in answer:
                if last == elem:
                    freq += 1
                else:
                    temp += str(freq) + last
                    last = elem
                    freq = 1
            
            answer = temp + str(freq) + last