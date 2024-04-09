class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        tmpB = B
        A = sorted(A)
        B = sorted(B)
        l, r = 0, len(A) - 1
        M = defaultdict(list)
        for a in A:
            if l > r:
                break
            if a > B[l]:
                M[B[l]].append(a)
                l += 1
            else:
                M[B[r]].append(a)
                r -= 1

        ans = []
        for b in tmpB:
            a = M[b].pop(0)
            ans.append(a)
        return ans
