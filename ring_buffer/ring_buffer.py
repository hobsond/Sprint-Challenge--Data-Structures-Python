class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.current = 0
    
    def __len__(self):
        return len(self.storage)
    

    def append(self, item):
        if len(self) != self.capacity:
            self.storage.append(item)
        else:
            if self.current >= self.capacity:
                self.current = 0 
            self.storage[self.current] = item
            self.current += 1
    
    

    def get(self):
        return self.storage
        
ad = RingBuffer(3)

ad.append(1)
ad.append(2)
ad.append(3)
ad.append(4)
ad.append(5)
ad.append(7)
ad.append(1)

print(ad.get())