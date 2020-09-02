class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        b_num = bin(num)
        return (len(b_num)-2)%2!=0 and b_num[2]=='1' and '1' not in b_num[3:]