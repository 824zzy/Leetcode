class Solution:
    def isHappy(self, n: int) -> bool:
        stop = []
        
        while n != 1:
            stop.append(n)
            
            n = sum(int(i)**2 for i in str(n))
            
            if n == 1:
                return True
            
            elif n in stop:
                return False
        
        return True