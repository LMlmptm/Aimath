# !/usr/bin/python
# -*- coding: UTF-8 -*-
# import sys
# 1.在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序
# ，每一列都按照从上到下递增的顺序排序。请完成一个函数，
# # 输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
# class Solution:
#     def Find(self, target, array):
#         n = len(array)
#         flag = False
#         for i in range(n):
#             if target in array[i]:
#                 flag = True
#                 break
#         return flag
#
# array = [9, 8, 7], [6, 5, 4], [3, 2, 1]
# target = 5
# s = Solution()
# print(s.Find(target,array))
#
#
# 2.请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
# class Solution:
#     def Replace(self, target):
#         target = target.replace(' ',"%20")
#         return target
#
# target = 'We Are Happy'
# s = Solution()
# print(s.Replace(target))
#
#
# 3.输入一个链表，按链表从尾到头的顺序返回一个ArrayList
# 利用栈
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     # 返回从尾部到头部的列表值序列，例如[1,2,3]
#     def printListFromTailToHead(self, listNode):
#         l = []
#         for i in listNode:
#             l.insert(0,i)
#         return l
#
# a = [1,2,3]
# ss = Solution()
# print (ss.printListFromTailToHead(a))
#
#
# 4输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列 pre = {1,2,4,7,3,5,6,8}
# 和中序遍历序列tin = {4,7,2,1,5,3,8,6}，则重建二叉树并返回。
# 二叉树三种遍历方式
# https:#www.pianshen.com/article/7106254596/
#
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         #这里踩坑 不要再None后面加,
# class Solution:
#     # 返回构造的TreeNode根节点
#     def reConstructBinaryTree(self, pre, tin):
#
#         if len(pre) == 0 or len(tin) == 0:
#             print "is over"
#             return None
#
#         root = TreeNode(pre[0])
#         print (pre[0])
#         for i in range(0, len(tin) ,1):
#             if pre[0] == tin[i]:
#                 root.left =  self.reConstructBinaryTree(pre[1:i+1],tin[0:i])
#                 root.right = self.reConstructBinaryTree(pre[i+1:len(pre)],tin[i+1:len(tin)])
#                 break
#         return root
#
# pre = [1,2,4,7,3,5,6,8]
# tin = [4,7,2,1,5,3,8,6]
# ss = Solution()
# root = ss.reConstructBinaryTree(pre,tin)
# print root
#
#
# 5.用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型
# 队列先进先出的  栈是先进后出的
#
# -*- coding:utf-8 -*-
# class Solution:
#     def __init__(self):
#         self.s1 = []
#         self.s2 = []
#     def push(self, node): #插入直接往一个栈里插入
#         self.s1.append(node)
#         print self.s1
#
#     def pop(self):
#
#         if len(self.s1) == 0:
#             return None
#         while len(self.s1) > 0:
#             self.s2.append(self.s1.pop())
#         node = self.s2.pop()
#
#         while len(self.s2) > 0:
#             self.s1.append(self.s2.pop())
#         return node
#
# ss = Solution()
# ss.push(1)
# ss.push(2)
# ss.push(3)
# ss.push(4)
# ss.push(5)
# print ss.pop()
# ss.push(6)
#
# 6把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# 输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
# NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
#
# 理解为需要输出该数组左边他大的一个元素
#
# -*- coding:utf-8 -*-
# class Solution:
#     def minNumberInRotateArray(self, rotateArray):
#         if len(rotateArray) == 0:
#             return 0
#
#         res_min = rotateArray[0];
#         for i in range(len(rotateArray)-1):#这里循环到从0开始倒数第二个元素
#             j = i + 1
#             if rotateArray[i] > rotateArray[j] and rotateArray[j] < res_min:
#                 res_min = rotateArray[j]
#         return res_min
#
# ss = Solution()
# rotateArray = [3,4,5,1,2]
# print  ss.minNumberInRotateArray(rotateArray)
#
# 7.大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
# n<=39
# -*- coding:utf-8 -*-
# class Solution:
#     def Fibonacci(self, n):
#         if n == 0:
#             return  0
#         if n == 1:
#             return 1
#         return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)
#
# ss = Solution()
# for i in range(10):
#     print ss.Fibonacci(i)
#
# 8.一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）
# -*- coding:utf-8 -*-
# class Solution:
#     def jumpFloor(self, number):
#         if number == 1:
#             return 1
#
#         if number == 2:
#             return 2
#
#         return self.jumpFloor(number - 1) + self.jumpFloor(number - 2)
#
# ss = Solution()
# for i in range(1,10,1):
#     print ss.jumpFloor(i)
#
#
# -*- coding:utf-8 -*-
# 动态规划
# class Solution:
#     def jumpFloor(self, n):
#         # write code here
#         res = [1, 1, 2]
#         while len(res) <= n:
#             # 负数是从后往前取数组
#             res.append(res[-1] + res[-2])
#         return res[n-1]
#
# ss = Solution()
# print ss.jumpFloor(4)
#
# 9.一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
# 相当于之前所有的出来的结果的和
# class Solution:
# #     def jumpFloorII(self, number):
# #         res = [1,1,2]
# #         while len(res) < number:
# #             t = 0
# #             for i in res:
# #                 t = t + res[i]
# #             res.append(t)
# #         return res[number-1]
# # ss = Solution()
# # print ss.jumpFloorII(4)
#
# class Solution:
#     def jumpFloorII(self, number):
#         if number == 1:
#             return 1
#
#         if number == 2:
#             return 2
#         return  2 * self.jumpFloorII(number - 1)
# ss = Solution()
# print ss.jumpFloorII(4)
#
#
# 10.我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
# 比如n=3时，2*3的矩形块有3种覆盖方法
#
# 横着放相当于青蛙走楼梯一样的，下面只能也横着放，就相当于走一步两步了
#
#
# -*- coding:utf-8 -*-
# class Solution:
#     def rectCover(self, number):
#         if number == 1:
#             return 1
#         if number == 2:
#             return 2
#         if number >= 3:
#             return self.rectCover(number - 1) + self.rectCover(number - 2)
#
# ss = Solution()
# out = ss.rectCover(3)
# print out
#
# 11.输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
# 把一个整数减去1在与它本身做与运算，就会把该整数最右边一个1变成0。那么一个整数的二进制有多少个1，就可以进行多少次这样的操作就可以了。
# 举个例子：一个二进制数1100，从右边数起第三位是处于最右边的一个1。减去1后，第三位变成0，它后面的两位0变成了1，而前面的1保持不变，
# 因此得到的结果是1011.我们发现减1的结果是把最右边的一个1开始的所有位都取反了。这个时候如果我们再把原来的整数和减去1之后的结果做与运算，
# 从原来整数最右边一个1那一位开始所有位都会变成0。如1100&1011=1000。
# & 运算 只有两个1才是1  否则都是0   1001 & 0111 = 0000
# -*- coding:utf-8 -*-
# class Solution:
#     def NumberOf1(self, n):
#         count = 0
#         while n > 0:
#             count = count + 1
#             n = n & (n-1)
#         return count
#
# ss =  Solution()
# print ss.NumberOf1(0)
#
# 12.给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
# 保证base和exponent不同时为0
# 这也相当于动态规划
# -*- coding:utf-8 -*-
# class Solution:
#     def Power(self, base, exponent):
#         if base == 0 or exponent == 0:
#             return False
#         total = 1
#
#         while exponent > 0:
#             total = total * base
#             exponent = exponent - 1
#
#         return total
#
#
# ss =  Solution()
# print  ss.Power(2,1)
#
#
# 13.输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
# 所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
# -*- coding:utf-8 -*-
# class Solution:
#     def reOrderArray(self, array):
#         ji = []
#         ou = []
#         for i in array:
#             if i % 2 == 0:
#                 ou.append(i)
#             else:
#                 ji.append(i)
#
#
#         return ji + ou
#
#
# temp = [3,5,6,8,1,7]
#
# ss = Solution()
# print ss.reOrderArray(temp)
#
#
# 14,输入一个链表，输出该链表中倒数第k个结点。
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 说下解题思路，我们可以获取到最后一个结点  那么先让一个指针走k-1可结点  在走一个指针
# 然后两个指针同时往后走  当第一个指针走到最后的时候 那么第二个指针正好走到k的地方
#
# class Solution:
#     def FindKthToTail(self, head, k):
#      firstNode = head
#      step = k
#      while step > 0:
#         firstNode = firstNode.next
#        step -= 1
#
#
#
#
# 15.输入一个链表，反转链表后，输出新链表的表头。
#
# 看了一下好像没有python的非递归实现。思路很简单：1->2->3->4->5，
# 遍历链表，把1的next置为None，2的next置为1，以此类推，5的next置为4。
# 得到反转链表。需要考虑链表只有1个元素的情况。图中有具体的每步迭代的思路，
# 最后输出pre而不是cur是因为最后一次迭代后cur已经指向None了，而pre是完整的反向链表。
#
# 用三个指针分别指向当前、前一个、后一个，每次循环使当前节点的next指针指向前一个（原指向后一个），然后依次向后平移三个指针（注意移动的先后次序）。
# 其实可以节省一个指向新链表头的指针，循环体如下便可：
# 最终需要返回pre，因为cur已经变成原链表中最后的那个空指针了。
#
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# 1  2  3
# 2  3  nil
# nil   1   2
# class Solution:
#     # 返回ListNode
#     def ReverseList(self, pHead):
#         if pHead.next == None:
#             return pHead
#
#         pre = None
#         cur = pHead
#         sec = pHead.next
#         while cur:
#             cur.next = pre
#             pre = cur
#             cur = sec
#             sec = cur.next
#         return sec
#
# 15.输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
# 1,3,5,7
# 2,4,6,8
#
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# class Solution:
#     # 返回合并后列表
#     def Merge(self, pHead1, pHead2):
#         head = []
#         while pHead1 or pHead2:
#             if pHead1 <= pHead2 or pHead2 == None:
#                 head.insert(pHead1)
#                 pHead1 = pHead1.next
#             else:
#                 head.insert(pHead2)
#                 pHead2 = pHead2.next
#         return head
#
# 16.输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
#
# / *思路：参考剑指offer
# 1、首先设置标志位result = false，因为一旦匹配成功result就设为true，
# 剩下的代码不会执行，如果匹配不成功，默认返回false
# 2、递归思想，如果根节点相同则递归调用DoesTree1HaveTree2（），
# 如果根节点不相同，则判断tree1的左子树和tree2是否相同，
# 再判断右子树和tree2是否相同
# 3、注意null的条件，HasSubTree中，如果两棵树都不为空才进行判断，
# DoesTree1HasTree2中，如果Tree2为空，则说明第二棵树遍历完了，即匹配成功，
# tree1为空有两种情况（1）如果tree1为空 & & tree2不为空说明不匹配，
# （2）如果tree1为空，tree2为空，说明匹配。
#
# * /
#
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class Solution:
#     def HasSubtree(self, pRoot1, pRoot2):
#         # write code here
#         if not pRoot1 or not pRoot2:
#             return False
#         return self.is_subtree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right,
#                                                                                                           pRoot2)
#
#     def is_subtree(self, A, B):
#         if not B:
#             return True
#         if not A or A.val != B.val:
#             return False
#         return self.is_subtree(A.left, B.left) and self.is_subtree(A.right, B.right)
#
# 17.操作给定的二叉树，将其变换为源二叉树的镜像
# 个人认为解题思路就是递归，将所有的子节点进行交换，然后继续下层
#
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class Solution:
#     # 返回镜像树的根节点
#     def Mirror(self, root):
#         if root != None:
#             root.left,root.right = root.right,root.left
#             self.Mirror(root.left)
#             self.Mirror(root.right)
#
# 18.输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵：
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
#
#
# 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
#
# a='python'
# b=a[::-1] 取反
# print(b) #nohtyp
#
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#
# # -*- coding:utf-8 -*-
# class Solution:
#     # matrix类型为二维列表，需要返回列表
#     def printMatrix(self, matrix):
#         # write code here
#         res = []
#         while matrix:
#             res += matrix.pop(0)  #pop为取栈 默认是取出最后一个维度的数据 index=-1
#             matrix = list(map(list, zip(*matrix)))[::-1]      map(list, zip(*matrix)是将二维数组进行xy轴的逆转  然后在外层上下翻转[::-1]
#         return res
#
# ss = Solution()
# print ss.printMatrix(matrix)
#
#
# 19.定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
# 注意：保证测试中不会当栈为空的时候，对栈调用pop()或者min()或者top()方法。
#
# 看到这个问题, 我们最开始可能会想, 添加一个成员变量用于保存最小元素, 每次压栈时如果压栈元素比当前最小元素更小, 就更新最小元素.
# 但是这样会有一个问题, 如果最小元素被弹出了呢, 如何获得下一个最小元素呢? 分析到这里可以发现, 仅仅添加一个成员变量存放最小元素是不够的,
# 我们需要在最小元素弹出后还能得到次小元素, 次小的弹出后, 还要能得到次次小的.
# 因此, 用另一个栈来保存这些元素是再合适不过的了. 我们叫它最小元素栈.
# 每次压栈操作时, 如果压栈元素比当前最小元素更小, 就把这个元素压入最小元素栈,
# 原本的最小元素就成了次小元素. 同理, 弹栈时, 如果弹出的元素和最小元素栈的栈顶元素相等, 就把最小元素的栈顶弹出.
#
# -*- coding:utf-8 -*-
# class Solution:
#     def __init__(self):
#         self.stack = []
#         self.minStack = []
#     def push(self, node):
#         self.zhan.append(node)
#         if not self.minStack or node < self.minStack[-1]:
#             self.minStack.append(node)
#     def pop(self):
#         if self.stack[-1] == self.minStack[-1]:
#             self.minStack.pop()
#         self.stack.pop()
#
#     def top(self):
#         return self.stack[-1]
#     def min(self):
#         return self.minStack[-1]
#
#
# 20.输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。
# 例如序列1,2,3,4,5是某栈的压入顺序
# ，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
# 但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
# -*- coding:utf-8 -*-
# class Solution:
#
#     def IsPopOrder(self, pushV, popV):
#         stack中存入pushV中取出的数据
#         stack=[]
#         while popV:
#             # 如果第一个元素相等，直接都弹出，根本不用压入stack
#             if pushV and popV[0]==pushV[0]
#                 popV.pop(0)
#                 pushV.pop(0)
#             #如果stack的最后一个元素与popV中第一个元素相等，将
#             elif stack and stack[-1]==popV
#                 stack.pop()
#                 popV.pop(0)
#             # 如果pushV中有数据，压入stack
#             elif pushV:
#                 stack.append(pushV.pop(0))
#             # 上面情况都不满足，直接返回false。
#             else:
#                 return False
#         return True
#
#
# pushV = [5,4,3,2,1]
# popV = [4,5,3,2,1]
# pushV = pushV[::-1]
# print pushV
#
# 21.从上往下打印出二叉树的每个节点，同层节点从左至右打印。
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class Solution:
#     # 返回从上到下每个节点值列表，例：[1,2,3]
#     def PrintFromTopToBottom(self, root):
#         if  not root:
#             return []
#         # write code here
#         ls=[root]
#         result=[]
#         while len(ls)>0:
#             node=ls.pop(0)
#             result.append(node.val)
#             if node.left!=None:
#                 ls.append(node.left)
#             if node.right!=None:
#                 ls.append(node.right)
#         return result
#
# python：使用两个数组，ls存储数组，ls相对值，把每一层的变量都放进去，开始就是循环数组的左右子例程，然后放在后面，结果存储数组的值用于最后返回打印
#
#
# 22.输入一个非空整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。(细分析)
# 二叉搜索树的规则是左节点都比跟节点小  右节点都比根节点大
# -*- coding:utf-8 -*-
# python:后序遍历 的序列中，最后一个数字是树的根节点 ，数组中前面的数字可以分为两部分：
# 第一部分是左子树节点 的值，都比根节点的值小；第二部分 是右子树 节点的值，都比 根 节点 的值大，
# 后面用递归分别判断前后两部分 是否 符合以上原则
#
# class Solution:
#     def VerifySquenceOfBST(self, sequence):
#         # write code here
#         if sequence==None or len(sequence)==0:
#             return False
#         length=len(sequence)
#         root=sequence[length-1]
#         # 在二叉搜索 树中 左子树节点小于根节点
#         for i in range(length):
#             if sequence[i]>root:
#                 break
#         # 二叉搜索树中右子树的节点都大于根节点
#         for j  in range(i,length):
#             if sequence[j]<root:
#                 return False
#         # 判断左子树是否为二叉树
#         left=True
#         if  i>0:
#             left=self.VerifySquenceOfBST(sequence[0:i])
#         # 判断右子树是否为二叉树
#         right=True
#         if i<length-1:
#             right=self.VerifySquenceOfBST(sequence[i:-1])
#         return left and right
#
#
# 23.输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
#
#
#
# 24.输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针random指向一个随机节点）
# ，请对此链表进行深拷贝，并返回拷贝后的头结点。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
#
# 思路  1.把复制的节点连接到相应节点的后面
#  2.把复制节点的随机节点变成下一个节点来赋值
#  3.最后按照基数偶数拆分节点
# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
# class Solution:
#  # 返回 RandomListNode
#  def Clone(self, pHead):
#     if not pHead:
#        return None
#
#     dummy = pHead
#
#     # first step, N' to N next
#     while dummy:
#        dummynext = dummy.next
#        copynode = RandomListNode(dummy.label)
#        copynode.next = dummynext
#        dummy.next = copynode
#        dummy = dummynext
#
#     dummy = pHead
#
#     # second step, random' to random'
#     while dummy:
#        dummyrandom = dummy.random
#        copynode = dummy.next
#        if dummyrandom:
#           copynode.random = dummyrandom.next
#        dummy = copynode.next
#
#     # third step, split linked list
#     dummy = pHead
#     copyHead = pHead.next
#     while dummy:
#        copyNode = dummy.next
#        dummynext = copyNode.next
#        dummy.next = dummynext
#        if dummynext:
#           copyNode.next = dummynext.next
#        else:
#           copyNode.next = None
#        dummy = dummynext
#
#     return copyHead
#
# 25.输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
#
# 26.题目描述
# 输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
# 输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
# -*- coding:utf-8 -*-
#
# 按字典顺序
# 打印所有组合
# -*- coding:utf-8 -*-
# class Solution:
#     def Permutation(self, ss):
#         # write code here
#         if len(ss)==0: return []
#         lst = list(ss)
#         lst.sort()
#         res = []
#         for i in range(0, len(ss)):
#             if i > 0 and lst[i]==lst[i-1]:
#                 continue
#             temp = self.Permutation(''.join(lst[:i]) + ''.join(lst[i+1:]))
#             if len(temp)==0:
#                 res.append(lst[i])
#             for str in temp:
#                 res.append(lst[i]+str)
#         return res
#
# ss = 'aabbb'
# a = Solution()
# print a.Permutation(ss)
#
# 附加  全排列
# 将整组数中的所有的数分别与第一个数交换，这样就总是在处理后n-1个数的全排列。
# import copy
# class Solution:
#     def Permutation(self, res, ss, idx):
#     if idx >= len(ss):
#        a = copy.deepcopy(ss)
#        res.append(a)
#        return
#     for i in range(idx, len(ss)):
#        ss[i],ss[idx] = ss[idx],ss[i]
#        self.Permutation(res,ss,idx+1)
#        ss[i],ss[idx] = ss[idx],ss[i]
# res = []
# ss = [1,2,3,4]
# a = Solution()
# a.Permutation(res,ss,0)
# print res
#
#
# 27.数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}
# 。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
# -*- coding:utf-8 -*-
# class Solution:
#     def MoreThanHalfNum_Solution(self, numbers):
#     halfNum = int(len(numbers)/2)
#     Calmap = {}
#     for i in range(len(numbers)):
#        if numbers[i] in Calmap.keys():
#           Calmap[numbers[i]] += 1
#
#           if Calmap[numbers[i]] > halfNum:
#              return numbers[i]
#        else:
#           Calmap[numbers[i]] = 1
#     return 0
#
#
# ss = Solution()
# num = [1,2,3,2,2,2,5,4,2]
# print ss.MoreThanHalfNum_Solution(num)
#
#
# 28.输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
# 方法一：蒂姆排序
# -*- coding:utf-8 -*-
# class Solution:
#  def GetLeastNumbers_Solution(self, tinput, k):
#     # write code here
#     if tinput == [] or k > len(tinput):
#        return []
#     tinput.sort()
#     return tinput[: k]
#
#
# #方法二：快速排序
# # -*- coding:utf-8 -*-
# class Solution:
#  def GetLeastNumbers_Solution(self, tinput, k):
#     # write code here
#     def quick_sort(lst):
#        if not lst:
#           return []
#        pivot = lst[0]
#        left = quick_sort([x for x in lst[1:] if x < pivot])
#        right = quick_sort([x for x in lst[1:] if x >= pivot])
#        return left + [pivot] + right
#
#     if tinput == [] or k > len(tinput):
#        return []
#     tinput = quick_sort(tinput)
#     return tinput[: k]
#
#
# #方法三：归并排序
# # -*- coding:utf-8 -*-
# class Solution:
#  def GetLeastNumbers_Solution(self, tinput, k):
#     # write code here
#     def merge_sort(lst):
#        if len(lst) <= 1:
#           return lst
#        mid = len(lst) # 2
#        left = merge_sort(lst[: mid])
#        right = merge_sort(lst[mid:])
#        return merge(left, right)
#
#     def merge(left, right):
#        l, r, res = 0, 0, []
#        while l < len(left) and r < len(right):
#           if left[l] <= right[r]:
#              res.append(left[l])
#              l += 1
#           else:
#              res.append(right[r])
#              r += 1
#        res += left[l:]
#        res += right[r:]
#        return res
#
#     if tinput == [] or k > len(tinput):
#        return []
#     tinput = merge_sort(tinput)
#     return tinput[: k]
#
#
# #方法四：堆排序
# # -*- coding:utf-8 -*-
# class Solution:
#  def GetLeastNumbers_Solution(self, tinput, k):
#     # write code here
#     def siftup(lst, temp, begin, end):
#        if lst == []:
#           return []
#        i, j = begin, begin * 2 + 1
#        while j < end:
#           if j + 1 < end and lst[j + 1] > lst[j]:
#              j += 1
#           elif temp > lst[j]:
#              break
#           else:
#              lst[i] = lst[j]
#              i, j = j, 2 * j + 1
#        lst[i] = temp
#
#     def heap_sort(lst):
#        if lst == []:
#           return []
#        end = len(lst)
#        for i in range((end # 2) - 1, -1, -1):
#           siftup(lst, lst[i], i, end)
#        for i in range(end - 1, 0, -1):
#           temp = lst[i]
#           lst[i] = lst[0]
#           siftup(lst, temp, 0, i)
#        return lst
#
#     if tinput == [] or k > len(tinput):
#        return []
#     tinput = heap_sort(tinput)
#     return tinput[: k]
#
#
# #方法五：冒泡排序
# # -*- coding:utf-8 -*-
# class Solution:
#  def GetLeastNumbers_Solution(self, tinput, k):
#     # write code here
#     def bubble_sort(lst):
#        if lst == []:
#           return []
#        for i in range(len(lst)):
#           for j in range(1, len(lst) - i):
#              if lst[j - 1] > lst[j]:
#                 lst[j - 1], lst[j] = lst[j], lst[j - 1]
#        return lst
#
#     if tinput == [] or k > len(tinput):
#        return []
#     tinput = bubble_sort(tinput)
#     return tinput[: k]
#
#
# #方法六：直接选择排序
# # -*- coding:utf-8 -*-
# class Solution:
#  def GetLeastNumbers_Solution(self, tinput, k):
#     # write code here
#     def select_sort(lst):
#        if lst == []:
#           return []
#        for i in range(len(lst) - 1):
#           smallest = i
#           for j in range(i, len(lst)):
#              if lst[j] < lst[smallest]:
#                 smallest = j
#           lst[i], lst[smallest] = lst[smallest], lst[i]
#
#        return lst
#
#     if tinput == [] or k > len(tinput):
#        return []
#     tinput = select_sort(tinput)
#     return tinput[: k]
#
#
# #方法七：插入排序
# # -*- coding:utf-8 -*-
# class Solution:
#  def GetLeastNumbers_Solution(self, tinput, k):
#     # write code here
#     def Insert_sort(lst):
#        if lst == []:
#           return []
#        for i in range(1, len(lst)):
#           temp = lst[i]
#           j = i
#           while j > 0 and temp < lst[j - 1]:
#              lst[j] = lst[j - 1]
#              j -= 1
#           lst[j] = temp
#        return lst
#
#     if tinput == [] or k > len(tinput):
#        return []
#     tinput = Insert_sort(tinput)
#     return tinput[: k]
#
#
# 29.HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:
# 在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。
# 但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},
# 连续子向量的最大和为8(从第0个开始,到第3个为止)。给一个数组，返回它的最大连续子序列的和，
# 你会不会被他忽悠住？(子向量的长度至少是1)
#
# -*- coding:utf-8 -*-
# class Solution:
#     def FindGreatestSumOfSubArray(self, array):
#         # write code here
#         max_sum, cur_sum = -0xffffff, 0
#         for i in array:
#             if cur_sum <= 0:
#                 cur_sum = i
#             else:
#                 cur_sum += i
#             if cur_sum > max_sum:
#                 max_sum = cur_sum
#         return max_sum
#
#
# arr = [-6,-3,-2,-7,-15,-2,-2,-2]
# ss = Solution()
# print ss.FindGreatestSumOfSubArray(arr)
#
# 30.求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
# 为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,
# 但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,
# 可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
#
# 思路 ，转换成字符串然后继续查找
#
# -*- coding:utf-8 -*-
# class Solution:
#     def NumberOf1Between1AndN_Solution(self, n):
#      def find1Count(n):
#         base_str = str(n)
#         count = 0
#         while base_str.find('1') != -1:
#            base_str = base_str[base_str.find('1') + 1:]
#            count += 1
#         return count
#
#      totalCount = 0
#      for i in range(0,n+1,1):
#         totalCount += find1Count(i)
#      return totalCount
#
#
# arr = 100000
# ss = Solution()
# print ss.NumberOf1Between1AndN_Solution(arr)
#
# 31.输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
# 打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，
# 则打印出这三个数字能排成的最小数字为321323。
#
# -*- coding:utf-8 -*-
# class Solution:
#     def PrintMinNumber(self, numbers):
#      if not numbers:
#         return ""
#      #这里将两个加起来做个排序，大于的取前者 小于的取后者
#      lmb = lambda n1, n2: int(str(n1) + str(n2)) - int(str(n2) + str(n1))
#      array = sorted(numbers, cmp=lmb)
#      return ''.join([str(i) for i in array])
#
#
# -*- coding:utf-8 -*-
# class Solution:
#  def PrintMinNumber(self, numbers):
#     # write code here
#     temp = [str(x) for x in sorted(numbers, cmp=self.f_cmp)]
#     return ''.join(temp)
#
#  def f_cmp(self, a, b):
#     if str(a) + str(b) < str(b) + str(a):
#        return -1
#     elif str(a) + str(b) > str(b) + str(a):
#        return 1
#     else:
#        return 0
#
# arr = [3,32,321]
# ss = Solution()
# print ss.PrintMinNumber(arr)
#
#
# 32.把只包含质因子2、3和5的数称作丑数（Ugly Number）。
# 例如6、8都是丑数，但14不是，因为它包含质因子7。
# 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
#
# 通俗易懂的解释：
# 首先从丑数的定义我们知道，一个丑数的因子只有2,3,5，那么丑数p = 2 ^ x * 3 ^ y * 5 ^ z，
# 换句话说一个丑数一定由另一个丑数乘以2或者乘以3或者乘以5得到，那么我们从1开始乘以2,3,5，
# 就得到2,3,5三个丑数，在从这三个丑数出发乘以2,3,5就得到4，6,10,6，9,15,10,15,25九个丑数，
# 我们发现这种方***得到重复的丑数，而且我们题目要求第N个丑数，这样的方法得到的丑数也是无序的。那么我们可以维护三个队列：
# 其实就是在他们三个队列里面找最小，找到了给他加1，继续找最小输出
# -*- coding:utf-8 -*-
# class Solution:
#     def GetUglyNumber_Solution(self, index):
#         # write code here
#         if index<1:
#             return 0
#         data=[1]
#         index2=0
#         index3=0
#         index5=0
#         indexitter=0
#         while indexitter<index:
#             indexitter+=1
#             d= min(data[index2]*2,data[index3]*3,data[index5]*5)
#             data.append(d)
#             if data[index2]*2==d:
#                 index2+=1
#             if data[index3]*3==d:
#                 index3+=1
#             if data[index5]*5==d:
#                 index5+=1
#         return data[index-1]
#
# idx = 5
# ss = Solution()
# print ss.GetUglyNumber_Solution(idx)
#
# 33.在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,
# 并返回它的位置, 如果没有则返回 -1（需要区分大小写）.（从0开始计数）
# class Solution:
#  def getLocationAppareOnce(self,str):
# import collections
#
# def firstChar(ss):
#  #这里使用的是排序的字典，根据传入的顺序进行输出，到时候在遍历一遍排序字典，找到count==1的
#  #就可以了
#  dicts = collections.OrderedDict()
#  if len(ss) <= 0:
#     return -1
#
#  if len(ss) == 1:
#     return ss
#
#  for key in ss:
#     if key in dicts:
#        dicts[key] += 1
#     else:
#        dicts[key] = 1
#
#  for key in dicts:
#     if dicts[key] == 1:
#        return key
#  return -1
# print firstChar("aabbccddeeff")
#
# 34.在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
# 输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
# 输入描述:
# 题目保证输入的数组中没有的相同的数字
#
# 数据范围：
#
#  对于%50的数据,size<=10^4
#
#  对于%75的数据,size<=10^5
#
#  对于%100的数据,size<=2*10^5
#
# 归并排序的改进，把数据分成前后两个数组(递归分到每个数组仅有一个数据项)，
# 合并数组，合并时，出现前面的数组值array[i]大于后面数组值array[j]时；则前面
# 数组array[i]~array[mid]都是大于array[j]的，count += mid+1 - i
# 参考剑指Offer，但是感觉剑指Offer归并过程少了一步拷贝过程。
# 还有就是测试用例输出结果比较大，对每次返回的count mod(1000000007)求余
#
# data = [1,2,3,4,5,6,7,0]
# # -*- coding:utf-8 -*-
# count = 0
# class Solution:
#     def InversePairs(self, data):
#         global count
#         def MergeSort(lists):
#             global count
#             if len(lists) <= 1:
#                 return lists
#             num = int( len(lists)/2 )
#             left = MergeSort(lists[:num])
#             right = MergeSort(lists[num:])
#             r, l=0, 0
#             result=[]
#             while l<len(left) and r<len(right):
#                 if left[l] < right[r]:
#                     result.append(left[l])
#                     l += 1
#                 else:
#                     result.append(right[r])
#                     r += 1
#                     count += len(left)-l
#             result += right[r:]
#             result += left[l:]
#             return result
#         MergeSort(data)
#         return count%1000000007
#
# ss = Solution()
# print ss.InversePairs(data)
#
#
# 35.输入两个链表，找出它们的第一个公共结点。
# （注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）
#   a   b   c       d    b   f
#
# 直接找或者用第一次遍历来确定二者的长度，然后用短的从开头开始往下遍历，找到相同val证明取到相同元素了
#
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#  def FindFirstCommonNode(self, head1, head2):
#     # write code here
#     list1 = []
#     list2 = []
#     node1 = head1
#     node2 = head2
#     while node1:
#        list1.append(node1.val)
#        node1 = node1.next
#     while node2:
#        if node2.val in list1:
#           return node2
#        else:
#           node2 = node2.next
#
# 36. 统计一个数字在排序数组中出现的次数
# 这题太简单了  感觉啥都没问
# -*- coding:utf-8 -*-
# class Solution:
#     def GetNumberOfK(self, data, k):
#         # write code here
#         count = len(data)
#         i = 0
#         for j in range(count):
#             if data[j] == k:
#                 i += 1
#         return i
#
#
# 37.输入一棵二叉树，求该树的深度。
# 从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
# class TreeNode:
#  def __init__(self, x):
#     self.val = x
#     self.left = None
#     self.right = None
#
#
# 使用递归方法
# class Solution:
#     def TreeDepth(self, pRoot):
#         # write code here
#         # 使用层次遍历
#         # 当树为空直接返回0
#         if pRoot is None:
#             return 0
#         # 方法2：使用递归
#         # 如果该树只有一个结点，它的深度为1.如果根节点只有左子树没有右子树，
#         # 那么树的深度为左子树的深度加1；同样，如果只有右子树没有左子树，
#         # 那么树的深度为右子树的深度加1。如果既有左子树也有右子树，
#         # 那该树的深度就是左子树和右子树的最大值加1.
#         count = max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1
#         return count
#
#
#
#
# 38.输入一棵二叉树，判断该二叉树是否是平衡二叉树。
# 在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 一看还是递归，平衡二叉树的规则是左边节点永远小于根节点  右边节点必须大于根节点
# 并且左右节点的高低差必须小于1
# class Solution:
#     def IsBalanced_Solution(self, pRoot):
#      # write code here
#      return self.balanceHeight(pRoot) >= 0
#
#     def balanceHeight(self, root):
#      #子节点不存在，给0
#      if root is None:
#         return 0
#      left = self.balanceHeight(root.left)
#      right = self.balanceHeight(root.right)
#
#     #不满足条件,高低差大于1了，直接返回
#      if (left < 0 or right < 0 or abs(left - right) > 1):
#         return -1
#      return max(left, right) + 1
#
# 39.一个整型数组里除了两个数字之外，其他的数字都出现了两次。
# 请写程序找出这两个只出现一次的数字。
# [1,2,3,4,5,3,2,1]
#
# 异或 相同为0  不同为1
# 首先：位运算中异或的性质：两个相同数字异或=0，一个数和0异或还是它本身。
#
# 当只有一个数出现一次时，我们把数组中所有的数，依次异或运算，最后剩下的就是落单的数，因为成对儿出现的都抵消了。
#
# 依照这个思路，我们来看两个数（我们假设是AB）出现一次的数组。我们首先还是先异或，剩下的数字肯定是A、B异或的结果，
# 这个结果的二进制中的1，表现的是A和B的不同的位。我们就取第一个1所在的位数，假设是第3位，接着把原数组分成两组，
# 分组标准是第3位是否为1。如此，相同的数肯定在一个组，因为相同数字所有位都相同，而不同的数，肯定不在一组。
# 然后把这两个组按照最开始的思路，依次异或，剩余的两个结果就是这两个只出现一次的数字。
#
#
# # -*- coding:utf-8 -*-
# from collections import Counter
#
#
# class Solution:
#  # 返回[a,b] 其中ab是出现一次的两个数字
#  def FindNumsAppearOnce(self, array):
#     # write code here
#     return list(self.dc(array, 0, len(array) - 1))
#
#  def dc(self, array, start, end):
#     res = set()
#     if start > end:
#        return res
#     if start == end:
#        return set(array[start:end])
#
#     spl = (start + end) / 2
#
#     s1 = self.dc(array, start, spl)
#     s2 = self.dc(array, spl + 1, end)
#
#     return s1.union(s2).difference(s1.intersection(s2))
#
#
# #intersection 返回交集  s1 和s2的
#
# array = [1,2,3,4,5,3,2,1]
# ss = Solution()
# print ss.FindNumsAppearOnce(array)
#
#
# 40.小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
# 但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
# 没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
# 现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
# 输出描述:
# 输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
# 滑动窗口技术,连续数字计算是 参考1到100的和怎么算， 如果满足条件把分母扩大  不满足条件扩大分子，直到所有条件都满足
#
# class Solution:
#     def FindContinuousSequence(self, tsum):
#     small = 1
#     big = 2
#     result = []
#
#     while small < big:
#        count = (small + big)* (big - small + 1 )/2
#        if count == tsum:
#           result.append(range(small,big+1))
#           small += 1
#        elif count < tsum:
#           big += 1
#        else:
#           small += 1
#     return     result
#
# ss = Solution()
# print ss.FindContinuousSequence(100)
#
#
# 40.输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
# 对应每个测试案例，输出两个数，小的先输出。
# 还是用滑动窗口做
#
# tsum = 5
# array = [1,2,3,4,5,6,7]
#
# # -*- coding:utf-8 -*-
# #解决方案，利用滑动窗口技术
# class Solution:
#     def FindNumbersWithSum(self, array, tsum):
#  small = 0
#  big = 1
#  calX = 0
#  temp = []
#
#  while array[small] < array[big]:
#     if (array[small] + array[big]) == tsum:
#        if calX == 0:
#           temp = []
#           temp.append(array[small])
#           temp.append(array[big])
#           small += 1
#        elif calX > array[small] * array[big]:
#           temp = []
#           temp.append(array[small])
#           temp.append(array[big])
#           small += 1
#     elif array[small] + array[big] < tsum:
#        big += 1
#     else:
#        small += 1
#  return temp
#
# ss = Solution()
# print ss.FindNumbersWithSum(array,tsum)
#
#
# 41.汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，
# 就是用字符串模拟这个指令的运算结果。对于一个给定的字符序列S，请你把其循环左移K位后的序列输出
# 例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
# -*- coding:utf-8 -*-
#
# s = "abcXYZdef"
#
# class Solution:
#     def LeftRotateString(self, s, n):
#     ls = list(s)
#     for i in range(n):
#        ls.append(ls[0])
#        ls.pop(0)
#     return ''.join(ls)
#
# 或者直接return  s[n:]  + s[:n]
#
# ss = Solution()
# print ss.LeftRotateString(s,3)
#
#
# 42.牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，
# 写些句子在本子上。同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，
# 但却读不懂它的意思。例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，
# 正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？
#
#
# 先把字符串切割成一个数组 然后在倒序插入空格输出
# 方数组里，然后倒序输出拼接
#
# s = 'student. a am I'
# # -*- coding:utf-8 -*-
# 方法1自实现
# class Solution:
#     def ReverseSentence(self, s):
#  ls = str.split(s,' ')
#  answer = ''
#  for idx in range(len(ls)-1,-1,-1):
#     answer = answer + ''.join(ls[idx]) + ' '
#  return answer
# ss = Solution()
# print ss.ReverseSentence(s)
#
# 方法2
# -*- coding:utf-8 -*-
# class Solution:
#     def ReverseSentence(self, s):
#         # write code here
#         l=s.split(' ')
#         return ' '.join(l[::-1])
#
# 43.LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...
# 他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！
# ！“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小
# 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),
# “So Lucky!”。LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何，
#  如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0。
#
# 先找出癞子的量，然后在用排列后的两个做差，肯定小于等于该顺子最大减最小的值，否则不是顺子
# import numpy as np
# numbers = [0,3,4,5,0]
# a = np.array(numbers)
# print np.sum(a == 0)
#
# # -*- coding:utf-8 -*-
# class Solution:
#     def IsContinuous(self, numbers):
#         # write code here
#         if not numbers:
#             return numbers
#         new_list = [i for i in numbers if i > 0]
#         new_list.sort()
#         if len(new_list)==1:
#             return True
#         n = 0
#         for j in range(len(new_list)-1):
#             if (new_list[j+1] - new_list[j]) > 0:
#                 n += (new_list[j+1] - new_list[j])
#             else:
#                 return False
#         if n <= 4:
#             return True
#         else:
#             return False
#
#
# 44.每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。
# HF作为牛客的资深元老,自然也准备了一些小游戏。其中,有个游戏是这样的:首先,让小朋友们围成一个大圈。
# 然后,他随机指定一个数m,让编号为0的小朋友开始报数。每次喊到m-1的那个小朋友要出列唱首歌,
# 然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,从他的下一个小朋友开始
# 继续0...m-1报数....这样下去....直到剩下最后一个小朋友,可以不用表演,
# 并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)
# 如果没有小朋友，请返回-1
#
# -*- coding:utf-8 -*-
# class Solution:
#     def LastRemaining_Solution(self, n, m):
#         # write code here
#         if not m or not n:
#             return -1
#         #将小朋友列表化
#         res = range(n)
#         i = 0
#         #只要小朋友大于1，则一直循环，每次弹出的小朋友是 （m-1 加 当前小朋友的i）取模当前的小朋友
#         while len(res)>1:
#             i = (m+i-1)%len(res)
#             res.pop(i)
#         return res[0]
#
#
# 45.求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）
# 啥都不让用  直接想递归
# 止损条件就是到n
# -*- coding:utf-8 -*-
# class Solution:
#  def __init__(self):
#     self.sum = 0
#
#  def Sum_Solution(self, n):
#     if n <= 0:
#        return self.sum
#     self.sum += n
#     n -=1
#     self.Sum_Solution(n)
#     return self.sum
#
# ss = Solution()
# print ss.Sum_Solution(5)
#
# 46.写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
#
# 首先看十进制是如何做的： 5+7=12，三步走
# 第一步：相加各位的值，不算进位，得到2。
# 第二步：计算进位值，得到10. 如果这一步的进位值为0，那么第一步得到的值就是最终结果。
#
# 第三步：重复上述两步，只是相加的值变成上述两步的得到的结果2和10，得到12。
#
# 同样我们可以用三步走的方式计算二进制值相加： 5-101，7-111 第一步：相加各位的值，不算进位，得到010，二进制每位相加就相当于各位做异或操作，101^111。
#
# 第二步：计算进位值，得到1010，相当于各位做与操作得到101，再向左移一位得到1010，(101&111)<<1。
#
# 第三步重复上述两步， 各位相加 010^1010=1000，进位值为100=(010&1010)<<1。
#      继续重复上述两步：1000^100 = 1100，进位值为0，跳出循环，1100为最终结果。
#
# -*- coding:utf-8 -*-
# class Solution:
#     def Add(self, num1, num2):
#     #简单方法
#     return sum([num1,num2])
#
#
# 47.将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0
# 输入描述:
# 输入一个字符串,包括数字字母符号,可以为空
# 输出描述:
# 如果是合法的数值表达则返回该数字，否则返回0
# 示例1
# 输入
# +2147483647
# 1a33
# 输出
# 2147483647
# 0
#
# 首先需要将字符串切割成数组，然后从最低位开始循环找，如果是数字那么将原数组*10 并且加上该数字
# 如果遇到符号，则直接放到最前面，在循环的话，或者遇到特殊符号的话报错
# -*- coding:utf-8 -*-
# s = '-12334'
# class Solution:
#     def StrToInt(self, s):
#     ls = list(s)
#     tNum = 0
#     for i in range(1, len(ls), 1):
#        if ls[i] < '0' or ls[i] > '9':
#           return 0
#        else:
#           if tNum == 0:
#              tNum = int(ls[i])
#           else:
#              tNum = tNum*10 + int(ls[i])
#
#     if ls[0] >= '0' and ls[0] <= '9':
#        tNum = tNum * 10 + int(ls[0])
#     elif ls[0] == '+':
#        tNum = tNum
#     elif ls[0] == '-':
#        tNum = -tNum
#     return tNum
# ss = Solution()
# print ss.StrToInt(s)
#
#
# 48.在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
# 请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
# -*- coding:utf-8 -*-
# class Solution:
#     这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
#     函数返回True/False
#
#
# 思路，完全22比较(两个for循环)可以比出来，但是方法比较笨
#     def duplicate(self, numbers, duplication):
#     for i in range(0,len(numbers)):
#        for j in range(0,len(numbers)):
#           if i == j:
#              continue
#           elif numbers[i] == numbers[j]:
#              duplication[0] = numbers[i]
#              return True
#     return False
#
#
# numbers = [2, 3, 1, 0, 2, 5, 3]
# duplication = []
# ss = Solution()
# print ss.duplicate(numbers,duplication)
#
# #python包实现，有点投机取巧
# # -*- coding:utf-8 -*-
# import collections
# class Solution:
#     def duplicate(self, numbers, duplication):
#         # write code here
#         flag=False
#         c=collections.Counter(numbers)
#         for k,v in c.items():
#             if v>1:
#                 duplication[0]=k
#                 flag=True
#                 break
#         return flag
#
# 49.给定一个数组A[0, 1, ..., n - 1], 请构建一个数组B[0, 1, ..., n - 1],
# 其中B中的元素B[i] = A[0] * A[1] * ... * A[i - 1] * A[i + 1] * ... *
#  A[n - 1]。不能使用除法。（注意：规定B[0] = A[1] * A[
# 2] * ... * A[n - 1]，B[n - 1] = A[0] * A[1] * ... * A[n - 2];）
# 再理解！！！！！！！
# https:#www.nowcoder.com/profile/645151/codeBookDetail?submissionId=1516453
# 其实是一个矩阵
#
# B[i] = A[0] * A[1] * ... * A[i - 1] * A[i + 1] * ... *A[n - 1]
# B[n - 1] = A[0] * A[1] * ... * A[n - 2]
# B[0] = A[1] * A[2] * ... * A[n - 1]
#
# -*- coding:utf-8 -*-
# class Solution:
#     def multiply(self, A):
#         # write code here
#         if not A:
#             return []
#         # 计算前面一部分
#         num = len(A)
#         B = [None] * num
#         B[0] = 1
#         B[i] = A[0]* B[0]
#         for i in range(1, num):
#             B[i] = B[i-1] * A[i-1]
#         # 计算后面一部分
#         # 自下而上
#         # 保留上次的计算结果乘本轮新的数,因为只是后半部分进行累加，所以设置一个tmp,能够保留上次结果
#         tmp = 1
#         for i in range(num-2, -1, -1):
#             tmp *= A[i+1]
#             B[i] *= tmp
#         return B
#
#
# ss = Solution()
# print ss.multiply([1,2,3,4,5])
#
#
# 50.请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'
# 表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
# 在本题中，匹配是指字符串的所有字符匹配整个模式。
# 例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
#
# 这里要
#
# class Solution:
#     # s, pattern都是字符串
#     def match(self, s, pattern):
#         # 如果s与pattern都为空，则True
#         if len(s) == 0 and len(pattern) == 0:
#             return True
#         # 如果s不为空，而pattern为空，则False
#         elif len(s) != 0 and len(pattern) == 0:
#             return False
#         # 如果s为空，而pattern不为空，则需要判断
#         elif len(s) == 0 and len(pattern) != 0:
#             # pattern中的第二个字符为*，则pattern后移两位继续比较
#             if len(pattern) > 1 and pattern[1] == '*':
#                 return self.match(s, pattern[2:])
#             else:
#                 return False
#         # s与pattern都不为空的情况
#         else:
#             # pattern的第二个字符为*的情况
#             if len(pattern) > 1 and pattern[1] == '*':
#                 # s与pattern的第一个元素不同，则s不变，pattern后移两位，相当于pattern前两位当成空
#                 if s[0] != pattern[0] and pattern[0] != '.':
#                     return self.match(s, pattern[2:])
#                 else:
#                     # 如果s[0]与pattern[0]相同，且pattern[1]为*，这个时候有三种情况
#                     # pattern后移2个，s不变；相当于把pattern前两位当成空，匹配后面的
#                     # pattern后移2个，s后移1个；相当于pattern前两位与s[0]匹配
#                     # pattern不变，s后移1个；相当于pattern前两位，与s中的多位进行匹配，因为*可以匹配多位
#                     return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern)
#             # pattern第二个字符不为*的情况
#             else:
#                 if s[0] == pattern[0] or pattern[0] == '.':
#                     return self.match(s[1:], pattern[1:])
#                 else:
#                     return False
#
# 51.请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
# 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
# 万能的
#
# -*- coding:utf-8 -*-
# class Solution:
#     # s字符串
#     def isNumeric(self, s):
#         try :
#             p = float(s)
#             return True
#         except:
#             return False
#
# ss = Solution()
# print ss.isNumeric("1.2.3")
#
# 52.请实现一个函数用来找出字符流中第一个只出现一次的字符。
# 例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
# 当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
# 输出描述:
# 如果当前字符流没有存在出现一次的字符，返回#字符。
#
# 利用一个字典记录出现数量，然后获取时候遍历每个元素，得到第一个元素后比较就完了
#
# -*- coding:utf-8 -*-
# class Solution:
#     # 返回对应char
#     def __init__(self):
#         self.s=''
#         self.dict1={}
#     def FirstAppearingOnce(self):
#         # write code here
#         for i in self.s:
#             if self.dict1[i]==1:
#                 return i
#         return '#'
#     def Insert(self, char):
#         # write code here
#         self.s=self.s+char
#         if char in self.dict1:
#             self.dict1[char]=self.dict1[char]+1
#         else:
#             self.dict1[char]=1
#
#
# 53.给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 声明俩指针同时走,一个走一步一个走两步，如果相遇证明有环，否则有人走没了 那就是没换
# class Solution:
#  def EntryNodeOfLoop(self, pHead):
#     if pHead == None or pHead.next == None or pHead.next.next == None:
#        return None
#     low = pHead.next
#     fast = pHead.next.next
#     while low != fast:
#        if fast.next == None or fast.next.next == None:
#           return None
#        low = low.next
#        fast = fast.next.next
#     #以上证明可以相遇了
#     #以下是为了找环口
#     fast = pHead
#     while low != fast:
#        low = low.next
#        fast = fast.next
#     return fast
#
#
# 54.在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，
# 重复的结点不保留，返回链表头指针。
# 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# https:#www.nowcoder.com/practice/fc533c45b73a41b0b44ccba763f866ef?
# tpId=13&tqId=11209&rp=2&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
#
# 是可以删除的，刚开始当pHead的值为1时，
# 到达return deleteDuplication(pNode)这个地方继续往下“递”。
# 直到最后pNode指向了5那个节点，再次调用该方法，所以return了pNode，
# 也就是5这个节点本身。然后往前“归”，直到“归”到该开始调用那时，
# 到达return deleteDuplication(pNode)，所以一路返回，
# 最后返回指向5的那个PNode。所以是可以删除的
#
# class Solution:
#     def deleteDuplication(self, pHead):
#         # write code here
#         if pHead is None or pHead.next is None:
#             return pHead
#         head1 = pHead.next
#         #比较next和本身是否相同
#         if head1.val != pHead.val:
#             pHead.next = self.deleteDuplication(pHead.next)
#             return pHead
#         else:#当前节点是重复结点
#             while pHead.val == head1.val and head1.next is not None:
#                 head1 = head1.next
#             if head1.val != pHead.val:
#                 return self.deleteDuplication(head1)
#             else:#这里是报错
#                 return None
#
# 55.给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
# 注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
# class Solution:
#     def GetNext(self, pNode):
#         # write code here
#         if not pNode:
#             return pNode
#         if pNode.right:
#             left1=pNode.right
#             while left1.left:
#                    left1=left1.left
#             return left1
#         p=pNode
#         while pNode.next:
#             tmp=pNode.next
#             if tmp.left==pNode:
#                 return tmp
#             pNode=tmp
#
#
# 56.请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# class Solution:
#     def isSymmetrical(self, pRoot):
#         # write code here
#         def is_same(p1,p2):
#             if not p1 and not p2:
#                 return True
#             if (p1 and p2) and p1.val==p2.val:
#                 return is_same(p1.left,p2.right) and is_same(p1.right,p2.left)
#             return False
#
#         if not pRoot:
#             return True
#         if pRoot.left and not pRoot.right:
#             return False
#         if not pRoot.left and pRoot.right:
#             return False
#         return is_same(pRoot.left,pRoot.right)
#
#
# 57.请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
# 第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class Solution:
#     def Print(self, pRoot):
#         # write code here
#         if not pRoot:
#             return []
#         from collections import deque
#         res,tmp=[],[]
#         last=pRoot
#         q=deque([pRoot])
#         left_to_right=True
#         while q:
#             t=q.popleft()
#             tmp.append(t.val)
#             if t.left:
#                 q.append(t.left)
#             if t.right:
#                 q.append(t.right)
#             if t == last:
#                 res.append(tmp if left_to_right else tmp[::-1])
#                 left_to_right= not left_to_right
#                 tmp=[]
#                 if q:last=q[-1]
#         return res
#
#
# 58.从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class Solution:
#     # 返回二维列表[[1,2],[4,5]]
#     def Print(self, pRoot):
#         # write code here
#         if not pRoot:
#             return []
#         res=[]
#         tmp=[pRoot]
#         while tmp:
#             size=len(tmp)
#             row=[]
#             for i in tmp:
#                 row.append(i.val)
#             res.append(row)
#             for i in range(size):
#                 node=tmp.pop(0)
#                 if node.left:
#                     tmp.append(node.left)
#                 if node.right:
#                     tmp.append(node.right)
#         return res
#
# 59.请实现两个函数，分别用来序列化和反序列化二叉树
# 二叉树的序列化是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，
# 从而使得内存中建立起来的二叉树可以持久保存。序列化可以基于先序、中序、后序、
# 层序的二叉树遍历方式来进行修改，序列化的结果是一个字符串，序列化时通过
# 某种符号表示空节点（#），以 ！ 表示一个结点值的结束（value!）。
# 二叉树的反序列化是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。
# 例如，我们可以把一个只有根节点为1的二叉树序列化为"1,"，然后通过自己的函数来解析回这个二叉树
# 略
#
# 60.给定一棵二叉搜索树，请找出其中的第k小的结点。
# 例如， （5，3，7，2，4，6，8）中，按结点数值大小顺序第三小结点的值为4。
#
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class Solution:
#  # 返回对应节点TreeNode
#  def KthNode(self, pRoot, k):
#     # write code here
#     # 第三个节点是4
#     # 前序遍历5324768
#     # 中序遍历2345678
#     # 后序遍历2436875
#     # 所以是中序遍历，左根右
#     global result
#     result = []
#     self.midnode(pRoot)
#     if k <= 0 or len(result) < k:
#        return None
#     else:
#        return result[k - 1]
#
#  def midnode(self, root):
#     if not root:
#        return None
#     self.midnode(root.left)
#     result.append(root)
#     self.midnode(root.right)
#
#
# 61.如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，
# 那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
# #是整数除法  理解一下！
# -*- coding:utf-8 -*-
# class Solution:
#  def __init__(self):
#     self.data = []
#
#  def Insert(self, num):
#     # write code here
#     self.data.append(num)
#     self.data.sort()
#
#  def GetMedian(self, data):
#     # write code here
#     length = len(self.data)
#     if length % 2 == 0:
#        return (self.data[length # 2] + self.data[length # 2 - 1]) / 2.0
#     else:
#        return self.data[int(length # 2)]
#
#
#
# 62.给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，
# 那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
#  {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}，
#  {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
# -*- coding:utf-8 -*-
# class Solution:
#     def maxInWindows(self, nums, size):
#     rs = []
#     ls =  len(nums)
#     for i in range(0,(ls - size)+1,1):
#        #rs.append(max(nums[i],nums[i+1],nums[i+2]))
#        rs.append(max[i:i+size])
#     return rs
#
# num = [2,3,4,2,6,2,5,1]
# size = 3
# ss = Solution()
# print ss.maxInWindows(num,size)
#
# # -*- coding:utf-8 -*-
# class Solution:
#     def maxInWindows(self, num, size):
#         # write code here
#         if size <= 0:
#             return []
#         res = []
#         for i in xrange(0, len(num)-size+1):
#             res.append(max(num[i:i+size]))
#         return res
#
# 63.请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
# 路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
# 如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子
# 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
#
# 思考，回溯法
# -*- coding:utf-8 -*-
# class Solution:
#     def hasPath(self, matrix, rows, cols, path):
#         # write code here
#         for i in range(rows):
#             for j in range(cols):
#                 if matrix[i*cols+j] == path[0]:
#                     if self.find(list(matrix),rows,cols,path[1:],i,j):
#                         return True
#         return False
#     def find(self,matrix,rows,cols,path,i,j):
#         if not path:
#             return True
#         matrix[i*cols+j]='0'
#         if j+1<cols and matrix[i*cols+j+1]==path[0]:
#             return self.find(matrix,rows,cols,path[1:],i,j+1)
#         elif j-1>=0 and matrix[i*cols+j-1]==path[0]:
#             return self.find(matrix,rows,cols,path[1:],i,j-1)
#         elif i+1<rows and matrix[(i+1)*cols+j]==path[0]:
#             return self.find(matrix,rows,cols,path[1:],i+1,j)
#         elif i-1>=0 and matrix[(i-1)*cols+j]==path[0]:
#             return self.find(matrix,rows,cols,path[1:],i-1,j)
#         else:
#             return False
#
#
# 64.地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，
# 下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），
# 因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
#
# 思路：将地图全部放置1，遍历能够到达的点，将遍历的点置0并计数1。
# 这个思路在找前后左右相连的点很有用，例如leetcode中的海岛个数问题/最大海岛问题都可以用这种方法来改造。
#
#
# -*- coding:utf-8 -*-
# class Solution:
#     def movingCount(self, threshold, rows, cols):
#         # write code here
#         board = [[0 for _ in range(cols)] for _ in range(rows)]
#         def block(r,c):
#             s = sum(map(int,str(r)+str(c)))
#             return s>threshold
#         class Context:
#             acc = 0
#         def traverse(r,c):
#             if not (0<=r<rows and 0<=c<cols): return
#             if board[r][c]!=0: return
#             if board[r][c]==-1 or block(r,c):
#                 board[r][c]=-1
#                 return
#             board[r][c] = 1
#             Context.acc+=1
#             traverse(r+1,c)
#             traverse(r-1,c)
#             traverse(r,c+1)
#             traverse(r,c-1)
#         traverse(0,0)
#         return Context.acc
#
#
# 65.给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1），
# 每段绳子的长度记为k[0],k[1],...,k[m]。
# 请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？
# 例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
# 输入一个数n，意义见题面。（2 <= n <= 60）
#
# 递归
# 我们先定义函数f(n)
# 为把绳子剪成若干段之后的各段长度乘积的最大值.在剪第一刀的时候, 我们会有n - 1
# 种可能的选择, 也就是说剪出来的第一段绳子的长度可能为1, 2, ......n - 1.
# 因此就有了递归公式
# f(n) = max(f(i) * f(n - i)), 其中0 < i < n.
# 代码如下:
#
# 递归写法
# class Solution:
#  def cutRope(self, number):
#     # write code here
#     if number < 2:
#        return 0
#     if number == 2:
#        return 1
#     if number == 3:
#        return 2
#     return self.cutRopeCore(number)
#
#  def cutRopeCore(self, number):
#     if number < 4:
#        return number
#     max_ = 0
#     for i in range(1, number / 2 + 1):
#        max_ = max(self.cutRopeCore(i) * self.cutRopeCore(number - i), max_)
#     return max_
#
#
# # 下面介绍动态规划的解法, 接着上面的递归解法我们可以将其转换成动态规划的写法.由于这是一个从上至下的递归公式, 递归会出现很多大量不必要的计算, 一个很好的方法就是按照从下而上的顺序计算, 即:
# # 我们先得到f(2), f(3), 再得到f(4), f(5), 直到f(n).
# # 我们可以得知f(2) = 1, f(3) = 2
# # 下面就可以写我们的代码啦:
#
# # 动态规划
# class Solution:
#  def cutRope(self, number):
#     # write code here
#     if number < 2:
#        return 0
#     if number == 2:
#        return 1
#     if number == 3:
#        return 2
#     # 申请辅助空间
#     products = [0] * (number + 1)
#     # 定义前几个初始变量的值
#     products[0] = 0
#     products[1] = 1
#     products[2] = 2
#     products[3] = 3
#     # 进行动态规划,也就是从下向上的进行求解
#     for i in range(4, number + 1):
#        max_ = 0
#        for j in range(1, i / 2 + 1):
#           max_ = max(products[j] * products[i - j], max_)
#        products[i] = max_
#
#     max_ = products[number]
#     return max_
#
#
# 3.下面介绍贪婪算法, 我目前对这个不是很了解, 需要一定的数学功底, 只能先贴出代码, 望大家谅解:
#
# # 贪婪算法
# class Solution:
#  def cutRope(self, number):
#     # write code here
#     if number < 2:
#        return 0
#     if number == 2:
#        return 1
#     if number == 3:
#        return 2
#     # 申请辅助空间
#     timesOf3 = number / 3
#     if (number - timesOf3 * 3) == 1:
#        timesOf3 -= 1
#     timesOf2 = (number - timesOf3 * 3) / 2
#     return pow(3, timesOf3) * pow(2, timesOf2)
#
#
# 求数组中第二大元素的方法
# class Solution:
#  def getSecondNum(self,num):
#     maxN = -99999
#     secN = -99999
#
#     for i in range(len(num)):
#        if num[i] > maxN:
#           secN = maxN
#           maxN  = num[i]
#        elif num[i] > secN and num[i] < maxN:
#           secN = num[i]
#        elif secN == -99999:
#           secN = num[i]
#     return secN
#
# ss = Solution()
# print  ss.getSecondNum([3,3,3,3,3])

#
#66.来理解下相应装饰器内容
# def a_decorator(a_func):
#     def wrap_the_func():
#         print("在装饰器前我要做这些")
#         a_func()
#         print("装饰器后做这些")
#
#     return wrap_the_func
#
# def func_foo():
#     print("运行func_foo")
#
# def func_bar():
#     print("运行func_bar")
#
# func_foo = a_decorator(func_foo)() # func1
# func_bar = a_decorator(func_bar)() # func2
#
# @a_decorator
# def func_foo():
#     print("运行func_foo")
#
# @a_decorator
# def func_bar():
#     print("运行func_bar")
# func_foo()
#

# 67.链表反转
# class Solution:
#  def fanzhuan(self,head):
#     reverseHead = None #记录最后一个结点
#     pNode = pHead;  #开始结点
#     pPreNode = None #他的前一个结点
#     while pNode != None: #当前结点
#        pNext = pNode.next #获取他下一个结点
#        if pNext == None: #下一个结点如果是空，证明到头了
#           reverseHead = pNode
#        pNode.next = pPreNode #把当前结点的next置为上一个结点
#        pPreNode = pNode     #赋值上一个结点为当前结点
#        pNode = pNext       #当前结点的下一个结点是当前结点
#     return reverseHead
#

# 68.快速排序
# # -*- coding:utf-8 -*-
# class Solution:
#  def GetLeastNumbers_Solution(self, tinput, k):
#     # write code here
#     def quick_sort(lst):
#        if not lst:
#           return []
#        pivot = lst[0]
#        left = quick_sort([x for x in lst[1:] if x < pivot])
#        right = quick_sort([x for x in lst[1:] if x >= pivot])
#        return left + [pivot] + right
#
#     if tinput == [] or k > len(tinput):
#        return []
#     tinput = quick_sort(tinput)
#     return tinput[: k]





# import random
# a=[1,2,3,4,5]
# print("1",random.randint(10, 20))
# print("2",random.uniform(10,20))
# print("3",random.random())
# print("4",random.sample([1,234,4],2))
# print("5",random.choices(a,weights=[0,2,0,0,1],k=5))
# print("6",random.choice([3,2,5]))
# print("7",random.shuffle([2,3,5]))
# print("8",random.getrandbits(4))#生成一个k比特长的数
#
#
#
# # 随机数不一样
# random.seed()
# print('随机数1：',random.random())
# random.seed()
# print('随机数2：',random.random())
#
# # 随机数一样
# random.seed(1)
# print('随机数3：',random.random())
# random.seed(1)
# print('随机数4：',random.random())
# random.seed(2)
# print('随机数5：',random.random())
# random.seed(2)
# print('随机数6：',random.random())
# random.seed(3)
# print("随机数7：",random.randint(2,6))
# random.seed(3)
# print("随机数8:",random.random())
#
#
# state=random.getstate()
# print("state1",random.random())
#
# print("state2",random.random())
#
# random.setstate(state=state)
# print("state3",random.random())


# a=[1,2,4,3]
# b=set(a)
# print(b)
# c=list(b)
# print(c)




# import random
# a_list=[[2,1],[1,2],[1,1],[2,2]]
# mid_list=[]
# mix_list=[]
#
# mid_list.extend(a_list)
# print("mid_list",mid_list)
# random_list=random.choice(mid_list)
# print("random_list",random_list)
# mid_list.remove(random_list)
# mix_list.append(random_list)
#
# print("mid_list",mid_list)
# print("mix_list",mix_list)

# a=[1,2,3]
# b=reversed(a)
# print(b)

