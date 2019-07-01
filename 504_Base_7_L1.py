class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'

        f = False
        if num < 0:
            f = True
            num = -num
        
        ans = ''        
        while num:
            ans += str(num)
            num //= 7

        return ans[::-1] if f else '-'+ans[::-1]