class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        seen = {}
        for i in range(len(graph)):
            if i not in seen:
                queue  = [(i, 1)]
                while queue:
                    node, color = queue.pop(0)
                    if node in seen:
                        if color == seen[node]: continue
                        else: return False
                    seen[node] = color
                    for nei in graph[node]:
                        queue.append((nei, color * (-1)))   
        return True