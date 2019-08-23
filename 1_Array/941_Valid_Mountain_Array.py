""" Google
"""
# 19-8-23: straightforward solution
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        
        top_ind = A.index(max(A))
        if top_ind==0 or top_ind==len(A)-1:
            return False
        
        left, right = A[:top_ind], A[top_ind:]
        if not left or not right:
            return False
        elif left!=sorted(left) or right!=sorted(right, reverse=True) or len(left)!=len(set(left)) or len(right)!=len(set(right)):
            return False
        else:
            return True

# 19-8-23: O(n) better solution
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        i = 0
        while i<len(A)-1 and A[i]<A[i+1]:
            i += 1
        
        if i==0 or i==len(A)-1:
            return False
        
        while i<len(A)-1:
            if A[i]<=A[i+1]:
                return False
            i+=1
        return True
        