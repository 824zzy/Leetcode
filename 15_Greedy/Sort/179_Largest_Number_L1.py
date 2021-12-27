import functools
class Solution:
    def largestNumber(self, nums):
        ans = ''.join(sorted(map(str, nums)), key=functools.cmp_to_key(lambda x, y: int(y+x)-int(x+y)))
        return ans if ans[0]!='0' else '0'
    

    
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        l = len(str(max(nums)))
        pnums = {}
        for i in range(len(nums)):
            sn = str(nums[i])
            pnums[i] = int(sn.ljust(l, max(sn))) if len(sn)<l else int(sn)
        print(pnums)
        pnums = sorted(pnums.items(), key=lambda i:i[1], reverse=True)
        print(pnums)
        ans = ''.join([str(nums[p[0]]) for p in pnums])
        return str(int(ans))
