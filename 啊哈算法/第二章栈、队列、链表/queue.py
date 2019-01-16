
# 《啊哈！ 算法》书上代码的python实现
class Queue():
    def __init__(self):
        self.data = [None for _ in range(100)]
        self.head = None
        self.tail = None


# 一般的队列的实现，不是很完全
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue1():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self,data):
        node = Node(data)
        if self.head is None and self.tail is None:
            self.head = node
        else:
            self.tail.next = node
    
    def dequeue(self):
        if self.head is None and self.tail is None:
            return None
        result = self.head.data
        self.head = self.head.next
        return result
    
    

if __name__ == "__main__":
    q = Queue()
    q.head = 0
    q.tail = 0
    for i in range(9):
        x = int(input('请输入一个数：'))
        q.data[i] = x
        q.tail += 1
    
    while q.head < q.tail:
        print("{}".format(q.data[q.head]))
        q.head += 1
        q.data[q.tail] = q.data[q.head]
        q.tail += 1
        q.head += 1





        