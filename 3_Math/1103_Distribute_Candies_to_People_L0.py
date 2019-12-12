class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people
        rnd = 0
        while candies>0:
            for i in range(num_people):
                if candies>rnd+i+1:
                    ans[i] += rnd+i+1
                elif candies>0:
                    ans[i] += candies
                candies -= rnd+i+1
            rnd += num_people
        return ans