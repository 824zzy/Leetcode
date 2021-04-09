class Solution:
    def isAlienSorted(self, A: List[str], order: str) -> bool:
        order = {c:i for i, c in enumerate(order)}
        for i in range(len(A)-1):
            if A[i+1]==A[i]: continue # ["hello","hello"]
            if A[i+1] in A[i]: return False # ["apple","app"]
            for j in range(min(len(A[i]), len(A[i+1]))):
                if order[A[i][j]]>order[A[i+1][j]]: return False
                elif order[A[i][j]]<order[A[i+1][j]]: break
        return True