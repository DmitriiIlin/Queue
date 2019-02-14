"""
Реализация класса Queue (очередь, Fifo), элемент очереди реализован через элементы класса Node
"""

class Queue:

    def __init__(self):
        #Инициализация класса Queue
        self.Queue_list=[] 

    def enqueue(self, item):
        # Добывление элемента в конец очереди 
        self.Queue_list.append(item)

    def dequeue(self):
        # Выдача элемента из головы списка
        if len(self.Queue_list)==0:
            return None
        else:
            Queue_element=self.Queue_list.pop(-len(self.Queue_list))
            return Queue_element

    def size(self):
        # Метод определяет размер очереди
        s=len(self.Queue_list)
        return s 
    
    def print(self):
        #Печать очереди
        s=len(self.Queue_list)
        for i in range(0,s):
            print(self.Queue_list[i],'output print all nodes')
            s+=1

S=Queue()
for i in range(0,10):
    S.enqueue(i**2)
S.print()
print("#####")
for i in range(0,5):
    S.dequeue()
S.print()
"""
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
"""



        




   