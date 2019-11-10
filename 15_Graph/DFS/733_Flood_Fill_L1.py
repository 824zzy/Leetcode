class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc]==newColor:
            return image
        m, n = len(image), len(image[0])
        def dfs(sr, sc, oriColor):
            if sr<0 or sr>=m or sc<0 or sc>=n or image[sr][sc]!=oriColor:
                return
            image[sr][sc] = newColor
            dfs(sr-1, sc, oriColor)
            dfs(sr+1, sc, oriColor)
            dfs(sr, sc-1, oriColor)
            dfs(sr, sc+1, oriColor)
        dfs(sr, sc, image[sr][sc])
        return image