class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n-1
    
class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while n>1:
            if n%2==0:
                ans += n/2
                n /= 2
            else:
                ans += n//2
                n = n//2+1
        return int(ans)