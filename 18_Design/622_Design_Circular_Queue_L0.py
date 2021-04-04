class MyCircularQueue:
    def __init__(self, k: int):
        self.Q = []
        self.k = k
        
    def enQueue(self, value: int) -> bool:
        if len(self.Q)<self.k: 
            self.Q.append(value)
            return True
        else: return False
        
    def deQueue(self) -> bool:
        if self.Q:
            self.Q.pop(0)
            return True
        else: return False
        
    def Front(self) -> int:
        if self.Q: return self.Q[0]
        else: return -1

    def Rear(self) -> int:
        if self.Q: return self.Q[-1]
        else: return -1

    def isEmpty(self) -> bool:
        return len(self.Q)==0

    def isFull(self) -> bool:
        return len(self.Q)==self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()