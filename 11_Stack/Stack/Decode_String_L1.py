class Solution:
    def decodeString(self, s: str) -> str:
        digit = ''
        ans = ''
        stack = []
        for c in s:
            if c.isnumeric():
                digit += c
            elif c.isalpha():
                ans += c
            elif c=='[':
                stack.append((ans, int(digit)))
                digit, ans = '', ''
            elif c==']':
                prev, n = stack.pop()
                ans = prev + ans * n
        return ans