class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.order = [] # track order of elements
        self.queue = []

    def append(self, item):
        # is queue less than capacity append to order and queue
        if len(self.queue) < self.capacity:
            self.order.append(item)
            self.queue.append(item)
        
        else:
            # if order greater than 0 pop next element in order
            if len(self.order) > 0:
                next = self.order.pop(0)

                # look for next element to be replaced in list 
                for x in range(self.capacity):
                    if next == self.queue[x]:
                        self.queue.pop(x)
                        self.queue.insert(x, item)

                        # append new item to order list
                        self.order.append(item)
            

    def get(self):
        return self.queue