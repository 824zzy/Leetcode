class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s)-1
        s = list(s)
        
        while l<r:
            while s[l] not in 'AEIOUaeiou' and l<r:
                l += 1
            while s[r] not in 'AEIOUaeiou' and l<r:
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)