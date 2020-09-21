class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = '123456789'
        ln, hn = len(str(low)), len(str(high))
        def dfs(idx, l):
            if idx>=len(s):
                return
            if low<=int(s[idx:idx+l])<=high:
                self.ans.append(int(s[idx:idx+l]))
            if idx+l<9:
                dfs(idx+1, l)
        
        self.ans = []
        for l in range(ln, hn+1):
            if l<10:
                dfs(0, l)
        return self.ans
    
    
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def trans(n):
            sn = str(n)
            seq = True
            for i in range(1, len(sn)):
                if int(sn[i])!=int(sn[i-1])+1:
                    seq = False
                    break
            t = ''
            if seq:
                for i in range(len(sn)):
                    t += str(int(sn[i])+1)
            else:
                t += sn[0]
                for i in range(1, len(sn)):
                    t += str(int(t[i-1])+1)
            return None if len(t)!=len(sn) else t
        ans = []
        curr = low-1
        while low-1<=curr<=high+1:
            tmp = trans(curr)
            if tmp:
                curr = int(tmp)
                if low<=int(tmp)<=high:
                    ans.append(tmp)
                else:
                    curr = int(str(int(str(curr)[0])+1)+(len(str(curr))-1)*'0')
            else:
                curr = int('1'+len(str(curr))*'0')
        return ans