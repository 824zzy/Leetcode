""" https://leetcode.com/problems/decode-string/
""" 
class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        ans = num = ""
        for c in s: 
            if c.isalpha(): ans += c
            elif c.isdigit(): num += c
            elif c == "[": 
                stk.append(num)
                stk.append(ans)
                ans = num = ""
            else: # c == "]"
                ans = stk.pop() + ans*int(stk.pop())
        return ans
                
            
"""
"3[a]2[bc]"
"3[a2[c]]"
"2[abc]3[cd]ef"
"3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
"100[leetcode]"
"""
            