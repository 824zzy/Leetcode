# Math: record items with same sum indexes
class Solution:
    def findDiagonalOrder(self, A: List[List[int]]) -> List[int]:
        ans, idxs = [], collections.defaultdict(list)
        for i_idx, i in enumerate(A):
            for j_idx, j in enumerate(i):
                idxs[i_idx+j_idx] += [j]
        for i, v in enumerate(idxs.values()):
            if i%2!=0: ans.extend(v)
            elif i%2==0: ans.extend(v[::-1])
        return ans


# Simulation
def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
	if not matrix: return
	s, i, j, m, n, d, tf = [], 0, 0, len(matrix), len(matrix[0]), 1, True
	for _ in range(m*n):
		s.append(matrix[i][j])
		if tf and j == n-1: 
			i += 1
			d *= -1
			tf = False  
		elif tf and i == 0: 
			j += 1
			d *= -1
			tf = False                              
		elif not tf and i == m-1: 
			j += 1
			d *= -1
			tf = True
		elif not tf and j == 0:
			i += 1
			d *= -1
			tf = True                
		else:
			i -= d
			j += d
	return s