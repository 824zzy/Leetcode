from itertools import permutations
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        if not any(A):
            return '00:00'
        perm = list(permutations(A))
        ans_h = 0
        ans_m = 0
        for p in perm:
            h = int(str(p[0])+str(p[1]))
            m = int(str(p[2])+str(p[3]))
            # print(h, m)
            if h*24+m>ans_h*24+ans_m and h<24 and m<60:
                ans_h = h
                ans_m = m
        
        ans_h = '0'+str(ans_h) if len(str(ans_h))==1 else ans_h
        ans_m = '00' if ans_m==0 else ans_m 
        ans_m = '0'+str(ans_m) if len(str(ans_m))==1 else ans_m 
        ans = str(ans_h)+':'+str(ans_m)
        # print(ans)
        if ans!='00:00':
            return ans
        else:
            return ''
        
        
# Best solution from lee215
def largestTimeFromDigits(self, A):
    return max(["%d%d:%d%d" % t for t in itertools.permutations(A) if t[:2] < (2, 4) and t[2] < 6] or [""])
