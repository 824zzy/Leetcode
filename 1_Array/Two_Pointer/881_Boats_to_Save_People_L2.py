# Google
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        people.sort(reverse=True)
        n = len(people)
        l, r = 0, n-1

        while l<=r:
            if people[l]+people[r] <= limit:
                r -= 1
            l += 1
            ans += 1
        
        return ans
        