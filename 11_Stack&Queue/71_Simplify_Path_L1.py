class Solution:
    def simplifyPath(self, path: str) -> str:
        plist = [p for p in path.split('/') if p]
        stack = []
        for p in plist:
            if p=='..':
                if stack:
                    stack.pop()
            elif p!='.':
                stack.append(p)
        return '/'+'/'.join(stack)