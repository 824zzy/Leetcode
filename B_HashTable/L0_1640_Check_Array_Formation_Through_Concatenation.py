"""
Hashmap for distinct number nature
"""


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        pieces = {p[0]: p for p in pieces}
        dummy = []
        for a in arr:
            if a in pieces:
                dummy += pieces[a]
        return dummy == arr


"""
String search solution
"""


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        arr = "".join([str(a) for a in arr])
        pieces = ["".join([str(s) for s in p]) for p in pieces]
        for p in pieces:
            if p not in arr:
                return False
        return True
