class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 0
        self.data = [0] * n

    def insert(self, id: int, value: str) -> List[str]:
        id -= 1
        self.data[id] = value
        if id>self.ptr: 
            return []
        while self.ptr<len(self.data) and self.data[self.ptr]:
            self.ptr += 1
        return self.data[id:self.ptr]