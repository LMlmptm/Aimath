import random
import re
from models.CreatImgs import CreatImgs


# todo 一、整时
class IntegralTime(object):

    def __init__(self, nums):
        self.nums = nums

    # 1. 认一认，填一填
    @staticmethod
    def integral_time_1():
        questions = [
            {
                "body": [
                    {
                        "type": "au-clock-input",
                        "stem": "认一认，填一填",
                        "list": [
                            {
                                "clock": 'v2/通用/时钟/整点/7点.svg',  # 时钟图片
                                "people": 'v2/通用/时钟/作息/作息2.svg',  # 作息人物图片
                                "time": 7  # 时钟指针位置，用于计算正确答案,需与时钟图片上的时间对应
                            },
                            {
                                "clock": 'v2/通用/时钟/整点/12点.svg',
                                "people": 'v2/通用/时钟/作息/作息1.svg',
                                "time": 12
                            },
                            {
                                "clock": 'v2/通用/时钟/整点/4点.svg',
                                "people": 'v2/通用/时钟/作息/作息3.svg',
                                "time": 4
                            }
                        ]  # 展示图片列表
                    }
                ],
                "answers": [7, 12, 4],  # 正确答案
                "resource": "",  # 这里填生产题目具体资源
                "explain": "",  # 题目相关解析
                "knowledges": ["整时"],  # 知识点，写成数组
                "level": "1",  # 难度等级
                "type": "填空",  # 题目类型
                "number": '1-8-1-01',  # 题目编号
            }
        ]
        return questions

    # 2. 选一选
    @staticmethod
    def integral_time_2_1(imgs):
        questions_all = []
        for img in imgs:
            questions = [
                {
                    "body": [
                        {
                            "type": "au-clock-select2",
                            "title": "选一选",
                            "imgUrl": "{}".format(img[0]),  # 过了整点时——时钟图片
                            "time": img[1]  # 与时钟图片指针显示对应，最大值12
                        }
                    ],
                    "answers": [0],
                    "resource": "",
                    "explain": "",
                    "knowledges": ["整时"],
                    "level": "1",
                    "type": "选择",
                    "number": "1-8-1-02"
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 2. 选一选
    @staticmethod
    def integral_time_2_2(imgs):
        questions_all = []
        for img in imgs:
            questions = [
                {
                    "body": [
                        {
                            "type": "au-clock-select2",
                            "title": "选一选",
                            "imgUrl": "{}".format(img[0]),  # 过了整点时——时钟图片
                            "time": img[1]  # 与时钟图片指针显示对应，最大值12
                        }
                    ],
                    "answers": [1],
                    "resource": "",
                    "explain": "",
                    "knowledges": ["整时"],
                    "level": "1",
                    "type": "选择",
                    "number": "1-8-1-02"
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 2. 选一选
    def integral_time_2_3(self, imgs):
        questions_all = []
        for img in imgs:
            questions = [
                {
                    "body": [
                        {
                            "stem": "连一连",
                            "content": [
                                [
                                    {
                                        "val": "{}".format(img[0][0]),
                                        "num": "{}".format(img[0][1])
                                    },
                                    {
                                        "val": "{}".format(img[1][0]),
                                        "num": "{}".format(img[1][1])
                                    },
                                    {
                                        "val": "{}".format(img[2][0]),
                                        "num": "{}".format(img[2][1])
                                    },
                                    {
                                        "val": "{}".format(img[3][0]),
                                        "num": "{}".format(img[3][1])
                                    }
                                ],  # 左边内容
                                [
                                    {
                                        "num": "8"
                                    },
                                    {
                                        "num": "12"
                                    },
                                    {
                                        "num": "3"
                                    },
                                    {
                                        "num": "10"
                                    }
                                ]  # 右边内容，同左边num值相同，排序不同
                            ],
                            "type": "au-clock-connect"
                        }
                    ],
                    "answers": [['0', '1'], ['1', '0'], ['2', '2'], ['3', '3']],
                    "knowledges": ["整时"],
                    "resource": "",
                    "type": "",
                    "explain": "",
                    "level": "1",
                    "number": "1-8-1-03"
                }
            ]
            questions_all.extend(questions)
        return questions_all


# todo 二、半时


# todo 三、整时、半时的应用
class AppOfIntegralAndHalfTime(object):

    def __init__(self, nums):
        self.nums = nums

    # 5.请在钟表上将下面时间表示出来(整时）
    def app_of_integral_and_half_time_5_1(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "title": "拨动时钟",
                            "stem": "拨动时针和分针，在钟表上表示",
                            "startTime": "{}:00".format(num[0]),  # 开始显示的时间 （注意本组件所有时间只支持整时或者半时）
                            "targetTime": "{}:00".format(num[1]),  # 题目要求的时间点 （题目要求的时间点不可与开始显示的时间相同）
                            "clockImg": "",  # 表背景图，不填则使用默认图
                            "hourHandImg": "",  # 时针图，不填则使用默认图
                            "minuteHandImg": "",  # 分针图，不填则使用默认图
                            "type": "au-clock-select"
                        }
                    ],
                    "answers": [num[1], 12],  # 代表时针、分针指向的数字
                    "knowledges": ["整时、半时的应用"],  # 知识点
                    "resource": "",
                    "type": "操作",
                    "explain": "",
                    "level": "1",  # 难度
                    "number": "1-8-3-05"  # 题型编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 5.请在钟表上将下面时间表示出来(半时）
    def app_of_integral_and_half_time_5_2(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "title": "拨动时钟",
                            "stem": "拨动时针和分针，在钟表上表示",
                            "startTime": "{}:00".format(num[0]),  # 开始显示的时间 （注意本组件所有时间只支持整时或者半时）
                            "targetTime": "{}:30".format(num[1]),  # 题目要求的时间点 （题目要求的时间点不可与开始显示的时间相同）
                            "clockImg": "",  # 表背景图，不填则使用默认图
                            "hourHandImg": "",  # 时针图，不填则使用默认图
                            "minuteHandImg": "",  # 分针图，不填则使用默认图
                            "type": "au-clock-select"
                        }
                    ],
                    "answers": [float("{}.5".format(num[1])), 6],  # 代表时针、分针指向的数字
                    "knowledges": ["整时、半时的应用"],  # 知识点
                    "resource": "",
                    "type": "操作",
                    "explain": "",
                    "level": "1",  # 难度
                    "number": "1-8-3-05"  # 题型编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

# todo 四、整时、半时的综合认识
