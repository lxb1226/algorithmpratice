
# python链表的一般实现，# 《啊哈！ 算法》书上用c语言实现的，实在是不想看
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Link():
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def insert(self,data):
        node = Node(data)
        if self.head == None:
            self.head.next = node
        temp = self.head
        while temp.next:
            temp = temp.next
        node = temp.next

    def search(self,x):
        if self.head == None:
            return "链表为空"
        temp = self.head
        while temp:
            if temp.data == x:
                return "找到了"
            else:
                temp = temp.next
        return "没找到"
    
    def delete(self,x):
        if self.head == None:
            return False
        prev = Node(-1) 
        curr = self.head
        while curr:
            if curr.data == x:
                prev.next = curr.next
                return "已经删除"
            else:
                curr = curr.next
                prev = prev.next

        return "没有找到元素"

    
        
            


                
        
            
        

        

