
# 栈的一般实现，不完全
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.top = None
    
    def enstack(self,data):
        node = Node(data)
        node.next = self.top
        self.top = node

    def destack(self):
        if self.top == None:
            return None
        result = self.top
        self.top = self.top.next
        return result

if __name__ == "__main__":

    # 《啊哈！ 算法》书上代码的python实现
    a = input('请输入一个字符串')
    s = [None for _ in range(101)]
    length = len(a)
    mid = length//2
    
    top = 0
    for i in range(mid):
        top += 1
        s[top] = a[i]
        
    if length % 2 == 0:
        next = mid 
    else:
        next = mid + 1

    for i in range(next,length):
        if a[i] != s[top]:
            break
        top -= 1
    if top == 0:
        print("是回文串")
    else:
        print("不是回文串")
    


