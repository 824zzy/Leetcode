class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        moves = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5], 
                 3: [0, 4], 4: [1, 3, 5], 5: [2, 4]}
        state = ''.join([str(b) for b in board[0]+board[1]])
        start = state.index('0')
        seen = set()
        queue = [[start, state, 0]]
        while queue:
            for _ in range(len(queue)):
                cur, state, steps = queue.pop(0)
                if state=='123450': return steps
                elif state in seen: continue
                else:
                    seen.add(state)
                    for nxt in moves[cur]:
                        tmp = list(state)
                        tmp[cur], tmp[nxt] = tmp[nxt], tmp[cur]
                        queue.append([nxt, ''.join(tmp), steps+1])
        return -1