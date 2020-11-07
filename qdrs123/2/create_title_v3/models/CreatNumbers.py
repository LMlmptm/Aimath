import random


# 生成数据类
class CreatNumbers(object):
    def __init__(self, num_max):
        self.num_max = num_max

    # todo 生成5以内加法数据类
    # 生成单个加法数据列表如：[1,4]
    def creatAddNumbers1(self):
        nums = []
        for i in range(1, self.num_max + 1):
            for j in range(1, self.num_max + 1):
                if i + j <= self.num_max:
                    nums.append([i, j])
        return nums

    # 生成两个加法数据列表如：[[1,4],[2,3]]
    def creatAddNumbers2(self):
        nums = CreatNumbers(self.num_max).creatAddNumbers1()
        nums_all = []
        for num1 in nums:
            for num2 in nums:
                if num1 != num2:
                    nums_all.append([num1, num2])
        return nums_all

    # 生成0的加法数据列表如：[0,4]或[4,0]
    def creatAddNumbers3_1(self):
        nums = []
        for i in range(1, self.num_max + 1):
            nums.append([i, 0])
            nums.append([0, i])
        return nums

    # 生成单个0的加法数据列表如：[4,0]
    def creatAddNumbers3_2(self):
        nums = []
        for i in range(1, self.num_max + 1):
            nums.append([i, 0])
        return nums

    # 生成三个加法数据列表如:[1,2,3],0位和1位/2位两个数相加<=5
    def creatAddNumbers4(self):
        nums = []
        for i in range(1, self.num_max + 1):
            for j in range(1, self.num_max + 1):
                for k in range(1, self.num_max + 1):
                    if i != j and i != k and j != k and i + j <= self.num_max and i + k <= self.num_max:
                        nums.append([i, j, k])
        return nums

    # 生成两个加法数据列表如:[2,3],0位为偶数（2,4）
    def creatAddNumbers5(self):
        nums = []
        for i in [num for num in range(1, self.num_max + 1) if num % 2 == 0]:
            for j in range(1, self.num_max + 1):
                if i / 2 != j and i / 2 + j <= self.num_max:
                    nums.append([i, j])
        return nums

    # 生成两个加法数据列表如:[2,3],0位为偶数（2,4）
    def creatAddNumbers6(self):
        nums = []
        for i in [num for num in range(1, self.num_max + 1) if num % 2 == 0]:
            for j in range(1, self.num_max + 1):
                if i / 2 + j <= self.num_max:
                    nums.append([i, j])
        return nums

    # 生成一个加法规律数据列表如：[2, 1] 表示从2开始每次加1，连加2次
    def creatAddNumbers7(self):
        nums = []
        for i in range(1, self.num_max + 1):
            for j in range(1, self.num_max + 1):
                if i + j * 2 <= self.num_max:
                    nums.append([i, j])
        return nums

    # 生成一个加法数据和单个数字的列表如：[[4,1],3]
    def creatAddNumbers8(self):
        nums = CreatNumbers(self.num_max).creatAddNumbers1()
        nums_all = []
        for num1 in nums:
            for num2 in range(1, self.num_max + 1):
                nums_all.append([num1, num2])
        return nums_all

    # 生成四个加法数据列表，用于选择四个选项如：[[4,1],[2,3],[2,4],[1,3]]
    def creatAddNumbers9(self):
        nums = CreatNumbers(self.num_max).creatAddNumbers1()
        nums_all = []
        for num1 in nums:
            for num2 in nums:
                for num3 in nums:
                    for num4 in nums:
                        if num1 != num2 and num1 != num3 and num1 != num4 and num2 != num3 and num2 != num4 \
                                and num3 != num4:
                            nums_all.append([num1, num2, num3, num4])
        return random.sample(nums_all, 30)

    # 生成四个加法数据列表，每个数据之和相等且第1个加数依次增加1，如：[[0,3],[1,2],[2,1],[3,0]]
    def creatAddNumbers10(self):
        nums = []
        for i in range(self.num_max + 1):
            for j in range(self.num_max + 1):
                if i + j <= self.num_max:
                    nums.append([i, j])
        nums_all = []
        for num1 in nums:
            for num2 in nums:
                for num3 in nums:
                    for num4 in nums:
                        if num1[0] + 1 == num2[0] and num2[0] + 1 == num3[0] and num3[0] + 1 == num4[0] and \
                                num1[0] + num1[1] == num2[0] + num2[1] and num1[0] + num1[1] == num3[0] + num3[1] and \
                                num1[0] + num1[1] == num4[0] + num4[1]:
                            nums_all.append([num1, num2, num3, num4])
        return nums_all

    # todo 生成5以内减法数据类
    # 生成单个减法数据列表如：[4,1]
    def creatSubNumbers1(self):
        nums = []
        for i in range(1, self.num_max + 1):
            for j in range(1, self.num_max + 1):
                if i - j > 0:
                    nums.append([i, j])
        return nums

    # 生成两个减法数据列表如：[[4,1],[3,2]]
    def creatSubNumbers2(self):
        nums = CreatNumbers(self.num_max).creatSubNumbers1()
        nums_all = []
        for num1 in nums:
            for num2 in nums:
                if num1 != num2:
                    nums_all.append([num1, num2])
        return nums_all

    # 生成一个减法数据和单个数字的列表如：[[4,1],3]
    def creatSubNumbers3(self):
        nums = CreatNumbers(self.num_max).creatSubNumbers1()
        nums_all = []
        for num1 in nums:
            for num2 in range(1, self.num_max + 1):
                nums_all.append([num1, num2])
        return nums_all

    # 生成一个减法规律数据列表如：[4, -1] 表示从4开始每次减1，连减2次
    def creatSubNumbers4(self):
        nums = []
        for i in range(1, self.num_max + 1):
            for j in range(1, self.num_max + 1):
                if i - j * 2 > 0:
                    nums.append([i, -j])
        return nums

    # 生成四个减法数据列表，用于选择四个选项如：[[4,1],[3,2],[2,1],[5,3]]
    def creatSubNumbers5(self):
        nums = CreatNumbers(self.num_max).creatSubNumbers1()
        nums_all = []
        for num1 in nums:
            for num2 in nums:
                for num3 in nums:
                    for num4 in nums:
                        if num1 != num2 and num1 != num3 and num1 != num4 and num2 != num3 and num2 != num4 \
                                and num3 != num4:
                            nums_all.append([num1, num2, num3, num4])
        return random.sample(nums_all, 30)

    # 生成四个减法数据列表，每个数据之差相等且第1个被减数依次减1，如：[[4,3],[3,2],[2,1],[1,0]]
    def creatSubNumbers6(self):
        nums = []
        for i in range(self.num_max + 1):
            for j in range(self.num_max + 1):
                if i - j > 0:
                    nums.append([i, j])
        nums_all = []
        for num1 in nums:
            for num2 in nums:
                for num3 in nums:
                    for num4 in nums:
                        if num1[0] - 1 == num2[0] and num2[0] - 1 == num3[0] and num3[0] - 1 == num4[0] and \
                                num1[0] - num1[1] == num2[0] - num2[1] and num1[0] - num1[1] == num3[0] - num3[1] and \
                                num1[0] - num1[1] == num4[0] - num4[1]:
                            nums_all.append([num1, num2, num3, num4])
        return nums_all

    # 生成0的减法数据，如[4,0]
    def creatSubNumbers7(self):
        return [[i, 0] for i in range(1, self.num_max + 1)]

    # 生成四个减法数据列表，且每项之差不相等，用于连线题如：[[4,1],[4,2],[3,2,[5,1]]
    def creatSubNumbers8(self):
        nums = CreatNumbers(self.num_max).creatSubNumbers1()
        nums_all = []
        for num1 in nums:
            for num2 in nums:
                for num3 in nums:
                    for num4 in nums:
                        if num1 != num2 and num1 != num3 and num1 != num4 and num2 != num3 and num2 != num4 and \
                                num3 != num4 and num1[0] - num1[1] != num2[0] - num2[1] and \
                                num1[0] - num1[1] != num3[0] - num3[1] and num1[0] - num1[1] != num4[0] - num4[1] and \
                                num2[0] - num2[1] != num3[0] - num3[1] and num2[0] - num2[1] != num4[0] - num4[1] and \
                                num3[0] - num3[1] != num4[0] - num4[1]:
                            nums_all.append([num1, num2, num3, num4])
        return random.sample(nums_all, 30)

    # todo 生成5以内加减法混合数据类
    # 生成加法和减法数据列表如:[[2,3],[4,1]]
    def creatAddSubNumbers1(self):
        nums_add = CreatNumbers(self.num_max).creatAddNumbers1()
        nums_sub = CreatNumbers(self.num_max).creatSubNumbers1()
        nums = []
        for num_sub in nums_sub:
            for num_add in nums_add:
                nums.append([num_sub, num_add])
        return nums

    # 生成0的加法和0的减法数据列表如:[[2,0],[3,0]]
    def creatAddSubNumbers2(self):
        nums_add = nums_sub = CreatNumbers(self.num_max).creatAddNumbers3_2()
        nums = []
        for num_sub in nums_sub:
            for num_add in nums_add:
                nums.append([num_sub, num_add])
        return nums

    # 生成加法和减法数据列表如:[2,3],0位为偶数（2,4）
    def creatAddSubNumbers3(self):
        nums = []
        for i in [num for num in range(1, self.num_max + 1) if num % 2 == 0]:
            for j in range(1, self.num_max + 1):
                if i / 2 != j and j - i / 2 > 0:
                    nums.append([i, j])
        return nums

    # todo 生成5以内数的认识类数据
    # 生成2个5以内的比较数据，且两数不相等，如[4,5]
    def creatCompareNumbers1(self):
        nums = []
        for i in range(1, self.num_max + 1):
            for j in range(1, self.num_max + 1):
                if i != j:
                    nums.append([i, j])
        return nums

    # 生成2个5以内的比较数据，且两数不相等，且两数之和<=5，如[3,2]
    def creatCompareNumbers2(self):
        nums = []
        for i in range(1, self.num_max + 1):
            for j in range(1, self.num_max + 1):
                if i != j and i + j <= self.num_max:
                    nums.append([i, j])
        return nums

    # 生成2个5以内的比较数据，两数可以相等，如[4,4]
    def creatCompareNumbers3(self):
        nums = []
        for i in range(1, self.num_max + 1):
            for j in range(1, self.num_max + 1):
                nums.append([i, j])
        return nums

    # 生成3个5以内的比较数据，且前两数不相等，第三个数字为前两个数字的随机一个如[[4,5],4]
    def creatCompareNumbers4(self):
        nums = []
        for i in range(1, self.num_max + 1):
            for j in range(1, self.num_max + 1):
                if i != j:
                    nums.append([[i, j], random.choice([i, j])])
        return nums

    # 生成5以内数的列表
    def creatCompareNumbers5(self):
        return [i for i in range(1, self.num_max + 1)]

    # 生成5以内数的列表，包含1.2.3.4.5一次和两次，如[1,1,2]
    def creatCompareNumbers6(self):
        nums = []
        for i in range(1, self.num_max + 1):
            for j in range(1, self.num_max + 1):
                if i == j:
                    for k in range(1, self.num_max + 1):
                        if i != k:
                            nums.append([i, j, k])
                else:
                    for k in range(1, self.num_max + 1):
                        if i != k:
                            nums.append([i, j, k])
        return nums

    # 生成4个5以内的比较数据，且两数不相等[3,2,1,4]
    def creatCompareNumbers7(self):
        nums = []
        for i in range(1, self.num_max + 1):
            for j in range(1, self.num_max + 1):
                for k in range(1, self.num_max + 1):
                    for l in range(1, self.num_max + 1):
                        if i != j and i != k and i != l and j != k and j != l and k != l:
                            nums.append([i, j, k, l])
        return nums

    # 生成3个5以内的比较数据，且两数可以相等[3,2,4]
    def creatCompareNumbers8(self):
        nums = []
        for i in range(1, self.num_max + 1):
            for j in range(1, self.num_max + 1):
                for k in range(1, self.num_max + 1):
                    nums.append([i, j, k])
        return nums

    # 生成3个5以内的比较数据，且两数不相等[3,2,4]
    def creatCompareNumbers9(self):
        nums = []
        for i in range(1, self.num_max + 1):
            for j in range(1, self.num_max + 1):
                for k in range(1, self.num_max + 1):
                    if i != j and i != k and j != k:
                        nums.append([i, j, k])
        return nums

    # 生成3个5以内的比较数据，且不包含5，且两数不相等[3,2,4]
    def creatCompareNumbers10(self):
        nums = []
        for i in range(1, self.num_max):
            for j in range(1, self.num_max):
                for k in range(1, self.num_max):
                    if i != j and i != k and j != k:
                        nums.append([i, j, k])
        return nums

    # 生成3个5以内的比较数据，且必包含0，三数不相等,且依次增加[0,2,4]
    def creatCompareNumbers11(self):
        nums = []
        for i in range(1, self.num_max + 1):
            for j in range(1, self.num_max + 1):
                if i < j:
                    nums.append([0, i, j])
        return nums

    # 生成5以内不包含1数据，[2,3,4,5]
    def creatCompareNumbers12(self):
        return [i for i in range(2, self.num_max + 1)]

    # 生成5以内拆分与合成数据，适用于单一题型
    def creatCompareNumbers13(self):
        nums = []
        for num1 in list(range(2, self.num_max + 1)):
            for num2 in list(range(2, self.num_max + 1)):
                if num1 == num2:
                    for num4 in range(1, num1):
                        for num5 in range(1, num2):
                            if num4 != num5 and num4 != num2 - num5 and num4 + num5 <= self.num_max:
                                num7 = num4 + num5
                                for num8 in list(range(1, self.num_max + 1)):
                                    if num7 + num8 <= self.num_max:
                                        num9 = num7 + num8
                                        num3 = num1 - num4
                                        num6 = num2 - num5
                                        nums.append([num1, num2, num3, num4, num5, num6, num7, num8, num9])
                else:
                    for num4 in range(1, num1):
                        for num5 in range(1, num2):
                            if num4 + num5 <= self.num_max:
                                num7 = num4 + num5
                                for num8 in list(range(1, self.num_max + 1)):
                                    if num7 + num8 <= self.num_max:
                                        num9 = num7 + num8
                                        num3 = num1 - num4
                                        num6 = num2 - num5
                                        nums.append([num1, num2, num3, num4, num5, num6, num7, num8, num9])
        return nums

    # 生成5个5以内的比较数据2组，且两数不相等[[3,2,1,4,5],[3,1,2,4,5]]（可用于连一连）
    def creatCompareNumbers14(self):
        nums = []
        for i in range(1, self.num_max + 1):
            for j in range(1, self.num_max + 1):
                for k in range(1, self.num_max + 1):
                    for l in range(1, self.num_max + 1):
                        for m in range(1, self.num_max + 1):
                            if i != j and i != k and i != l and i != m and j != k and j != l and j != m and k != l \
                                    and k != m and l != m:
                                nums.append([i, j, k, l, m])
        nums_comp = []
        for num1 in nums:
            for num2 in nums:
                if num1 != num2:
                    nums_comp.append([num1, num2])
        return random.sample(nums_comp, 30)

    # 生成3个5以内的比较数据，且依次增大[1,2,4]
    def creatCompareNumbers15(self):
        nums = []
        for i in range(1, self.num_max + 1):
            for j in range(1, self.num_max + 1):
                for k in range(1, self.num_max + 1):
                    if i < j and j < k:
                        nums.append([i, j, k])
        return nums

    # 生成3个5以内的比较数据，且依次减小[1,2,4]
    def creatCompareNumbers16(self):
        nums = []
        for i in range(1, self.num_max + 1):
            for j in range(1, self.num_max + 1):
                for k in range(1, self.num_max + 1):
                    if i > j and j > k:
                        nums.append([i, j, k])
        return nums

    # 生成2个5以内的比较数据(不包含1），两数可以相等且第二个数不小于第一个数，如[4,4]
    def creatCompareNumbers17(self):
        nums = []
        for i in range(2, self.num_max + 1):
            for j in range(2, self.num_max + 1):
                if i <= j:
                    nums.append([i, j])
        return nums

    # 生成5以内的数据，如[1,2,3,4,5]
    def creatCompareNumbers18(self):
        nums = []
        for num1 in range(1, self.num_max + 1):
            for num2 in range(1, self.num_max + 1):
                for num3 in range(1, self.num_max + 1):
                    for num4 in range(1, self.num_max + 1):
                        for num5 in range(1, self.num_max + 1):
                            if num1 != num2 and num1 != num3 and num1 != num4 and num1 != num5 and num2 != num3 and \
                                    num2 != num4 and num2 != num5 and num3 != num4 and num3 != num5 and num4 != num5:
                                nums.append([num1, num2, num3, num4, num5])
        return nums

    # 生成4个5以内的比较数据，且必包含0，四数不相等,且依次增加[0,2,3,4]
    def creatCompareNumbers19(self):
        nums = []
        for i in range(1, self.num_max + 1):
            for j in range(1, self.num_max + 1):
                for k in range(1, self.num_max + 1):
                    if i < j and j < k:
                        nums.append([0, i, j, k])
        return nums

    # 生成4个5以内的比较数据2组，且两数不相等[[3,2,1,4],[3,1,2,4]]（可用于连一连）
    def creatCompareNumbers20(self):
        nums = []
        for i in range(1, self.num_max + 1):
            for j in range(1, self.num_max + 1):
                for k in range(1, self.num_max + 1):
                    for m in range(1, self.num_max + 1):
                        if i != j and i != k and i != m and j != k and j != m and k != m:
                            nums1 = [i, j, k, m]
                            random.shuffle(nums1)
                            nums.append([[i, j, k, m], nums1])
        return random.sample(nums, 30)

    # todo 生成10以内的数据
    # 生成10以内的列表数据[6,7,8,9,10]
    def creatNumbersWithinTen1(self):
        return list(range(6, self.num_max + 1))

    # 生成10以内的任意两个不相等数的数据列表，如[6,8]
    def creatNumbersWithinTen2(self):
        nums = []
        for i in range(6, self.num_max + 1):
            for j in range(6, self.num_max + 1):
                if i != j:
                    nums.append([i, j])
        return nums

    # 生成1-10内的任意三个不相等数的数据列表，且从小到大排序，如[1,3,5]
    def creatNumbersWithinTen3(self):
        nums = []
        for i in range(1, self.num_max + 1):
            for j in range(1, self.num_max + 1):
                for k in range(1, self.num_max + 1):
                    if i < j and j < k:
                        nums.append([i, j, k])
        return random.sample(nums, 30)

    # 生成10以内的数据两组，一组为正序，一组为倒序，每一组包含连续5个数和随机从这5个数中取2个数的组合，如[[[3,4,5,6,7],[4,6]],[[7,6,5,4,3],[6,4]]]
    def creatNumbersWithinTen4(self):
        nums1 = [[i, i + 1, i + 2, i + 3, i + 4] for i in range(1, self.num_max + 1) if
                 i + 4 > 5 and i + 4 <= self.num_max]
        nums2 = [[i, i - 1, i - 2, i - 3, i - 4] for i in range(self.num_max, 0, -1) if i > 5 and i <= self.num_max]
        nums1_1 = []
        for num1 in nums1:
            for i in range(num1[0], num1[4] + 1):
                for j in range(num1[0], num1[4] + 1):
                    if i < j:
                        nums1_1.append([num1, [i, j]])
        nums2_1 = []
        for num2 in nums2:
            for i in range(num2[0], num2[4] - 1, -1):
                for j in range(num2[0], num2[4] - 1, -1):
                    if i > j:
                        nums2_1.append([num2, [i, j]])
        nums = []
        for i in nums1_1:
            for j in nums2_1:
                if i != j:
                    nums.append([i, j])
        return random.sample(nums, 30)

    # 生成10以内的列表数据,从1开始，最大为9的数据，[1,2,3,4,5,6,7,8,9]
    def creatNumbersWithinTen5(self):
        return list(range(1, self.num_max))

    # 生成10以内的数据列表,最大可为11，如：[3,8]
    def creatNumbersWithinTen6(self):
        nums = []
        for i in range(1, self.num_max + 1):
            for j in range(1, self.num_max + 1):
                if i + j > 6 and i + j <= self.num_max + 1:
                    nums.append([i, j])
        return nums

    # 生成10以内的两个相邻数的数据列表，如[6,7]
    def creatNumbersWithinTen7(self):
        nums = []
        for i in range(6, self.num_max + 1):
            for j in range(6, self.num_max + 1):
                if i + 1 == j:
                    nums.append([i, j])
        return nums

    # 生成10以内的任意两个数及其中间数与非中间数的数据列表(中间数可为1个或2个），如[[5,8],[6,7,9]]
    def creatNumbersWithinTen8(self):
        nums = []
        for num1 in range(6, self.num_max + 1):
            for num2 in range(6, self.num_max + 1):
                if num1 < num2 - 1:
                    num3 = list(range(num1 + 1, num2))
                    num4 = sorted(set(range(6, self.num_max + 1)).difference(set(num3)).difference([num1, num2]))
                    num5 = []
                    if len(num3) == 1 and len(num4) > 1:
                        num5.append(random.choice(num3))
                        num5.extend(random.sample(num4, 2))
                        random.shuffle(num5)
                        nums.append([[num1, num2], num5])
                    elif len(num3) == 2 and len(num4):
                        num5.extend(num3)
                        num5.append(random.choice(num4))
                        random.shuffle(num5)
                        nums.append([[num1, num2], num5])
        return nums

    # 生成10以内的列表数据,从1开始，最大为10的数据，[1,2,3,4,5,6,7,8,9,10]
    def creatNumbersWithinTen9(self):
        return list(range(1, self.num_max + 1))

    # 生成10以内的列表数据,从2开始，最大为10的数据，[2,3,4,5,6,7,8,9,10]
    def creatNumbersWithinTen10(self):
        return list(range(2, self.num_max + 1))

    # 生成10以内的列表数据,从0开始，最大为10的数据，第1.2维为不相等的列表，第三维为第2位与第1维最近、最近、最远的数，如[[4, 6, 9, 8, 7, 5], [1, 2, 3], [4, 4, 9]]
    def creatNumbersWithinTen11(self):
        nums = []
        for i in range(1, self.num_max + 1):
            for j in range(1, self.num_max + 1):
                for k in range(1, self.num_max + 1):
                    if i != j and i != k and j != k:
                        num1 = [i, j, k]
                        num2 = list(set(list(range(self.num_max + 1))).difference(set(num1)))
                        num2 = random.sample(num2, 6)
                        counts = 0
                        num5 = []
                        for m in num1:
                            num3 = list(map(lambda x: abs(x - m), num2))
                            if len(num3) != len(set(num3)):
                                continue
                            counts += 1
                            if counts < 3:
                                num5.append(num2[num3.index(min(num3))])
                            else:
                                num5.append(num2[num3.index(max(num3))])
                        if counts == 3:
                            nums.append([num2, num1, num5])
        return nums

    # 生成10以内的任意两个不相等数的数据和其中一个数的列表，如[6,[6,8]]
    def creatNumbersWithinTen12(self):
        nums = []
        for i in range(6, self.num_max + 1):
            for j in range(6, self.num_max + 1):
                if i != j:
                    nums.append([random.choice([i, j]), [i, j]])
        return nums

    # 生成10以内的任意三个不相等数的数据列表，如[6,8,9]
    def creatNumbersWithinTen13(self):
        nums = []
        for i in range(6, self.num_max + 1):
            for j in range(6, self.num_max + 1):
                for k in range(6, self.num_max + 1):
                    if i != j and i != k and j != k:
                        nums.append([i, j, k])
        return nums

    # 生成10以内拆分与合成数据，适用于单一题型
    def creatNumbersWithinTen14(self):
        nums = []
        for num1 in list(range(6, self.num_max + 1)):
            for num2 in list(range(6, self.num_max + 1)):
                for num3 in list(range(1, self.num_max + 1)):
                    for num4 in list(range(1, self.num_max + 1)):
                        for num5 in list(range(1, self.num_max + 1)):
                            for num6 in list(range(1, self.num_max + 1)):
                                if num3 + num4 == num1 and num5 + num6 == num2:
                                    num7 = num4 + num5
                                    if num7 > 0 and num7 <= self.num_max:
                                        nums.append([num1, num2, num3, num4, num5, num6, num7])
        return random.sample(nums, 30)

    # 生成10以内(从1开始）的任意两个不相等数的数据列表，如[6,8]
    def creatNumbersWithinTen15(self):
        nums = []
        for i in range(1, self.num_max + 1):
            for j in range(1, self.num_max + 1):
                if i != j:
                    nums.append([i, j])
        return nums

    # todo 生成10以内加法数据类
    # 生成单个加法数据列表如：[1,4]
    def creatAddNumbersWithTen1(self):
        nums = []
        for i in range(1, self.num_max + 1):
            for j in range(1, self.num_max + 1):
                if i + j < self.num_max + 1 and i + j > 5:
                    nums.append([i, j])
        return nums

    # todo 生成20以内的数据
    # 生成20以内的列表数据
    def creatNumbersWithTwenty1(self):
        return list(range(11, self.num_max))

    # todo 生成20以内的加减数据
    # 生成20以内的加减数据,第三等于第一加第二，如[[10, 11, 12, 13, 14, 15, 16], 1, [11, 12, 13, 14, 15, 16, 17]]
    def creatAddSubWithinTwenty1(self):
        nums1 = [[i, i + 1, i + 2, i + 3, i + 4, i + 5, i + 6] for i in range(self.num_max + 1) if
                 i > 10 and i + 5 < self.num_max]
        nums = []
        for num1 in nums1:
            for i in range(1, self.num_max + 1):
                num2 = list(map(lambda x: x - i, num1))
                if num2[0] >= 0:
                    nums.append([num2, i, num1])
        return nums

    # 生成20以内的加减数据,一组，如[7,8]
    def creatAddSubWithinTwenty2(self):
        nums = []
        for i in range(2, 10):
            for j in range(2, 10):
                if i + j > 10 and i + j < self.num_max:
                    nums.append([i, j])
        return nums

    # 生成20以内的加减数据,三组，如[[7,8],[6,8],[9,7]]
    def creatAddSubWithinTwenty3(self):
        nums = []
        num1 = CreatNumbers(self.num_max).creatAddSubWithinTwenty2()
        for i in num1:
            for j in num1:
                for k in num1:
                    if i != j and i != k and j != k:
                        nums.append([i, j, k])
        return random.sample(nums, 30)
