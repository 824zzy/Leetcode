class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = ''
        while n > 26:
            curr = n % 26
            if curr!=0:
                ans += str(chr(curr+64))
            else:
                ans += 'Z'
                n -= 1
            n = n // 26
        if n!=0:
            ans += str(chr(n+64))
        else:
            ans += 'Z'
        return ans[::-1]