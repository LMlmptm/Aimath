
###青蛙跳台阶问题
1、一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

&nbsp;&nbsp;&nbsp;&nbsp;　假设只有一级台阶，则总共只有一种跳法；

　　假设有两级台阶，则总共有两种跳法；

　　假设有n级台阶，那么第一步就要分为跳一步和跳两步：

　　跳一步，那么接下来就是跳n-1；

　　跳两步，那么接下来就是跳n-2；

　　所以，总数可以认为是f(n-1)+f(n-2)。

```python

class Solution:
    # 　一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
    def jumpFloorII(self, number):
        # write code here
        if number == 0:
            return 0
        if number in (1, 2):
            return number

        # 1 1 2 3 5
        step1,step2 = 1,2

        while number > 2:
            # 跳下一级台阶的情况
            ret = step1 + step2
            # 赋值，累加的效果，将上一次跳的情况都统一复制给step1，step2
            step1, step2 = step2, ret
            number -= 1
        return ret

```

2、一只青蛙一次可以跳上1级台阶，也可以跳上2级......它也可以跳上n阶。求该青蛙跳上一个n级的台阶总共有多少种跳法。

分析：

　　相比之前的跳台阶，这次可以从任意台阶跳上n级，所以总体来看与上一个问题差不多，只不过递归公式应该是各个台阶之和再加上直接跳上去的情况，
所以总数应该是f(n-1)+f(n-2)+f(n-3)+...+f(2)+f(1)=2**n-1。

```python

    class Solution:
        def jumpFloorII(self, number):
            # write code here
            if number == 0:
                return 0
            #这样的结果的是通过算法规律找出来的
            return 2 ** (number - 1)


```






###2个栈实现队列的push和pop

&nbsp;&nbsp;&nbsp;&nbsp;思路是用两个栈A和B，A是队列的正序存储，B栈是队列的倒序存储。队列和栈A栈B的示意图如下所示：
<p>
<img src="https:#img-blog.csdnimg.cn/20190605191332913.png" width="76" height="126">
<img src="https:#img-blog.csdnimg.cn/20190605191515691.png" width="76" height="126">
<img src="https:#img-blog.csdnimg.cn/20190605191413809.png" width="76" height="126">
</p>

&nbsp;&nbsp;&nbsp;&nbsp;在队列Push时的操作为：将数据直接Push进栈A中；在队列Pop时将数据从B中Pop
意思就是这样，队列A push数据，那队列B就得pop数据
在做这两个操作的前提是栈A和栈B中都保持着当前队列中的元素。因此，当对A和B进行Push和Pop操作之前，我们都需要从对方栈中倒着载入数据，具体代码如下：

```python

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


```