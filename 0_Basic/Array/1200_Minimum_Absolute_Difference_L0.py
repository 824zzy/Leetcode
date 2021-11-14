class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        dis = float('inf')
        ans = []
        for i in range(len(arr)-1):
            dis = min(abs(arr[i]-arr[i+1]), dis)
        for i in range(len(arr)-1):
            if abs(arr[i]-arr[i+1])==dis:
                ans.append([arr[i], arr[i+1]])
        return ans