class Solution:
    def movesToStamp(self, S: str, T: str) -> List[int]:
        def mat(s1, s2):
            s1, s2 = list(s1), list(s2)
            for i in range(len(s1)):
                if s1[i]=='*': s2[i] = '*'
            return s1==s2
        
        ans = []
        flag = True
        while T!='*'*len(T) and flag:
            flag = False
            for i in range(len(T)-len(S)+1):
                if T[i:i+len(S)]!='*'*len(S):
                    if T[i:i+len(S)]==S or mat(T[i:i+len(S)], S):
                        ans.append(i)
                        T = T[:i]+'*'*len(S)+T[i+len(S):]
                        flag = True
        if T!='*'*len(T): return []
        else: return ans[::-1]