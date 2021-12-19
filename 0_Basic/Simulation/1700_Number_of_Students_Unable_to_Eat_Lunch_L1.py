""" https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
simulate the assignment and count those students who will eat
"""
class Solution:
    def countStudents(self, stu: List[int], san: List[int]) -> int:
        ans = len(stu)
        while stu and san:
            pre = stu.copy()
            while stu[0]!=san[0]:
                stu.append(stu.pop(0))
                if stu==pre: return ans
            else:
                stu.pop(0)
                san.pop(0)
            ans -= 1
        return ans