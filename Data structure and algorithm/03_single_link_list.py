# 单向链表

class Node(object):
    '''结点类'''
    def __init__(self,elem):
        self.Elem = elem
        self.Next = None

class SingleLinkList(object):
    '''单项链表类'''
    def __init__(self,node= None):
        self.__head =node
        

    def is_empty(self):
        """判断链表是否为空"""
        if self.__head == None:
            return True
        return False

    def lenth(self):
        '''返回长度'''
        # 结点数量
        nodeCount = 0
        
            # 索引器“指针”
        curr = self.__head
           
        while curr != None:
            nodeCount += 1
            curr = curr.Next
        
        return nodeCount

    def travel(self):
        '''遍历打印'''
        curr = self.__head
        while curr != None:
            print(curr.Elem)
            curr = curr.Next
            # print(curr.Elem)

    def add(self,node):
        '''头插法'''
        # 为空是
        if self.__head == None:
            self.__head =node
        # 已经存在结点的时候，从头部插入
        else:
            node.Next = self.__head
            self.__head = node

    def append(self,node):
        '''尾插法'''
        curr = self.__head
        while curr != None:
            # 如果next为None说明是最后一个节点了
            if curr.Next== None:
                curr.Next= node
                break
            else:
                curr = curr.Next
    def insert(self,pos,node  ):
        '''按位置插入'''

        curr = self.__head
        # 指向当前位置前一个的游标
        pre = None
        # 当前节点的位置
        currIndex = 0
        # 总节点数
        nodeCount = 0
        # 这里不去使用length是为了不增加时间复杂度
        
        
        while curr != None:
            nodeCount += 1
            currIndex = nodeCount-1
            pre = curr
            curr = curr.Next
            if (pos == currIndex):
                pre.Next= node
                node.Next = curr

    def remove(self):
        '''删除指定位置元素'''
        pass 
    def search(self):
        '''搜索元素'''
        pass

        

def main():

    # 实例化单项列表
    sll = SingleLinkList()
    #实例化结点1 node1

    
    # 头插法添加元素
    sll.add(Node(200))
    sll.add(Node(100))

    print(f"插入新节点前，该链表内结点数量为：{sll.lenth()}")
    sll.travel()
    # sll.append(Node(400))
    sll.insert(1,Node(300))
    print(f"插入新节点后，该链表内结点数量为：{sll.lenth()}")
    sll.travel()


<<<<<<< HEAD
def main():
    print("执行main()主函数")
    node1 = Node(200)
    print(node1)
    sll = SingleLinkList(node1)
    print(sll.__head.Elem)


if (__name__ == '__main__'):
=======
if __name__ == "__main__":
>>>>>>> 635b94f3299ac970f48e2067085515be107d6a43
    main()