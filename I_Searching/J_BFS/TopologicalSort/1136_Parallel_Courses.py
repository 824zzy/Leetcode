""" L0: http://lkw222.pythonanywhere.com/question_detail/parallel-courses/
"""
from collections import defaultdict
class Solution:
    def parallel_courses(self, n, relations):
        e = defaultdict(list)
        inD = [0] * n
        for i, j in relations:
            e[j-1].append(i-1)
            inD[i-1] += 1
            
        Q = [i for i, d in enumerate(inD) if d==0]
        
        ans = 0
        while Q:
            for _ in range(len(Q)):
                i = Q.pop(0)
                for j in e[i]:
                    inD[j] -= 1
                    if not inD[j]: 
                        Q.append((j))
            ans += 1
        if not ans: return -1
        else: return ans

if __name__ == '__main__':
    s = Solution()
    ans = s.parallel_courses(3, [[1,2],[2,3],[3,1]])
    print(ans)