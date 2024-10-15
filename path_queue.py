class PathQueue:
    """
    Queue used to follow a set path
    """
    def __init__(self):
        self._queue = []
        
    def enqueue(self, value) -> None:
        self._queue.append(value)
        
    def dequeue(self):
        """
        returns first item in the queue
        and reinserts to the back of the queue
        """
        if len(self._queue) > 0:
            item = self._queue.pop(0)
            self.enqueue(item)
        else:
            raise IndexError("Path is Empty")
            return
        return item
        
    def is_empty(self) -> bool:
        if len(self._queue) == 0:
            return True
        else:
            return False
        
    def clear_queue(self) -> None:
        self._queue.clear()