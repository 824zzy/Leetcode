""" L2: https://leetcode.com/problems/operations-on-tree/
"""


class LockingTree:
    def __init__(self, parent: List[int]):
        self.parent = parent
        self.tree = [[] for _ in parent]
        for i, x in enumerate(parent):
            if x != -1:
                self.tree[x].append(i)
        self.locked = {}

    def lock(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked.get(num) != user:
            return False
        self.locked.pop(num)
        return True

    def upgrade(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False  # check for unlocked

        node = num
        while node != -1:
            if node in self.locked:
                break  # locked ancestor
            node = self.parent[node]
        else:
            stack = [num]
            descendant = []
            while stack:
                node = stack.pop()
                if node in self.locked:
                    descendant.append(node)
                for child in self.tree[node]:
                    stack.append(child)
            if descendant:
                self.locked[num] = user  # lock given node
                for node in descendant:
                    self.locked.pop(node)  # unlock all descendants
                return True
        return False  # locked ancestor


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
