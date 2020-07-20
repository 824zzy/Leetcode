from collections import OrderedDict
class Solution:
    def intToRoman(self, num: int) -> str:
        nums2str = OrderedDict()
        nums2str[1000] = 'M'
        nums2str[900] = 'CM'
        nums2str[500] = 'D'
        nums2str[400] = 'CD'
        nums2str[100] = 'C'
        nums2str[90] = 'XC'
        nums2str[50] = 'L'
        nums2str[40] = 'XL'
        nums2str[10] = 'X'
        nums2str[9] = 'IX'
        nums2str[5] = 'V'
        nums2str[4] = 'IV'
        nums2str[1] = 'I'
        
        ans = ''
        for k, v in nums2str.items():
            while num//k != 0:
                num -= k
                ans += v
        return ans