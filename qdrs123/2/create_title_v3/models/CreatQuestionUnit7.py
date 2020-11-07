import random
import re
from models.CreatImgs import CreatImgs


# todo 一、20以内数的认识


# todo 二、20以内数的组成
class ComposnumbersWithin20(object):

    def __init__(self, nums):
        self.nums = nums

    # 4.1 - 7 - 2 - 04【标题】填一填
    def compos_numbers_within_20_4(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "type": "know-fill-in",
                            "stem": "填一填",
                            "sum": num  # 求和数
                        }
                    ],
                    "answers": list(map(lambda x: int(x), list(str(num)))),
                    "knowledges": ["20以内数的组成"],
                    "type": "填空",
                    "explain": "",
                    "level": "1",
                    "number": "1-7-2-04"
                }
            ]
            questions_all.extend(questions)
        return questions_all


# todo 三、个位,十位的认识


# todo 四、20以内数的大小比较


# todo 五、20以内数的排序


# todo 六、20以内的不进位加法
class AddWithoutCarryWithin20(object):

    def __init__(self, nums):
        self.nums = nums

    # 15.1 - 7 - 6 - 15【标题】填一填
    def add_without_carry_within_20_15(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "title": "加法计算，和{}相加".format(num[1]),
                            "stem": "加法计算，和",
                            "type": "au-fill-add",
                            "augend": num[1],  # 加数
                            "add": [  # 被加数列表
                                {
                                    "add": num[0][0],  # 加数
                                    "result": num[2][0]  # 加数 + 被加数的结果
                                },
                                {
                                    "add": num[0][1]
                                },
                                {
                                    "add": num[0][2]
                                },
                                {
                                    "add": num[0][3]
                                },
                                {
                                    "add": num[0][4]
                                },
                                {
                                    "add": num[0][5]
                                }
                            ]
                        }
                    ],
                    "type": "填空",
                    "explain": "",
                    "level": "1",
                    "answers": [
                        num[2][1],
                        num[2][2],
                        num[2][3],
                        num[2][4],
                        num[2][5]
                    ],
                    "knowledges": ["20以内的不进位加法"],
                    "number": "1-7-6-15"
                }
            ]
            questions_all.extend(questions)
        return questions_all


# todo 七、20以内的不进位加法应用


# todo 八、20以内数的进位加法
class AddWithCarryWithin20(object):

    def __init__(self, nums):
        self.nums = nums

    # 1.1 - 7 - 8 - 01【标题】填一填
    def add_with_carry_within_20_1(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "title": "算一算，填一填",
                            "stem": "算一算，填一填",
                            "type": "au-num-deciliter",
                            "content": [
                                "{}".format(num[0]),
                                "+",
                                "{}".format(num[1]),
                                "=",
                                ""
                            ]  # 列式数组
                        }
                    ],
                    "type": "填空",
                    "explain": "",
                    "level": "1",
                    "answers": [
                        num[0] + num[1],
                        10 - num[0],
                        num[1] - (10 - num[0]),
                        10
                    ],
                    "knowledges": ["20以内数的进位加法"],
                    "number": "1-7-8-01"
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 18.1 - 7 - 8 - 18【标题】算一算
    def add_with_carry_within_20_18(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "type": "au-fill-table",
                            "title": "填一填",
                            "stem": "完成表格",
                            "table": {
                                "title": [
                                    "",
                                    "一组",
                                    "二组",
                                    "一共"
                                ],
                                "list": [
                                    {
                                        "one": "{}个".format(num[0][0]),  # 第二列（一组对应数据）
                                        "two": "{}个".format(num[0][1]),  # 第三列（二组对应数据）
                                        "imgUrl": "sphere_items/ff2b0783e751a9388728a960d16ef998.svg"  # 第一列(图片)
                                    },
                                    {
                                        "one": "{}个".format(num[1][0]),
                                        "two": "{}个".format(num[1][1]),
                                        "imgUrl": "sphere_items/d1855a4119663766d6aaa7b21d24d83f.svg"
                                    },
                                    {
                                        "one": "{}个".format(num[2][0]),
                                        "two": "{}个".format(num[2][1]),
                                        "imgUrl": "sphere_items/480be6f2d92bce113cc00f6595b969c1.svg"
                                    }
                                ]  # 表格列表
                            }
                        }
                    ],
                    "type": "填空",
                    "explain": "",
                    "level": "1",
                    "answers": [
                        num[0][0] + num[0][1],
                        num[1][0] + num[1][1],
                        num[2][0] + num[2][1]
                    ],
                    "knowledges": ["20以内的进位加法"],
                    "number": "1-7-8-18"
                }
            ]
            questions_all.extend(questions)
        return questions_all


# todo 九、20以内的进位加法应用
class AppCarryAddWithin20(object):

    def __init__(self, nums):
        self.nums = nums

    # 8. 1-7-9-08【标题】解决问题
    def app_carry_add_within_20_8(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "type": "au-add-up",
                            "stem": "算一算，一共有多少",
                            "unit": "本",  # 单位
                            "name": "书",  # 名称
                            "content": [
                                {
                                    "img": "people_head_boy/1286eb2d0fa94d0b7583c3af55643ac1.svg",  # 左边人物
                                    "num": num[0]
                                },
                                {
                                    "img": "people_head_girl/44bcdca877fc0ab92e8f0f65cda753ac.svg",  # 右边人物
                                    "num": num[1]
                                }
                            ],
                            "equation": [
                                "",
                                "+",
                                "",
                                "=",
                                ""
                            ]  # 列式列表（空值代表可以输入）
                        }
                    ],
                    "answers": [num[0], num[1], num[0] + num[1]],
                    "explain": "",
                    "knowledges": ["20以内进位加法应用"],
                    "type": "填空",
                    "level": "1",
                    "number": "1-7-9-08"
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 9. 1-7-9-09【标题】解决问题
    def app_carry_add_within_20_9(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "type": "au-add-up2",
                            "stem": "看图列算式，原来有多少",
                            "unit": "个",  # 单位
                            "name": "篮球",  # 名称
                            "show": {
                                "img": "sphere_items/ff2b0783e751a9388728a960d16ef998.svg",  # 展示列式图片
                                "num": num[0]  # 数量
                            },  # 展示对象
                            "tips": {
                                "img": "people_head_boy/1286eb2d0fa94d0b7583c3af55643ac1.svg",  # 头像
                                "num": num[1]  # 数量（例如：多少个球）
                            },  # 气泡对象
                            "equation": [
                                "",
                                "+",
                                "",
                                "=",
                                ""
                            ]  # 列式列表（值为空代表可编辑）
                        }
                    ],
                    "answers": [num[0], num[1], num[0] + num[1]],
                    "explain": "",
                    "knowledges": ["20以内进位加法应用"],
                    "type": "填空",
                    "level": "1",
                    "number": "1-7-9-09"
                }
            ]
            questions_all.extend(questions)
        return questions_all

# todo 十、20以内的不退位减法


# todo 十一、20以内的不退位减法应用
