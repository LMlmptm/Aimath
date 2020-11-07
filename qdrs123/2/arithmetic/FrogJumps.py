# -*- coding:utf-8 -*-


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

    #一只青蛙一次可以跳上1级台阶，也可以跳上2级......它也可以跳上n阶。求该青蛙跳上一个n级的台阶总共有多少种跳法。
    # -*- coding:utf-8 -*-
    class Solution:
        def jumpFloorII(self, number):
            # write code here
            if number == 0:
                return 0
            #这样的结果的是通过算法规律找出来的
            return 2 ** (number - 1)

