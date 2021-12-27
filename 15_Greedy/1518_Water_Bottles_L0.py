class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        cnt = 0
        ans = 0
        while numBottles:
            numBottles -= 1
            ans += 1
            cnt += 1
            if cnt%numExchange==0:
                cnt = 0
                numBottles += 1
        return ans
        
class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        ans = numBottles
        while numBottles>=numExchange:
            tmp = numBottles // numExchange 
            numBottles = numBottles % numExchange + tmp
            ans += tmp
        return ans