# 单向链表

class Node(object):
    '''结点类'''
    def __init__(self,elem):
        self.Elem = elem
        self.Next = None
     
    

class SingleLinkList(object):
    '''单项链表类'''
    def __init__(self,node = None):
        self.__head = node
        

    def is_empty(self):
        pass

    def lenth(self):
        '''返回长度'''
        pass

    def travel(self):
        '''遍历打印'''
        pass

    def add(self):
        '''头插法'''
        pass
    def append(self):
        '''尾插法'''
        pass
    def insert(self):
        '''按位置插入'''
        pass
    def remove(self):
        '''删除指定位置元素'''
        pass 
    def search(self):
        '''搜索元素'''
        pass

        

def main():
    print("执行main()主函数")
    node1 = Node(200)
    print(node1)
    sll = SingleLinkList(node1)
    print(sll.__head.Elem)


if (__name__ == '__main__'):
    main()