""" https://leetcode.com/problems/stone-game-iv/
https://leetcode.com/problems/stone-game-iv/discuss/909373/Python-DP-solution-using-game-theory-explained
In this problems we have game with two persons, and we need to understand who is winning, if they play with optimal strategies. 
In this game at each moment of time we have several (say k) stones, and we say that it is position in our game. 
At each step, each player can go from one position to another. Let us use classical definitions:

The empty game (the game where there are no moves to be made) is a losing position.
A position is a winning position if at least one of the positions that can be obtained from this position by a single move is a losing position.
A position is a losing position if every position that can be obtained from this position by a single move is a winning position.

So, what we need to check now for position state: all positions, we can reach from it and if at least one of them is False, 
our position is winning and we can immedietly return True. If all of them are True, our position is loosing, and we return False. 
Also we return False, if it is our terminal position.
"""
class Solution:
    def winnerSquareGame(self, n):
        @lru_cache(None)
        def dfs(state):
            if state == 0: return False # losing position
            for i in reversed(range(1, isqrt(state)+1)):
                if not dfs(state - i*i): return True # wining position
            return False # losing position
        
        return dfs(n)
    
    
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(1, n+1):
            for k in range(1, int(i**0.5)+1):
                if k*k<=i and dp[i-k*k]==0:
                    dp[i] = 1
        return dp[n]