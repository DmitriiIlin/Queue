class Stack:
#Реализация класса Стек
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop(-1)

    def push(self, value):
        if len(self.stack)>0:
            #print("insert")
            return self.stack.insert(0,value)
        else:
            #print("append")
            return self.stack.append(value)

    def peek(self):
        if len(self.stack) <= 0:
            return None
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)
    
    def print_stack(self):
        for i in range(0,len(self.stack)):
            print(self.stack[i])

"""
Реализация класса Queue с помошью двух элементов класса Stack
"""
class Queue_stack(Stack):

    def __init__(self):
        #Инициализация класса
        self.a=Stack()
        self.b=Stack()
    
    def enqueue(self,value):
        # Заполнение первого стека
        self.a.push(value)
    
    def dequeue(self):
        #Выдача элемента из второго стека
        while self.a.size()>0:
            element_for_secont_stack=self.a.pop()
            self.b.push(element_for_secont_stack)
        element_for_delete=self.b.pop()
        while self.b.size()>0:
            element_for_first_stack=self.b.pop()
            self.a.push(element_for_first_stack)
        return element_for_delete
    
    def size_queue(self):
        #Возвращает кол-во элементов в очереди 
        return self.a.size()



Z=Queue_stack()
for i in range (0,10):
    Z.enqueue(i*2)
while Z.size_queue()>0:
    D=Z.dequeue()
    print(D)    