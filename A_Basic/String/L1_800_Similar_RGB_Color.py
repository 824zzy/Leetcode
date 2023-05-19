""" https://leetcode.com/problems/similar-rgb-color/
greedily find the target character in the range of [int(s[i], 16)-1, int(s[i], 16)+1] by customized min function
"""
class Solution:
    def similarRGB(self, s: str) -> str:
        HEX = '0123456789abcdef'
        ans = '#'
        for i in range(1, len(s), 2):
            c1, c2, c3 = HEX[(int(s[i], 16)-1)%16], HEX[(int(s[i], 16)+1)%16], HEX[int(s[i], 16)%16]
            mn = min([c1, c2, c3], key=lambda x: abs(int(x+x, 16)-int(s[i:i+2], 16)))
            ans += mn*2
        return ans
            
        
"""
"#09f166"
"#4e3fe1"
"#71c986"
"""
