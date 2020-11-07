import random
import re
from models.CreatImgs import CreatImgs


# todo 一、数一数
class Count(object):
    pass


# todo 二、比多少
class Comparison(object):
    def __init__(self, nums):
        self.nums = nums

    # 3.    【标题】连一连
    def comparison_3(self, imgs):
        questions_all = []
        for num in self.nums:
            imgs_sample = random.sample(imgs, 10)
            questions = [
                {
                    "body": [
                        {
                            "title": "动物连线",
                            "stem": "把同样多的动物用线连起来",
                            "content": [
                                [
                                    {
                                        "val": "{}".format(imgs_sample[0][0]),  # 图片路径
                                        "num": "{}".format(num[0][0]),  # 数量
                                        "type": "img"  # 图片类型
                                    },
                                    {
                                        "val": "{}".format(imgs_sample[1][0]),
                                        "num": "{}".format(num[0][1]),
                                        "type": "img"
                                    },
                                    {
                                        "val": "{}".format(imgs_sample[2][0]),
                                        "num": "{}".format(num[0][2]),
                                        "type": "img"
                                    },
                                    {
                                        "val": "{}".format(imgs_sample[3][0]),
                                        "num": "{}".format(num[0][3]),
                                        "type": "img"
                                    },
                                    {
                                        "val": "{}".format(imgs_sample[4][0]),
                                        "num": "{}".format(num[0][4]),
                                        "type": "img"
                                    }
                                ],  # 左边列表项
                                [
                                    {
                                        "val": "{}".format(imgs_sample[5][0]),  # 圆背景颜色值
                                        "num": "{}".format(num[1][0]),  # 数量
                                        "type": "img"  # 圆类型
                                    },
                                    {
                                        "val": "{}".format(imgs_sample[6][0]),
                                        "num": "{}".format(num[1][1]),
                                        "type": "img"
                                    },
                                    {
                                        "val": "{}".format(imgs_sample[7][0]),
                                        "num": "{}".format(num[1][2]),
                                        "type": "img"
                                    },
                                    {
                                        "val": "{}".format(imgs_sample[8][0]),
                                        "num": "{}".format(num[1][3]),
                                        "type": "img"
                                    },
                                    {
                                        "val": "{}".format(imgs_sample[9][0]),
                                        "num": "{}".format(num[1][4]),
                                        "type": "img"
                                    }
                                ]  # 右边列表项
                            ],
                            "type": "animal-connect"
                        }
                    ],
                    "answers": [
                        ["0", "{}".format(num[1].index(num[0][0]))],
                        ["1", "{}".format(num[1].index(num[0][1]))],
                        ["2", "{}".format(num[1].index(num[0][2]))],
                        ["3", "{}".format(num[1].index(num[0][3]))],
                        ["4", "{}".format(num[1].index(num[0][4]))]
                    ],  # 正确下标对应答案
                    "knowledges": ["比多少"],
                    "resource": "",
                    "type": "连线",
                    "explain": "",
                    "level": "2",
                    "number": "1-1-2-03"
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 8.    【标题】解决问题
    def comparison_8(self, imgs):
        questions_all = []
        for num in self.nums:
            imgs_sample = random.sample(imgs, 3)
            questions = [
                {
                    "body": [
                        {
                            "title": "多图单选框(带容器）",
                            "stem": "3个盘子原来有同样多的草莓，3个小朋友各吃了一些，都剩下一些，谁吃的最多？",
                            "content": [
                                {
                                    "src": "{}".format(imgs_sample[0]),  # 左边人物svg地址
                                    "num": "{}".format(num[0])  # 右方草莓数量
                                },
                                {
                                    "src": "{}".format(imgs_sample[1]),
                                    "num": "{}".format(num[1])
                                },
                                {
                                    "src": "{}".format(imgs_sample[2]),
                                    "num": "{}".format(num[2])
                                }
                            ],  # 表示选项内容
                            "type": "select-img-1"
                        }
                    ],
                    "answers": [num.index(min(num)) + 1],  # 表示第1个选项为正确答案
                    "knowledges": ["比多少"],
                    "resource": "",
                    "type": "选择",
                    "explain": "",
                    "level": "3",
                    "number": '1-1-2-08',  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all


# todo 三、5以内数的认识
class AnderstandNumbersWithin5(object):
    def __init__(self, nums):
        self.nums = nums

    # 1、【标题】数一数
    def anderstand_numbers_within_5_1(self, imgs):
        questions_all = []
        for num in self.nums:
            img = random.choice(imgs)
            questions = [
                {
                    "body": [
                        {
                            "title": "数一数",
                            "stem": "有多少",
                            "type": "count-it",  # 组件名称
                            "unit": '{}'.format(img[1]),  # 单位
                            "name": '{}'.format(img[2]),  # 名称
                            "figure": {  # 数量对象
                                "img": '{}'.format(img[0]),  # 图片路径
                                "num": num  # 图片展示的数量(5以内数)
                            },
                            "keyBoardType": 5,  # 键盘总数（5以内数只能填5）值为5或者10
                        }
                    ],
                    "answers": [num],
                    "knowledges": ["5以内数的认识"],
                    "resource": "",  # 这里填生产题目具体的资源名称
                    "explain": "",  # 题目相关解析
                    "level": "1",  # 难度等级
                    "type": "选择",  # 题目类型
                    "number": '1-1-3-01'  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 3、【标题】放一放
    def anderstand_numbers_within_5_3(self, imgs):
        questions_all = []
        for num in self.nums:
            img = random.choice(imgs)
            questions = [
                {
                    "body": [
                        {
                            "title": "动物连线",
                            "stem": "在图中放{}{}{}".format(num, img[1], img[2]),
                            "content": [
                                {
                                    "type": "background",  # 公园背景
                                    "src": "address/2dab42777ade0ff96be8395b6c95e58a.svg",  # 背景图片路径
                                    "num": 1
                                },
                                {
                                    "type": "animal",  # 拖拽动物
                                    "src": "{}".format(img[0]),  # 动物图片路径
                                    "num": 5  # 显示的动物数量
                                }
                            ],
                            "results": [num],  # 需要拖拽的个数
                            "type": "animal-drag"
                        }
                    ],
                    "answers": [num],  # 正确答案
                    "knowledges": ["5以内数的认识"],
                    "resource": "",
                    "type": "操作",
                    "explain": "",
                    "level": "1",
                    "number": '1-1-3-03',  # 题型编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 5、【标题】连一连
    def anderstand_numbers_within_5_5(self, imgs):
        questions_all = []
        for num in self.nums:
            img = random.sample(imgs, 4)
            questions = [
                {
                    "body": [
                        {
                            "title": "连一连",
                            "stem": "把同样多的动物用线连起来",
                            "content": [
                                [
                                    {
                                        "val": "{}".format(img[0][0]),  # 图片路径
                                        "num": "{}".format(num[0][0]),  # 数量
                                        "type": "img"  # 图片类型（img-图片类型，circle-圆类型，num-数字类型）
                                    },
                                    {
                                        "val": "{}".format(img[1][0]),
                                        "num": "{}".format(num[0][1]),
                                        "type": "img"
                                    },
                                    {
                                        "val": "{}".format(img[2][0]),
                                        "num": "{}".format(num[0][2]),
                                        "type": "img"
                                    },
                                    {
                                        "val": "{}".format(img[3][0]),
                                        "num": "{}".format(num[0][3]),
                                        "type": "img"
                                    }
                                ],  # 左边列表项
                                [
                                    {
                                        "val": "{}".format(num[1][0]),  # type为num时，此字段与num字段保持一致
                                        "num": "{}".format(num[1][0]),  # 数量
                                        "type": "num"  # 数字
                                    },
                                    {
                                        "val": "{}".format(num[1][1]),
                                        "num": "{}".format(num[1][1]),
                                        "type": "num"
                                    },
                                    {
                                        "val": "{}".format(num[1][2]),
                                        "num": "{}".format(num[1][2]),
                                        "type": "num"
                                    },
                                    {
                                        "val": "{}".format(num[1][3]),
                                        "num": "{}".format(num[1][3]),
                                        "type": "num"
                                    }
                                ]  # 右边列表项
                            ],
                            "type": "animal-connect"
                        }
                    ],
                    "answers": [
                        ["0", "{}".format(num[1].index(num[0][0]))],
                        ["1", "{}".format(num[1].index(num[0][1]))],
                        ["2", "{}".format(num[1].index(num[0][2]))],
                        ["3", "{}".format(num[1].index(num[0][3]))]
                    ],  # 正确下标对应答案
                    "knowledges": ["5以内数的认识"],
                    "resource": "",
                    "type": "连线",
                    "explain": "",
                    "level": "1",
                    "number": "1-1-3-05"
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 6、【标题】涂一涂
    def anderstand_numbers_within_5_6(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "title": "涂色题",
                            "stem": "选出{}个".format(num),
                            "imgUrl": [
                                "base_shape/41cea18eb1dd940e5960e3ccbc2cbe41.svg",  # 未染色前的图片（星星、三角、圆、任意相关都可）
                                "base_shape/304fe1b9874a12bf13ce39f62414d1e6.svg"  # 点击染色后的图片
                            ],
                            "titleType": "2",  # 可取值1、2
                            "content": ["10", "{}".format(num)],  # titleType为1时，代表共10个，涂第6个；为2时，代表共十个，随意涂其中6个
                            "type": "drag-color-circle2"
                        }
                    ],
                    "answers": [num],  # 正确答案： titleType为1时，代表所涂素材的下标；titleType为2时,代表所涂总数量
                    "knowledges": ["5以内数的认识"],
                    "resource": "",
                    "type": "操作",
                    "explain": "",
                    "level": "1",
                    "number": "1-1-3-06"
                }
            ]
            questions_all.extend(questions)
        return questions_all


# todo 四、比较符号的认识
class UnderstandComparativeSymbols(object):

    # 1、	【标题】选一选
    def understand_comparative_symbols_1(self):
        questions = [
            {
                "body": [
                    {
                        "type": "choose-symbol",
                        "title": "选一选",
                        "stem": "选一选，哪个是",
                        "symbol": "大于号",
                        "list": [
                            "more",
                            "less",
                        ]
                    }
                ],
                "answers": [0],  # 正确答案
                "knowledges": ["比较符号的认识"],  # 知识点，写成数组
                "resource": "",  # 这里填生产题目具体资源
                "explain": "",  # 题目相关解析
                "level": "1",  # 难度等级
                "type": "选择",  # 题目类型
                "number": '1-1-4-01',  # 题目编号
            }
        ]
        return questions

    # 2、	【标题】选一选
    def understand_comparative_symbols_2(self):
        questions = [
            {
                "body": [
                    {
                        "type": "choose-symbol",
                        "title": "选一选",
                        "stem": "选一选，哪个是",
                        "symbol": "等于号",
                        "list": [
                            "more",
                            "less",
                            "equal"
                        ]
                    }
                ],
                "answers": [2],  # 正确答案
                "knowledges": ["比较符号的认识"],  # 知识点，写成数组
                "resource": "",  # 这里填生产题目具体资源
                "explain": "",  # 题目相关解析
                "level": "1",  # 难度等级
                "type": "选择",  # 题目类型
                "number": '1-1-4-02',  # 题目编号
            }
        ]
        return questions


# todo 五、5以内数的大小比较
class ComparNumbersWithin5(object):
    def __init__(self, nums):
        self.nums = nums

    # 2、	【标题】填一填
    def compar_numbers_within_5_2(self):
        questions_all = []
        for num in self.nums:
            if num[0] > num[1]:
                answer = ">"
            elif num[0] < num[1]:
                answer = "<"
            else:
                answer = '='
            questions = [
                {
                    "body": [
                        {
                            "type": "five-size-fill",
                            "title": "填一填",
                            "stem": "填写“>” “<” 或 “=”",
                            "list": [num[0], num[1]]  # 比较数列表
                        }
                    ],
                    "answers": [answer],  # 正确答案
                    "resource": "",  # 这里填生产题目具体资源
                    "explain": "",  # 题目相关解析
                    "knowledges": ["5以内数的大小比较"],  # 知识点，写成数组
                    "level": "1",  # 难度等级
                    "type": "填空",  # 题目类型
                    "number": '1-1-5-02',  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 3、	【标题】选一选
    def compar_numbers_within_5_3(self):
        questions_all = []
        for num in self.nums:
            if num[0] > num[1]:
                answer = 0
            elif num[0] < num[1]:
                answer = 1
            else:
                answer = 2
            questions = [
                {
                    "body": [
                        {
                            "type": "choose-symbol",
                            "title": "选一选",
                            "stem": "哪个符号使陈述正确？",
                            "symbol": "大于号",
                            "list": [
                                "more",
                                "less",
                                "equal"
                            ],
                            "numList": [num[0], num[1]]
                            # 比较数 注意：这个字段同时决定是否显示比较数(有这个字段是1-1-4-01和1-1-4-02题型，无这个字段是题型1-1-5-03)
                        }
                    ],
                    "answers": [answer],  # 正确答案
                    "knowledges": ["5以内数的大小比较"],  # 知识点，写成数组
                    "resource": "",  # 这里填生产题目具体资源
                    "explain": "",  # 题目相关解析
                    "level": "1",  # 难度等级
                    "type": "选择",  # 题目类型
                    "number": '1-1-5-03',  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 8、【标题】填一填
    def compar_numbers_within_5_8(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "type": "compare-fill",
                            "title": "选一选",
                            "stem": "代表的数可能是",
                            "content": {
                                "num": num,
                                "symbol": "more",
                                "img": "botany_flowers/5944736d8b5a1a6d5916be3182aedf89.svg"
                            }
                        }
                    ],
                    "answers": list(range(num)),  # 正确答案
                    "knowledges": ["5以内数的大小比较"],  # 知识点，写成数组
                    "resource": "",  # 这里填生产题目具体资源
                    "explain": "",  # 题目相关解析
                    "level": "2",  # 难度等级
                    "type": "填空",  # 题目类型
                    "number": '1-1-5-08',  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all


# todo 六、5以内数的排序
class SortNumbersWithin5(object):
    def __init__(self, nums):
        self.nums = nums

    # 1、	【标题】填一填
    def sort_numbers_within_5_1(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "type": "carriage-fill",
                            "title": "填一填",
                            "stem": "按顺序给每一节车厢标上序号",
                            "list": [
                                1 if 1 in num else "",
                                2 if 2 in num else "",
                                3 if 3 in num else "",
                                4 if 4 in num else "",
                                5 if 5 in num else "",
                            ]  # 有值代表默认显示不可操作，无值可填写  注意（值为数字类型）
                        }
                    ],
                    "answers": sorted(set(list(range(1, 6))).difference(set(num))),  # 正确答案
                    "resource": "",  # 这里填生产题目具体资源
                    "explain": "",  # 题目相关解析
                    "knowledges": ["5以内数的排序"],  # 知识点，写成数组
                    "level": "1",  # 难度等级
                    "type": "填空",  # 题目类型
                    "number": '1-1-6-01',  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 2、    【标题】选一选
    def sort_numbers_within_5_2_1(self, imgs):
        questions_all = []
        for num in self.nums:
            img = random.choice(imgs)
            questions = [
                {
                    "body": [
                        {
                            "type": "select-position",
                            "title": "选一选",
                            "stem": "选出从",
                            "content": {
                                "position": "left",
                                "num": num,
                                "unit": "{}".format(img[1]),
                                "name": "{}".format(img[2]),
                                "total": 5,
                                "img": "{}".format(img[0])
                            }
                        }
                    ],
                    "answers": [num - 1],  # 正确答案
                    "knowledges": ["5以内数的排序"],  # 知识点，写成数组
                    "resource": "",  # 这里填生产题目具体资源
                    "explain": "",  # 题目相关解析
                    "level": "2",  # 难度等级
                    "type": "选择",  # 题目类型
                    "number": '1-1-6-02',  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 2、    【标题】选一选
    def sort_numbers_within_5_2_2(self, imgs):
        questions_all = []
        for num in self.nums:
            img = random.choice(imgs)
            questions = [
                {
                    "body": [
                        {
                            "type": "select-position",
                            "title": "选一选",
                            "stem": "选出从",
                            "content": {
                                "position": "right",
                                "num": num,
                                "unit": "{}".format(img[1]),
                                "name": "{}".format(img[2]),
                                "total": 5,
                                "img": "{}".format(img[0])
                            }
                        }
                    ],
                    "answers": [5 - num],  # 正确答案
                    "knowledges": ["5以内数的排序"],  # 知识点，写成数组
                    "resource": "",  # 这里填生产题目具体资源
                    "explain": "",  # 题目相关解析
                    "level": "2",  # 难度等级
                    "type": "选择",  # 题目类型
                    "number": '1-1-6-02',  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 3、    【标题】涂一涂
    def sort_numbers_within_5_3(self):
        stem_dic = {1: '一', 2: '二', 3: '三', 4: '四', 5: '五'}
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "title": "涂色题",
                            "stem": "从左起涂第{}个".format(stem_dic[num]),
                            "content": [
                                "5",
                                "{}".format(num)
                            ],  # 第一个数表示共多少个圈，第二个表示涂第几个圈
                            "type": "drag-color-circle"
                        }
                    ],
                    "answers": [num],  # 正确答案表示涂第三个
                    "knowledges": ["5以内数的排序"],
                    "resource": "",
                    "type": "操作",
                    "explain": "",
                    "level": "2",
                    "number": '1-1-6-03'  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 5、	【标题】填一填
    def sort_numbers_within_5_5_1(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "type": "order-fill",
                            "title": "填一填",
                            "stem": "按顺序填一填",
                            "list": [
                                1 if 1 in num else "",
                                2 if 2 in num else "",
                                3 if 3 in num else "",
                                4 if 4 in num else "",
                                5 if 5 in num else "",
                            ]
                        }
                    ],
                    "answers": sorted(set(list(range(1, 6))).difference(set(num))),  # 正确答案
                    "resource": "",  # 这里填生产题目具体资源
                    "explain": "",  # 题目相关解析
                    "knowledges": ["5以内数的排序"],  # 知识点，写成数组
                    "level": "2",  # 难度等级
                    "type": "填空",  # 题目类型
                    "number": '1-1-6-05',  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 5、	【标题】填一填
    def sort_numbers_within_5_5_2(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "type": "order-fill",
                            "title": "填一填",
                            "stem": "按顺序填一填",
                            "list": [
                                5 if 5 in num else "",
                                4 if 4 in num else "",
                                3 if 3 in num else "",
                                2 if 2 in num else "",
                                1 if 1 in num else ""
                            ]
                        }
                    ],
                    "answers": sorted(set(list(range(1, 6))).difference(set(num)), reverse=True),  # 正确答案
                    "resource": "",  # 这里填生产题目具体资源
                    "explain": "",  # 题目相关解析
                    "knowledges": ["5以内数的排序"],  # 知识点，写成数组
                    "level": "2",  # 难度等级
                    "type": "填空",  # 题目类型
                    "number": '1-1-6-05',  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 6、    【标题】解决问题
    def sort_numbers_within_5_6(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "title": "解决问题（素材遮挡素材）",
                            "stem": "从后面数，卡车排第{}".format(num),
                            "backgroundItem": "background/f0894871aade1de8f6513f4608254696.svg",  # 道路背景
                            "content": [
                                {
                                    "type": "general",  # 表示寻常图片类型
                                    "src": "traffic_car/438e4eca099346ac0494f7c2fe764103.svg"  # 图片路径
                                },
                                {
                                    "type": "shelter",  # 表示遮挡物
                                    "src": "trees/592b5eceae806b89b6d602c3aecfc2e9.svg"
                                },
                                {
                                    "type": "general",
                                    "src": "traffic_car/7a0a2529d900672fbc93cd0d23dfa8b0.svg"
                                },
                            ],
                            "result": [
                                [
                                    {
                                        "val": "图中一共有",
                                        "type": "text"
                                    },
                                    {
                                        "val": "",
                                        "type": "input"
                                    },
                                    {
                                        "val": "辆车",
                                        "type": "text"
                                    }
                                ]
                            ],
                            "type": "source-shade",
                            "keyboardtype": "num"
                        }
                    ],
                    "answers": ["{}".format(num)],
                    "knowledges": ["5以内数的排序"],
                    "resource": "",
                    "type": "填空",
                    "explain": "",
                    "level": "2",
                    "number": "1-1-6-06"  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all


# todo 七、5以内数的合与分
class CombSepWithin5(object):
    def __init__(self, nums):
        self.nums = nums

    # 1、    【标题】填一填
    def comb_sep_within_5_1(self, imgs):
        questions_all = []
        for num in self.nums:
            img = random.choice(imgs)
            questions = [
                {
                    "body": [
                        {
                            "type": "look-picture-fill",
                            "title": "填一填",
                            "stem": "看图填数",
                            "splitObj": {
                                "left": {
                                    "img": "{}".format(img[0]),
                                    "num": num[0]
                                },
                                "right": {
                                    "img": "{}".format(img[0]),
                                    "num": num[1]
                                },
                                "sum": num[0] + num[1],  # 总和
                                "item": num[0]  # 拆分子项
                            }
                        }
                    ],
                    "answers": [num[1]],  # 正确答案
                    "resource": "",  # 这里填生产题目具体资源
                    "explain": "",  # 题目相关解析
                    "knowledges": ["5以内数的合与分"],  # 知识点，写成数组
                    "level": "1",  # 难度等级
                    "type": "填空",  # 题目类型
                    "number": '1-1-7-01',  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 3、    【标题】解决问题
    def comb_sep_within_5_3(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "type": "select-divide",
                            "title": "解决问题",
                            "unit": '个',  # 单位
                            "name": "桃子",  # 名称
                            "unit2": '只',  # 单位
                            "name2": "猴子",  # 名称
                            "stem": "他们能分到同样多的",
                            "animal": {
                                "img": 'animal_monkey/793fc4b39c09915005e03c0a5974abf4.svg',  # 图片路径
                                "num": num[0]
                            },  # 动物（上面展示）
                            "thing": {
                                "imgItem": [
                                    'tableware_plate/6e3aab481345454d985eb3169d703e2a.svg',  # 盘子
                                    'fruits/8afcdefaeb0f5edf4f1d45ec4b0acbd7.svg'  # 水果
                                ],
                                "num": num[1]  # 数量--（不能超过5）
                            }  # 分的东西（下面展示）
                        }
                    ],
                    "answers": [0 if num[1] % num[0] == 0 else 1],  # 正确答案 0（能） 和 1（不能）
                    "resource": "",  # 这里填生产题目具体资源
                    "explain": "",  # 题目相关解析
                    "knowledges": ["5以内数的合与分"],  # 知识点，写成数组
                    "level": "2",  # 难度等级
                    "type": "选择",  # 题目类型
                    "number": '1-1-7-03',  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 4、	【标题】填一填
    def comb_sep_within_5_4(self, imgs):
        questions_all = []
        for num in self.nums:
            img = random.choice(imgs)
            questions = [
                {
                    "body": [
                        {
                            "type": "count-things",
                            "title": "填一填",
                            "stem": "从左往右数",
                            "stem2": "合起来有",
                            "sum": 5,  # 和数
                            "unit": "朵",  # 单位
                            "name": "花",  # 名称
                            "list": [
                                "{}".format(img[num[0]]),
                                "{}".format(img[num[1]]),
                                "{}".format(img[num[2]]),
                                "{}".format(img[num[3]]),
                                "{}".format(img[num[4]]),
                            ]  # 从左往右，展示图片列表
                        }
                    ],
                    "answers": [
                        [num.index(1) + 1, num.index(4) + 1],
                        [num.index(2) + 1, num.index(3) + 1],
                        [num.index(4) + 1, num.index(1) + 1],
                        [num.index(3) + 1, num.index(2) + 1]
                    ],  # 正确答案
                    "resource": "",  # 这里填生产题目具体资源
                    "explain": "",  # 题目相关解析
                    "knowledges": ["5以内数的合与分"],  # 知识点，写成数组
                    "level": "3",  # 难度等级
                    "type": "填空",  # 题目类型
                    "number": '1-1-7-04',  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 5、    【标题】填一填
    def comb_sep_within_5_5(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "title": "数的分合",
                            "stem": "看图填数",
                            "content": [
                                [
                                    {
                                        "type": "num",  # 数字类型
                                        "val": "{}".format(num[0])
                                    },
                                    {
                                        "type": "num",
                                        "val": "{}".format(num[1])
                                    }
                                ],  # 第一行数字
                                [
                                    {
                                        "type": "symbol",  # 符号类型
                                        "val": "split"  # split代表拆分 sum代表求和
                                    },
                                    {
                                        "type": "symbol",
                                        "val": "split"
                                    }
                                ],  # 第二行 符号
                                [
                                    {
                                        "type": "num",
                                        "val": "{}".format(num[2])
                                    },
                                    {
                                        "type": "input",  # 输入框
                                        "val": ""
                                    },
                                    {
                                        "type": "input",
                                        "val": ""
                                    },
                                    {
                                        "type": "num",
                                        "val": "{}".format(num[5])
                                    }
                                ],  # 第三行
                                [
                                    {
                                        "type": "symbol",
                                        "val": "sum"
                                    }
                                ],  # 第四行
                                [
                                    {
                                        "type": "input",
                                        "val": ""
                                    },
                                    {
                                        "type": "input",
                                        "val": ""
                                    }
                                ],  # 第五行
                                [
                                    {
                                        "type": "symbol",
                                        "val": "sum"
                                    }
                                ],  # 第六行
                                [
                                    {
                                        "type": "num",
                                        "val": "{}".format(num[8])
                                    }
                                ]  # 第七行
                            ],
                            "type": "num-open-close",
                            "keyboardtype": "num"
                        }
                    ],
                    "answers": [num[3], num[4], num[6], num[7]],
                    "knowledges": ["5以内数的合与分"],
                    "resource": "",
                    "type": "填空",
                    "explain": "",
                    "level": "3",
                    "number": '1-1-7-05'  # 题型编号
                }
            ]
            questions_all.extend(questions)
        return questions_all


# todo 八、0的认识
class Anderstand0(object):
    def __init__(self, nums):
        self.nums = nums

    # 1、	【标题】选一选
    @staticmethod
    def anderstand_0_1():
        questions = [
            {
                "body": [
                    {
                        "type": "choose-zero",
                        "title": "选一选",
                        "stem": "哪张图中有",
                        "num": 0,  # 数字
                        "list": [
                            "zero_number/ad6ebf4e4db9fc2d14d30782acc509be.svg",
                            "zero_number/132a687fd3a9fffb8d498304ec19b132.svg",
                            "background/57f2ecaf3a133833e99a7db8cdf9f684.svg"
                        ]  # 图片；列表
                    }
                ],
                "answers": [0],  # 正确答案
                "resource": "",  # 这里填生产题目具体资源
                "explain": "",  # 题目相关解析
                "knowledges": ["0的认识"],  # 知识点，写成数组
                "level": "1",  # 难度等级
                "type": "选择",  # 题目类型
                "number": '1-1-8-01',  # 题目编号
            }
        ]
        return questions

    # 2、	【标题】填一填
    def anderstand_0_2(self, imgs):
        questions_all = []
        for num in self.nums:
            img = random.choice(imgs)
            questions = [
                {
                    "body": [
                        {
                            "type": "add-up-fill",
                            "title": "填一填",
                            "stem": "数一数，将花朵的数量填到相应的位置",
                            "list": [
                                "{}".format(img[num[0]]),  # 图片路径
                                "{}".format(img[num[1]]),
                                "{}".format(img[num[2]]),
                                "{}".format(img[num[3]]),
                            ]  # 从左往右(不超过5) 展示图片列表
                        }
                    ],
                    "answers": [num[0], num[1], num[2], num[3]],  # 正确答案
                    "resource": "",  # 这里填生产题目具体资源
                    "explain": "",  # 题目相关解析
                    "knowledges": ["0的认识"],  # 知识点，写成数组
                    "level": "1",  # 难度等级
                    "type": "填空",  # 题目类型
                    "number": '1-1-8-02'  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 3、	【标题】选一选
    def anderstand_0_3(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "type": "mean-num",
                            "title": "选一选",
                            "stem": "哪个可以用",
                            "num": '0',  # 数字
                            "stem2": "表示？",
                            "list": [
                                {
                                    "imgItem": [
                                        'tableware_plate/6e3aab481345454d985eb3169d703e2a.svg',  # 盘子
                                        'fruits/8afcdefaeb0f5edf4f1d45ec4b0acbd7.svg'  # 水果
                                    ],
                                    "num": num[0]  # 数量
                                },
                                {
                                    "imgItem": [
                                        'tableware_plate/6e3aab481345454d985eb3169d703e2a.svg',  # 盘子
                                        'fruits/8afcdefaeb0f5edf4f1d45ec4b0acbd7.svg'  # 水果
                                    ],
                                    "num": num[1]  # 数量
                                }
                            ]  # 展示列表
                        }
                    ],
                    "answers": [0 if num[0] == 0 else 1],  # 正确答案(0/1)
                    "resource": "",  # 这里填生产题目具体资源
                    "explain": "",  # 题目相关解析
                    "knowledges": ["0的认识"],  # 知识点，写成数组
                    "level": "1",  # 难度等级
                    "type": "选择",  # 题目类型
                    "number": '1-1-8-03',  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 4、	【标题】填一填
    @staticmethod
    def anderstand_0_4_1():
        questions = [
            {
                "body": [
                    {
                        "type": "zero-order-fill",
                        "title": "填一填",
                        "stem": "按顺序填一填",
                        "list": ["", 1, 2, 3, 4, 5]  # 等式（""空字符代表可填，反之）,
                    }
                ],
                "answers": [0],  # 正确答案
                "resource": "",  # 这里填生产题目具体资源
                "explain": "",  # 题目相关解析
                "knowledges": ["0的认识"],  # 知识点，写成数组
                "level": "2",  # 难度等级
                "type": "填空",  # 题目类型
                "number": '1-1-8-04',  # 题目编号
            }
        ]
        return questions

    # 4、	【标题】填一填
    @staticmethod
    def anderstand_0_4_2():
        questions = [
            {
                "body": [
                    {
                        "type": "zero-order-fill",
                        "title": "填一填",
                        "stem": "按顺序填一填",
                        "list": [5, 4, 3, 2, 1, ""]  # 等式（""空字符代表可填，反之）,
                    }
                ],
                "answers": [0],  # 正确答案
                "resource": "",  # 这里填生产题目具体资源
                "explain": "",  # 题目相关解析
                "knowledges": ["0的认识"],  # 知识点，写成数组
                "level": "2",  # 难度等级
                "type": "填空",  # 题目类型
                "number": '1-1-8-04',  # 题目编号
            }
        ]
        return questions

    # 5、    【标题】填一填
    def anderstand_0_5(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "title": "尺子输入框",
                            "stem": "按照顺序填一填",
                            "content": [
                                "{}".format(num[0]),
                                "{}".format(num[1]),
                                "{}".format(num[2])
                            ],  # 需要填的数
                            "number": '1-1-8-05',  # 题目编号
                            "type": "rule-number",
                            "keyboardtype": "num"
                        }
                    ],
                    "answers": [
                        "{}".format(num[0]),
                        "{}".format(num[1]),
                        "{}".format(num[2])
                    ],  # 正确答案
                    "knowledges": ["0的认识"],
                    "resource": "",
                    "type": "填空",
                    "explain": "",
                    "level": "2",
                    "number": '1-1-8-05'  # 题型编号
                }
            ]
            questions_all.extend(questions)
        return questions_all


# todo 九、10以内数的认识
class AnderstandNumbersWithin10(object):
    def __init__(self, nums):
        self.nums = nums

    # 1.标题：选一选
    def anderstand_numbers_within_10_1(self, imgs):
        questions_all = []
        for num in self.nums:
            img = random.choice(imgs)
            num_shuf = num.copy()
            random.shuffle(num_shuf)
            questions = [
                {
                    "body": [
                        {
                            "title": "数一数",
                            "stem": "表示{}数量的圆".format(img[2]),
                            "content": [
                                {
                                    "src": "{}".format(img[0]),  # 动物路径
                                    "num": num[0]  # 动物个数
                                }
                            ],
                            "answeritem": num_shuf,  # 选项展示
                            "type": "animal-num-sum"
                        }
                    ],
                    "answers": [num[0]],  # 正确选项
                    "knowledges": ["10以内数的认识"],
                    "resource": "",
                    "type": "选择",
                    "explain": "",
                    "level": "1",
                    "number": "1-1-9-01"  # 题型编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 2. 标题：填一填
    def anderstand_numbers_within_10_2(self, imgs):
        questions_all = []
        for num in self.nums:
            img = random.choice(imgs)
            questions = [
                {
                    "body": [
                        {
                            "type": "look-img-fill",
                            "title": "填一填",
                            "stem": "看图写数",
                            "content": {  # 展示的图片
                                "img": "{}".format(img),  # 图片
                                "num": num  # 数量
                            },
                            "dom": num  # dom节点标识，唯一性
                        }
                    ],
                    "answers": [num],  # 正确答案
                    "resource": "resource",  # 这里填生产题目具体资源
                    "explain": "explain",  # 题目相关解析
                    "knowledges": ["10以内数的认识"],  # 知识点，写成数组
                    "level": "1",  # 难度等级
                    "type": "填空",  # 题目类型
                    "number": '1-1-9-02',  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 3. 标题：涂一涂
    def anderstand_numbers_within_10_3(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "type": "coloring-circle",
                            "title": "填一填",
                            "stem": "看数字选择对应个数的圆",
                            "num": num  # 展示的数字
                        }
                    ],
                    "answers": [num],  # 正确答案(所涂圆个数)
                    "resource": "",  # 这里填生产题目具体资源
                    "explain": "",  # 题目相关解析
                    "knowledges": ["10以内数的认识"],  # 知识点，写成数组
                    "level": "1",  # 难度等级
                    "type": "多选",  # 题目类型
                    "number": '1-1-9-03',  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 5.标题：选一选
    def anderstand_numbers_within_10_5_1(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "title": "数字单选框（1-10）",
                            "stem": "有多少个方块",
                            "content": [
                                {
                                    "type": "square",  # 正方形类型 也可换成img类型
                                    "val": "#6DD8FA",  # 正方形颜色，如是img类型，val为图片路径
                                    "num": num  # 数量
                                }
                            ],
                            "type": "number-select"
                        }
                    ],
                    "answers": num,  # 答案
                    "knowledges": ["10以内数的认识"],
                    "resource": "",
                    "type": "选择",
                    "explain": "",
                    "level": "1",
                    "number": '1-1-9-05'  # 题型编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 5.标题：选一选
    def anderstand_numbers_within_10_5_2(self, imgs):
        questions_all = []
        for num in self.nums:
            img = random.choice(imgs)
            questions = [
                {
                    "body": [
                        {
                            "title": "选一选",
                            "stem": "有多少",
                            "type": "count-it",  # 组件名称
                            "unit": '{}'.format(img[1]),  # 单位
                            "name": '{}'.format(img[2]),  # 名称
                            "figure": {  # 数量对象
                                "img": '{}'.format(img[0]),  # 图片路径
                                "num": num  # 图片展示的数量(5以内数)
                            },
                            "keyBoardType": 10,  # 键盘总数（5以内数只能填5）值为5或者10
                        }
                    ],
                    "answers": [num],
                    "knowledges": ["10以内数的认识"],
                    "resource": "",  # 这里填生产题目具体的资源名称
                    "explain": "",  # 题目相关解析
                    "level": "1",  # 难度等级
                    "type": "选择",  # 题目类型
                    "number": '1-1-9-05'  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 6. 标题：选一选
    def anderstand_numbers_within_10_6(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "title": "选一选",
                            "stem": "有多少",
                            "number": '1-1-9-06',  # 题目编号
                            "type": "count-circle",  # 组件名称
                            "total": num,  # 展示圆总数
                            "unit": '个',  # 单位
                            "name": "圆",  # 名称
                        }
                    ],
                    "answers": [num],  # 正确答案
                    "resource": "",  # 这里填生产题目具体资源
                    "explain": "",  # 题目相关解析
                    "knowledges": ["10以内数的认识"],  # 知识点，写成数组
                    "level": "1",  # 难度等级
                    "type": "单选",  # 题目类型
                    "number": '1-1-9-06',  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 8. 标题：选一选
    def anderstand_numbers_within_10_8(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "type": "number-of-figure",
                            "title": "填一填",
                            "stem": "哪组有",
                            "num": num[0],
                            "unit": '个',
                            "name": '方块',
                            "list": [
                                {
                                    "img": 'v2/通用/基本平面图形/正方形_1.svg',
                                    "num": num[1][0]
                                },  # 左边
                                {
                                    "img": 'v2/通用/基本平面图形/正方形_1.svg',
                                    "num": num[1][1]
                                }  # 右边
                            ]  # 展示图形列表
                        }
                    ],
                    "answers": [0 if num[1][0] == num[0] else 1],  # 正确答案（下标 0,1） 值 0 / 1
                    "resource": "",  # 这里填生产题目具体资源
                    "explain": "",  # 题目相关解析
                    "knowledges": ["10以内数的认识"],  # 知识点，写成数组
                    "level": "1",  # 难度等级
                    "type": "选择",  # 题目类型
                    "number": '1-1-9-08',  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 9.标题：放一放
    def anderstand_numbers_within_10_9(self, imgs):
        questions_all = []
        for num in self.nums:
            img = random.choice(imgs)
            questions = [
                {
                    "body": [
                        {
                            "title": "动物连线",
                            "stem": "在图片中放{}{}{}".format(num, img[1], img[2]),
                            "content": [
                                {
                                    "type": "background",  # 公园背景
                                    "src": "address/2dab42777ade0ff96be8395b6c95e58a.svg",  # 背景图片路径
                                    "num": 1
                                },
                                {
                                    "type": "animal",  # 拖拽动物
                                    "src": "{}".format(img[0]),  # 动物图片路径
                                    "num": 10  # 显示的动物数量
                                }
                            ],
                            "results": [num],  # 需要拖拽的个数
                            "type": "animal-drag"
                        }
                    ],
                    "answers": [num],  # 正确答案
                    "knowledges": ["10以内数的认识"],
                    "resource": "",
                    "type": "操作",
                    "explain": "",
                    "level": "1",
                    "number": "1-1-9-09",  # 题型编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 10. 标题：放一放
    def anderstand_numbers_within_10_10(self, imgs):
        questions_all = []
        for num in self.nums:
            img = random.choice(imgs)
            questions = [
                {
                    "body": [
                        {
                            "title": "放一放",
                            "type": "put-the-figure",  # 组件名称
                            "dispense": {
                                "min": "0",
                                "total": "{}".format(num),
                                "itemSrc": "{}".format(img[0]),
                            },
                            "itemUnit": "个",
                            "itemName": "{}".format(img[1]),
                        }
                    ],
                    "answers": ["{}".format(num)],  # 正确答案
                    "resource": "",  # 这里填生产题目具体资源
                    "explain": "",  # 题目相关解析
                    "knowledges": ["10以内数的认识"],  # 知识点，写成数组
                    "level": "1",  # 难度等级
                    "type": "填空",  # 题目类型
                    "number": '1-1-9-10',  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all


# todo 十、10以内数的排序
class SortNumbersWithin10(object):
    def __init__(self, nums):
        self.nums = nums

    # 2. 标题：填一填
    def sort_numbers_within_10_2_1(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "type": "direction-fill-num",
                            "title": "填一填",
                            "stem": {
                                "text": '开始数，第',  # 文本
                                'start': num[0],  # 开始数
                                'sort': num[1],  # 第几个数
                                'unit': '个',  # 单位
                                'name': '数'  # 名称
                            }
                        }
                    ],
                    "answers": [num[0] + num[1] - 1],  # 正确答案
                    "resource": "",  # 这里填生产题目具体资源
                    "explain": "",  # 题目相关解析
                    "knowledges": ["10以内数的排序"],  # 知识点，写成数组
                    "level": "2",  # 难度等级
                    "type": "填空",  # 题目类型
                    "number": '1-1-10-02',  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 2. 标题：填一填
    def sort_numbers_within_10_2_2(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "type": "direction-fill-num",
                            "title": "填一填",
                            "stem": {
                                "text": '开始向后数，第',  # 文本
                                'start': num[0],  # 开始数
                                'sort': num[1],  # 第几个数
                                'unit': '个',  # 单位
                                'name': '数'  # 名称
                            }
                        }
                    ],
                    "answers": [num[0] + num[1] - 1],  # 正确答案
                    "resource": "",  # 这里填生产题目具体资源
                    "explain": "",  # 题目相关解析
                    "knowledges": ["10以内数的排序"],  # 知识点，写成数组
                    "level": "2",  # 难度等级
                    "type": "填空",  # 题目类型
                    "number": '1-1-10-02',  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 2. 标题：填一填
    def sort_numbers_within_10_2_3(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "type": "direction-fill-num",
                            "title": "填一填",
                            "stem": {
                                "text": '开始倒数，第',  # 文本
                                'start': num[0] + num[1] - 1,  # 开始数
                                'sort': num[1],  # 第几个数
                                'unit': '个',  # 单位
                                'name': '数'  # 名称
                            }
                        }
                    ],
                    "answers": [num[0]],  # 正确答案
                    "resource": "",  # 这里填生产题目具体资源
                    "explain": "",  # 题目相关解析
                    "knowledges": ["10以内数的排序"],  # 知识点，写成数组
                    "level": "2",  # 难度等级
                    "type": "填空",  # 题目类型
                    "number": '1-1-10-02',  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 2. 标题：填一填
    def sort_numbers_within_10_2_4(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "type": "direction-fill-num",
                            "title": "填一填",
                            "stem": {
                                "text": '开始向前数，第',  # 文本
                                'start': num[0] + num[1] - 1,  # 开始数
                                'sort': num[1],  # 第几个数
                                'unit': '个',  # 单位
                                'name': '数'  # 名称
                            }
                        }
                    ],
                    "answers": [num[0]],  # 正确答案
                    "resource": "",  # 这里填生产题目具体资源
                    "explain": "",  # 题目相关解析
                    "knowledges": ["10以内数的排序"],  # 知识点，写成数组
                    "level": "2",  # 难度等级
                    "type": "填空",  # 题目类型
                    "number": '1-1-10-02',  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 3. 标题：填一填
    def sort_numbers_within_10_3_1(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "type": "direction-fill-num",
                            "title": "填一填",
                            "stem_two": {
                                "num": num[1],  # 数
                                'position': 'front',  # 方向  前--》front 后--》behind
                                'text': '的数是'
                            }
                        }
                    ],
                    "answers": [num[0]],  # 正确答案
                    "resource": "",  # 这里填生产题目具体资源
                    "explain": "",  # 题目相关解析
                    "knowledges": ["10以内数的排序"],  # 知识点，写成数组
                    "level": "1",  # 难度等级
                    "type": "填空",  # 题目类型
                    "number": '1-1-10-03',  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 3. 标题：填一填
    def sort_numbers_within_10_3_2(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "type": "direction-fill-num",
                            "title": "填一填",
                            "stem_two": {
                                "num": num[0],  # 数
                                'position': 'behind',  # 方向  前--》front 后--》behind
                                'text': '的数是'
                            }
                        }
                    ],
                    "answers": [num[1]],  # 正确答案
                    "resource": "",  # 这里填生产题目具体资源
                    "explain": "",  # 题目相关解析
                    "knowledges": ["10以内数的排序"],  # 知识点，写成数组
                    "level": "1",  # 难度等级
                    "type": "填空",  # 题目类型
                    "number": '1-1-10-03',  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 4.标题：填一填
    def sort_numbers_within_10_4_1(self):
        questions_all = []
        for num in self.nums:
            content_num = ['', '', '', '', '', '', '', '', '', '']
            for i in num:
                content_num[i - 1] = i
            questions = [
                {
                    "body": [
                        {
                            "title": "填一填（多个输入框）",
                            "stem": "按顺序填数",
                            "content": [content_num],  # 1-10中，显示的数为提示得数， “”为需要填的数，不可超过10
                            "showType": "z",  # z形输入
                            "animalImg": "animal_tardigvada_right/6f5c724ea90d5e90d33164e874dee461.svg",  # 昆虫图片地址
                            "houseImg": "house/77abdce8471ab5207a64cc3381b4d8ee.svg",  # 房子图片地址
                            "type": "number-multiple-input",
                            "keyboardtype": "num"
                        }
                    ],
                    "answers": [sorted(set(list(range(1, 11))).difference(num))],  # 答案
                    "knowledges": ["10以内数的排序"],
                    "resource": "",
                    "type": "填空",
                    "explain": "",
                    "level": "2",
                    "number": "1-1-10-04"
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 4.标题：填一填
    def sort_numbers_within_10_4_2(self):
        def f1(x1, x2):
            if x1 in x2:
                return x1
            else:
                return ''

        questions_all = []
        for num in self.nums:
            content_num0 = list(map(lambda x: f1(x, num[0][1]), num[0][0]))
            content_num1 = list(map(lambda x: f1(x, num[1][1]), num[1][0]))
            questions = [
                {
                    "body": [
                        {
                            "title": "填一填（多个输入框）",
                            "stem": "按顺序填数",
                            "content": [
                                content_num0,
                                content_num1
                            ],  # 可提供多组五个以内的数组，每组至少两个提示的数
                            "showType": "s",  # 波浪形输入
                            "animalImg": "animal_tardigvada_right/6f5c724ea90d5e90d33164e874dee461.svg",  # 昆虫图片
                            "type": "number-multiple-input",
                            "keyboardtype": "num"
                        }
                    ],
                    "answers": [
                        sorted(set(num[0][0]).difference(num[0][1])),
                        sorted(set(num[1][0]).difference(num[1][1]), reverse=True)
                    ],  # 正确答案顺序
                    "knowledges": ["10以内数的排序"],
                    "resource": "",
                    "type": "填空",
                    "explain": "",
                    "level": "2",
                    "number": "1-1-10-04"
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 6. 标题：选一选
    def sort_numbers_within_10_6(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "type": "au-mutil-select-text",
                            "title": "选一选",  # 标题
                            "stemSection": "之间的数有",
                            "start": num[0][0],  # 数
                            "end": num[0][1],
                            "answeritem": [
                                {
                                    "text": "{}".format(num[1][0]),
                                    "aligntype": "checkbox-span-tick",
                                },
                                {
                                    "text": "{}".format(num[1][1]),
                                    "aligntype": "checkbox-span-tick",
                                },
                                {
                                    "text": "{}".format(num[1][2]),
                                    "aligntype": "checkbox-span-tick",
                                }
                            ]
                        }
                    ],
                    "answers": sorted(list(map(lambda x: num[1].index(x), list(
                        (set(list(range(num[0][0] + 1, num[0][1])))).intersection(set(num[1])))))),  # 答案是下标 0,1,2
                    "resource": "",
                    "explain": "",
                    "knowledges": ["10以内数的排序"],
                    "level": "2",
                    "type": "选择",
                    "number": "1-1-10-06"
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 7. 标题：填一填
    def sort_numbers_within_10_7(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "type": "law-fill",
                            "title": "选一选",
                            "stem": "按规律填数",
                            "content": {
                                "num": 10,
                                "img": 'fruits/9c51e61782a968ea70809645cb2ba7c3.svg'
                            },
                            "position": ["右边", "左边"],  # 方向-->从右边数 是 左边数的第几个
                            "num": num,
                            "unit": '个',
                            "sort": 'big',  # 序号排序 big(从大到小) small(从小到大) 默认从小到大排序
                            "index": [2, 3, 7],  # 默认展示序号
                        }
                    ],
                    "answers": [10 - num + 1],  # 正确答案
                    "resource": "",  # 这里填生产题目具体资源
                    "explain": "",  # 题目相关解析
                    "knowledges": ["10以内数的排序"],  # 知识点，写成数组
                    "level": "2",  # 难度等级
                    "type": "填空",  # 题目类型
                    "number": '1-1-10-07',  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 8. 标题：选一选
    def sort_numbers_within_10_8(self, imgs):
        questions_all = []
        for num in self.nums:
            img1 = random.sample(imgs, 3)
            img = img1 * 3
            img.append(img[0])
            random.shuffle(img)
            questions = [
                {
                    "body": [
                        {
                            "type": "number-sort",
                            "title": "选一选",
                            "stem": "第1张图片是",
                            "name": "{}".format(img[0][2]),
                            "stem2": "那么第{}张图片是".format(num),
                            "list": [
                                {
                                    "name": "{}".format(img[0][2]),
                                    "img": "{}".format(img[0][0])
                                },
                                {
                                    "name": "{}".format(img[1][2]),
                                    "img": "{}".format(img[1][0])
                                },
                                {
                                    "name": "{}".format(img[2][2]),
                                    "img": "{}".format(img[2][0])
                                },
                                {
                                    "name": "{}".format(img[3][2]),
                                    "img": "{}".format(img[3][0])
                                },
                                {
                                    "name": "{}".format(img[4][2]),
                                    "img": "{}".format(img[4][0])
                                },
                                {
                                    "name": "{}".format(img[5][2]),
                                    "img": "{}".format(img[5][0])
                                },
                                {
                                    "name": "{}".format(img[6][2]),
                                    "img": "{}".format(img[6][0])
                                },
                                {
                                    "name": "{}".format(img[7][2]),
                                    "img": "{}".format(img[7][0])
                                },
                                {
                                    "name": "{}".format(img[8][2]),
                                    "img": "{}".format(img[8][0])
                                },
                                {
                                    "name": "{}".format(img[9][2]),
                                    "img": "{}".format(img[9][0])
                                }
                            ],  # 图片展示列表
                            "index": 1,
                            "sort": "small",  # 序号排序 big(从大到小) small(从小到大) 默认从小到大排序
                            "kindArr": ["{}".format(img1[0][2]), "{}".format(img1[1][2]), "{}".format(img1[2][2])]
                            # 种类列表
                        }
                    ],
                    "answers": [
                        ["{}".format(img1[0][2]),
                         "{}".format(img1[1][2]),
                         "{}".format(img1[2][2])].index(img[num - 1][2])
                    ],  # 0 1 2（答案）
                    "resource": "",
                    "explain": "",
                    "knowledges": ["10以内数的排序"],
                    "level": "1",
                    "type": "选择",
                    "number": "1-1-10-08"
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 9. 标题：填一填
    def sort_numbers_within_10_9(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "type": "near-number",
                            "title": "填一填",
                            "stem": "上面几个数字中",
                            "list": [num[0][0], num[0][1], num[0][2], num[0][3], num[0][4], num[0][5]],  # 数字展示列表
                            "content": [
                                '与{}最接近'.format(num[1][0]),
                                '与{}最接近'.format(num[1][1]),
                                '距离{}最远'.format(num[1][2])],
                        }  # 填空内容列表
                    ],
                    "answers": [num[2][0], num[2][1], num[2][2]],  # 正确答案
                    "resource": "",  # 这里填生产题目具体资源
                    "explain": "",  # 题目相关解析
                    "knowledges": ["10以内数的排序"],  # 知识点，写成数组
                    "level": "2",  # 难度等级
                    "type": "填空",  # 题目类型
                    "number": '1-1-10-09',  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all


# todo 十一、10以内数的大小比较
class ComparNumbersWithin10(object):
    def __init__(self, nums):
        self.nums = nums

    # 1. 标题：选一选
    def compar_numbers_within_10_1(self, imgs):
        questions_all = []
        for num in self.nums:
            img = random.choice(imgs)
            questions = [
                {
                    "body": [
                        {
                            "type": "compare-figure",
                            "title": "选一选",
                            "stem": "哪组更多",
                            "list": [
                                {
                                    "img": '{}'.format(img[0]),  # 展示图形
                                    "num": num[0]  # 数量--》数字类型
                                },
                                {
                                    "img": '{}'.format(img[0]),
                                    "num": num[1]
                                },
                                {
                                    "img": '{}'.format(img[0]),
                                    "num": num[2]
                                }
                            ]
                        }
                    ],
                    "answers": [num.index(max(num))],  # 正确答案（下标 0,1,2）
                    "resource": "",  # 这里填生产题目具体资源
                    "explain": "",  # 题目相关解析
                    "knowledges": ["10以内数的大小比较"],  # 知识点，写成数组
                    "level": "1",  # 难度等级
                    "type": "选择",  # 题目类型
                    "number": '1-1-11-01',  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 2. 标题：选一选
    def compar_numbers_within_10_2(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "type": "compare-much",
                            "title": "选一选",
                            "stem": "{}比{}(){}".format(num[0], num[1], abs(num[0] - num[1])),
                            "list": ['more', 'less'],  # 选择列表  值--》more（多） less（少）
                        }
                    ],
                    "answers": [0 if num[0] > num[1] else 1],  # 正确答案 （下标 0,1）
                    "resource": "",  # 这里填生产题目具体资源
                    "explain": "",  # 题目相关解析
                    "knowledges": ["10以内数的大小比较"],  # 知识点，写成数组
                    "level": "1",  # 难度等级
                    "type": "选择",  # 题目类型
                    "number": '1-1-11-02',  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 3. 标题：比一比
    def compar_numbers_within_10_3(self, imgs):
        questions_all = []
        for num in self.nums:
            img = random.sample(imgs, 2)
            questions = [
                {
                    "body": [
                        {
                            "type": "compare-count",
                            "title": "选一选",
                            "stem": "数一数，比一比",
                            "list": [
                                {
                                    "img": '{}'.format(img[0][0]),
                                    "num": num[0]
                                },  # 上
                                {
                                    "img": '{}'.format(img[1][0]),
                                    "num": num[1]
                                },  # 下
                            ],  # 展示数数量图片列表
                            "compareText": '多' if num[0] > num[1] else '少'  # 比较数量 （多或者少）
                        }
                    ],
                    "answers": [abs(num[0] - num[1])],  # 正确答案 （下标 0,1）
                    "resource": "",  # 这里填生产题目具体资源
                    "explain": "",  # 题目相关解析
                    "knowledges": ["10以内数的大小比较"],  # 知识点，写成数组
                    "level": "2",  # 难度等级
                    "type": "填空",  # 题目类型
                    "number": '1-1-11-03',  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all


# todo 十二、10以内数的合与分
class CombSepWithin10(object):
    def __init__(self, nums):
        self.nums = nums

    # 1. 标题：填一填
    def comb_sep_within_10_1(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "title": "数的分合",
                            "stem": "看图填数",
                            "content": [
                                [
                                    {
                                        "type": "num",  # 代表数字类型
                                        "val": "{}".format(num[0] + num[1])  # 数字
                                    }
                                ],  # 第一行
                                [
                                    {
                                        "type": "symbol",  # 代表运算符类型
                                        "val": "split"  # split代表拆分线， sum代表求和线
                                    }
                                ],  # 第二行
                                [
                                    {
                                        "type": "num",
                                        "val": "{}".format(num[0])
                                    },
                                    {
                                        "type": "input",  # 代表输入框类型
                                        "val": ""  # 默认空值
                                    }
                                ]  # 第三行
                            ],
                            "type": "num-open-close",
                            "keyboardtype": "num"
                        }
                    ],
                    "answers": [num[1]],  # 答案，输入的数
                    "knowledges": ["10以内数的合与分"],  # 知识点
                    "resource": "",
                    "type": "填空",  # 题型
                    "explain": "",
                    "level": "2",  # 难度
                    "number": "1-1-12-01"
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 3. 标题：填一填
    def comb_sep_within_10_3(self):
        questions_all = []
        for num in self.nums:
            questions = [
                {
                    "body": [
                        {
                            "title": "数的分合",
                            "stem": "看图填数",
                            "content": [
                                [
                                    {
                                        "type": "num",  # 数字类型（num-数字，symbol-符号， input-输入框）
                                        "val": "{}".format(num[0])  # 数字值
                                    },
                                    {
                                        "type": "num",
                                        "val": "{}".format(num[1])
                                    }
                                ],
                                [
                                    {
                                        "type": "symbol",
                                        "val": "split"  # split-拆分符 sum-求和符
                                    },
                                    {
                                        "type": "symbol",
                                        "val": "split"
                                    }
                                ],
                                [
                                    {
                                        "type": "input",
                                        "val": ""  # 输入框val默认空值
                                    },
                                    {
                                        "type": "input",
                                        "val": ""
                                    },
                                    {
                                        "type": "num",
                                        "val": "{}".format(num[4])
                                    },
                                    {
                                        "type": "input",
                                        "val": ""
                                    }
                                ],
                                [
                                    {
                                        "type": "symbol",
                                        "val": "sum"
                                    }
                                ],
                                [
                                    {
                                        "type": "num",
                                        "val": "{}".format(num[6])
                                    }
                                ]
                            ],
                            "type": "num-open-close",
                            "keyboardtype": "num"
                        }
                    ],
                    "answers": [num[2], num[3], num[5]],  # 答案，输入的数
                    "knowledges": ["10以内数的合与分"],  # 知识点
                    "resource": "",
                    "type": "填空",  # 题型
                    "explain": "",
                    "level": "3",  # 难度
                    "number": "1-1-12-03"
                }
            ]
            questions_all.extend(questions)
        return questions_all

    # 8.标题：选一选
    def comb_sep_within_10_8(self, imgs):
        questions_all = []
        for num in self.nums:
            img = random.choice(imgs)
            questions = [
                {
                    "body": [
                        {
                            "title": "选一选",
                            "stem": "表格中有",
                            "stem2": "还要多少",
                            "stem3": "可以生成",
                            "type": "choose-table",  # 组件名称
                            "total": 10,  # 图形总数
                            "unit": '个',  # 单位
                            "name": '{}'.format(img[1]),  # 名称
                            "figure": {  # 数量对象
                                "img": '{}'.format(img[0]),  # 图片路径
                                "num": num  # 图片展示的数量(10以内数)
                            }
                        }
                    ],
                    "answers": [10 - num],
                    "knowledges": ["10以内数的合与分"],
                    "resource": "",  # 这里填生产题目具体的资源名称
                    "explain": "",  # 题目相关解析
                    "level": "1",  # 难度等级
                    "type": "选择",  # 题目类型
                    "number": '1-1-12-08',  # 题目编号
                }
            ]
            questions_all.extend(questions)
        return questions_all
