"""
Реализация класса Queue (очередь, Fifo), элемент очереди реализован через элементы класса Node
"""
class Node:

    def __init__(self, v):
        #Инициализация класса Node
        self.value = v
        self.next = None

class Queue:

    def __init__(self):
        #Инициализация класса Queue
        self.head = None
        self.tail = None 

    def enqueue(self, item):
        # Добывление элемента в конец очереди 
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def dequeue(self):
        # Выдача элемента из головы списка
        if self.head==0:
            return None
        else: 
            node=self.head
            self.head=node.next
            return node

    def size(self):
        # Метод определяет размер очереди
        node=self.head
        l=0
        while node is not None:
            l+=1
            node=node.next
        return l 
    
    def print(self):
        #Печать очереди
        node=self.head
        while node!=None:
            print(node.value,'output print all nodes')
            node=node.next

def circle_queue(N,M=0):
    # Ф-ция создает цикическую очередь. Параметр N кол-во элементов в очереди, M кол-во единиц сдвига. 
    a=Queue()
    for i in range(0,N):
        input_node=Node(int(input("input integer ")))
        a.enqueue(input_node)
    print("##Initial Queue##")
    a.print()
    print("##End##")
    for i in range(0,M):
        if M>=0:
            node_for_insert=a.dequeue()
            value_for_insert=node_for_insert.value
            a.enqueue(Node(value_for_insert))
        else:
            print("Shift should be >=0")
    print("Result")
    a.print()
    print("-----")



circle_queue(4,5)



        




   