class Solution:
    def numberOfSteps (self, num: int) -> int:
        cnt = 0
        while num:
            if num%2!=0:
                num -= 1
            else:
                num /= 2
            cnt += 1
        return cnt