from draw import q_CreatImgs
import random


class LoationQuestions(object):
    def __init__(self):
        self.count = 0

    # todo 1-5-1-01 看图填一填
    def CognitionFrontAndBack(self):
        all_questions = []
        dup_questions = []
        for i in range(30):
            mix_list = []
            images_animals_url = q_CreatImgs.UpImages().FrontAndBack()
            mix_list.extend(random.sample(images_animals_url, 2))
            print(mix_list[0][1], mix_list[1][1])
            questions = [
                {
                    "body": [
                        {
                            "title": "看图填一填",
                            "stem": "看图填一填",  # 标题
                            "backgroundImg": "v2/通用/地点/草坪2.svg",  # 草坪背景
                            "animalImg": [
                                mix_list[0][0],  # 前面的动物路径
                                mix_list[1][0]  # 后面的动物路径
                            ],
                            "inputList": [
                                [
                                    {
                                        "type": "keyword",  # 关键字类型：需高亮显示的关键字
                                        "value": mix_list[0][1]  # 关键字内容
                                    },
                                    {
                                        "type": "text",  # 普通文本类型
                                        "value": "在"  # 文本内容
                                    },
                                    {
                                        "type": "keyword",
                                        "value": mix_list[1][1]
                                    },
                                    {
                                        "type": "text",
                                        "value": "的"
                                    },
                                    {
                                        "type": "str",  # 方位字符类型输入框
                                        "value": ""  # 空值
                                    },
                                    {
                                        "type": "text",
                                        "value": "面"
                                    }
                                ],  # 一个数组代表一行内容
                                [
                                    {
                                        "type": "keyword",
                                        "value": mix_list[1][1]
                                    },
                                    {
                                        "type": "text",
                                        "value": "在"
                                    },
                                    {
                                        "type": "keyword",
                                        "value": mix_list[0][1]
                                    },
                                    {
                                        "type": "text",
                                        "value": "的"
                                    },
                                    {
                                        "type": "str",
                                        "value": ""
                                    },
                                    {
                                        "type": "text",
                                        "value": "面"
                                    }
                                ]
                            ],
                            "type": "pos-sequence-realize-input",  # 组件名
                            "keyboardtype": "txt"  # 方向键盘
                        }
                    ],
                    "answers": [
                        "前",
                        "后"
                    ],  # 答案
                    "knowledges": [
                        "认识前后"
                    ],  # 知识点
                    "resource": "resource",
                    "type": "填空",  # 题型
                    "explain": "explain",
                    "level": "1",  # 难度
                    "number": "1-5-1-01"  # 题型编号
                }

            ]
            dup_questions.extend(questions)
        for dup in dup_questions:
            if dup not in all_questions:
                all_questions.append(dup)
        return all_questions

    # todo 1-5-1-02 看图填一填
    def CognitionFrontAndBack2(self):
        all_questions = []
        dup_questions = []
        for i in range(30):
            mix_list = []
            images_animals_url = q_CreatImgs.UpImages().FrontAndBack()
            mix_list.extend(random.sample(images_animals_url, 4))
            questions = [
                {
                    "body": [
                        {
                            "title": "看图填一填",
                            "stem": "看图填一填",  # 标题
                            "animalImg": [
                                mix_list[0][0],
                                mix_list[1][0],
                                mix_list[2][0],
                                mix_list[3][0]
                            ],  # 依次四个动物路径
                            "inputList": [
                                [
                                    {
                                        "type": "img",  # 图片类型
                                        "value": mix_list[2][0]  # 图片资源路径
                                    },
                                    {
                                        "type": "text",  # 普通文本类型
                                        "value": "在"  # 文本内容
                                    },
                                    {
                                        "type": "img",
                                        "value": mix_list[0][0]
                                    },
                                    {
                                        "type": "text",
                                        "value": "和"
                                    },
                                    {
                                        "type": "img",
                                        "value": mix_list[1][0]
                                    },
                                    {
                                        "type": "str",  # 方向文字输入框
                                        "value": ""  # 空值
                                    },
                                    {
                                        "type": "text",
                                        "value": "面"
                                    }
                                ]
                            ],
                            "type": "pos-sequence-input2",  # 组件名
                            "keyboardtype": "txt"  # 方向文字键盘
                        }
                    ],
                    "answers": [
                        "后"
                    ],  # 答案
                    "knowledges": [
                        "认识前后"
                    ],  # 知识点
                    "resource": "resource",
                    "type": "填空",  # 题型
                    "explain": "explain",
                    "level": "1",  # 难度
                    "number": "1-5-1-02"  # 题型编号
                }
            ]
            dup_questions.extend(questions)
        for dup in dup_questions:
            if dup not in all_questions:
                all_questions.append(dup)
        return all_questions

    # todo 1-5-1-03 看图选一选
    def CognitionFrontAndBack3(self):
        all_questions = []
        dup_questions = []
        for i in range(30):
            mix_list = []
            showtype_list = [1, 2]
            images_house_url, images_tree_url = q_CreatImgs.UpImages().HouseAndLoaction()
            mix_list.extend(random.sample(images_house_url, 1))
            mix_list.extend(random.sample(images_tree_url, 1))
            # showtype=random.choice(showtype_list)
            # if showtype==1:
            questions = [
                {
                    "body": [
                        {
                            "title": "看图选一选",
                            "stem": "看图选一选",  # 标题
                            "imgType": "后",  # 背景图的类型 - -前、后
                            "inputList": [  # 问题行
                                [
                                    {
                                        "type": "text",
                                        "value": "房屋的"
                                    },
                                    {
                                        "type": "str",  # 输入框
                                        "value": "？"  # 必须填中文的？号，表示输入框不可输入
                                    },
                                    {
                                        "type": "text",
                                        "value": "面有"
                                    },
                                    {
                                        "type": "img",  # 图片类型
                                        "value": "v2/通用/植物/树木/树_16.svg"  # 图片资源路径（图中路径暂未更新）
                                    }
                                ]
                            ],
                            "options": [
                                "前",
                                "后"
                            ],  # 选项
                            "type": "pos-sequence-select"  # 组件
                        }
                    ],
                    "answers": [
                        "后"
                    ],  # 答案，选项中的某一个
                    "knowledges": [
                        "认识前后"
                    ],  # 知识点
                    "resource": "resource",
                    "type": "选择",  # 题型
                    "explain": "explain",
                    "level": "1",  # 难度
                    "number": "1-2-5-03"  # 题型编号
                }
            ]
            dup_questions.extend(questions)
        for dup in dup_questions:
            if dup not in all_questions:
                all_questions.append(dup)
        return all_questions

    # todo 1-5-1-04 看图填一填
    def CognitionFrontAndBack4(self):
        all_questions = []
        dup_questions = []
        for i in range(30):
            mix_list = []
            images_animals_url = q_CreatImgs.UpImages().FrontAndBack()
            mix_list.extend(random.sample(images_animals_url, 5))
            questions = [
                {
                    "body": [
                        {
                            "title": "看图填一填",
                            "stem": "看图填一填",  # 标题
                            "animalImg": [  # 排列的动物资源路径
                                mix_list[0][0],
                                mix_list[1][0],
                                mix_list[2][0],
                                mix_list[3][0],
                                mix_list[4][0]
                            ],
                            "inputList": [  # 输入行
                                [
                                    {
                                        "type": "img",  # 图片类型
                                        "value": mix_list[2][0]  # 图片资源路径
                                    },
                                    {
                                        "type": "text",  # 文字类型
                                        "value": "的"
                                    },
                                    {
                                        "type": "str",  # 方向字符输入框
                                        "value": ""  # 空值
                                    },
                                    {
                                        "type": "text",
                                        "value": "面是"
                                    },
                                    {
                                        "type": "img",
                                        "value": mix_list[3][0]
                                    }
                                ]
                            ],
                            "dragList": [  # 拖动目标行
                                [
                                    {
                                        "type": "str",  # 可供拖进的框
                                        "value": ""  # 空值
                                    },
                                    {
                                        "type": "text",  # 文字类型
                                        "value": "的前面是"  # 值
                                    },
                                    {
                                        "type": "img",  # 图片类型
                                        "value": mix_list[3][0]  # 图片资源路径
                                    }
                                ]
                            ],
                            "type": "pos-sequence-dragInput",  # 组件名
                            "keyboardtype": "txt"  # 方向文字键盘
                        }
                    ],
                    "answers": [
                        "后",
                        4
                    ],  # 答案： 输入行输入的值、与拖动行拖入图片项的下标
                    "knowledges": [
                        "认识前后"
                    ],  # 知识点
                    "resource": "resource",
                    "type": "操作",  # 题型 - --带拖动的题型都定义为操作
                    "explain": "explain",
                    "level": "1",  # 难度
                    "number": "1-5-1-04"  # 题型编号
                }
            ]
            dup_questions.extend(questions)
        for dup in dup_questions:
            if dup not in all_questions:
                all_questions.append(dup)
        return all_questions

    # todo 1-5-1-05 看图选一选
    def CognitionFrontAndBack5(self):
        all_questions = []
        dup_questions = []
        for i in range(30):
            mix_list = []
            images_people_url = q_CreatImgs.UpImages().XiaoBaoRun()
            mix_list.extend(random.sample(images_people_url, 3))
            questions = [
                {
                    "body": [
                        {
                            "title": "看图填一填",  # 标题
                            "inputList": [  # 题目内容
                                [
                                    {
                                        "type": "text",  # 普通文本类型
                                        "value": "三人赛跑，"
                                    },
                                    {
                                        "type": "keyword",  # 关键字类型
                                        "value": mix_list[1][1]
                                    },
                                    {
                                        "type": "text",
                                        "value": "在"
                                    },
                                    {
                                        "type": "keyword",
                                        "value": mix_list[0][1]
                                    },
                                    {
                                        "type": "text",
                                        "value": "的后面，"
                                    },
                                    {
                                        "type": "keyword",
                                        "value": mix_list[2][1]
                                    },
                                    {
                                        "type": "text",
                                        "value": "的前面。选出那个是"
                                    },
                                    {
                                        "type": "keyword",
                                        "value": mix_list[1][1]
                                    },
                                    {
                                        "type": "text",
                                        "value": "？"
                                    }
                                ]
                            ],
                            "content": [  # 人物选项资源路径
                                {
                                    "src": mix_list[0][0]
                                },
                                {
                                    "src": mix_list[1][0]
                                },
                                {
                                    "src": mix_list[2][0]
                                }
                            ],
                            "type": "pos-sequence-select2"  # 组件名
                        }
                    ],
                    "answers": [
                        1
                    ],  # 答案，选中人物的下标
                    "knowledges": [
                        "认识前后"
                    ],  # 知识点
                    "resource": "resource",
                    "type": "选择",  # 题型
                    "explain": "explain",
                    "level": "2",  # 难度
                    "number": "1-2-4-05"  # 题型编号
                }
            ]
            dup_questions.extend(questions)
        for dup in dup_questions:
            if dup not in all_questions:
                all_questions.append(dup)
        return all_questions

    # todo  1-5-1-06 看图填一填
    def CognitionFrontAndBack6(self):
        all_questions = []
        dup_questions = []
        for i in range(30):
            mix_list = []
            images_animals_url = q_CreatImgs.UpImages().FrontAndBack()
            mix_list.extend(random.sample(images_animals_url, 3))
            questions = [
                {
                    "body": [
                        {
                            "title": "看图填一填",
                            "stem": "动物们正在向前走，管理员一声下：向后转，此时：",  # 题目内容
                            "animalImg": [
                                mix_list[0][0],
                                mix_list[1][0],
                                mix_list[2][0],
                            ],  # 依次三个动物路径
                            "inputList": [
                                [
                                    {
                                        "type": "keyword",  # 关键字类型：需要高亮的文字
                                        "value": mix_list[2][1],  # 关键字内容
                                    },
                                    {
                                        "type": "text",  # 普通文本类型
                                        "value": "在"  # 普通文本内容
                                    },
                                    {
                                        "type": "keyword",
                                        "value": mix_list[1][1]
                                    },
                                    {
                                        "type": "str",  # 方向文字输入框
                                        "value": ""  # 空值
                                    },
                                    {
                                        "type": "text",
                                        "value": "面"
                                    }
                                ]
                            ],
                            "type": "pos-sequence-input3",  # 组件名
                            "keyboardtype": "txt"  # 方向文字键盘
                        }
                    ],
                    "answers": [
                        "前"
                    ],  # 答案
                    "knowledges": [
                        "认识前后"
                    ],  # 知识点
                    "resource": "resource",
                    "type": "填空",  # 题型
                    "explain": "explain",
                    "level": "2",  # 难度
                    "number": "1-5-1-06"  # 题型编码
                }
            ]
            dup_questions.extend(questions)
        for dup in dup_questions:
            if dup not in all_questions:
                all_questions.append(dup)
        return all_questions

    # todo 1-5-1-07  拖一拖，排排序
    def CognitionFrontAndBack7(self):
        all_questions = []
        dup_questions = []
        for i in range(30):
            mix_list = []
            sorted_list = []
            answer_list = []
            mid_list = []
            images_animals_url = q_CreatImgs.UpImages().FrontAndBack()
            mid_list.extend(random.sample(images_animals_url, 4))
            sorted_list.extend([mid_list[0], mid_list[1], mid_list[2], mid_list[3]])
            for mid in mid_list:
                mix_list.append(mid)
            random.shuffle(mix_list)
            for mix in mix_list:
                if mix == sorted_list[0]:
                    answer_list.append(mix_list.index(mix) + 1)
                    for mix1 in mix_list:
                        if mix1 == sorted_list[1]:
                            answer_list.append(mix_list.index(mix1) + 1)
                            for mix2 in mix_list:
                                if mix2 == sorted_list[2]:
                                    answer_list.append(mix_list.index(mix2) + 1)
                                    for mix3 in mix_list:
                                        if mix3 == sorted_list[3]:
                                            answer_list.append(mix_list.index(mix3) + 1)

            print("mid_list", mid_list)
            print("sorted_list", sorted_list)
            print("mix_list", mix_list)
            print("answer_list", answer_list)

            questions = [
                {
                    "body": [
                        {
                            "title": "拖一拖，排排序。",  # 标题
                            "inputList": [  # 题目信息(如有题目错乱情况，请调整对象中value字段值长度)
                                [
                                    {
                                        "type": "keyword",  # 关键字
                                        "value": mid_list[0][1]
                                    },
                                    {
                                        "type": "text",  # 普通文本
                                        "value": "站在"
                                    },
                                    {
                                        "type": "keyword",
                                        "value": mid_list[1][1]
                                    },
                                    {
                                        "type": "text",
                                        "value": "的前面，"
                                    },
                                    {
                                        "type": "keyword",
                                        "value": mid_list[3][1]
                                    },
                                    {
                                        "type": "text",
                                        "value": "站在"
                                    },
                                    {
                                        "type": "keyword",
                                        "value": mid_list[2][1]
                                    },
                                    {
                                        "type": "text",
                                        "value": "的"
                                    },
                                    {
                                        "type": "text",
                                        "value": "后面，"
                                    },
                                    {
                                        "type": "keyword",
                                        "value": mid_list[1][1]
                                    },
                                    {
                                        "type": "text",
                                        "value": "站在"
                                    },
                                    {
                                        "type": "keyword",
                                        "value": mid_list[2][1]
                                    },
                                    {
                                        "type": "text",
                                        "value": "的前面。请按照从前"
                                    },
                                    {
                                        "type": "text",
                                        "value": "往后的顺序给他们排排队。"
                                    }
                                ]
                            ],
                            "content": [  # 动物资源路径信息
                                {
                                    "order": 1,  # 原始的顺序  用于答案排序
                                    "src": mix_list[0][0]
                                },
                                {
                                    "order": 2,
                                    "src": mix_list[1][0]
                                },
                                {
                                    "order": 3,
                                    "src": mix_list[2][0]
                                },
                                {
                                    "order": 4,
                                    "src": mix_list[3][0]
                                }
                            ],
                            "type": "pos-sequence-dragSort"
                        }
                    ],
                    "answers": answer_list,  # 答案，对应拖动完成后的动物order字段值
                    "knowledges": [
                        "认识前后"
                    ],  # 知识点
                    "resource": "resource",
                    "type": "操作",  # 题型
                    "explain": "explain",
                    "level": "2",  # 难度
                    "number": "1-2-4-07"  # 题型编号
                }
            ]
            dup_questions.extend(questions)
        for dup in dup_questions:
            if dup not in all_questions:
                all_questions.append(dup)
        return all_questions

    # todo 1-5-1-08  拖一拖，排排序
    def CognitionFrontAndBack8(self):
        all_questions = []
        dup_questions = []
        for i in range(28):
            mix_list = []
            sorted_list = []
            answer_list = []
            mid_list = []
            images_animals_url = q_CreatImgs.UpImages().FrontAndBack()
            mid_list.extend(random.sample(images_animals_url, 3))
            sorted_list.extend([mid_list[0], mid_list[1], mid_list[2]])
            for mid in mid_list:
                mix_list.append(mid)
            random.shuffle(mix_list)
            for mix in mix_list:
                if mix == sorted_list[0]:
                    answer_list.append(mix_list.index(mix) + 1)
                    for mix1 in mix_list:
                        if mix1 == sorted_list[1]:
                            answer_list.append(mix_list.index(mix1) + 1)
                            for mix2 in mix_list:
                                if mix2 == sorted_list[2]:
                                    answer_list.append(mix_list.index(mix2) + 1)

            print("mid_list", mid_list)
            print("sorted_list", sorted_list)
            print("mix_list", mix_list)
            print("answer_list", answer_list)

            questions = [
                {
                    "body": [
                        {
                            "title": "拖一拖，排排序。",  # 标题
                            "inputList": [  # 题目内容 （如有文本错乱情况，请适当调整value字段长短）
                                [
                                    {
                                        "type": "keyword",  # 关键字
                                        "value": sorted_list[0][1] + "、" + sorted_list[1][1] + "和" + sorted_list[2][1]
                                    },
                                    {
                                        "type": "text",  # 普通文本
                                        "value": "比赛跑步。"
                                    },
                                    {
                                        "type": "keyword",
                                        "value": mid_list[0][1]
                                    },
                                    {
                                        "type": "text",
                                        "value": "在"
                                    },
                                    {
                                        "type": "keyword",
                                        "value": mid_list[1][1]
                                    },
                                    {
                                        "type": "text",
                                        "value": "之前到达终点"
                                    },
                                    {
                                        "type": "text",
                                        "value": "，"
                                    },
                                    {
                                        "type": "keyword",
                                        "value": mid_list[2][1]
                                    },
                                    {
                                        "type": "text",
                                        "value": "在"
                                    },
                                    {
                                        "type": "keyword",
                                        "value": mid_list[0][1]
                                    },
                                    {
                                        "type": "text",
                                        "value": "之"
                                    },
                                    {
                                        "type": "text",
                                        "value": "后到达终点，"
                                    },
                                    {
                                        "type": "keyword",
                                        "value": mid_list[2][1]
                                    },
                                    {
                                        "type": "text",
                                        "value": "不是最后一名，请给"
                                    },
                                    {
                                        "type": "text",
                                        "value": "他们三个排名次。"
                                    }
                                ]
                            ],
                            "content": [  # 操作项 动物资源路径
                                {
                                    "order": 1,  # 初始排序， 用于返回答案
                                    "src": mix_list[0][0]
                                },
                                {
                                    "order": 2,
                                    "src": mix_list[1][0]
                                },
                                {
                                    "order": 3,
                                    "src": mix_list[2][0]
                                }
                            ],
                            "type": "pos-sequence-dragSort"  # 组件名
                        }
                    ],
                    "answers": [answer_list[0], answer_list[2], answer_list[1]],  # 答案， 对应图片排序后的order值
                    "knowledges": [
                        "认识前后"
                    ],  # 知识点
                    "resource": "resource",
                    "type": "操作",  # 题型
                    "explain": "explain",
                    "level": "3",  # 难度
                    "number": "1-2-4-08"  # 题型编号
                }
            ]
            dup_questions.extend(questions)
        for dup in dup_questions:
            if dup not in all_questions:
                all_questions.append(dup)
        return all_questions

    # todo 1-5-1-09 拖一拖，排排序
    def CognitionFrontAndBack9(self):
        all_questions = []
        dup_questions = []
        for i in range(30):
            mix_list = []
            mid_list = []
            images_character_url = q_CreatImgs.UpImages().SortedCharacter()
            mid_list.extend(random.sample(images_character_url, 4))
            answer_list = [mid_list[2][1], mid_list[0][1], mid_list[1][1]]
            for mid in range(3):
                mix_list.append(mid_list[mid])
            random.shuffle(mix_list)
            print("answer_list", answer_list)
            print("mid_list", mid_list)
            print("mix_list", mix_list)
            questions = [
                {
                    "body": [
                        {
                            "title": "拖一拖，排排序。",
                            "dragItem": [mid_list[0][1], mid_list[1][1], mid_list[2][1]],  # 可拖动的人物选项名
                            "content": [
                                {
                                    "type": "input",  # 拖入框类型
                                    "value": "",  # 传空值
                                    "src": mix_list[0][0]  # 拖入框上方人物资源路径
                                },
                                {
                                    "type": "input",
                                    "value": "",
                                    "src": mix_list[1][0]
                                },
                                {
                                    "type": "text",  # 文字类型
                                    "value": mid_list[3][1],  # 人物名
                                    "src": mid_list[3][0]  # 文字上面人物资源路径
                                },
                                {
                                    "type": "input",
                                    "value": "",
                                    "src": mix_list[2][0]
                                }
                            ],
                            "inputList": [  # 提示信息行（如有文本错乱情况请调整对象长度，可适当分为多个对象，或合为一个对象）
                                [
                                    {
                                        "type": "text",  # 普通文本类型
                                        "value": "(1)"  # 文本内容
                                    },
                                    {
                                        "type": "keyword",  # 关键字类型
                                        "value": mid_list[0][1]  # 关键字内容
                                    },
                                    {
                                        "type": "text",
                                        "value": "在"
                                    },
                                    {
                                        "type": "keyword",
                                        "value": mid_list[3][1]
                                    },
                                    {
                                        "type": "text",
                                        "value": "前面。"
                                    }
                                ],  # 一组代表一行
                                [
                                    {
                                        "type": "text",
                                        "value": "(2)从后往前数，"
                                    },
                                    {
                                        "type": "keyword",
                                        "value": mid_list[1][1]
                                    },
                                    {
                                        "type": "text",
                                        "value": "排第1，"
                                    },
                                    {
                                        "type": "keyword",
                                        "value": mid_list[2][1]
                                    },
                                    {
                                        "type": "text",
                                        "value": "排第"
                                    },
                                    {
                                        "type": "text",
                                        "value": "4"
                                    }
                                ]
                            ],
                            "type": "pos-sequence-dragSort2"
                        }
                    ],
                    "answers": answer_list,  # 答案  拖入框中对应的选项
                    "knowledges": [
                        "认识前后"
                    ],  # 知识点
                    "resource": "resource",
                    "type": "操作",
                    "explain": "explain",
                    "level": "2",
                    "number": "1-5-1-09"
                }
            ]
            dup_questions.extend(questions)
        for dup in dup_questions:
            if dup not in all_questions:
                all_questions.append(dup)
        return all_questions

    # todo 1-5-1-10 看图填一填
    def CognitionFrontAndBack10(self):
        all_questions = []
        dup_questions = []
        for i in range(30):
            mix_list = []
            platform_list = ["购物广场", "南湖公园", "动物园", "新华书店"]
            platform = platform_list.index(random.choice(platform_list))
            platforms = platform + 1
            questions = [
                {
                    "body": [
                        {
                            "title": "填一填",
                            "stem": "看图填一填。",  # 标题
                            "backgroundImg": "v2/组件/认识前后/公交与公交站.svg",  # 背景图
                            "animalImg": [],  # 传空
                            "inputList": [
                                [
                                    {
                                        "type": "text",  # 普通文本类型
                                        "value": "从"  # 普通文本内容
                                    },
                                    {
                                        "type": "keyword",  # 关键字
                                        "value": "人民医院"  # 关键字内容
                                    },
                                    {
                                        "type": "text",
                                        "value": "到"
                                    },
                                    {
                                        "type": "keyword",
                                        "value": platform_list[platform]
                                    },
                                    {
                                        "type": "text",
                                        "value": "一共有"
                                    },
                                    {
                                        "type": "num",  # 数字输入框
                                        "value": ""  # 空值
                                    },
                                    {
                                        "type": "text",
                                        "value": "站"
                                    }
                                ]
                            ],
                            "type": "pos-sequence-realize-input",  # 组件
                            "keyboardtype": "num"  # 数字输入框
                        }
                    ],
                    "answers": [
                        platforms
                    ],  # 答案
                    "knowledges": [
                        "认识前后"
                    ],  # 知识点
                    "resource": "resource",
                    "type": "填空",  # 题型
                    "explain": "explain",
                    "level": "2",  # 难度
                    "number": "1-5-1-10"  # 题型编号
                }
            ]
            dup_questions.extend(questions)
        for dup in dup_questions:
            if dup not in all_questions:
                all_questions.append(dup)
        return all_questions

    # todo 1-5-1-11 填一填
    def CognitionFrontAndBack11(self):
        all_questions = []
        dup_questions = []
        for i in range(30):
            mix_list = []
            platform_list = ["老虎园", "鸟园", "金鱼池", "孔雀家园"]
            platform = platform_list.index(random.choice(platform_list))
            if platform_list[platform] != "老虎园":
                platforms = platform
                questions = [
                    {
                        "body": [
                            {
                                "title": "填一填",
                                "stem": "填一填。",  # 标题
                                "startPoint": "猴园",  # 起始点，决定图上小蓝点的位置
                                "inputList": [  # 输入行信息
                                    [
                                        {
                                            "type": "text",  # 普通文本类型
                                            "value": "从"  # 文本内容
                                        },
                                        {
                                            "type": "keyword",  # 关键字
                                            "value": "猴园"  # 关键字
                                        },
                                        {
                                            "type": "text",
                                            "value": "到"
                                        },
                                        {
                                            "type": "keyword",
                                            "value": platform_list[platform]
                                        },
                                        {
                                            "type": "text",
                                            "value": "还要经过"
                                        },
                                        {
                                            "type": "num",  # 数字输入框
                                            "value": ""  # 传空值
                                        },
                                        {
                                            "type": "text",
                                            "value": "个景点"
                                        }
                                    ]  # 一组代表一行
                                ],
                                "type": "pos-sequence-input4",  # 组件名
                                "keyboardtype": "num"  # 数字键盘
                            }
                        ],
                        "answers": [
                            platforms
                        ],  # 答案，代表输入数字
                        "knowledges": [
                            "认识前后"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "填空",  # 题型
                        "explain": "explain",
                        "level": "2",  # 难度
                        "number": "1-5-1-11"  # 题型编码
                    }
                ]
                dup_questions.extend(questions)
            for dup in dup_questions:
                if dup not in all_questions:
                    all_questions.append(dup)
            return all_questions

    # todo 1-5-2-01 选一选
    def ToChoiceA(self):
        all_questions = []
        dup_questions = []
        for i in range(30):
            mix_list = []
            answer_list = []
            showtype_list = [1, 2]
            life_cube_url, life_cuboid_url, life_globe_url, life_cylinder_url = q_CreatImgs.UpImages().LifeSolid()
            mix_list.extend(random.sample(life_globe_url, 2))
            showtype = random.choice(showtype_list)
            if showtype == 1:
                questions = [
                    {
                        "body": [
                            {
                                "title": "看图选一选",
                                "stem": "选中桌子上面的物体。",  # 题目
                                "tableImg": "v2/通用/家具/桌子5.svg",  # 桌子资源路径
                                "objectImg": [
                                    mix_list[0][0],
                                    mix_list[1][0]
                                ],  # 物体的资源路径 （可传不同物体、最多可传三个，传三个物体的时候，前两个在桌子上）
                                "position": [
                                    17,  # 桌子上范围[3, 29]
                                    12.8  # 桌子下范围[7, 25]，如超出前端自动转为默认值
                                ],  # 桌子上下的物体与左侧的距离，依次对应上下两个物体，如果是三个物体，则前两个展示在桌子上方，第三个为桌子下位置
                                "type": "pos-sequence-select3"  # 组件名
                            }
                        ],
                        "answers": [
                            0
                        ],  # 答案 物体在objectImg内对应的下标
                        "knowledges": [
                            "认识上下"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "选择",  # 题型
                        "explain": "explain",
                        "level": "1",  # 难度
                        "number": "1-5-2-01"  # 题型编号
                    }
                ]
            if showtype == 2:
                questions = [
                    {
                        "body": [
                            {
                                "title": "看图选一选",
                                "stem": "选中桌子下面的物体。",  # 题目
                                "tableImg": "v2/通用/家具/桌子5.svg",  # 桌子资源路径
                                "objectImg": [
                                    mix_list[0][0],
                                    mix_list[1][0]
                                ],  # 物体的资源路径 （可传不同物体、最多可传三个，传三个物体的时候，前两个在桌子上）
                                "position": [
                                    17,  # 桌子上范围[3, 29]
                                    12.8  # 桌子下范围[7, 25]，如超出前端自动转为默认值
                                ],  # 桌子上下的物体与左侧的距离，依次对应上下两个物体，如果是三个物体，则前两个展示在桌子上方，第三个为桌子下位置
                                "type": "pos-sequence-select3"  # 组件名
                            }
                        ],
                        "answers": [
                            1
                        ],  # 答案 物体在objectImg内对应的下标
                        "knowledges": [
                            "认识上下"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "选择",  # 题型
                        "explain": "explain",
                        "level": "1",  # 难度
                        "number": "1-5-2-01"  # 题型编号
                    }
                ]
            dup_questions.extend(questions)
        for dup in dup_questions:
            if dup not in all_questions:
                all_questions.append(dup)
        return all_questions

    # todo 1-5-2-02 选一选
    def ToChoiceA1(self):
        all_questions = []
        dup_questions = []
        for i in range(30):
            mix_list = []
            showtype_list = [1, 2]
            images_animal_url, images_plant_url = q_CreatImgs.UpImages().PlantAndAnimal()
            mix_list.extend(random.sample(images_animal_url, 2))
            mix_list.extend(random.sample(images_plant_url, 1))
            random.shuffle(mix_list)
            showtype = random.choice(showtype_list)
            if showtype == 1:
                questions = [
                    {
                        "body": [
                            {
                                "title": "看图选一选",
                                "stem": "选一选，哪个在最上面。",  # 标题
                                "objectImg": [
                                    mix_list[0][1],
                                    mix_list[1][1],
                                    mix_list[2][1]
                                ],  # m物体图片
                                "type": "pos-sequence-select4"  # 组件名
                            }
                        ],
                        "answers": [
                            0
                        ],  # 答案，所选图案下标
                        "knowledges": [
                            "认识上下"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "选择",  # 题型
                        "explain": "explain",
                        "level": "1",  # 难度
                        "number": "1-5-2-02"  # 题型编号
                    }
                ]
            if showtype == 2:
                questions = [
                    {
                        "body": [
                            {
                                "title": "看图选一选",
                                "stem": "选一选，哪个在最下面。",  # 标题
                                "objectImg": [
                                    mix_list[0][1],
                                    mix_list[1][1],
                                    mix_list[2][1]
                                ],  # m物体图片
                                "type": "pos-sequence-select4"  # 组件名
                            }
                        ],
                        "answers": [
                            2
                        ],  # 答案，所选图案下标
                        "knowledges": [
                            "认识上下"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "选择",  # 题型
                        "explain": "explain",
                        "level": "1",  # 难度
                        "number": "1-5-2-02"  # 题型编号
                    }
                ]
            dup_questions.extend(questions)
        for dup in dup_questions:
            if dup not in all_questions:
                all_questions.append(dup)
        return all_questions

    # todo 1-5-2-03 填一填
    def ToChoiceA2(self):
        dup_questions = []
        all_questions = []
        for i in range(30):
            mix_list = []
            abstract_list = ["眼睛", "眉毛", "嘴巴"]
            answer_list = []
            mix_list.extend(abstract_list)
            random.shuffle(mix_list)
            if mix_list[0] == "眼睛" and mix_list[1] == "眉毛" and mix_list[2] == "嘴巴":
                answer_list.append(["下", "上"])
                questions = [
                    {
                        "body": [
                            {
                                "title": "填一填",
                                "stem": "填一填。",  # 标题
                                "inputList": [  # 题目内容
                                    [
                                        {
                                            "type": "keyword",  # 关键字类型
                                            "value": mix_list[0]  # 内容
                                        },
                                        {
                                            "type": "text",  # 普通文本类型
                                            "value": "在"  # 内容
                                        },
                                        {
                                            "type": "keyword",
                                            "value": mix_list[1]
                                        },
                                        {
                                            "type": "text",
                                            "value": "的"
                                        },
                                        {
                                            "type": "str",  # 方向文字输入框
                                            "value": ""  # 传空值
                                        },
                                        {
                                            "type": "text",
                                            "value": "面。在"
                                        },
                                        {
                                            "type": "keyword",
                                            "value": mix_list[2]
                                        },
                                        {
                                            "type": "text",
                                            "value": "的"
                                        },
                                        {
                                            "type": "str",
                                            "value": ""
                                        },
                                        {
                                            "type": "text",
                                            "value": "面。"
                                        }
                                    ]
                                ],
                                "type": "pos-sequence-input5",  # 组件名
                                "keyboardtype": "txt"  # 方向文字键盘
                            }
                        ],
                        "answers": answer_list,  # 输入框答案
                        "knowledges": [
                            "认识上下"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "填空",  # 题型
                        "explain": "explain",
                        "level": "1",  # 难度
                        "number": "1-5-2-03"  # 题型编号
                    }
                ]
            if mix_list[0] == "眼睛" and mix_list[1] == "嘴巴" and mix_list[2] == "眉毛":
                answer_list.append(["上", "下"])
                questions = [
                    {
                        "body": [
                            {
                                "title": "填一填",
                                "stem": "填一填。",  # 标题
                                "inputList": [  # 题目内容
                                    [
                                        {
                                            "type": "keyword",  # 关键字类型
                                            "value": mix_list[0]  # 内容
                                        },
                                        {
                                            "type": "text",  # 普通文本类型
                                            "value": "在"  # 内容
                                        },
                                        {
                                            "type": "keyword",
                                            "value": mix_list[1]
                                        },
                                        {
                                            "type": "text",
                                            "value": "的"
                                        },
                                        {
                                            "type": "str",  # 方向文字输入框
                                            "value": ""  # 传空值
                                        },
                                        {
                                            "type": "text",
                                            "value": "面。在"
                                        },
                                        {
                                            "type": "keyword",
                                            "value": mix_list[2]
                                        },
                                        {
                                            "type": "text",
                                            "value": "的"
                                        },
                                        {
                                            "type": "str",
                                            "value": ""
                                        },
                                        {
                                            "type": "text",
                                            "value": "面。"
                                        }
                                    ]
                                ],
                                "type": "pos-sequence-input5",  # 组件名
                                "keyboardtype": "txt"  # 方向文字键盘
                            }
                        ],
                        "answers": answer_list,  # 输入框答案
                        "knowledges": [
                            "认识上下"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "填空",  # 题型
                        "explain": "explain",
                        "level": "1",  # 难度
                        "number": "1-5-2-03"  # 题型编号
                    }
                ]
            if mix_list[0] == "眉毛" and mix_list[1] == "眼睛" and mix_list[2] == "嘴巴":
                answer_list.append(["上", "上"])
                questions = [
                    {
                        "body": [
                            {
                                "title": "填一填",
                                "stem": "填一填。",  # 标题
                                "inputList": [  # 题目内容
                                    [
                                        {
                                            "type": "keyword",  # 关键字类型
                                            "value": mix_list[0]  # 内容
                                        },
                                        {
                                            "type": "text",  # 普通文本类型
                                            "value": "在"  # 内容
                                        },
                                        {
                                            "type": "keyword",
                                            "value": mix_list[1]
                                        },
                                        {
                                            "type": "text",
                                            "value": "的"
                                        },
                                        {
                                            "type": "str",  # 方向文字输入框
                                            "value": ""  # 传空值
                                        },
                                        {
                                            "type": "text",
                                            "value": "面。在"
                                        },
                                        {
                                            "type": "keyword",
                                            "value": mix_list[2]
                                        },
                                        {
                                            "type": "text",
                                            "value": "的"
                                        },
                                        {
                                            "type": "str",
                                            "value": ""
                                        },
                                        {
                                            "type": "text",
                                            "value": "面。"
                                        }
                                    ]
                                ],
                                "type": "pos-sequence-input5",  # 组件名
                                "keyboardtype": "txt"  # 方向文字键盘
                            }
                        ],
                        "answers": answer_list,  # 输入框答案
                        "knowledges": [
                            "认识上下"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "填空",  # 题型
                        "explain": "explain",
                        "level": "1",  # 难度
                        "number": "1-5-2-03"  # 题型编号
                    }
                ]
            if mix_list[0] == "嘴巴" and mix_list[1] == "眼睛" and mix_list[2] == "眉毛":
                answer_list.append(["下", "下"])
                questions = [
                    {
                        "body": [
                            {
                                "title": "填一填",
                                "stem": "填一填。",  # 标题
                                "inputList": [  # 题目内容
                                    [
                                        {
                                            "type": "keyword",  # 关键字类型
                                            "value": mix_list[0]  # 内容
                                        },
                                        {
                                            "type": "text",  # 普通文本类型
                                            "value": "在"  # 内容
                                        },
                                        {
                                            "type": "keyword",
                                            "value": mix_list[1]
                                        },
                                        {
                                            "type": "text",
                                            "value": "的"
                                        },
                                        {
                                            "type": "str",  # 方向文字输入框
                                            "value": ""  # 传空值
                                        },
                                        {
                                            "type": "text",
                                            "value": "面。在"
                                        },
                                        {
                                            "type": "keyword",
                                            "value": mix_list[2]
                                        },
                                        {
                                            "type": "text",
                                            "value": "的"
                                        },
                                        {
                                            "type": "str",
                                            "value": ""
                                        },
                                        {
                                            "type": "text",
                                            "value": "面。"
                                        }
                                    ]
                                ],
                                "type": "pos-sequence-input5",  # 组件名
                                "keyboardtype": "txt"  # 方向文字键盘
                            }
                        ],
                        "answers": answer_list,  # 输入框答案
                        "knowledges": [
                            "认识上下"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "填空",  # 题型
                        "explain": "explain",
                        "level": "1",  # 难度
                        "number": "1-5-2-03"  # 题型编号
                    }
                ]
            dup_questions.extend(questions)
        for dup in dup_questions:
            if dup not in all_questions:
                all_questions.append(dup)
        return all_questions

    # todo 1-5-2-04 填一填
    def ToChoiceA3(self):
        all_questions = []
        dup_questions = []
        for i in range(30):
            mix_list = []
            mid_list = []
            showtype_list = [1, 2]
            answer_list = []
            images_figure_url = q_CreatImgs.UpImages().KartoonFigure()
            mid_list.extend(random.sample(images_figure_url, 3))
            for mid in mid_list:
                mix_list.append([mid, mid_list.index(mid)])
            random.shuffle(mix_list)
            print("mid_list", mid_list)
            print("mix_list", mix_list)
            if mix_list[0][1] > mix_list[1][1]:
                answer_list.append("下")
            else:
                answer_list.append("上")

            showtype = random.choice(showtype_list)
            if showtype == 1:
                questions = [
                    {
                        "body": [
                            {
                                "title": "填一填",
                                "stem": "填一填。",  # 标题
                                "houseImgType": "1",  # 房子的类型，目前提供两种 1或2
                                "personImg": [
                                    mid_list[0],
                                    mid_list[1],
                                    mid_list[2]
                                ],  # 房子中的三个人物头像可随意更换
                                "inputList": [  # 输入框行
                                    [
                                        {
                                            "type": "img",  # 图片类型
                                            "value": mix_list[0][0]  # 图片资源
                                        },
                                        {
                                            "type": "text",  # 文本类型
                                            "value": "在"  # 内容
                                        },
                                        {
                                            "type": "img",
                                            "value": mix_list[1][0]
                                        },
                                        {
                                            "type": "text",
                                            "value": "的"
                                        },
                                        {
                                            "type": "str",  # 方向文字输入框
                                            "value": ""
                                        },
                                        {
                                            "type": "text",
                                            "value": "面。"
                                        }
                                    ]
                                ],
                                "type": "pos-sequence-input6",  # 组件名
                                "keyboardtype": "txt"  # 方向文字键盘
                            }
                        ],
                        "answers": answer_list,  # 答案
                        "knowledges": [
                            "认识上下"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "填空",  # 题型
                        "explain": "explain",
                        "level": "2",  # 难度
                        "number": "1-5-2-04"  # 题型编码
                    }
                ]

            if showtype == 2:
                questions = [
                    {
                        "body": [
                            {
                                "title": "填一填",
                                "stem": "填一填",  # 标题
                                "houseImgType": "2",  # 房子的类型，目前提供两种 1或2
                                "personImg": [
                                    mid_list[0],
                                    mid_list[1],
                                    mid_list[2]
                                ],  # 房子中的三个人物头像可随意更换
                                "inputList": [  # 输入框行
                                    [
                                        {
                                            "type": "img",  # 图片类型
                                            "value": mix_list[0][0]  # 图片资源
                                        },
                                        {
                                            "type": "text",  # 文本类型
                                            "value": "在"  # 内容
                                        },
                                        {
                                            "type": "img",
                                            "value": mix_list[1][0]
                                        },
                                        {
                                            "type": "text",
                                            "value": "的"
                                        },
                                        {
                                            "type": "str",  # 方向文字输入框
                                            "value": ""
                                        },
                                        {
                                            "type": "text",
                                            "value": "面。"
                                        }
                                    ]
                                ],
                                "type": "pos-sequence-input6",  # 组件名
                                "keyboardtype": "txt"  # 方向文字键盘
                            }
                        ],
                        "answers": answer_list,  # 答案
                        "knowledges": [
                            "认识上下"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "填空",  # 题型
                        "explain": "explain",
                        "level": "2",  # 难度
                        "number": "1-5-2-04"  # 题型编码
                    }
                ]
            dup_questions.extend(questions)
        for dup in dup_questions:
            if dup not in all_questions:
                all_questions.append(dup)
        return all_questions

    # todo 1-5-2-05 填一填
    def ToChoiceA4(self):
        all_questions = []
        dup_questions = []
        for i in range(30):
            mix_list = []
            mid_list = []
            answer_list = []
            first_list = []
            second_list = []
            third_list = []
            images_toy_url, images_stationery_url, images_clothing_url, images_sportEquipment_url = q_CreatImgs.UpImages().ToyAndStationeryEC()
            mid_list.extend(random.sample(images_toy_url, 9))

            first_list.append([mid_list[0], mid_list[1], mid_list[2]])
            second_list.append([mid_list[3], mid_list[4], mid_list[5]])
            third_list.append([mid_list[6], mid_list[7], mid_list[8]])
            # print("second_list", second_list)

            mix_list.append([random.sample(first_list[0], 1)[0], 1])
            mix_list.append([random.sample(second_list[0], 1)[0], 2])
            mix_list.append([random.sample(second_list[0], 1)[0], 2])
            mix_list.append([random.sample(third_list[0], 1)[0], 3])
            random.shuffle(mix_list)
            print("first_list", mix_list[0][1], mix_list[1][1], mix_list[2][1], mix_list[3][1])

            if mix_list[0][1] == mix_list[1][1]:
                print("m", mix_list[0][1], mix_list[3][1])
                mix_list[0], mix_list[3] = mix_list[3], mix_list[0]
                print("y", mix_list[0][1], mix_list[3][1])
            if mix_list[2][1] == mix_list[3][1]:
                mix_list[0], mix_list[3] = mix_list[3], mix_list[0]

            # print("mix_list", mix_list)
            if mix_list[0][1] > mix_list[1][1] and mix_list[2][1] > mix_list[3][1]:
                answer_list.append("上")
                answer_list.append("上")

            if mix_list[0][1] > mix_list[1][1] and mix_list[2][1] < mix_list[3][1]:
                answer_list.append("上")
                answer_list.append("下")

            if mix_list[0][1] < mix_list[1][1] and mix_list[2][1] < mix_list[3][1]:
                answer_list.append("下")
                answer_list.append("下")

            if mix_list[0][1] < mix_list[1][1] and mix_list[2][1] > mix_list[3][1]:
                answer_list.append("下")
                answer_list.append("上")

            questions = [
                {
                    "body": [
                        {
                            "title": "填一填",
                            "stem": "填一填。",  # 标题
                            "toyImg": [
                                third_list[0][0][0],
                                third_list[0][1][0],
                                third_list[0][2][0],
                                second_list[0][0][0],
                                second_list[0][1][0],
                                second_list[0][2][0],
                                first_list[0][0][0],
                                first_list[0][1][0],
                                first_list[0][2][0],
                            ],  # 柜子中依次展示的玩具，可任意更换，也可不放玩具，不放则传空值
                            "inputList": [  # 输入行信息
                                [
                                    {
                                        "type": "img",  # 图片类型
                                        "value": mix_list[0][0][0]  # 图片路径
                                    },
                                    {
                                        "type": "text",  # 文本类型
                                        "value": "在"  # 文本
                                    },
                                    {
                                        "type": "img",
                                        "value": mix_list[1][0][0]
                                    },
                                    {
                                        "type": "text",
                                        "value": "的"
                                    },
                                    {
                                        "type": "str",  # 方向文字输入框
                                        "value": ""  # 空值
                                    },
                                    {
                                        "type": "text",
                                        "value": "面。"
                                    }
                                ],
                                [
                                    {
                                        "type": "img",
                                        "value": mix_list[2][0][0]
                                    },
                                    {
                                        "type": "text",
                                        "value": "在"
                                    },
                                    {
                                        "type": "img",
                                        "value": mix_list[3][0][0]
                                    },
                                    {
                                        "type": "text",
                                        "value": "的"
                                    },
                                    {
                                        "type": "str",
                                        "value": ""
                                    },
                                    {
                                        "type": "text",
                                        "value": "面。"
                                    }
                                ]
                            ],
                            "type": "pos-sequence-input7",  # 组件名
                            "keyboardtype": "txt"  # 方向文字键盘
                        }
                    ],
                    "answers": answer_list,
                    "knowledges": [
                        "认识上下"
                    ],  # 知识点
                    "resource": "resource",
                    "type": "填空",  # 题型
                    "explain": "explain",
                    "level": "2",  # 难度
                    "number": "1-5-2-05"  # 题型编号
                }
            ]
            dup_questions.extend(questions)
        for dup in dup_questions:
            if dup not in all_questions:
                all_questions.append(dup)
        return all_questions

    # todo 1-5-2-06 填一填
    def ToChoiceA5(self):
        all_questions = []
        dup_questions = []
        for i in range(30):
            mix_list = []
            mid_list = []
            answer_list = []
            images_animal_url = q_CreatImgs.UpImages().Bird()
            mid_list.extend(random.sample(images_animal_url, 3))
            for mid in mid_list:
                mix_list.append([mid, mid_list.index(mid)])
            random.shuffle(mix_list)
            print("mid_list", mid_list)
            print("mix_list", mix_list)
            if mix_list[0][1] > mix_list[1][1]:
                answer_list.append("下")
            else:
                answer_list.append("上")

            questions = [
                {
                    "body": [
                        {
                            "title": "填一填",
                            "stem": "填一填。",  # 标题
                            "animalImg": [
                                mid_list[0][1],
                                mid_list[1][1],
                                mid_list[2][1],
                            ],
                            "inputList": [  # 输入框行
                                [
                                    {
                                        "type": "img",  # 图片类型
                                        "value": mix_list[0][0][1]  # 图片路径
                                    },
                                    {
                                        "type": "text",  # 文本类型
                                        "value": "在"  # 值
                                    },
                                    {
                                        "type": "img",
                                        "value": mix_list[1][0][1]
                                    },
                                    {
                                        "type": "text",
                                        "value": "的"
                                    },
                                    {
                                        "type": "str",  # 方向文字输入框
                                        "value": ""  # 空值
                                    },
                                    {
                                        "type": "text",
                                        "value": "面。"
                                    }
                                ]
                            ],
                            "type": "pos-sequence-input8",  # 组件名
                            "keyboardtype": "txt"  # 方向文字输入框
                        }
                    ],
                    "answers": answer_list,  # 答案
                    "knowledges": [
                        "认识上下"
                    ],  # 知识点
                    "resource": "resource",
                    "type": "填空",  # 题型
                    "explain": "explain",
                    "level": "1",  # 难度
                    "number": "1-5-2-06"  # 题型编号
                }
            ]

            dup_questions.extend(questions)
        for dup in dup_questions:
            if dup not in all_questions:
                all_questions.append(dup)
        return all_questions

    # todo 1-5-2-07 填一填
    def ToChoiceA6(self):
        all_questions = []
        dup_questions = []
        for i in range(16):
            showtype_list = [1, 2, 3]
            showtype = random.choice(showtype_list)
            if showtype == 1:
                questions = [
                    {
                        "body": [
                            {
                                "title": "看图填一填",
                                "stem": "看图填一填",  # 题目
                                "animalImg": [
                                    "v2/通用/动物/1-动物基础分类/哺乳动物/哺乳类动物_2组/Left/松鼠_带坚果_L1.svg",  # 树上的动物
                                    "v2/通用/动物/1-动物基础分类/哺乳动物/哺乳类动物_2组/Right/狐狸_R1.svg"  # 树下的动物
                                ],
                                "inputList": [  # 问题行
                                    [
                                        {
                                            "type": "text",  # 文本类型
                                            "value": "（1）"
                                        },
                                        {
                                            "type": "img",  # 图片类型
                                            "value": "v2/通用/动物/1-动物基础分类/哺乳动物/哺乳类动物_2组/Right/狐狸_R1.svg"
                                        },
                                        {
                                            "type": "text",
                                            "value": "在"
                                        },
                                        {
                                            "type": "img",
                                            "value": "v2/通用/植物/树木/树_17.svg"
                                        },
                                        {
                                            "type": "text",
                                            "value": "的"
                                        },
                                        {
                                            "type": "str",  # 方向文字输入框类型
                                            "value": ""
                                        },
                                        {
                                            "type": "text",
                                            "value": "面。"
                                        }
                                    ],  # 一个数组表示一个问题
                                    [
                                        {
                                            "type": "text",
                                            "value": "（2）"
                                        },
                                        {
                                            "type": "img",
                                            "value": "v2/通用/动物/1-动物基础分类/哺乳动物/哺乳类动物_2组/Right/狐狸_R1.svg"
                                        },
                                        {
                                            "type": "text",
                                            "value": "想尽办法，终于让"
                                        },
                                        {
                                            "type": "img",
                                            "value": "v2/通用/动物/1-动物基础分类/哺乳动物/哺乳类动物_2组/Left/松鼠_带坚果_L1.svg"
                                        },
                                        {
                                            "type": "text",
                                            "value": "手里的"
                                        },
                                        {
                                            "type": "text",
                                            "value": "果子从"
                                        },
                                        {
                                            "type": "str",
                                            "value": ""
                                        },
                                        {
                                            "type": "text",
                                            "value": "面掉下来。"
                                        }
                                    ]
                                ],
                                "type": "pos-sequence-input10",
                                "keyboardtype": "txt"
                            }
                        ],
                        "answers": [
                            "下",
                            "上"
                        ],
                        "knowledges": [
                            "认识上下"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "填空",  # 题型
                        "explain": "explain",
                        "level": "1",  # 难度
                        "number": "1-5-2-07"  # 题型编码
                    }
                ]
            if showtype == 2:
                questions = [
                    {
                        "body": [
                            {
                                "title": "看图填一填",
                                "stem": "看图填一填",  # 题目
                                "animalImg": [
                                    "v2/通用/动物/1-动物基础分类/哺乳动物/哺乳类动物_2组/Left/松鼠_带坚果_L1.svg",  # 树上的动物
                                    "v2/通用/动物/1-动物基础分类/哺乳动物/哺乳类动物_2组/Right/狐狸_R1.svg"  # 树下的动物
                                ],
                                "inputList": [  # 问题行
                                    [
                                        {
                                            "type": "text",  # 文本类型
                                            "value": "（1）"
                                        },
                                        {
                                            "type": "img",  # 图片类型
                                            "value": "v2/通用/动物/1-动物基础分类/哺乳动物/哺乳类动物_2组/Right/狐狸_R1.svg"
                                        },
                                        {
                                            "type": "text",
                                            "value": "在"
                                        },
                                        {
                                            "type": "img",
                                            "value": "v2/通用/植物/树木/树_17.svg"
                                        },
                                        {
                                            "type": "text",
                                            "value": "的"
                                        },
                                        {
                                            "type": "str",  # 方向文字输入框类型
                                            "value": ""
                                        },
                                        {
                                            "type": "text",
                                            "value": "面。"
                                        }
                                    ],  # 一个数组表示一个问题
                                    [
                                        {
                                            "type": "text",
                                            "value": "（2）"
                                        },
                                        {
                                            "type": "img",
                                            "value": "v2/通用/动物/1-动物基础分类/哺乳动物/哺乳类动物_2组/Left/松鼠_带坚果_L1.svg"
                                        },
                                        {
                                            "type": "text",
                                            "value": "在"
                                        },
                                        {
                                            "type": "img",
                                            "value": "v2/通用/植物/树木/树_17.svg"
                                        },
                                        {
                                            "type": "text",
                                            "value": "的"
                                        },
                                        {
                                            "type": "str",
                                            "value": ""
                                        },
                                        {
                                            "type": "text",
                                            "value": "面。"
                                        }
                                    ]
                                ],
                                "type": "pos-sequence-input10",
                                "keyboardtype": "txt"
                            }
                        ],
                        "answers": [
                            "下",
                            "上"
                        ],
                        "knowledges": [
                            "认识上下"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "填空",  # 题型
                        "explain": "explain",
                        "level": "1",  # 难度
                        "number": "1-5-2-07"  # 题型编码
                    }
                ]
            if showtype == 3:
                questions = [
                    {
                        "body": [
                            {
                                "title": "看图填一填",
                                "stem": "看图填一填",  # 题目
                                "animalImg": [
                                    "v2/通用/动物/1-动物基础分类/哺乳动物/哺乳类动物_2组/Left/松鼠_带坚果_L1.svg",  # 树上的动物
                                    "v2/通用/动物/1-动物基础分类/哺乳动物/哺乳类动物_2组/Right/狐狸_R1.svg"  # 树下的动物
                                ],
                                "inputList": [  # 问题行
                                    [
                                        {
                                            "type": "text",  # 文本类型
                                            "value": "（1）"
                                        },
                                        {
                                            "type": "img",  # 图片类型
                                            "value": "v2/通用/动物/1-动物基础分类/哺乳动物/哺乳类动物_2组/Left/松鼠_带坚果_L1.svg"
                                        },
                                        {
                                            "type": "text",
                                            "value": "在"
                                        },
                                        {
                                            "type": "img",
                                            "value": "v2/通用/植物/树木/树_17.svg"
                                        },
                                        {
                                            "type": "text",
                                            "value": "的"
                                        },
                                        {
                                            "type": "str",  # 方向文字输入框类型
                                            "value": ""
                                        },
                                        {
                                            "type": "text",
                                            "value": "面。"
                                        }
                                    ],  # 一个数组表示一个问题
                                    [
                                        {
                                            "type": "text",
                                            "value": "（2）"
                                        },
                                        {
                                            "type": "img",
                                            "value": "v2/通用/动物/1-动物基础分类/哺乳动物/哺乳类动物_2组/Right/狐狸_R1.svg"
                                        },
                                        {
                                            "type": "text",
                                            "value": "想尽办法，终于让"
                                        },
                                        {
                                            "type": "img",
                                            "value": "v2/通用/动物/1-动物基础分类/哺乳动物/哺乳类动物_2组/Left/松鼠_带坚果_L1.svg"
                                        },
                                        {
                                            "type": "text",
                                            "value": "手里的"
                                        },
                                        {
                                            "type": "text",
                                            "value": "果子从"
                                        },
                                        {
                                            "type": "str",
                                            "value": ""
                                        },
                                        {
                                            "type": "text",
                                            "value": "面掉下来。"
                                        }
                                    ]
                                ],
                                "type": "pos-sequence-input10",
                                "keyboardtype": "txt"
                            }
                        ],
                        "answers": [
                            "上",
                            "上"
                        ],
                        "knowledges": [
                            "认识上下"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "填空",  # 题型
                        "explain": "explain",
                        "level": "1",  # 难度
                        "number": "1-5-2-07"  # 题型编码
                    }
                ]
            dup_questions.extend(questions)
        for dup in dup_questions:
            if dup not in all_questions:
                all_questions.append(dup)
        return all_questions

    # todo 1-5-2-10 选一选
    def ToChoiceA7(self):
        all_questions = []
        dup_questions = []
        for i in range(10):
            showtype_list = [1, 2, 3, 4]

            showtype = random.choice(showtype_list)
            if showtype == 1:
                questions = [
                    {
                        "body": [
                            {
                                "title": "看图选一选",
                                "stem": "选一选，玩具在几号盒子里？",  # 标题
                                "personImg": "v2/通用/人物/人物头像系列/男孩/8.svg",  # 人物头像
                                "bubbleImg": "v2/组件/认识上下/气泡.svg",  # 气泡资源
                                "textList": [  # 气泡内字体
                                    [
                                        {
                                            "type": "text",  # 普通文本类型
                                            "value": "玩具在"  # 内容
                                        },
                                        {
                                            "type": "keyword",  # 关键字类型
                                            "value": "1号盒子"  # 关键字
                                        },
                                        {
                                            "type": "text",
                                            "value": "下"
                                        },
                                        {
                                            "type": "text",
                                            "value": "面的盒子里，但不"
                                        },
                                        {
                                            "type": "text",
                                            "value": "是"
                                        },
                                        {
                                            "type": "keyword",
                                            "value": "3号盒子"
                                        },
                                        {
                                            "type": "text",
                                            "value": "，也不"
                                        },
                                        {
                                            "type": "text",
                                            "value": "是最下面的盒子。"
                                        }
                                    ]
                                ],
                                "boxImg": [  # 右侧的礼盒与文字信息
                                    {
                                        "text": "1号",  # 显示的文字选项框
                                        "src": "v2/通用/装饰/礼盒_7.svg"  # 礼盒图片资源
                                    },
                                    {
                                        "text": "2号",
                                        "src": "v2/通用/装饰/礼盒_7.svg"
                                    },
                                    {
                                        "text": "3号",
                                        "src": "v2/通用/装饰/礼盒_7.svg"
                                    },
                                    {
                                        "text": "4号",
                                        "src": "v2/通用/装饰/礼盒_7.svg"
                                    }
                                ],
                                "type": "pos-sequence-select5"  # 组件名
                            }
                        ],
                        "answers": [
                            1
                        ],  # 选中项在boxImg内的下标
                        "knowledges": [
                            "认识上下"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "选择",  # 题型
                        "explain": "explain",
                        "level": "2",  # 难度
                        "number": "1-5-2-10"  # 题型编号
                    }
                ]

            if showtype == 2:
                questions = [
                    {
                        "body": [
                            {
                                "title": "看图选一选",
                                "stem": "选一选，玩具在几号盒子里？",  # 标题
                                "personImg": "v2/通用/人物/人物头像系列/男孩/8.svg",  # 人物头像
                                "bubbleImg": "v2/组件/认识上下/气泡.svg",  # 气泡资源
                                "textList": [  # 气泡内字体
                                    [
                                        {
                                            "type": "text",  # 普通文本类型
                                            "value": "玩具在"  # 内容
                                        },
                                        {
                                            "type": "keyword",  # 关键字类型
                                            "value": "1号盒子"  # 关键字
                                        },
                                        {
                                            "type": "text",
                                            "value": "下"
                                        },
                                        {
                                            "type": "text",
                                            "value": "面的盒子里，但不"
                                        },
                                        {
                                            "type": "text",
                                            "value": "是"
                                        },
                                        {
                                            "type": "keyword",
                                            "value": "2号盒子"
                                        },
                                        {
                                            "type": "text",
                                            "value": "，也不"
                                        },
                                        {
                                            "type": "text",
                                            "value": "是最下面的盒子。"
                                        }
                                    ]
                                ],
                                "boxImg": [  # 右侧的礼盒与文字信息
                                    {
                                        "text": "1号",  # 显示的文字选项框
                                        "src": "v2/通用/装饰/礼盒_7.svg"  # 礼盒图片资源
                                    },
                                    {
                                        "text": "2号",
                                        "src": "v2/通用/装饰/礼盒_7.svg"
                                    },
                                    {
                                        "text": "3号",
                                        "src": "v2/通用/装饰/礼盒_7.svg"
                                    },
                                    {
                                        "text": "4号",
                                        "src": "v2/通用/装饰/礼盒_7.svg"
                                    }
                                ],
                                "type": "pos-sequence-select5"  # 组件名
                            }
                        ],
                        "answers": [
                            2
                        ],  # 选中项在boxImg内的下标
                        "knowledges": [
                            "认识上下"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "选择",  # 题型
                        "explain": "explain",
                        "level": "2",  # 难度
                        "number": "1-5-2-10"  # 题型编号
                    }
                ]

            if showtype == 3:
                questions = [
                    {
                        "body": [
                            {
                                "title": "看图选一选",
                                "stem": "选一选，玩具在几号盒子里？",  # 标题
                                "personImg": "v2/通用/人物/人物头像系列/男孩/8.svg",  # 人物头像
                                "bubbleImg": "v2/组件/认识上下/气泡.svg",  # 气泡资源
                                "textList": [  # 气泡内字体
                                    [
                                        {
                                            "type": "text",  # 普通文本类型
                                            "value": "玩具在"  # 内容
                                        },
                                        {
                                            "type": "keyword",  # 关键字类型
                                            "value": "2号盒子"  # 关键字
                                        },
                                        {
                                            "type": "text",
                                            "value": "下"
                                        },
                                        {
                                            "type": "text",
                                            "value": "面的盒子里,"
                                        },
                                        {
                                            "type": "text",
                                            "value": "但不"
                                        },
                                        {
                                            "type": "text",
                                            "value": "是最下面的盒子。"
                                        }
                                    ]
                                ],
                                "boxImg": [  # 右侧的礼盒与文字信息
                                    {
                                        "text": "1号",  # 显示的文字选项框
                                        "src": "v2/通用/装饰/礼盒_7.svg"  # 礼盒图片资源
                                    },
                                    {
                                        "text": "2号",
                                        "src": "v2/通用/装饰/礼盒_7.svg"
                                    },
                                    {
                                        "text": "3号",
                                        "src": "v2/通用/装饰/礼盒_7.svg"
                                    },
                                    {
                                        "text": "4号",
                                        "src": "v2/通用/装饰/礼盒_7.svg"
                                    }
                                ],
                                "type": "pos-sequence-select5"  # 组件名
                            }
                        ],
                        "answers": [
                            2
                        ],  # 选中项在boxImg内的下标
                        "knowledges": [
                            "认识上下"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "选择",  # 题型
                        "explain": "explain",
                        "level": "2",  # 难度
                        "number": "1-5-2-10"  # 题型编号
                    }
                ]

            if showtype == 4:
                questions = [
                    {
                        "body": [
                            {
                                "title": "看图选一选",
                                "stem": "选一选，玩具在几号盒子里？",  # 标题
                                "personImg": "v2/通用/人物/人物头像系列/男孩/8.svg",  # 人物头像
                                "bubbleImg": "v2/组件/认识上下/气泡.svg",  # 气泡资源
                                "textList": [  # 气泡内字体
                                    [
                                        {
                                            "type": "text",  # 普通文本类型
                                            "value": "玩具在"  # 内容
                                        },
                                        {
                                            "type": "keyword",  # 关键字类型
                                            "value": "2号盒子"  # 关键字
                                        },
                                        {
                                            "type": "text",
                                            "value": "上"
                                        },
                                        {
                                            "type": "text",
                                            "value": "面的盒子里。"
                                        },
                                    ]
                                ],
                                "boxImg": [  # 右侧的礼盒与文字信息
                                    {
                                        "text": "1号",  # 显示的文字选项框
                                        "src": "v2/通用/装饰/礼盒_7.svg"  # 礼盒图片资源
                                    },
                                    {
                                        "text": "2号",
                                        "src": "v2/通用/装饰/礼盒_7.svg"
                                    },
                                    {
                                        "text": "3号",
                                        "src": "v2/通用/装饰/礼盒_7.svg"
                                    },
                                    {
                                        "text": "4号",
                                        "src": "v2/通用/装饰/礼盒_7.svg"
                                    }
                                ],
                                "type": "pos-sequence-select5"  # 组件名
                            }
                        ],
                        "answers": [
                            0
                        ],  # 选中项在boxImg内的下标
                        "knowledges": [
                            "认识上下"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "选择",  # 题型
                        "explain": "explain",
                        "level": "2",  # 难度
                        "number": "1-5-2-10"  # 题型编号
                    }
                ]

            dup_questions.extend(questions)
        for dup in dup_questions:
            if dup not in all_questions:
                all_questions.append(dup)
        return all_questions

    #todo 1-5-1-11 看图填一填
    def ToChoiceA8(self):
        all_questions=[]
        dup_questions=[]
        for i in range(30):
            answer_list=[]
            standard_list=[3,4,5,6,7,8,9]
            issue_list=[]
            standard=random.choice(standard_list)
            for star in range(1,standard-1):
                issue_list.append(star)
            print("issue_list",issue_list)
            below=random.choice(issue_list)
            above=standard-below-1
            present_floor=below+1
            answer_list.append(present_floor)
            answer_list.append(standard)

            print("总的层数",standard)
            print("下面有几层",below)
            print("上面有几层",above)
            print("当前层",present_floor)
            questions=[
                {
                    "body": [
                        {
                            "title": "看图填一填",
                            "stem": "看图填一填", # 标题
                        "houseImg": "v2/组件/认识上下/单楼层.svg", # 房子图片
            "personImg": "v2/通用/人物/人物头像系列/女孩/19.svg", # 人物图片
            "bubbleImg": "v2/组件/认识上下/气泡2.svg", # 气泡图片
            "textList": [ # 气泡文字
            [
                {
                    "type": "text",
                    "value": "我家上面有"+str(above)+"层，下面有"+str(below)+"层。"
                }
            ]
            ],
            "inputList": [ # 输入行的信息
            [
                {
                    "type": "img", # 图片类型
            "value": "v2/通用/人物/人物头像系列/女孩/19.svg" # 图片资源
            },
            {
                "type": "text", # 文本类型
            "value": "家在" # 文本
            },
            {
                "type": "num", # 数字输入框
            "value": "" # 空值
            },
            {
                "type": "text",
                "value": "层，"
            },
            {
                "type": "text",
                "value": "这栋楼一共有"
            },
            {
                "type": "num",
                "value": ""
            },
            {
                "type": "text",
                "value": "层"
            }
            ]
            ],
            "type": "pos-sequence-input9", # 组件名
            "keyboardtype": "num" # 数字键盘
            }
            ],
            "answers": answer_list, # 答案
            "knowledges": [
                "认识上下"
            ], # 知识点
            "resource": "resource",
            "type": "填空", # 题型
            "explain": "explain",
            "level": "2", # 难度
            "number": "1-5-2-11" # 题型编号
            }
            ]
            dup_questions.extend(questions)
        for dup in dup_questions:
            if dup not in all_questions:
                all_questions.append(dup)
        return all_questions

    #todo 1-5-3-01  看图选一选
    def LeftAndRight(self):
        all_questions=[]
        dup_questions=[]
        for i in range(10):
            mix_list = []
            questions=[
                {
                    "body": [
                        {
                            "title": "看图选一选",
                            "stem": "选一选，辰辰的哪只手拎着书包？", # 标题（可以换成哪只手拿着书包，以及替换别的素材）
            "personList": [ # 人物信息
            {
                "name": "", # 传空
            "src": "v2/通用/人物/人物_front/辰辰.svg" # 人物资源图片
            }
            ],
            "options": [
                "左",
                "右"
            ], # 选项
            "type": "pos-sequence-select6" # 组件名
            }
            ],
            "answers": [
                "右"
            ], # 答案
            "knowledges": [
                "认识左右"
            ], # 知识点
            "resource": "resource",
            "type": "选择", # 题型
            "explain": "explain",
            "level": "1", # 难度
            "number": "1-5-3-01" # 题型编号
            }
            ]
            dup_questions.extend(questions)
        for dup in dup_questions:
            if dup not in all_questions:
                all_questions.append(dup)
        return all_questions

    #todo 1-5-3-02 看图选一选
    def LeftAndRight1(self):
        all_questions=[]
        dup_questions=[]
        for i in range(30):
            images_character_url=q_CreatImgs.UpImages().RightAndLeftCharacter()
            mid_list=[]
            mix_list=[]
            answer_list=[]
            mid_list.extend(random.sample(images_character_url,2))
            mix_list.append([mid_list[0],1])
            mix_list.append([mid_list[1],2])
            random.shuffle(mix_list)
            print("mid_list",mid_list)
            print("mix_list",mix_list)
            if mix_list[0][1] > mix_list[1][1]:
                answer_list.append("右")
            elif mix_list[0][1] < mix_list[1][1]:
                answer_list.append("左")

            questions=[
                {
                    "body": [
                        {
                "title": "看图选一选",
                "stem": "选一选，"+mid_list[0][1]+"在"+mid_list[1][1]+"的哪边？", # 标题
            "personList": [
                              {
                                  "name": mix_list[0][0][1],
                                  "src": mix_list[0][0][0]
                              },
                              {
                                  "name": mix_list[1][0][1],
                                  "src": mix_list[1][0][0]
                              }
                          ], # 两个人务的名字和图片路径
            "options": [
                "左",
                "右"
            ], # 选项
            "type": "pos-sequence-select6" # 组件名
            }
            ],
            "answers":answer_list, # 答案
            "knowledges": [
                "认识左右"
            ], # 知识点
            "resource": "resource",
            "type": "选择", # 题型
            "explain": "explain",
            "level": "1", # 难度
            "number": "1-5-3-02" # 题型编号
            }
            ]
            dup_questions.extend(questions)
        for dup in dup_questions:
            if dup not in all_questions:
                all_questions.append(dup)
        return all_questions


    #todo 1-5-3-03 看图填一填
    def LeftAndRight2(self):
        questions=[
            {
                "body": [
                    {
                        "title": "看图填一填",
                        "stem": "看图填一填",
                        "personImg": [ # 人物路径及信息
                        {
                            "name": "小明", # 人物名
                            "src": "v2/通用/人物/人物_手上拿物品系列/辰辰.svg" # 路径
        },
        {
            "name": "红红",
            "src": "v2/通用/人物/人物_手上拿物品系列/月月.svg"
        }
        ],
        "inputList": [ # 答题行信息，如有位置错乱，请调整对象value值的长度，适当分为多个对象或合为一个对象
        [
            {
                "type": "text", # 文本类型
        "value": "（1）"
        },
        {
            "type": "keyword", # 关键字类型
        "value": "小明"
        },
        {
            "type": "str", # 字符文字输入框
        "value": "" # 传空值
        },
        {
            "type": "text",
            "value": "手里拿着铅笔，"
        },
        {
            "type": "str",
            "value": ""
        },
        {
            "type": "text",
            "value": "手"
        },
        {
            "type": "text",
            "value": "里拿着书包。"
        }
        ], # 一个数组代表一行文本信息
              [
                  {
                      "type": "text",
                      "value": "（2）"
                  },
                  {
                      "type": "keyword",
                      "value": "红红"
                  },
                  {
                      "type": "str",
                      "value": ""
                  },
                  {
                      "type": "text",
                      "value": "手里拿着风车。"
                  }
              ],
              [
                  {
                      "type": "text",
                      "value": "（3）"
                  },
                  {
                      "type": "keyword",
                      "value": "小明"
                  },
                  {
                      "type": "text",
                      "value": "站在"
                  },
                  {
                      "type": "keyword",
                      "value": "红红"
                  },
                  {
                      "type": "text",
                      "value": "的"
                  },
                  {
                      "type": "str",
                      "value": ""
                  },
                  {
                      "type": "text",
                      "value": "边，"
                  },
                  {
                      "type": "keyword",
                      "value": "红红"
                  },
                  {
                      "type": "text",
                      "value": "站在"
                  },
                  {
                      "type": "keyword",
                      "value": "小明"
                  },
                  {
                      "type": "text",
                      "value": "的"
                  },
                  {
                      "type": "str",
                      "value": ""
                  },
                  {
                      "type": "text",
                      "value": "边"
                  }
              ]
        ],
        "type": "pos-sequence-input11", # 组件名
        "keyboardtype": "txt" # 方向文字键盘
        }
        ],
        "answers": [
            "右",
            "左",
            "左",
            "右",
            "左"
        ], # 答案，依次从左到右，从上到下输入框的值
        "knowledges": [
            "认识左右"
        ], # 知识点
        "resource": "resource",
        "type": "填空", # 题型
        "explain": "explain",
        "level": "2", # 难度
        "number": "1-5-3-03" # 题型编码
        }
        ]

        return questions

    #todo 1-5-3-06 连一连
    def LeftAndRight3(self):
        all_questions=[]
        dup_questions = []
        for i in range(20):
            answer_list=[]
            mix_list=[]
            images_finger_url=q_CreatImgs.UpImages().Finger()
            mix_list.extend(random.sample(images_finger_url,4))
            random.shuffle(mix_list)
            for mix in mix_list:
                if mix[1]=="左手":
                    answer_list.append([mix_list.index(mix),0])
                elif mix[1]=="右手":
                    answer_list.append([mix_list.index(mix),1])
            print("mix_list",mix_list)
            print("answer_list",answer_list)
            questions=[
                {
                    "body": [
                        {
                            "title": "连一连",
                            "stem": "连一连", # 标题
                        "content": [
                                       [
                                           {
                                               "val": mix_list[0][0],
                                               "type": "img"
                                           },
                                           {
                                               "val": mix_list[1][0],
                                               "type": "img"
                                           },
                                           {
                                               "val": mix_list[2][0],
                                               "type": "img"
                                           },
                                           {
                                               "val": mix_list[3][0],
                                               "type": "img"
                                           }
                                       ], # 左边图片资源
                                   [
                                       {
                                           "val": "左手",
                                           "type": "text"
                                       },
                                       {
                                           "val": "右手",
                                           "type": "text"
                                       }
                                   ] # 右边手文字
            ],
            "type": "pos-sequence-connect" # 组件名
            }
            ],
            "answers": answer_list, # 答案
            "knowledges": [
                "认识左右"
            ], # 知识点
            "resource": "resource",
            "type": "操作", # 题型
            "explain": "explain",
            "level": "2", # 难度
            "number": "1-5-3-06" # 组件编码
            }
            ]
            dup_questions.extend(questions)
        for dup in dup_questions:
            if dup not in all_questions:
                all_questions.append(dup)
        return all_questions


    #todo 1-5-3-07 连一连
    def LeftAndRight4(self):
        all_questions=[]
        dup_questions=[]
        for i in range(20):
            mix_list=[]
            mid_list=[]
            mid_next_list=[]
            answer_list=[]
            images_flower_url=q_CreatImgs.UpImages().Flower()
            mid_list.extend(random.sample(images_flower_url,3))
            for mid in mid_list:
                mid_next_list.append(mid)
            random.shuffle(mid_next_list)
            mix_list.append([mid_next_list[0],0])
            mix_list.append([mid_next_list[1],2])
            mix_list.append([mid_next_list[2],1])
            print("mid_list",mid_list)
            print("mid_next_list",mid_next_list)
            print("mix_list",mix_list)

            for mid1 in mid_list:
                for mix in mix_list:
                    if mid1==mix[0]:
                        # print("mid1",mid_list.index(mid1))
                        # print("mix",mix[1])
                        answer_list.append([mid_list.index(mid1),mix[1]])
            print("answer_list",answer_list)
            questions=[
                {
                    "body": [
                        {
                            "title": "连一连",
                            "stem": "根据要求连一连", # 标题
                        "vaseImg": "v2/通用/235数数/0-5支花/0支花_2.svg", # 花瓶资源路径
            "content": [
                {
                    "val": mid_list[0][0],
                    "type": "img"
                },
                {
                    "val": mid_list[1][0],
                    "type": "img"
                },
                {
                    "val": mid_list[2][0],
                    "type": "img"
                }
            ], # 花资源路径列表
            "inputList": [
                [
                    {
                        "type": "text", # 普通文本类型
                    "value": "（1）"
            },
            {
                "type": "img", # 图片类型
            "value": mix_list[0][0][0],
            "title": mix_list[0][0][1]
            },
            {
                "type": "text",
                "value": "放在"
            },
            {
                "type": "keyword", # 关键字类型
            "value": "最左边"
            },
            {
                "type": "text",
                "value": "的瓶子里。"
            }
            ], # 一个数组代表一行，如有显示错乱。请调整单个对象的value长度
                                  [
                                      {
                                          "type": "text",
                                          "value": "（2）"
                                      },
                                      {
                                          "type": "img",
                                          "value": mix_list[1][0][0],
                                          "title": mix_list[1][0][1]
                                      },
                                      {
                                          "type": "text",
                                          "value": "放在"
                                      },
                                      {
                                          "type": "keyword",
                                          "value": "最右边"
                                      },
                                      {
                                          "type": "text",
                                          "value": "的瓶子里。"
                                      }
                                  ],
                                  [
                                      {
                                          "type": "text",
                                          "value": "（3）"
                                      },
                                      {
                                          "type": "img",
                                          "value": mix_list[2][0][0],
                                          "title": mix_list[2][0][1]
                                      },
                                      {
                                          "type": "text",
                                          "value": "在"
                                      },
                                      {
                                          "type": "img",
                                          "value": mix_list[1][0][0],
                                          "title": mix_list[1][0][1]
                                      },
                                      {
                                          "type": "keyword",
                                          "value": "左边"
                                      },
                                      {
                                          "type": "text",
                                          "value": "。"
                                      }
                                  ]
            ],
            "type": "pos-sequence-connect2" # 组件名
            }
            ], # 提示信息列表
            # "answers": answer_list, # 答案"{[0,1];[1,0];[2,2]}"
            "answers": "{"+str(answer_list[0])+";"+str(answer_list[1])+";"+str(answer_list[2])+"}", # 答案"{[0,1];[1,0];[2,2]}"
            "knowledges": [
                "认识左右"
            ], # 知识点
            "resource": "resource",
            "type": "操作", # 题型
            "explain": "explain",
            "level": "1", # 难度
            "number": "1-5-3-07" # 题型编号
            }
            ]
            print("questions",questions)
            dup_questions.extend(questions)
        for dup in dup_questions:
            if dup not in all_questions:
                all_questions.append(dup)
        return all_questions


    #todo 1-5-3-08 选一选
    def LeftAndRight5(self):
        all_questions=[]
        dup_questions = []
        for i in range(20):
            images_hat_url=q_CreatImgs.UpImages().HatRightAndLeft()
            mix_list=[]
            showtype_list=[1,2]
            mix_list.extend(images_hat_url)
            random.shuffle(mix_list)
            showtype=random.choice(showtype_list)
            if showtype==1:
                questions=[
                    {
                        "body": [
                            {
                                "title": "选一选",
                                "stem": "根据要求选一选",
                                "content": [
                                    mix_list[0][0],
                                    mix_list[1][0],
                                    mix_list[2][0],
                                    mix_list[3][0],
                                    mix_list[4][0]
                                ], # 帽子图片资源
                            "inputList": [
                    [
                        {
                            "type": "text", # 普通文本
                        "value": "（1）"
                },
                {
                    "type": "keyword", # 关键字
                "value": "小明"
                },
                {
                    "type": "text",
                    "value": "的帽子在"
                },
                {
                    "type": "img", # 图片类型
                "value": mix_list[1][0],
                "title": mix_list[1][1]
                },
                {
                    "type": "text",
                    "value": "的"
                },
                {
                    "type": "keyword",
                    "value": "右边"
                },
                {
                    "type": "text",
                    "value": "，"
                },
                {
                    "type": "img",
                    "value": mix_list[3][0],
                    "title": mix_list[3][1]
                },
                {
                    "type": "text",
                    "value": "的"
                },
                {
                    "type": "keyword",
                    "value": "左边，"
                },
                {
                    "type": "text",
                    "value": "把它选出来。"
                }
                ], # 一个数组代表一行
                [
                    {
                        "type": "text",
                        "value": "（2）"
                    },
                    {
                        "type": "img",
                         "value": mix_list[1][0],
                         "title": mix_list[1][1]
                    },
                    {
                        "type": "text",
                        "value": "的"
                    },
                    {
                        "type": "keyword",
                        "value": "左边"
                    },
                    {
                        "type": "text",
                        "value": "是"
                    },
                    {
                        "type": "keyword",
                        "value": "小红"
                    },
                    {
                        "type": "text",
                        "value": "的帽子，把它选出来。"
                    }
                ]
                ], # 题目描述信息
                "type": "pos-sequence-mulSelect" # 组件编号
                }
                ],
                "answers": [
                    0,
                    2
                ], # 答案
                "knowledges": [
                    "认识左右"
                ],
                "resource": "resource",
                "type": "选择", # 题型
                "explain": "explain",
                "level": "2", # 难度
                "number": "1-5-3-08" # 组件编号
                }
                ]

            if showtype == 2:
                questions = [
                {
                    "body": [
                        {
                            "title": "选一选",
                            "stem": "根据要求选一选",
                            "content": [
                                mix_list[0][0],
                                mix_list[1][0],
                                mix_list[2][0],
                                mix_list[3][0],
                                mix_list[4][0]
                            ],  # 帽子图片资源
                            "inputList": [
                                [
                                    {
                                        "type": "text",  # 普通文本
                                        "value": "（1）"
                                    },
                                    {
                                        "type": "keyword",  # 关键字
                                        "value": "小白"
                                    },
                                    {
                                        "type": "text",
                                        "value": "的帽子在"
                                    },
                                    {
                                        "type": "img",  # 图片类型
                                        "value": mix_list[3][0],
                                        "title": mix_list[3][1]
                                    },
                                    {
                                        "type": "text",
                                        "value": "的"
                                    },
                                    {
                                        "type": "keyword",
                                        "value": "右边"
                                    },
                                    {
                                        "type": "text",
                                        "value": "，"
                                    },
                                    {
                                        "type": "text",
                                        "value": "把它选出来。"
                                    }
                                ],  # 一个数组代表一行
                                [
                                    {
                                        "type": "text",
                                        "value": "（2）"
                                    },
                                    {
                                        "type": "img",
                                        "value": mix_list[2][0],
                                        "title": mix_list[2][1]
                                    },
                                    {
                                        "type": "text",
                                        "value": "的"
                                    },
                                    {
                                        "type": "keyword",
                                        "value": "右边"
                                    },
                                    {
                                        "type": "text",
                                        "value": "是"
                                    },
                                    {
                                        "type": "keyword",
                                        "value": "小黄"
                                    },
                                    {
                                        "type": "text",
                                        "value": "的帽子，把它选出来。"
                                    }
                                ]
                            ],  # 题目描述信息
                            "type": "pos-sequence-mulSelect"  # 组件编号
                        }
                    ],
                    "answers": [
                        4,
                        3
                    ],  # 答案
                    "knowledges": [
                        "认识左右"
                    ],
                    "resource": "resource",
                    "type": "选择",  # 题型
                    "explain": "explain",
                    "level": "2",  # 难度
                    "number": "1-5-3-08"  # 组件编号
                }
            ]
            dup_questions.extend(questions)
        for dup in dup_questions:
            if dup not in all_questions:
                all_questions.append(dup)
        return all_questions


    #todo 1-5-3-09 拖一拖
    def LeftAndRight6(self):
        all_questions=[]
        dup_questions = []
        for i in range(20):
            images_crab_url=q_CreatImgs.UpImages().CrabAndOctopus()
            mix_list=[]
            mix_list.extend(random.sample(images_crab_url,2))
            print("mix_list",mix_list)
            answer_list=[]
            right_left_list=[["左","左"],["右","右"]]
            rl1=random.choice(right_left_list)

            if rl1==right_left_list[0]:
                answer_list.append(2)
                answer_list.append(1)
            if rl1==right_left_list[1]:
                answer_list.append(1)
                answer_list.append(2)
            questions=[
                {
                    "body": [
                        {
                            "title": "拖一拖",
                            "bubbleList": [ # 气泡内容
                            {
                                "src": "v2/组件/认识左右/1-5-3-09/左气泡.svg", # 左气泡资源
                                "titltText": "我在"+str(mix_list[0][1])+"的"+str(rl1[0])+"边." # 左气泡内文字
            },
            {
                "src": "v2/组件/认识左右/1-5-3-09/右气泡.svg",
                "titltText": "我在"+str(mix_list[1][1])+"的"+str(rl1[1])+"边."
            }
            ],
            "titleList": [ # 题目内容
            {
                "type": "text",
                "value": "描述正确的拖入"
            },
            {
                "type": "symbol",
                "value": "/v2/通用/对错符号/对号.svg",
                "title": "对" # 用于语音读题功能的备用
            },
            {
                "type": "text",
                "value": "。"
            },
            {
                "type": "text",
                "value": "描述错误的拖入"
            },
            {
                "type": "symbol",
                "value": "/v2/通用/对错符号/错号2.svg",
                "title": "错" # 用于语音读题功能的备用
            },
            {
                "type": "text",
                "value": "。"
            }
            ],
            "content": [
                {
                    "name": mix_list[1][1],
                    "src": mix_list[1][0]
                },
                {
                    "name": mix_list[0][1],
                    "src": mix_list[0][0]
            }
            ], # 左右两个动物图片，必须要正面图！！！！！
            "options": [
                {
                    "type": "1", # 用于返回答案
                "src": "/v2/通用/对错符号/对号.svg" # 选项资源
            },
            {
                "type": "2",
                "src": "/v2/通用/对错符号/错号2.svg"
            }
            ], # 选项
            "type": "pos-sequence-dragInput2" # 组件名
            }
            ],
            "answers":answer_list, # 答案  对应option选项中的type值
            "knowledges": [
                "认识左右"
            ], # 知识点
            "resource": "resource",
            "type": "操作", # 题型
            "explain": "explain",
            "level": "1", # 难度
            "number": "1-5-3-09" # 题型编号
            }
            ]

            dup_questions.extend(questions)
        for dup in dup_questions:
            if dup not in all_questions:
                all_questions.append(dup)
        return all_questions
















if __name__ == '__main__':
    loation = LoationQuestions()
    # loation.CognitionFrontAndBack7()
    # loation.ToChoiceA3()
    # loation.ToChoiceA4()
    # loation.ToChoiceA8()
    # loation.LeftAndRight1()
    loation.LeftAndRight4()
