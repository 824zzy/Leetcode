class Solution:
    def simplifyPath(self, path: str) -> str:
        plist = [p for p in path.split('/') if p]
        stack = []
        for p in plist:
            if p=='..' and stack: stack.pop()
            elif p!='.': stack.append(p)
        return '/'+'/'.join(stack)
    
# same idea as above
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stk = []
        for p in path:
            if not p or p=='.': continue
            elif p=='..':
                if stk: stk.pop()
                else: continue
            else: stk.append(p)
        return '/'+'/'.join(stk)