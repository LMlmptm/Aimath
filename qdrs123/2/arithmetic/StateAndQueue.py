# -*- coding:utf-8 -*-

#用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
class Solution:
    def __init__(self):
        self.stateA=State(-1,[],0)
        self.stateB=State(-1,[],0)

    def push(self, node):
        if self.stateA.state_element_size==0:
            # 栈A没有数据，那肯定栈B必须有数据，
             while self.stateB.state_element_size>0:
                 #这样的画栈A没有数据，那栈B就得pop数据到栈A中
                 self.stateA.Push(self.stateB.Pop())

        self.stateA.Push(node)

    def pop(self):
        if self.stateB.state_element_size==0:
            while self.stateA.state_element_size>0:
                self.stateB.Push(self.stateA.Pop())
        return self.stateB.Pop()


class State():

    def __init__(self,top,state_list,state_element_size):
        self.top=top
        self.state_list=state_list
        self.state_element_size=state_element_size

    def Push(self,node):
        self.state_list.append(node)
        self.top=len(self.state_list)-1
        self.state_element_size+=1

    def Pop(self):
        if self.state_element_size==0:
            return -1
        new_state_list=self.state_list.pop()
        self.top = len(self.state_list) - 1
        self.state_element_size-=1
        return new_state_list



