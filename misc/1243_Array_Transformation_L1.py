# array, 
class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        while 1:
            currL = arr[:]
            for i in range(1, len(arr)-1):
                if arr[i]<arr[i-1] and arr[i]<arr[i+1]:
                    currL[i] += 1
                if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                    currL[i] -= 1
            if currL==arr:
                break
            else:
                arr = currL
        return currL