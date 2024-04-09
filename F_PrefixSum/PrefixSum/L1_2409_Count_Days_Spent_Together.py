""" https://leetcode.com/problems/count-days-spent-together/
1. find the maximum and minimum date
2. calculate the number of days between the maximum and minimum date by prefix sum
"""
from header import *


class Solution:
    def countDaysTogether(
            self,
            arriveAlice: str,
            leaveAlice: str,
            arriveBob: str,
            leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        prefix = list(accumulate(days, initial=0))
        start_m, start_d = str(max(arriveAlice, arriveBob)).split('-')
        end_m, end_d = str(min(leaveAlice, leaveBob)).split('-')
        start_m, start_d, end_m, end_d = int(
            start_m), int(start_d), int(end_m), int(end_d)

        return max(0, (prefix[end_m - 1] + end_d) -
                   (prefix[start_m - 1] + start_d) + 1)

# another implementation


class Solution:
    def countDaysTogether(
            self,
            arriveAlice: str,
            leaveAlice: str,
            arriveBob: str,
            leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        prefix = list(accumulate(days, initial=0))
        start_m, start_d = str(max(arriveAlice, arriveBob)).split('-')
        end_m, end_d = str(min(leaveAlice, leaveBob)).split('-')

        start_m, start_d, end_m, end_d = int(
            start_m), int(start_d), int(end_m), int(end_d)
        if start_m == end_m:
            return max(end_d - start_d + 1, 0)
        elif start_m > end_m:
            return 0
        else:
            ans = days[start_m] - start_d + 1
            for m in range(int(start_m) + 1, int(end_m)):
                ans += days[m]
            ans += end_d
            return ans


"""
"08-15"
"08-18"
"08-16"
"08-19"
"10-01"
"10-31"
"06-01"
"12-31"
"09-01"
"10-19"
"06-19"
"10-20"
"""
