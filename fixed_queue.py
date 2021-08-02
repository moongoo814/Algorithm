#-*- coding: cp949 -*-
#-*- coding: utf-8 -*-

from typing import Any

class FixedQueue:

    class empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: Any) -> None:
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity

    def __len__(self) -> int:
        return self.no
    
    def is_empty(self) -> bool:
        return self.no <= 0

    def is_full(self) -> bool:
        return self.no >= self.capacity

    def enqueue(self, x: Any) -> None:
        if self.is_full():
            raise FixedQueue.full
        self.que[self.rear] = x
        self.rear += 1 
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0

    def dequeue(self) -> Any:
        if self.is.empty():
            raise FixedQueue.empty
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x
