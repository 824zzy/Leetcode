class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        self.seen = set()
        def dfs(arr, idx):
            if idx>=len(arr) or idx<0 or idx in self.seen:
                return False
            if arr[idx]==0:
                return True
            self.seen.add(idx)
            return dfs(arr, idx+arr[idx]) or dfs(arr, idx-arr[idx])
        return dfs(arr, start)