""" https://leetcode.com/problems/queue-reconstruction-by-height/
greedy by sorting and inserting
1. sort the array by height from tallest to shortest
2. insert the elements into a queue
"""


class Solution:
    def reconstructQueue(self, A: List[List[int]]) -> List[List[int]]:
        A.sort(key=lambda x: (-x[0], x[1]))  # tallest -> shortest
        ans = []
        for p in A:
            ans.insert(p[1], p)
        return ans


# less optimal solution: sort the order first and then insert by height
class Solution:
    def reconstructQueue(self, A: List[List[int]]) -> List[List[int]]:
        A.sort(key=lambda x: (x[1], -x[0]))
        ans = [[-1, 0]]
        for i in range(len(A)):
            cnt = 0
            for j in range(len(ans)):
                if ans[j][0] >= A[i][0]:
                    cnt += 1
                if cnt == A[i][1]:
                    ans.insert(j + 1, A[i])
                    break
        return ans[1:]
