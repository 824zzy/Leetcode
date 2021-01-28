# Time Complexity: O(N), Space Complexity: O(1)
class Solution:
    def firstMissingPositive(self, A: List[int]) -> int:
        for i in range(len(A)):
            if A[i]<=0 or A[i]>len(A): A[i] = len(A)+1
        
        for a in A:
            a = abs(a)
            if a<=len(A) and A[a-1]>=0: A[a-1] *= -1
        
        for i, a in enumerate(A):
            if a>0: return i+1
        
        return len(A)+1


# Time Complexity: O(N), Space Complexity: O(N)
class Solution:
    def firstMissingPositive(self, A: List[int]) -> int:
        if not A or max(A)<=0: return 1
        
        l = []
        for a in A:
            if a>0: l.append(a)
                
        if min(l)!=1: return 1
        else:
            cnt = 2
            while cnt in l:
                cnt += 1
            return cnt