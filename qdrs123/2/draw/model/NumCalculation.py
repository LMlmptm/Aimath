import random
from draw import q_CreatImgs



class CalculNum():
    def __init__(self):
        self.num_max=1
        self.all_questions=[]

    def All_questions(self, questions):

        self.all_questions.extend(questions)
        self.num_max+=1
        # self.AnimalSelect()
        self.AnimalColoring()

    # todo 【编号】1-4-1-01  把动物选出来
    def AnimalSelect(self):
        all_questions=[]
        for i in range(16):
            mix_list=[]
            all_images_list=[]
            answer_list=[]
            images_animal_url,images_plant_url=q_CreatImgs.UpImages().PlantAndAnimal()
            mix_list.extend(random.sample(images_animal_url,1))
            all_images_list.extend(images_animal_url)
            all_images_list.extend(images_plant_url)
            while True:
                a=random.choice(all_images_list)
                if a not in mix_list:
                    print("a",a)
                    mix_list.append(a)
                if len(mix_list)==8:
                    break

            random.shuffle(mix_list)
            for m in mix_list:
                if m[0]=="animal":
                    answer_list.append(mix_list.index(m))
            print("mix_list", mix_list)
            print("answer_list",answer_list)
            questions=[
                {
                    "body": [
                        {
                            "title": "动物分类选择",
                            "stem": "把动物选出来。", # 与selectType对应
                        "content": [
                {
                    "type": mix_list[0][0], # 图片类型两种 动物： animal、 植物： plant
            "src": mix_list[0][1] # 图片路径
            },
            {
                "type": mix_list[1][0],
                "src": mix_list[1][1]
            },
            {
                "type": mix_list[2][0],
                "src": mix_list[2][1]
            },
            {
                "type": mix_list[3][0],
                "src": mix_list[3][1]
            },
            {
                "type": mix_list[4][0],
                "src": mix_list[4][1]
            },
            {
                "type": mix_list[5][0],
                "src": mix_list[5][1]
            },
            {
                "type": mix_list[6][0],
                "src": mix_list[6][1]
            },
            {
                "type": mix_list[7][0],
                "src": mix_list[7][1]
            }
            ], # 展示图片的类别和路径
            "selectType": "animal", # 需要选择的类型
            "type": "au-animal-classify"
            }
            ],
            "answers": answer_list, # 正确答案的下标
            "knowledges": [
                "分类"
            ], # 知识点
            "resource": "resource",
            "type": "操作", # 题目类型
            "explain": "explain",
            "level": "1", # 难度
            "number": "1-4-1-01" # 题目编号
            }
            ]
            print("questions",questions)
            all_questions.extend(questions)
        return all_questions




    # todo 1-4-1-02 选一选，给会飞的动物涂上颜色
    def AnimalColoring(self):
        all_questions=[]
        for i in range(12):
            mix_list=[]
            answer_list=[]
            images_fly_url,images_run_url,images_swim_url=q_CreatImgs.UpImages().SketchAnimal()
            mix_list.extend(random.sample(images_fly_url,3))
            mix_list.extend(random.sample(images_run_url,3))
            # mix_list.extend(random.sample(images_swim_url,3))
            random.shuffle(mix_list)
            for m in mix_list:
                if m[1]=="fly":
                    answer_list.append(mix_list.index(m))
            print("mix_list",mix_list)
            print("answer_list",answer_list)
            questions=[
                {
                    "body": [
                        {
                            "title": "动物分类选择",
                            "stem": "选一选，给会飞的动物涂上颜色。", # 与selectType字段值对应
                        "content": [
                {
                    "type": mix_list[0][1], # 图片类别两种：天上飞的动物：fly、地上跑的：run(如有需要也可按三种展示：+水里游的：swim)
            "src1": mix_list[0][2], # 未上色的图片
            "src2": mix_list[0][0] # 上色后的图片
            },
            {
                "type": mix_list[1][1], # 图片类别  地上跑的动物
            "src1": mix_list[1][2],
            "src2": mix_list[1][0]
            },
            {
                  "type": mix_list[2][1], # 图片类别  地上跑的动物
            "src1": mix_list[2][2],
            "src2": mix_list[2][0]
            },
            {
                  "type": mix_list[3][1], # 图片类别  地上跑的动物
            "src1": mix_list[3][2],
            "src2": mix_list[3][0]
            },
            {
                  "type": mix_list[4][1], # 图片类别  地上跑的动物
            "src1": mix_list[4][2],
            "src2": mix_list[4][0]
            },
            {
                "type": mix_list[5][1],  # 图片类别  地上跑的动物
                "src1": mix_list[5][2],
                "src2": mix_list[5][0]
            }
            ],
            "selectType": "fly", # 表示需要选出的类型
            "type": "au-animal-color"
            }
            ],
            "answers": answer_list, # 正确答案的下标
            "knowledges": [
                "分类"
            ], # 知识点
            "resource": "resource",
            "type": "操作",
            "explain": "explain",
            "level": "1",
            "number": "1-4-1-02" # 题型编号，也可是1 - 4 - 1 - 03
            }
            ]
            print("questions",questions)
            all_questions.extend(questions)
        return all_questions

    # todo 1-4-1-03 选一选，给会飞的动物涂上颜色
    def AnimalColoringSelect(self):
        all_questions=[]
        for i in range(12):
            mix_list=[]
            answer_list=[]
            images_fly_url,images_run_url,images_swim_url=q_CreatImgs.UpImages().SketchAnimal()
            mix_list.extend(random.sample(images_fly_url,3))
            # mix_list.extend(random.sample(images_run_url,3))
            mix_list.extend(random.sample(images_swim_url,3))
            random.shuffle(mix_list)
            for m in mix_list:
                if m[1]=="fly":
                    answer_list.append(mix_list.index(m))
            print("mix_list",mix_list)
            print("answer_list",answer_list)
            questions=[
                {
                    "body": [
                        {
                            "title": "动物分类选择",
                            "stem": "选一选，给会飞的动物涂上颜色。", # 与selectType字段值对应
                        "content": [
                {
                    "type": mix_list[0][1], # 图片类别两种：天上飞的动物：fly、地上跑的：run(如有需要也可按三种展示：+水里游的：swim)
            "src1": mix_list[0][2], # 未上色的图片
            "src2": mix_list[0][0] # 上色后的图片
            },
            {
                "type": mix_list[1][1], # 图片类别  地上跑的动物
            "src1": mix_list[1][2],
            "src2": mix_list[1][0]
            },
            {
                  "type": mix_list[2][1], # 图片类别  地上跑的动物
            "src1": mix_list[2][2],
            "src2": mix_list[2][0]
            },
            {
                  "type": mix_list[3][1], # 图片类别  地上跑的动物
            "src1": mix_list[3][2],
            "src2": mix_list[3][0]
            },
            {
                  "type": mix_list[4][1], # 图片类别  地上跑的动物
            "src1": mix_list[4][2],
            "src2": mix_list[4][0]
            },
            {
                "type": mix_list[5][1],  # 图片类别  地上跑的动物
                "src1": mix_list[5][2],
                "src2": mix_list[5][0]
            }
            ],
            "selectType": "fly", # 表示需要选出的类型
            "type": "au-animal-color"
            }
            ],
            "answers": answer_list, # 正确答案的下标
            "knowledges": [
                "分类"
            ], # 知识点
            "resource": "resource",
            "type": "操作",
            "explain": "explain",
            "level": "1",
            "number": "1-4-1-02" # 题型编号，也可是1 - 4 - 1 - 03
            }
            ]
            print("questions",questions)
            all_questions.extend(questions)
        return all_questions


    # todo 1-4-1-04 在蔬菜下面输入“0”，在水果下面输入“1”
    def FruitVegetableSelect(self):
        images_fruit_url,images_vegetable_url=q_CreatImgs.UpImages().FruitAndVagetable()
        all_questions=[]
        for q in range(21):
            mix_list=[]
            start_mix_list=[]
            for i in range(3):
                start_mix_list.extend(random.sample(images_fruit_url,1))
                start_mix_list.extend(random.sample(images_vegetable_url,1))
            print("start_mix_list",start_mix_list)
            for mix in start_mix_list:
                if mix not in mix_list:
                    mix_list.append(mix)
            print("mix_list去重后",mix_list)
            if len(mix_list)<6:
                while True:
                    f=random.sample(images_fruit_url, 1)
                    if f not in mix_list:
                        mix_list.extend(f)
                        if len(mix_list)==6:
                            break

                    else:
                        v=random.sample(images_vegetable_url,1)
                        if v not in mix_list:
                            mix_list.extend(v)
                            if len(mix_list)==6:
                                break



            random.shuffle(mix_list)
            print("mix_list",mix_list)
            print("mix_list指定种类",mix_list[0][2])

            questions=[
                        {
                            "body": [
                                {
                                    "title": "分类填空",
                                    "stem": "在蔬菜下面输入“0”，在水果下面输入“1”。",
                                    "titleInfo": [
                                        {
                                            "type": "vegetable",
                                            "num": 0
                                        },
                                        {
                                            "type": "fruits",
                                            "num": 1
                                        }
                                    ], # 表示题中有蔬菜和水果两种类型，以及他们各自对应代表的数字
                    "content": [
                        {
                            "type": mix_list[0][1], # 图片类别 蔬菜
                        "src": mix_list[0][0], # 图片路径
                    "val": "" # 用于前端绑定用户输入框输入的值，后端可忽略
                    },
                    {
                        "type": mix_list[1][1], # 图片类别水果
                    "src": mix_list[1][0],
                    "val": ""
                    },
                    {
                        "type": mix_list[2][1],
                        "src": mix_list[2][0],
                        "val": ""
                    },
                    {
                        "type": mix_list[3][1],
                        "src": mix_list[3][0],
                        "val": ""
                    },
                    {
                        "type": mix_list[4][1],
                        "src": mix_list[4][0],
                        "val": ""
                    },
                    {
                        "type": mix_list[5][1],
                        "src": mix_list[5][0],
                        "val": ""
                    }
                    ],
                    "type": "au-classify-input",
                    "keyboardtype": "num" # 数字键盘
                    }
                    ],
                    "answers": [
                        mix_list[0][2],
                        mix_list[1][2],
                        mix_list[2][2],
                        mix_list[3][2],
                        mix_list[4][2],
                        mix_list[5][2]
                    ], # 正确答案
                    "knowledges": "分类", "knowledges": [
                        "分类"
                    ], # 知识点
                    "resource": "resource",
                    "type": "选择",
                    "explain": "explain",
                    "level": "2",
                    "number": "1-4-1-04"
                    }
                    ]
            all_questions.extend(questions)

        # print("all_questions",all_questions)
        return all_questions


    #todo 1-4-1-05 天上飞的输入“0”，水里游的输入“1”，地上跑的输入“2”
    def FlyAndSwimAndRunSelect(self):
        images_fly_url,images_swim_url,images_run_url = q_CreatImgs.UpImages().FlyAndSwimAndRun()
        all_questions = []
        for i in range(21):
            mix_list = []
            start_mix_list=[]
            for i in range(2):
                start_mix_list.extend(random.sample(images_fly_url, 1))
                start_mix_list.extend(random.sample(images_swim_url, 1))
                start_mix_list.extend(random.sample(images_run_url, 1))

            print("start_mix_list",start_mix_list)
            for mix in start_mix_list:
                if mix not in mix_list:
                    mix_list.append(mix)
            print("mix_list去重后",mix_list)
            if len(mix_list)<6:
                while True:
                    f=random.sample(images_fly_url, 1)

                    if f not in mix_list:
                        mix_list.extend(f)
                        if len(mix_list)==6:
                            break

            random.shuffle(mix_list)
            print("mix_list", mix_list)
            print("mix_list指定种类", mix_list[0][2])
            questions=[
                    {
                        "body": [
                            {
                                "title": "分类填空",
                                "stem": "天上飞的输入“0”，水里游的输入“1”，地上跑的输入“2”",
                                "titleInfo": [
                                    {
                                        "type": "fly", # 天上飞的
                                    "num": 0
                },
                {
                    "type": "swim", # 水里游的
                "num": 1
                },
                {
                    "type": "run", # 地上跑的
                "num": 2
                }
                ], # 表示题中的三种类型，以及他们各自对应代表的数字
                "content": [
                    {
                        "type": mix_list[0][1], # 图片类别
                    "src": mix_list[0][0], # 图片路径
                "val": "" # 用于前端绑定用户输入框输入的值，后端可忽略
                },
                {
                    "type": mix_list[1][1],
                    "src": mix_list[1][0],
                    "val": ""
                },
                {
                    "type": mix_list[2][1],
                    "src": mix_list[2][0],
                    "val": ""
                },
                {
                    "type": mix_list[3][1],
                    "src": mix_list[3][0],
                    "val": ""
                },
                {
                    "type": mix_list[4][1],
                    "src": mix_list[4][0],
                    "val": ""
                },
                {
                    "type": mix_list[5][1],
                    "src": mix_list[5][0],
                    "val": ""
                }
                ],
                "type": "au-classify-input",
                "keyboardtype": "num" # 数字键盘
                }
                ],
                "answers": [
                    mix_list[0][2],
                    mix_list[1][2],
                    mix_list[2][2],
                    mix_list[3][2],
                    mix_list[4][2],
                    mix_list[5][2],
                ], # 正确答案
                "knowledges": [
                    "分类"
                ], # 知识点
                "resource": "resource",
                "type": "选择",
                "explain": "explain",
                "level": "2",
                "number": "1-4-1-05" # 题型编号
                }
            ]

            all_questions.extend(questions)

        print("all_questions",all_questions)
        return all_questions


    #todo 拖一拖﹐把下面生活用品分为三类
    def ToyAndStationerySelect(self):
        images_toy_url,images_stationery_url,images_clothing_url,images_sportEquipment_url = q_CreatImgs.UpImages().ToyAndStationeryEC()
        all_questions = []

        for i in range(14):
            mix_list = []
            mix_list.extend(random.sample(images_toy_url, 3))
            mix_list.extend(random.sample(images_stationery_url, 3))
            mix_list.extend(random.sample(images_clothing_url, 3))

            random.shuffle(mix_list)
            # print("mix_list", mix_list)
            # print("mix_list指定种类", mix_list[0][1])

            questions=[
                    {
                        "body": [
                            {
                                "title": "拖拽分类",
                                "stem": "拖一拖，把下面生活用品分为三类。",
                                "typeList": [
                                    {
                                        "type": "toy",
                                        "desc": "玩具"
                                    },
                                    {
                                        "type": "stationery",
                                        "desc": "学习文具"
                                    },
                                    {
                                        "type": "clothing",
                                        "desc": "服装鞋帽"
                                    }
                                ], # 对应三个拖入框展示的三种类别
                            "content": [
                    {
                        "type": mix_list[0][1], # 三种图片类别（toy：玩具、stationery：学习文具、clothing：服装鞋帽）
                "src": mix_list[0][0] # 资源路径
                },
                {
                    "type": mix_list[1][1],
                    "src": mix_list[1][0]
                },
                {
                     "type": mix_list[2][1],
                    "src": mix_list[2][0]
                },
                {
                     "type": mix_list[3][1],
                    "src": mix_list[3][0]
                },
                {
                     "type": mix_list[4][1],
                    "src": mix_list[4][0]
                },
                {
                    "type": mix_list[5][1],
                    "src": mix_list[5][0]
                },
                {
                    "type": mix_list[6][1],
                    "src": mix_list[6][0]
                },
                {
                    "type": mix_list[7][1],
                    "src": mix_list[7][0]
                },
                {
                    "type": mix_list[8][1],
                    "src": mix_list[8][0]
                }
                ], # 展示的路片不局限于6张，大于6张可多行展示
                "type": "au-classify-drag" # 组件名
                }
                ],
                "answers": [
                    [
                        "toy",
                        "toy",
                        "toy"
                    ],
                    [
                        "stationery",
                        "stationery",
                        "stationery"
                    ],
                    [
                        "clothing",
                        "clothing",
                        "clothing"
                    ]
                ], # 正确答案，为拖入图片的type类型集合
                "knowledges": [
                    "分类"
                ],
                "resource": "resource",
                "type": "操作",
                "explain": "explain",
                "level": "2",# 难度
                "number": "1-4-1-06" # 题型编号
                }
                ]
            all_questions.extend(questions)

        print("all_questions",all_questions)
        return all_questions


    #todo 1-4-1-07 拖一拖﹐把下面生活用品分为三类
    def ToyAndSportEquipmentSelect(self):
        images_toy_url,images_stationery_url,images_clothing_url,images_sportEquipment_url = q_CreatImgs.UpImages().ToyAndStationeryEC()
        images_fruit_url,images_vegetable_url = q_CreatImgs.UpImages().FruitAndVagetable()
        all_questions = []

        for i in range(14):
            mix_list = []
            mix_list.extend(random.sample(images_stationery_url, 4))
            mix_list.extend(random.sample(images_vegetable_url, 4))
            mix_list.extend(random.sample(images_sportEquipment_url, 4))

            random.shuffle(mix_list)
            # print("mix_list", mix_list)
            # print("mix_list指定种类", mix_list[0][1])

            questions=[
                    {
                        "body": [
                            {
                                "title": "拖拽分类",
                                "stem": "拖一拖，把下面生活用品分为三类。",
                                "typeList": [
                                    {
                                        "type": "stationery",
                                        "desc": "学习用品"
                                    },
                                    {
                                        "type": "vegetable",
                                        "desc": "蔬菜"
                                    },
                                    {
                                        "type": "sportEquipment",
                                        "desc": "体育用品"
                                    }
                                ], # 对应三个拖入框展示的三种类别
                            "content": [
                    {
                        "type": mix_list[0][1], # 三种图片类别（toy：玩具、stationery：学习文具、clothing：服装鞋帽）
                "src": mix_list[0][0] # 资源路径
                },
                {
                    "type": mix_list[1][1],
                    "src": mix_list[1][0]
                },
                {
                     "type": mix_list[2][1],
                    "src": mix_list[2][0]
                },
                {
                     "type": mix_list[3][1],
                    "src": mix_list[3][0]
                },
                {
                     "type": mix_list[4][1],
                    "src": mix_list[4][0]
                },
                {
                    "type": mix_list[5][1],
                    "src": mix_list[5][0]
                },
                                {
                                    "type": mix_list[6][1],
                                    "src": mix_list[6][0]
                                },
                                {
                                    "type": mix_list[7][1],
                                    "src": mix_list[7][0]
                                },
                                {
                                    "type": mix_list[8][1],
                                    "src": mix_list[8][0]
                                },
                                {
                                    "type": mix_list[9][1],
                                    "src": mix_list[9][0]
                                },
                                {
                                    "type": mix_list[10][1],
                                    "src": mix_list[10][0]
                                },
                                {
                                    "type": mix_list[11][1],
                                    "src": mix_list[11][0]
                                },

                ], # 展示的路片不局限于6张，大于6张可多行展示
                "type": "au-classify-drag" # 组件名
                }
                ],
                "answers": [
                    [
                        "stationery",
                        "stationery",
                        "stationery",
                        "stationery",
                    ],
                    [
                        "vegetable",
                        "vegetable",
                        "vegetable",
                        "vegetable",
                    ],
                    [
                        "sportEquipment",
                        "sportEquipment",
                        "sportEquipment",
                        "sportEquipment",
                    ]
                ], # 正确答案，为拖入图片的type类型集合
                "knowledges": [
                    "分类"
                ],
                "resource": "resource",
                "type": "操作",
                "explain": "explain",
                "level": "2",# 难度
                "number": "1-4-1-06" # 题型编号
                }
                ]
            all_questions.extend(questions)

        print("all_questions",all_questions)
        return all_questions


    #todo 1-4-1-08 算一算，将得数相同的算式拖入到相同的框里
    def EquationClassifySelect(self):
        all_questions=[]
        for i in range(10):
            mix_list_random=[]
            mix_list=[]
            answer_list1=[]
            answer_list2=[]
            mix_list_sample=[]
            One,Two,Thire,Four,Fif,Six,Seven,Eight,Nine = q_CreatImgs.UpImages().EquationClassify()
            mix_list_random.extend([random.sample(One,3)])
            mix_list_random.extend([random.sample(Two,3)])
            mix_list_random.extend([random.sample(Thire,3)])
            mix_list_random.extend([random.sample(Four,3)])
            mix_list_random.extend([random.sample(Fif,3)])
            mix_list_random.extend([random.sample(Six,3)])
            mix_list_random.extend([random.sample(Seven,3)])
            mix_list_random.extend([random.sample(Eight,3)])
            mix_list_random.extend([random.sample(Nine,3)])
            mix_list_sample.extend(random.sample(mix_list_random,2))
            for sam in mix_list_sample:
                for sa in sam:
                    # print("sa",sa)
                    mix_list.append(sa)
            random.shuffle(mix_list)
            print("mix_list", mix_list)
            answer_num=mix_list[0][1]
            print("answer_num", answer_num)
            for mix in mix_list:
                if mix[1]==answer_num:
                    answer_list1.append(mix)
                else:
                    answer_list2.append(mix)
            print("answer_list1",answer_list1)
            print("answer_list2",answer_list2)





            questions=[
                {
                    "body": [
                        {
                            "title": "算式分类",
                            "stem": "算一算，将得数相同的算式拖入到相同的框里。",
                            "questionItem": [
                                mix_list[0][0],
                                mix_list[1][0],
                                mix_list[2][0],
                                mix_list[3][0],
                                mix_list[4][0],
                                mix_list[5][0],
                            ], # 算式选项
                        "type": "au-equation-drag"
            }
            ],
                    "answers": "{{" + str(answer_list1[0][0]) + ";" + str(answer_list1[1][0]) + ";" + str(answer_list1[
                        2][0]) + "};{" + str(answer_list2[0][0]) + ";" + str(answer_list2[1][0]) + ";" + str(answer_list2[
                                   2][0]) + "}}",
                    # 正确答案分组
            "knowledges": [
                "分类"
            ],
            "resource": "",
            "type": "操作",
            "explain": "",
            "level": "3",
            "number": "1-4-1-08" # 题型编号
            }

            ]

            all_questions.extend(questions)
        print("all_questions",all_questions)
        return all_questions

    #todo 1-4-1-09 把会飞的动物选出来，再填一填
    def FlyAnimalSelect(self):
        all_questions = []
        for i in range(10):
            answer_index_list=[]
            answer_swim_list=[]
            answer_run_list=[]
            fly_swim_run_mix_list=[]
            mix_list = []
            choice_fly_swim_run=[1,2,3]
            images_fly_url, images_swim_url, images_run_url = q_CreatImgs.UpImages().FlyAndSwimAndRun()
            fly_swim_run_mix_list.extend(images_run_url)
            fly_swim_run_mix_list.extend(images_swim_url)
            fly_swim_run_mix_list.extend(random.sample(images_fly_url,4))
            print("fly_swim_run_mix_list",fly_swim_run_mix_list)

            while True:
                f = random.sample(images_fly_url, 1)
                if f[0] not in fly_swim_run_mix_list:
                    print("f")
                    mix_list.extend(f)
                    print("f",f)
                    break

            mix_list.extend(random.sample(fly_swim_run_mix_list,11))
            random.shuffle(mix_list)
            print("mix_list", mix_list)
            for mix in range(len(mix_list)):
                if mix_list[mix][1]=="fly":
                    answer_index_list.append(mix)
                if mix_list[mix][1]=="swim":
                    answer_swim_list.append(mix)
                if mix_list[mix][1]=="run":
                    answer_run_list.append(mix)
            print("answer_index_list",answer_index_list)

            choice=random.choice(choice_fly_swim_run)
            if choice==1:
                questions=[
                    {
                        "body": [
                            {
                                "title": "分类选择",
                                "stem": "把天上飞的动物选出来，再填一填。", # 与selectType值对应
                            "content": [
                    {
                        "type": mix_list[0][1], # 三种类型（run： 地上跑的、swim: 水里游的、fly: 天上飞的）
                "src": mix_list[0][0] # 资源路径
                },
                {
                    "type": mix_list[1][1],
                    "src": mix_list[1][0]
                },
                {
                     "type": mix_list[2][1],
                    "src": mix_list[2][0]
                },
                {
                    "type": mix_list[3][1],
                    "src": mix_list[3][0]
                },
                {
                    "type": mix_list[4][1],
                    "src": mix_list[4][0]
                },
                {
                    "type": mix_list[5][1],
                    "src": mix_list[5][0]
                },
                {
                     "type": mix_list[6][1],
                    "src": mix_list[6][0]
                },
                {
                     "type": mix_list[7][1],
                    "src": mix_list[7][0]
                },
                {
                     "type": mix_list[8][1],
                    "src": mix_list[8][0]
                },
                {
                     "type": mix_list[9][1],
                    "src": mix_list[9][0]
                },
                {
                    "type": mix_list[10][1],
                    "src": mix_list[10][0]
                },
                {
                    "type": mix_list[11][1],
                    "src": mix_list[11][0]
                }
                ],
                "unit": "只", # 输入框后面的单位
                "selectType": "fly", # 需要选出的类型
                "type": "au-classify-fill-in",
                "keyboardtype": "num" # 数字键盘
                }
                ],
                "answers": [answer_index_list,len(answer_index_list)], # 正确答案
                "knowledges": [
                    "分类"
                ], # 知识点
                "resource": "resource",
                "type": "操作",
                "explain": "explain",
                "level": "2",
                "number": "1-4-1-09"
                }
                ]

            if choice==2:
                questions=[
                    {
                        "body": [
                            {
                                "title": "分类选择",
                                "stem": "把水里游的动物选出来，再填一填。", # 与selectType值对应
                            "content": [
                    {
                        "type": mix_list[0][1], # 三种类型（run： 地上跑的、swim: 水里游的、fly: 天上飞的）
                "src": mix_list[0][0] # 资源路径
                },
                {
                    "type": mix_list[1][1],
                    "src": mix_list[1][0]
                },
                {
                     "type": mix_list[2][1],
                    "src": mix_list[2][0]
                },
                {
                    "type": mix_list[3][1],
                    "src": mix_list[3][0]
                },
                {
                    "type": mix_list[4][1],
                    "src": mix_list[4][0]
                },
                {
                    "type": mix_list[5][1],
                    "src": mix_list[5][0]
                },
                {
                     "type": mix_list[6][1],
                    "src": mix_list[6][0]
                },
                {
                     "type": mix_list[7][1],
                    "src": mix_list[7][0]
                },
                {
                     "type": mix_list[8][1],
                    "src": mix_list[8][0]
                },
                {
                     "type": mix_list[9][1],
                    "src": mix_list[9][0]
                },
                {
                    "type": mix_list[10][1],
                    "src": mix_list[10][0]
                },
                {
                    "type": mix_list[11][1],
                    "src": mix_list[11][0]
                }
                ],
                "unit": "只", # 输入框后面的单位
                "selectType": "swim", # 需要选出的类型
                "type": "au-classify-fill-in",
                "keyboardtype": "num" # 数字键盘
                }
                ],
                "answers": [answer_swim_list,len(answer_swim_list)], # 正确答案
                "knowledges": [
                    "分类"
                ], # 知识点
                "resource": "resource",
                "type": "操作",
                "explain": "explain",
                "level": "2",
                "number": "1-4-1-09"
                }
                ]

            if choice == 3:
                questions = [
                    {
                        "body": [
                            {
                                "title": "分类选择",
                                "stem": "把地上跑的动物选出来，再填一填。",  # 与selectType值对应
                                "content": [
                                    {
                                        "type": mix_list[0][1],  # 三种类型（run： 地上跑的、swim: 水里游的、fly: 天上飞的）
                                        "src": mix_list[0][0]  # 资源路径
                                    },
                                    {
                                        "type": mix_list[1][1],
                                        "src": mix_list[1][0]
                                    },
                                    {
                                        "type": mix_list[2][1],
                                        "src": mix_list[2][0]
                                    },
                                    {
                                        "type": mix_list[3][1],
                                        "src": mix_list[3][0]
                                    },
                                    {
                                        "type": mix_list[4][1],
                                        "src": mix_list[4][0]
                                    },
                                    {
                                        "type": mix_list[5][1],
                                        "src": mix_list[5][0]
                                    },
                                    {
                                        "type": mix_list[6][1],
                                        "src": mix_list[6][0]
                                    },
                                    {
                                        "type": mix_list[7][1],
                                        "src": mix_list[7][0]
                                    },
                                    {
                                        "type": mix_list[8][1],
                                        "src": mix_list[8][0]
                                    },
                                    {
                                        "type": mix_list[9][1],
                                        "src": mix_list[9][0]
                                    },
                                    {
                                        "type": mix_list[10][1],
                                        "src": mix_list[10][0]
                                    },
                                    {
                                        "type": mix_list[11][1],
                                        "src": mix_list[11][0]
                                    }
                                ],
                                "unit": "只",  # 输入框后面的单位
                                "selectType": "swim",  # 需要选出的类型
                                "type": "au-classify-fill-in",
                                "keyboardtype": "num"  # 数字键盘
                            }
                        ],
                        "answers": [answer_run_list, len(answer_run_list)],  # 正确答案
                        "knowledges": [
                            "分类"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "操作",
                        "explain": "explain",
                        "level": "2",
                        "number": "1-4-1-09"
                    }
                ]


            all_questions.extend(questions)
        return all_questions


    #todo 1-4-1-10 把学习文具选出来﹐再填—填
    def StationerySelect(self):
        all_questions = []
        for i in range(10):
            answer_stationery_list=[]
            answer_toy_list=[]
            answer_clothing_list=[]
            answer_sportEquipment_list=[]
            stationery_list=[]
            toy_list=[]
            clothing_list=[]
            sportEquipment_list=[]
            all_images_list=[]
            title_list=["学习文具","玩具","服饰","体育器材"]
            mix_list = []
            images_toy_url,images_stationery_url,images_clothing_url,images_sportEquipment_url = q_CreatImgs.UpImages().ToyAndStationeryEC()
            all_images_list.extend(images_toy_url)
            all_images_list.extend(images_stationery_url)
            all_images_list.extend(images_clothing_url)
            all_images_list.extend(images_sportEquipment_url)
            toy_list.extend(random.sample(images_toy_url,1))
            stationery_list.extend(random.sample(images_stationery_url,1))
            clothing_list.extend(random.sample(images_clothing_url,1))
            sportEquipment_list.extend(random.sample(images_sportEquipment_url,1))
            title=random.choice(title_list)
            print("title",title)
            if title=="玩具":
                while True:
                    t=random.choice(all_images_list)
                    if t not in toy_list:
                        toy_list.append(t)
                    if len(toy_list)==8:
                        break
                random.shuffle(toy_list)
                for toy in toy_list:
                    if toy[1]=="toy":
                        answer_toy_list.append(toy_list.index(toy))

                print("answer_toy_list",answer_toy_list)
                questions = [
                    {
                        "body": [
                            {
                                "title": "分类选择",
                                "stem": "把"+str(title)+"选出来，再填一填。",  # 与selectType字段值对应
                                "content": [
                                    {
                                        "type": toy_list[0][1],  # 三种类型（run： 地上跑的、swim: 水里游的、fly: 天上飞的）
                                        "src": toy_list[0][0]  # 资源路径
                                    },
                                    {
                                        "type": toy_list[1][1],
                                        "src": toy_list[1][0]
                                    },
                                    {
                                        "type": toy_list[2][1],
                                        "src": toy_list[2][0]
                                    },
                                    {
                                        "type": toy_list[3][1],
                                        "src": toy_list[3][0]
                                    },
                                    {
                                        "type": toy_list[4][1],
                                        "src": toy_list[4][0]
                                    },
                                    {
                                        "type": toy_list[5][1],
                                        "src": toy_list[5][0]
                                    },
                                    {
                                        "type": toy_list[6][1],
                                        "src": toy_list[6][0]
                                    },
                                    {
                                        "type": toy_list[7][1],
                                        "src": toy_list[7][0]
                                    },

                                ],
                                "unit": "件",  # 输入框后面的单位
                                "selectType": "toy",  # 需要选出的类型
                                "type": "au-classify-fill-in",
                                "keyboardtype": "num"  # 数字键盘
                            }
                        ],
                        "answers": [answer_toy_list, [len(answer_toy_list)]],  # 正确答案
                        "knowledges": [
                            "分类"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "操作",
                        "explain": "explain",
                        "level": "2",
                        "number": "1-4-1-10"
                    }
                ]

            if title == "学习文具":
                while True:
                    s = random.choice(all_images_list)
                    if s not in stationery_list:
                        stationery_list.append(s)
                    if len(stationery_list) == 8:
                        break
                random.shuffle(stationery_list)
                for st in stationery_list:
                    if st[1] == "stationery":
                        answer_stationery_list.append(stationery_list.index(st))

                print("answer_toy_list", answer_stationery_list)
                questions = [
                    {
                        "body": [
                            {
                                "title": "分类选择",
                                "stem": "把" + str(title) + "选出来，再填一填。",  # 与selectType字段值对应
                                "content": [
                                    {
                                        "type": stationery_list[0][1],  # 三种类型（run： 地上跑的、swim: 水里游的、fly: 天上飞的）
                                        "src": stationery_list[0][0]  # 资源路径
                                    },
                                    {
                                        "type": stationery_list[1][1],
                                        "src": stationery_list[1][0]
                                    },
                                    {
                                        "type": stationery_list[2][1],
                                        "src": stationery_list[2][0]
                                    },
                                    {
                                        "type": stationery_list[3][1],
                                        "src": stationery_list[3][0]
                                    },
                                    {
                                        "type": stationery_list[4][1],
                                        "src": stationery_list[4][0]
                                    },
                                    {
                                        "type": stationery_list[5][1],
                                        "src": stationery_list[5][0]
                                    },
                                    {
                                        "type": stationery_list[6][1],
                                        "src": stationery_list[6][0]
                                    },
                                    {
                                        "type": stationery_list[7][1],
                                        "src": stationery_list[7][0]
                                    },

                                ],
                                "unit": "件",  # 输入框后面的单位
                                "selectType": "stationery",  # 需要选出的类型
                                "type": "au-classify-fill-in",
                                "keyboardtype": "num"  # 数字键盘
                            }
                        ],
                        "answers": [answer_stationery_list, [len(answer_stationery_list)]],  # 正确答案
                        "knowledges": [
                            "分类"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "操作",
                        "explain": "explain",
                        "level": "2",
                        "number": "1-4-1-10"
                    }
                ]

            if title == "服饰":
                while True:
                    c = random.choice(all_images_list)
                    if c not in clothing_list:
                        clothing_list.append(c)
                    if len(clothing_list) == 8:
                        break
                random.shuffle(clothing_list)
                for cl in clothing_list:
                    if cl[1] == "clothing":
                        answer_clothing_list.append(clothing_list.index(cl))

                print("answer_clothing_list", answer_clothing_list)
                questions = [
                    {
                        "body": [
                            {
                                "title": "分类选择",
                                "stem": "把" + str(title) + "选出来，再填一填。",  # 与selectType字段值对应
                                "content": [
                                    {
                                        "type": clothing_list[0][1],  # 三种类型（run： 地上跑的、swim: 水里游的、fly: 天上飞的）
                                        "src": clothing_list[0][0]  # 资源路径
                                    },
                                    {
                                        "type": clothing_list[1][1],
                                        "src": clothing_list[1][0]
                                    },
                                    {
                                        "type": clothing_list[2][1],
                                        "src": clothing_list[2][0]
                                    },
                                    {
                                        "type": clothing_list[3][1],
                                        "src": clothing_list[3][0]
                                    },
                                    {
                                        "type": clothing_list[4][1],
                                        "src": clothing_list[4][0]
                                    },
                                    {
                                        "type": clothing_list[5][1],
                                        "src": clothing_list[5][0]
                                    },
                                    {
                                        "type": clothing_list[6][1],
                                        "src": clothing_list[6][0]
                                    },
                                    {
                                        "type": clothing_list[7][1],
                                        "src": clothing_list[7][0]
                                    },

                                ],
                                "unit": "件",  # 输入框后面的单位
                                "selectType": "stationery",  # 需要选出的类型
                                "type": "au-classify-fill-in",
                                "keyboardtype": "num"  # 数字键盘
                            }
                        ],
                        "answers": [answer_clothing_list, [len(answer_clothing_list)]],  # 正确答案
                        "knowledges": [
                            "分类"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "操作",
                        "explain": "explain",
                        "level": "2",
                        "number": "1-4-1-10"
                    }
                ]


            if title == "体育器材":
                while True:
                    p = random.choice(all_images_list)
                    if p not in sportEquipment_list:
                        sportEquipment_list.append(p)
                    if len(sportEquipment_list) == 8:
                        break
                random.shuffle(sportEquipment_list)
                for sport in sportEquipment_list:
                    if sport[1] == "sportEquipment":
                        answer_sportEquipment_list.append(sportEquipment_list.index(sport))

                print("answer_clothing_list", answer_sportEquipment_list)
                questions = [
                    {
                        "body": [
                            {
                                "title": "分类选择",
                                "stem": "把" + str(title) + "选出来，再填一填。",  # 与selectType字段值对应
                                "content": [
                                    {
                                        "type": sportEquipment_list[0][1],  # 三种类型（run： 地上跑的、swim: 水里游的、fly: 天上飞的）
                                        "src": sportEquipment_list[0][0]  # 资源路径
                                    },
                                    {
                                        "type": sportEquipment_list[1][1],
                                        "src": sportEquipment_list[1][0]
                                    },
                                    {
                                        "type": sportEquipment_list[2][1],
                                        "src": sportEquipment_list[2][0]
                                    },
                                    {
                                        "type": sportEquipment_list[3][1],
                                        "src": sportEquipment_list[3][0]
                                    },
                                    {
                                        "type": sportEquipment_list[4][1],
                                        "src": sportEquipment_list[4][0]
                                    },
                                    {
                                        "type": sportEquipment_list[5][1],
                                        "src": sportEquipment_list[5][0]
                                    },
                                    {
                                        "type": sportEquipment_list[6][1],
                                        "src": sportEquipment_list[6][0]
                                    },
                                    {
                                        "type": sportEquipment_list[7][1],
                                        "src": sportEquipment_list[7][0]
                                    },

                                ],
                                "unit": "件",  # 输入框后面的单位
                                "selectType": "sportEquipment",  # 需要选出的类型
                                "type": "au-classify-fill-in",
                                "keyboardtype": "num"  # 数字键盘
                            }
                        ],
                        "answers": [answer_sportEquipment_list, [len(answer_sportEquipment_list)]],  # 正确答案
                        "knowledges": [
                            "分类"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "操作",
                        "explain": "explain",
                        "level": "2",
                        "number": "1-4-1-10"
                    }
                ]


            all_questions.extend(questions)
        return all_questions


    #todo 1-4-1-11 分一分﹐填―填
    def TransportSelect(self):
        all_questions = []
        for i in range(20):
            transport_fly_url, transport_land_url, transport_steamer_url = q_CreatImgs.UpImages().Transport()
            fly = 0
            land = 0
            steamer = 0
            mix_all_list = []
            mix_list = []
            mix_all_list.extend(random.sample(transport_fly_url, 8))
            mix_all_list.extend(random.sample(transport_land_url, 8))
            mix_all_list.extend(random.sample(transport_steamer_url, 8))
            mix_list.extend(random.sample(mix_all_list, 8))
            print("mix_list", mix_list)
            for transport in mix_list:
                if transport[1] == "fly":
                    fly += 1
                elif transport[1] == "land":
                    land += 1
                else:
                    steamer += 1
            print(fly, land, steamer)

            questions=[
                {
                    "body": [
                        {
                            "title": "分一分， 填一填",
                            "stem": "分一分， 填一填。", # 显示的标题
                        "content": [ # 图片的资源路径
            {
                "src": mix_list[0][0]
            },
            {
                "src": mix_list[1][0]
            },
            {
                "src": mix_list[2][0]
            },
            {
                "src": mix_list[3][0]
            },
            {
                "src": mix_list[4][0]
            },
            {
                "src": mix_list[5][0]
            },
            {
                "src": mix_list[6][0]
            },
            {
                "src": mix_list[7][0]
            }
            ],
            "unitText": "个数", # 表格显示单位
            "typeList": [
                "天上飞的",
                "地上跑的",
                "水里游的"
            ], # 表格左侧显示的分类描述
            "type": "au-classify-transport", # 组件名
            "keyboardtype": "num" # 数字键盘
            }
            ],
            "answers": [
               fly,
               land,
               steamer
            ], # 正确答案
            "knowledges": "分类", # 知识点
            "resource": "resource",
            "type": "填空", # 题型
            "explain": "explain",
            "level": "2", # 难度
            "number": "1-4-1-11" # 题型编号
            }
            ]
            all_questions.extend(questions)

        return all_questions


    #todo 1-4-2-3 拖一拖﹐把下面生活用品分为三类
    def ClothingclssifySelectT(self):

        all_questions = []
        for i in range(16):
            images_hat_url, images_surface_url, images_skirt_url, images_orb_url, images_shoes_url = q_CreatImgs.UpImages().Clothingclssify()
            mix_all_list = []
            mix_mid_list=[]
            mix_list=[]
            answer_list=[]
            mix_all_list.extend([random.sample(images_orb_url,3)])
            mix_all_list.extend([random.sample(images_shoes_url,3)])
            mix_all_list.extend([random.sample(images_skirt_url,3)])
            mix_all_list.extend([random.sample(images_surface_url,3)])
            mix_all_list.extend([random.sample(images_hat_url,3)])
            mix_mid_list.extend(random.sample(mix_all_list,3))
            for mid in mix_mid_list:
                for mi in mid:
                    mix_list.append(mi)
            random.shuffle(mix_list)
            print("mix_list",mix_list)
            for mix in mix_list:
                if [mix[1],mix[1],mix[1]] not in answer_list:
                    answer_list.append([mix[1],mix[1],mix[1]])
            print("answer_list",answer_list)
            questions=[
                {
                    "body": [
                        {
                            "title": "拖拽分类",
                            "stem": "拖一拖，把下面生活用品分为三类。",
                            "content": [

            {
                "type": mix_list[0][1],
                "src": mix_list[0][0]
            },
            {
                 "type": mix_list[1][1],
                "src": mix_list[1][0]
            },
            {
                "type": mix_list[2][1],
                "src": mix_list[2][0]
            },
            {
                 "type": mix_list[3][1],
                "src": mix_list[3][0]
            },
            {
                 "type": mix_list[4][1],
                "src": mix_list[4][0]
            },
            {
                "type": mix_list[5][1],
                "src": mix_list[5][0]
            },
            {
                "type": mix_list[6][1],
                "src": mix_list[6][0]
            },
            {
                "type": mix_list[7][1],
                "src": mix_list[7][0]
            },
            {
                "type": mix_list[8][1],
                "src": mix_list[8][0]
            },
            ],
            "type": "au-classify-drag"
            }
            ], # 图片数量支持多行展示
            "answers": answer_list, # 正确答案，为拖入的图片type类型值集合
            "knowledges": [
                "按不同的标准分类"
            ],
            "resource": "resource",
            "type": "填空",
            "explain": "explain",
            "level": "3", # 难度
            "number": "1-4-2-3" # 题型编号
                }
            ]
            all_questions.extend(questions)
        return all_questions

    #todo 1-4-2-3 拖一拖﹐把下面生活用品分为三类
    def ClothingclssifySelect(self):

        all_questions = []
        for i in range(16):
            images_hat_url, images_surface_url, images_skirt_url, images_orb_url, images_shoes_url = q_CreatImgs.UpImages().Clothingclssify()
            mix_all_list = []
            mix_mid_list=[]
            mix_list=[]
            answer_list=[]
            mix_all_list.extend([random.sample(images_orb_url,3)])
            mix_all_list.extend([random.sample(images_shoes_url,3)])
            mix_all_list.extend([random.sample(images_skirt_url,3)])
            mix_all_list.extend([random.sample(images_surface_url,3)])
            mix_all_list.extend([random.sample(images_hat_url,3)])
            mix_mid_list.extend(random.sample(mix_all_list,3))
            for mid in mix_mid_list:
                for mi in mid:
                    mix_list.append(mi)
            random.shuffle(mix_list)
            print("mix_list",mix_list)
            for mix in mix_list:
                if [mix[1],mix[1],mix[1]] not in answer_list:
                    answer_list.append([mix[1],mix[1],mix[1]])
            print("answer_list",answer_list)
            questions=[
                {
                    "body": [
                        {
                            "title": "拖拽分类",
                            "stem": "拖一拖，把下面物品分为三类。",
                            "content": [

            {
                "type": mix_list[0][1],
                "src": mix_list[0][0]
            },
            {
                 "type": mix_list[1][1],
                "src": mix_list[1][0]
            },
            {
                "type": mix_list[2][1],
                "src": mix_list[2][0]
            },
            {
                 "type": mix_list[3][1],
                "src": mix_list[3][0]
            },
            {
                 "type": mix_list[4][1],
                "src": mix_list[4][0]
            },
            {
                "type": mix_list[5][1],
                "src": mix_list[5][0]
            },
            {
                "type": mix_list[6][1],
                "src": mix_list[6][0]
            },
            {
                "type": mix_list[7][1],
                "src": mix_list[7][0]
            },
            {
                "type": mix_list[8][1],
                "src": mix_list[8][0]
            },
            ],
            "type": "au-classify-drag"
            }
            ], # 图片数量支持多行展示
            "answers": "{"+str(answer_list[0])+";"+str(answer_list[1])+";"+str(answer_list[2])+"}",
            "knowledges": [
                "按不同的标准分类"
            ],
            "resource": "resource",
            "type": "填空",
            "explain": "explain",
            "level": "3", # 难度
            "number": "1-4-2-3" # 题型编号
                }
            ]
            all_questions.extend(questions)
        return all_questions


    #todo 1-4-2-1 选择同类﹐涂上相同的颜色
    def ClassifyTintageSelect(self):
        all_questions = []
        for i in range(20):
            mix_list=[]
            mix_mix_list=[]
            brush_list=[]
            brush_addr_list=[]
            random_three_mix_list=[]
            variety_list=[]
            blue_brush_list=[]
            red_brush_list=[]
            yellow_brush_list=[]
            images_stationery_url, images_fruit_url, images_animal_url, images_brush_url = q_CreatImgs.UpImages().ClassifyTintage()
            random_three_mix_list.extend([random.sample(images_stationery_url,3)])
            random_three_mix_list.extend([random.sample(images_fruit_url,3)])
            random_three_mix_list.extend([random.sample(images_animal_url,3)])
            mix_mix_list.extend(random.sample(random_three_mix_list,2))

            for mix in mix_mix_list:
                for m in mix:
                    mix_list.append(m)

            random.shuffle(mix_list)
            print("mix_list",mix_list)

            for mm in mix_list:
                if mm[8] not in brush_list:
                    brush_list.append(mm[8])
                if mm[7] not in variety_list:
                    variety_list.append(mm[7])
                if mm[8] == "blue":
                    blue_brush_list.append(mix_list.index(mm))
                if mm[8] == "red":
                    red_brush_list.append(mix_list.index(mm))
                if mm[8] == "yellow":
                    yellow_brush_list.append(mix_list.index(mm))
            # if len(blue_brush_list)>0:
            #     blue_brush_list=set(blue_brush_list)
            # if len(red_brush_list)>0:
            #     red_brush_list=set(red_brush_list)
            # if len(yellow_brush_list)>0:
            #     yellow_brush_list=set(yellow_brush_list)
            print("blue_brush_list", blue_brush_list)
            print("red_brush_list", red_brush_list)
            print("yellow_brush_list", yellow_brush_list)
            print("brush_list",brush_list)
            print("variety_list",variety_list)
            for brush in images_brush_url:
                if brush[1] in brush_list:
                    brush_addr_list.append(brush[0])
            print("brush_addr_list",brush_addr_list)
            if len(blue_brush_list)>0 and len(red_brush_list)>0:
                questions=[
                {
                    "body": [
                        {
                            "title": "分类涂色",
                            "stem": "选择同类，涂上相同的颜色。",
                            "typeList": [
                                variety_list[0],
                                variety_list[1],

                            ], # 图片的三种类型（此处为水果、学习文具、动物，也可更改为上述已有其他类型） 1 - 4 - 2 - 1  只需选两种，1 - 4 - 2 - 2   需选三种
            "colorList": [
                {
                    "type": images_brush_url[0][1],  # 蓝色刷子
                    "src": images_brush_url[0][0]  # 刷子资源路径
            },
            {
                "type": images_brush_url[1][1], # 黄色刷子
            "src": images_brush_url[1][0]
            },

            ], # 刷子 1 - 4 - 2 - 1只需选任意两种 1 - 4 - 2 - 1  需三种（顺序任意）
            "brushImg": "/v2/组件/分类与整理/1-4-2-2/橡皮.svg", # 橡皮的资源路径
            "content": [ # 1 - 4 - 2 - 1只需传6个对象，1 - 4 - 2 - 2 需传8个对象
            {
                "type": mix_list[0][7], # 这里的类别需要与typeList字段符合
            "src": mix_list[0][0], # 未上色原图
            "redSrc": mix_list[0][1], # 对应的填色图片
            "blueSrc": mix_list[0][2],
            "yellowSrc": mix_list[0][3],
            "redLineSrc": mix_list[0][4], # 带色线描图：刷子移入图片时展示
            "blueLineSrc": mix_list[0][5],
            "yellowLineSrc": mix_list[0][6]
            },
            {
                "type": mix_list[1][7],  # 这里的类别需要与typeList字段符合
                "src": mix_list[1][0],  # 未上色原图
                "redSrc": mix_list[1][1],  # 对应的填色图片
                "blueSrc": mix_list[1][2],
                "yellowSrc": mix_list[1][3],
                "redLineSrc": mix_list[1][4],  # 带色线描图：刷子移入图片时展示
                "blueLineSrc": mix_list[1][5],
                "yellowLineSrc": mix_list[1][6]
            },
            {
                "type": mix_list[2][7],  # 这里的类别需要与typeList字段符合
                "src": mix_list[2][0],  # 未上色原图
                "redSrc": mix_list[2][1],  # 对应的填色图片
                "blueSrc": mix_list[2][2],
                "yellowSrc": mix_list[2][3],
                "redLineSrc": mix_list[2][4],  # 带色线描图：刷子移入图片时展示
                "blueLineSrc": mix_list[2][5],
                "yellowLineSrc": mix_list[2][6]
            },
            {
                "type": mix_list[3][7],  # 这里的类别需要与typeList字段符合
                "src": mix_list[3][0],  # 未上色原图
                "redSrc": mix_list[3][1],  # 对应的填色图片
                "blueSrc": mix_list[3][2],
                "yellowSrc": mix_list[3][3],
                "redLineSrc": mix_list[3][4],  # 带色线描图：刷子移入图片时展示
                "blueLineSrc": mix_list[3][5],
                "yellowLineSrc": mix_list[3][6]
            },
            {
                "type": mix_list[4][7],  # 这里的类别需要与typeList字段符合
                "src": mix_list[4][0],  # 未上色原图
                "redSrc": mix_list[4][1],  # 对应的填色图片
                "blueSrc": mix_list[4][2],
                "yellowSrc": mix_list[4][3],
                "redLineSrc": mix_list[4][4],  # 带色线描图：刷子移入图片时展示
                "blueLineSrc": mix_list[4][5],
                "yellowLineSrc": mix_list[4][6]
            },
            {
                "type": mix_list[5][7],  # 这里的类别需要与typeList字段符合
                "src": mix_list[5][0],  # 未上色原图
                "redSrc": mix_list[5][1],  # 对应的填色图片
                "blueSrc": mix_list[5][2],
                "yellowSrc": mix_list[5][3],
                "redLineSrc": mix_list[5][4],  # 带色线描图：刷子移入图片时展示
                "blueLineSrc": mix_list[5][5],
                "yellowLineSrc": mix_list[5][6]
            },

            ],
            "type": "au-classify-variousColor" # 组件名
            }
            ],
            # "answers":  "{"+str(blue_brush_list)+";"+str(red_brush_list)+"}",
            "answers":  "{{"+str(blue_brush_list[0])+";"+str(blue_brush_list[1])+";"+str(blue_brush_list[2])+"};{"+str(red_brush_list[0])+";"+str(red_brush_list[1])+";"+str(red_brush_list[2])+"}}",

           # 对应的图片数组染色情况
            "knowledges": "按不同的标准分类", # 知识点
            "resource": "resource",
            "type": "操作", # 题型
            "explain": "explain",
            "level": "2", # 难度
            "number": "1-4-2-1" # 题型编号 依据实际情况 两种是1 - 4 - 2 - 1， 三种是1 - 4 - 2 - 1
            }
            ]
            if len(blue_brush_list)>0 and len(yellow_brush_list)>0:
                questions = [
                    {
                        "body": [
                            {
                                "title": "分类涂色",
                                "stem": "选择同类，涂上相同的颜色",
                                "typeList": [
                                    variety_list[0],
                                    variety_list[1],

                                ],  # 图片的三种类型（此处为水果、学习文具、动物，也可更改为上述已有其他类型） 1 - 4 - 2 - 1  只需选两种，1 - 4 - 2 - 2   需选三种
                                "colorList": [
                                    {
                                        "type": images_brush_url[0][1],  # 蓝色刷子
                                        "src": images_brush_url[0][0]  # 刷子资源路径
                                    },
                                    {
                                        "type": images_brush_url[1][1],  # 黄色刷子
                                        "src": images_brush_url[1][0]
                                    },

                                ],  # 刷子 1 - 4 - 2 - 1只需选任意两种 1 - 4 - 2 - 1  需三种（顺序任意）
                                "brushImg": "/v2/组件/分类与整理/1-4-2-2/橡皮.svg",  # 橡皮的资源路径
                                "content": [  # 1 - 4 - 2 - 1只需传6个对象，1 - 4 - 2 - 2 需传8个对象
                                    {
                                        "type": mix_list[0][7],  # 这里的类别需要与typeList字段符合
                                        "src": mix_list[0][0],  # 未上色原图
                                        "redSrc": mix_list[0][1],  # 对应的填色图片
                                        "blueSrc": mix_list[0][2],
                                        "yellowSrc": mix_list[0][3],
                                        "redLineSrc": mix_list[0][4],  # 带色线描图：刷子移入图片时展示
                                        "blueLineSrc": mix_list[0][5],
                                        "yellowLineSrc": mix_list[0][6]
                                    },
                                    {
                                        "type": mix_list[1][7],  # 这里的类别需要与typeList字段符合
                                        "src": mix_list[1][0],  # 未上色原图
                                        "redSrc": mix_list[1][1],  # 对应的填色图片
                                        "blueSrc": mix_list[1][2],
                                        "yellowSrc": mix_list[1][3],
                                        "redLineSrc": mix_list[1][4],  # 带色线描图：刷子移入图片时展示
                                        "blueLineSrc": mix_list[1][5],
                                        "yellowLineSrc": mix_list[1][6]
                                    },
                                    {
                                        "type": mix_list[2][7],  # 这里的类别需要与typeList字段符合
                                        "src": mix_list[2][0],  # 未上色原图
                                        "redSrc": mix_list[2][1],  # 对应的填色图片
                                        "blueSrc": mix_list[2][2],
                                        "yellowSrc": mix_list[2][3],
                                        "redLineSrc": mix_list[2][4],  # 带色线描图：刷子移入图片时展示
                                        "blueLineSrc": mix_list[2][5],
                                        "yellowLineSrc": mix_list[2][6]
                                    },
                                    {
                                        "type": mix_list[3][7],  # 这里的类别需要与typeList字段符合
                                        "src": mix_list[3][0],  # 未上色原图
                                        "redSrc": mix_list[3][1],  # 对应的填色图片
                                        "blueSrc": mix_list[3][2],
                                        "yellowSrc": mix_list[3][3],
                                        "redLineSrc": mix_list[3][4],  # 带色线描图：刷子移入图片时展示
                                        "blueLineSrc": mix_list[3][5],
                                        "yellowLineSrc": mix_list[3][6]
                                    },
                                    {
                                        "type": mix_list[4][7],  # 这里的类别需要与typeList字段符合
                                        "src": mix_list[4][0],  # 未上色原图
                                        "redSrc": mix_list[4][1],  # 对应的填色图片
                                        "blueSrc": mix_list[4][2],
                                        "yellowSrc": mix_list[4][3],
                                        "redLineSrc": mix_list[4][4],  # 带色线描图：刷子移入图片时展示
                                        "blueLineSrc": mix_list[4][5],
                                        "yellowLineSrc": mix_list[4][6]
                                    },
                                    {
                                        "type": mix_list[5][7],  # 这里的类别需要与typeList字段符合
                                        "src": mix_list[5][0],  # 未上色原图
                                        "redSrc": mix_list[5][1],  # 对应的填色图片
                                        "blueSrc": mix_list[5][2],
                                        "yellowSrc": mix_list[5][3],
                                        "redLineSrc": mix_list[5][4],  # 带色线描图：刷子移入图片时展示
                                        "blueLineSrc": mix_list[5][5],
                                        "yellowLineSrc": mix_list[5][6]
                                    },

                                ],
                                "type": "au-classify-variousColor"  # 组件名
                            }
                        ],
                        # "answers": "{"+str(blue_brush_list)+";"+str(yellow_brush_list)+"}",
                        "answers": "{{"+str(blue_brush_list[0])+";"+str(blue_brush_list[1])+";"+str(blue_brush_list[2])+"};{"+str(yellow_brush_list[0])+";"+str(yellow_brush_list[1])+";"+str(yellow_brush_list[2])+"}}",
                        # 对应的图片数组染色情况
                        "knowledges": "按不同的标准分类",  # 知识点
                        "resource": "resource",
                        "type": "操作",  # 题型
                        "explain": "explain",
                        "level": "2",  # 难度
                        "number": "1-4-2-1"  # 题型编号 依据实际情况 两种是1 - 4 - 2 - 1， 三种是1 - 4 - 2 - 1
                    }
                ]
            if len(red_brush_list)>0 and len(yellow_brush_list)>0:
                questions = [
                    {
                        "body": [
                            {
                                "title": "分类涂色",
                                "stem": "选择同类，涂上相同的颜色",
                                "typeList": [
                                    variety_list[0],
                                    variety_list[1],

                                ],  # 图片的三种类型（此处为水果、学习文具、动物，也可更改为上述已有其他类型） 1 - 4 - 2 - 1  只需选两种，1 - 4 - 2 - 2   需选三种
                                "colorList": [
                                    {
                                        "type": images_brush_url[0][1],  # 蓝色刷子
                                        "src": images_brush_url[0][0]  # 刷子资源路径
                                    },
                                    {
                                        "type": images_brush_url[1][1],  # 黄色刷子
                                        "src": images_brush_url[1][0]
                                    },

                                ],  # 刷子 1 - 4 - 2 - 1只需选任意两种 1 - 4 - 2 - 1  需三种（顺序任意）
                                "brushImg": "/v2/组件/分类与整理/1-4-2-2/橡皮.svg",  # 橡皮的资源路径
                                "content": [  # 1 - 4 - 2 - 1只需传6个对象，1 - 4 - 2 - 2 需传8个对象
                                    {
                                        "type": mix_list[0][7],  # 这里的类别需要与typeList字段符合
                                        "src": mix_list[0][0],  # 未上色原图
                                        "redSrc": mix_list[0][1],  # 对应的填色图片
                                        "blueSrc": mix_list[0][2],
                                        "yellowSrc": mix_list[0][3],
                                        "redLineSrc": mix_list[0][4],  # 带色线描图：刷子移入图片时展示
                                        "blueLineSrc": mix_list[0][5],
                                        "yellowLineSrc": mix_list[0][6]
                                    },
                                    {
                                        "type": mix_list[1][7],  # 这里的类别需要与typeList字段符合
                                        "src": mix_list[1][0],  # 未上色原图
                                        "redSrc": mix_list[1][1],  # 对应的填色图片
                                        "blueSrc": mix_list[1][2],
                                        "yellowSrc": mix_list[1][3],
                                        "redLineSrc": mix_list[1][4],  # 带色线描图：刷子移入图片时展示
                                        "blueLineSrc": mix_list[1][5],
                                        "yellowLineSrc": mix_list[1][6]
                                    },
                                    {
                                        "type": mix_list[2][7],  # 这里的类别需要与typeList字段符合
                                        "src": mix_list[2][0],  # 未上色原图
                                        "redSrc": mix_list[2][1],  # 对应的填色图片
                                        "blueSrc": mix_list[2][2],
                                        "yellowSrc": mix_list[2][3],
                                        "redLineSrc": mix_list[2][4],  # 带色线描图：刷子移入图片时展示
                                        "blueLineSrc": mix_list[2][5],
                                        "yellowLineSrc": mix_list[2][6]
                                    },
                                    {
                                        "type": mix_list[3][7],  # 这里的类别需要与typeList字段符合
                                        "src": mix_list[3][0],  # 未上色原图
                                        "redSrc": mix_list[3][1],  # 对应的填色图片
                                        "blueSrc": mix_list[3][2],
                                        "yellowSrc": mix_list[3][3],
                                        "redLineSrc": mix_list[3][4],  # 带色线描图：刷子移入图片时展示
                                        "blueLineSrc": mix_list[3][5],
                                        "yellowLineSrc": mix_list[3][6]
                                    },
                                    {
                                        "type": mix_list[4][7],  # 这里的类别需要与typeList字段符合
                                        "src": mix_list[4][0],  # 未上色原图
                                        "redSrc": mix_list[4][1],  # 对应的填色图片
                                        "blueSrc": mix_list[4][2],
                                        "yellowSrc": mix_list[4][3],
                                        "redLineSrc": mix_list[4][4],  # 带色线描图：刷子移入图片时展示
                                        "blueLineSrc": mix_list[4][5],
                                        "yellowLineSrc": mix_list[4][6]
                                    },
                                    {
                                        "type": mix_list[5][7],  # 这里的类别需要与typeList字段符合
                                        "src": mix_list[5][0],  # 未上色原图
                                        "redSrc": mix_list[5][1],  # 对应的填色图片
                                        "blueSrc": mix_list[5][2],
                                        "yellowSrc": mix_list[5][3],
                                        "redLineSrc": mix_list[5][4],  # 带色线描图：刷子移入图片时展示
                                        "blueLineSrc": mix_list[5][5],
                                        "yellowLineSrc": mix_list[5][6]
                                    },

                                ],
                                "type": "au-classify-variousColor"  # 组件名
                            }
                        ],
                        # "answers":"{"+str(red_brush_list)+";"+str(yellow_brush_list)+"}",
                        "answers":"{{"+str(red_brush_list[0])+";"+str(red_brush_list[1])+";"+str(red_brush_list[2])+"};{"+str(yellow_brush_list[0])+";"+str(yellow_brush_list[1])+";"+str(yellow_brush_list[2])+"}}",
                        # 对应的图片数组染色情况
                        "knowledges": "按不同的标准分类",  # 知识点
                        "resource": "resource",
                        "type": "操作",  # 题型
                        "explain": "explain",
                        "level": "2",  # 难度
                        "number": "1-4-2-1"  # 题型编号 依据实际情况 两种是1 - 4 - 2 - 1， 三种是1 - 4 - 2 - 1
                    }
                ]
            all_questions.extend(questions)
        return all_questions


    #todo 1-4-2-2 选择同类﹐涂上相同的颜色
    def ClassifyTintageSelect2(self):
        all_questions = []
        for i in range(20):
            mix_list=[]
            mix_mix_list=[]
            brush_list=[]
            brush_addr_list=[]
            random_three_mix_list=[]
            variety_list=[]
            blue_brush_list=[]
            red_brush_list=[]
            yellow_brush_list=[]
            images_stationery_url, images_fruit_url, images_animal_url, images_brush_url = q_CreatImgs.UpImages().ClassifyTintage()
            random_three_mix_list.extend([random.sample(images_stationery_url,3)])
            random_three_mix_list.extend([random.sample(images_fruit_url,2)])
            random_three_mix_list.extend([random.sample(images_animal_url,3)])
            mix_mix_list.extend(random.sample(random_three_mix_list,3))

            for mix in mix_mix_list:
                for m in mix:
                    mix_list.append(m)

            random.shuffle(mix_list)
            print("mix_list",mix_list)

            for mm in mix_list:
                if mm[8] not in brush_list:
                    brush_list.append(mm[8])
                if mm[7] not in variety_list:
                    variety_list.append(mm[7])
                if mm[8]=="blue":
                    blue_brush_list.append(mix_list.index(mm))
                if mm[8]=="red":
                    red_brush_list.append(mix_list.index(mm))
                if mm[8]=="yellow":
                    yellow_brush_list.append(mix_list.index(mm))
            # blue_brush_list=set(blue_brush_list)
            # red_brush_list=set(red_brush_list)
            # yellow_brush_list=set(yellow_brush_list)
            print("blue_brush_list",blue_brush_list)
            print("red_brush_list",red_brush_list)
            print("yellow_brush_list",yellow_brush_list)

            print("brush_list",brush_list)
            print("variety_list",variety_list)
            for brush in images_brush_url:
                if brush[1] in brush_list:
                    brush_addr_list.append(brush[0])
            print("brush_addr_list",brush_addr_list)


            questions=[
                {
                    "body": [
                        {
                            "title": "分类涂色",
                            "stem": "选择同类，涂上相同的颜色。",
                            "typeList": [
                                variety_list[0],
                                variety_list[1],
                                variety_list[2],

                            ], # 图片的三种类型（此处为水果、学习文具、动物，也可更改为上述已有其他类型） 1 - 4 - 2 - 1  只需选两种，1 - 4 - 2 - 2   需选三种
            "colorList": [
                {
                    "type": images_brush_url[0][1], # 蓝色刷子
                "src": images_brush_url[0][0] # 刷子资源路径
            },
            {
                "type": images_brush_url[1][1], # 黄色刷子
            "src":  images_brush_url[1][0]
            },
            {
                "type": images_brush_url[2][1],  # 黄色刷子
                "src": images_brush_url[2][0]
            },

            ], # 刷子 1 - 4 - 2 - 1只需选任意两种 1 - 4 - 2 - 1  需三种（顺序任意）
            "brushImg": "/v2/组件/分类与整理/1-4-2-2/橡皮.svg", # 橡皮的资源路径
            "content": [ # 1 - 4 - 2 - 1只需传6个对象，1 - 4 - 2 - 2 需传8个对象
                {
                    "type": mix_list[0][7],  # 这里的类别需要与typeList字段符合
                    "src": mix_list[0][0],  # 未上色原图
                    "redSrc": mix_list[0][1],  # 对应的填色图片
                    "blueSrc": mix_list[0][2],
                    "yellowSrc": mix_list[0][3],
                    "redLineSrc": mix_list[0][4],  # 带色线描图：刷子移入图片时展示
                    "blueLineSrc": mix_list[0][5],
                    "yellowLineSrc": mix_list[0][6]
                },
                {
                    "type": mix_list[1][7],  # 这里的类别需要与typeList字段符合
                    "src": mix_list[1][0],  # 未上色原图
                    "redSrc": mix_list[1][1],  # 对应的填色图片
                    "blueSrc": mix_list[1][2],
                    "yellowSrc": mix_list[1][3],
                    "redLineSrc": mix_list[1][4],  # 带色线描图：刷子移入图片时展示
                    "blueLineSrc": mix_list[1][5],
                    "yellowLineSrc": mix_list[1][6]
                },
                {
                    "type": mix_list[2][7],  # 这里的类别需要与typeList字段符合
                    "src": mix_list[2][0],  # 未上色原图
                    "redSrc": mix_list[2][1],  # 对应的填色图片
                    "blueSrc": mix_list[2][2],
                    "yellowSrc": mix_list[2][3],
                    "redLineSrc": mix_list[2][4],  # 带色线描图：刷子移入图片时展示
                    "blueLineSrc": mix_list[2][5],
                    "yellowLineSrc": mix_list[2][6]
                },
                {
                    "type": mix_list[3][7],  # 这里的类别需要与typeList字段符合
                    "src": mix_list[3][0],  # 未上色原图
                    "redSrc": mix_list[3][1],  # 对应的填色图片
                    "blueSrc": mix_list[3][2],
                    "yellowSrc": mix_list[3][3],
                    "redLineSrc": mix_list[3][4],  # 带色线描图：刷子移入图片时展示
                    "blueLineSrc": mix_list[3][5],
                    "yellowLineSrc": mix_list[3][6]
                },
                {
                    "type": mix_list[4][7],  # 这里的类别需要与typeList字段符合
                    "src": mix_list[4][0],  # 未上色原图
                    "redSrc": mix_list[4][1],  # 对应的填色图片
                    "blueSrc": mix_list[4][2],
                    "yellowSrc": mix_list[4][3],
                    "redLineSrc": mix_list[4][4],  # 带色线描图：刷子移入图片时展示
                    "blueLineSrc": mix_list[4][5],
                    "yellowLineSrc": mix_list[4][6]
                },
                {
                    "type": mix_list[5][7],  # 这里的类别需要与typeList字段符合
                    "src": mix_list[5][0],  # 未上色原图
                    "redSrc": mix_list[5][1],  # 对应的填色图片
                    "blueSrc": mix_list[5][2],
                    "yellowSrc": mix_list[5][3],
                    "redLineSrc": mix_list[5][4],  # 带色线描图：刷子移入图片时展示
                    "blueLineSrc": mix_list[5][5],
                    "yellowLineSrc": mix_list[5][6]
                },
                {
                    "type": mix_list[6][7],  # 这里的类别需要与typeList字段符合
                    "src": mix_list[6][0],  # 未上色原图
                    "redSrc": mix_list[6][1],  # 对应的填色图片
                    "blueSrc": mix_list[6][2],
                    "yellowSrc": mix_list[6][3],
                    "redLineSrc": mix_list[6][4],  # 带色线描图：刷子移入图片时展示
                    "blueLineSrc": mix_list[6][5],
                    "yellowLineSrc": mix_list[6][6]
                },
                {
                    "type": mix_list[7][7],  # 这里的类别需要与typeList字段符合
                    "src": mix_list[7][0],  # 未上色原图
                    "redSrc": mix_list[7][1],  # 对应的填色图片
                    "blueSrc": mix_list[7][2],
                    "yellowSrc": mix_list[7][3],
                    "redLineSrc": mix_list[7][4],  # 带色线描图：刷子移入图片时展示
                    "blueLineSrc": mix_list[7][5],
                    "yellowLineSrc": mix_list[7][6]
                },

            ],
            "type": "au-classify-variousColor" # 组件名
            }
            ],
            # "answers": "{"+str(blue_brush_list)+";"+str(red_brush_list)+";"+str(yellow_brush_list)+"}", # 答案 对应的图片数组分类情况
            "answers": "{{"+str(blue_brush_list[0])+";"+str(blue_brush_list[1])+"};{"+str(red_brush_list[0])+";"+str(red_brush_list[1])+";"+str(red_brush_list[2])+"};{"+str(yellow_brush_list[0])+";"+str(yellow_brush_list[1])+";"+str(yellow_brush_list[2])+"}}", # 答案 对应的图片数组分类情况
            # "answers": [(str(blue_brush_list)),(str(red_brush_list)),(str(yellow_brush_list))], # 答案 对应的图片数组分类情况
           # 对应的图片数组染色情况
            "knowledges": "按不同的标准分类", # 知识点
            "resource": "resource",
            "type": "操作", # 题型
            "explain": "explain",
            "level": "2", # 难度
            "number": "1-4-2-2" # 题型编号 依据实际情况 两种是1 - 4 - 2 - 1， 三种是1 - 4 - 2 - 1
            }
            ]
            print("================================================================================")
            print("questions",questions)
            all_questions.extend(questions)
        return all_questions


    #todo 1-4-2-4  按形状分类
    def ClassifyShapeT(self):

        all_questions = []
        for i in range(18):
            mix_list=[]
            mid_list=[]

            answer_fruit_list1=[]
            answer_fruit_list2=[]
            answer_fruit_list3=[]
            answer_shape_list1=[]
            answer_shape_list2=[]
            answer_shape_list3=[]
            comparison_shape_list=["circle","square","triangle"]
            cardShape_list=["cardShape","fruitType"]
            shape_list=["circle","square","triangle","circle","square","triangle","circle","square","triangle"]
            random.shuffle(shape_list)
            images_fruit_url = q_CreatImgs.UpImages().FruitShape()
            mid_list.extend(random.sample(images_fruit_url,3))
            mix_list.extend(random.sample(mid_list,3))
            mix_list.extend(random.sample(mid_list,3))
            mix_list.extend(random.sample(mid_list,3))
            random.shuffle(mix_list)
            print("len_mix_list",len(mix_list))

            for m in range(len(mix_list)):
                if mix_list[m][1]==mid_list[0][1]:
                    answer_fruit_list1.append(m+1)
                elif mix_list[m][1]==mid_list[1][1]:
                    answer_fruit_list2.append(m+1)
                elif mix_list[m][1]==mid_list[2][1]:
                    answer_fruit_list3.append(m+1)
            for comp in range(len(shape_list)):
                if shape_list[comp]==comparison_shape_list[0]:
                    answer_shape_list1.append(comp+1)
                elif shape_list[comp]==comparison_shape_list[1]:
                    answer_shape_list2.append(comp+1)
                elif shape_list[comp]==comparison_shape_list[2]:
                    answer_shape_list3.append(comp+1)

            print("mid_list", mid_list)
            print("mix_list",mix_list)
            print("answer_fruit_list1",answer_fruit_list1)
            print("answer_fruit_list2",answer_fruit_list2)
            print("answer_fruit_list3",answer_fruit_list3)
            print("answer_shape_list1",answer_shape_list1)
            print("answer_shape_list2",answer_shape_list2)
            print("answer_shape_list3",answer_shape_list3)


            card=random.choice(cardShape_list)

            if card=="cardShape":
                questions = [
                    {
                        "body": [
                            {
                                "title": "拖拽分类",
                                "stem": "按卡片形状分类。",  # 与classifyType字段值对应
                                "classifyType": "cardShape",  # 分类标准（2 种） 根据卡片形状：cardShape、水果种类：fruitType
                                "typeList": [
                                    {
                                        "order": 1,
                                        "type": mix_list[0][1],  # 水果类型任意三种（此处   苹果: apple 、草莓：berry、菠萝：pineapple）
                                        "shape": shape_list[0],
                                        "src": mix_list[0][0]  # 图片路径
                                    },
                                    {
                                        "order": 2,
                                        "type": mix_list[1][1],
                                        "shape": shape_list[1],
                                        "src": mix_list[1][0]
                                    },
                                    {
                                        "order": 3,
                                        "type": mix_list[2][1],
                                        "shape": shape_list[2],
                                        "src": mix_list[2][0]
                                    },
                                    {
                                        "order": 4,
                                        "type": mix_list[3][1],  # 水果类型任意三种（此处   苹果: apple 、草莓：berry、菠萝：pineapple）
                                        "shape": shape_list[3],
                                        "src": mix_list[3][0]  # 图片路径
                                    },
                                    {
                                        "order": 5,
                                        "type": mix_list[4][1],
                                        "shape": shape_list[4],
                                        "src": mix_list[4][0]
                                    },
                                    {
                                        "order": 6,
                                        "type": mix_list[5][1],
                                        "shape": shape_list[5],
                                        "src": mix_list[5][0]
                                    },
                                    {
                                        "order": 7,
                                        "type": mix_list[6][1],  # 水果类型任意三种（此处   苹果: apple 、草莓：berry、菠萝：pineapple）
                                        "shape": shape_list[6],
                                        "src": mix_list[6][0]  # 图片路径
                                    },
                                    {
                                        "order": 8,
                                        "type": mix_list[7][1],
                                        "shape": shape_list[7],
                                        "src": mix_list[7][0]
                                    },
                                    {
                                        "order": 9,
                                        "type": mix_list[8][1],
                                        "shape": shape_list[8],
                                        "src": mix_list[8][0]
                                    },
                                ],  # 提供三种水果类型和资源路径
                                "type": "au-classify-byshape"  # 组件名
                            }
                        ],
                        "answers": "{{"+str(answer_shape_list1[0])+";"+str(answer_shape_list1[1])+";"+str(answer_shape_list1[2])+"};{"+str(answer_shape_list2[0])+";"+str(answer_shape_list2[1])+";"+str(answer_shape_list2[2])+"};{"+str(answer_shape_list3[0])+";"+str(answer_shape_list3[1])+";"+str(answer_shape_list3[2])+"}}",
                        "knowledges": [
                            "按不同的标准分类"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "操作",  # 题型
                        "explain": "explain",
                        "level": "3",  # 难度
                        "number": "1-4-2-4"  # 题型编号
                    }
                ]

            if card=="fruitType":
                questions = [
                    {
                        "body": [
                            {
                                "title": "拖拽分类",
                                "stem": "按水果种类分类。",  # 与classifyType字段值对应
                                "classifyType": "fruitType",  # 分类标准（2 种） 根据卡片形状：cardShape、水果种类：fruitType
                                "typeList": [
                                    {
                                        "order": 1,
                                        "type": mix_list[0][1],  # 水果类型任意三种（此处   苹果: apple 、草莓：berry、菠萝：pineapple）
                                        "shape": shape_list[0],
                                        "src": mix_list[0][0]  # 图片路径
                                    },
                                    {
                                        "order": 2,
                                        "type": mix_list[1][1],
                                        "shape": shape_list[1],
                                        "src": mix_list[1][0]
                                    },
                                    {
                                        "order": 3,
                                        "type": mix_list[2][1],
                                        "shape": shape_list[2],
                                        "src": mix_list[2][0]
                                    },
                                    {
                                        "order": 4,
                                        "type": mix_list[3][1],  # 水果类型任意三种（此处   苹果: apple 、草莓：berry、菠萝：pineapple）
                                        "shape": shape_list[3],
                                        "src": mix_list[3][0]  # 图片路径
                                    },
                                    {
                                        "order": 5,
                                        "type": mix_list[4][1],
                                        "shape": shape_list[4],
                                        "src": mix_list[4][0]
                                    },
                                    {
                                        "order": 6,
                                        "type": mix_list[5][1],
                                        "shape": shape_list[5],
                                        "src": mix_list[5][0]
                                    },
                                    {
                                        "order": 7,
                                        "type": mix_list[6][1],  # 水果类型任意三种（此处   苹果: apple 、草莓：berry、菠萝：pineapple）
                                        "shape": shape_list[6],
                                        "src": mix_list[6][0]  # 图片路径
                                    },
                                    {
                                        "order": 8,
                                        "type": mix_list[7][1],
                                        "shape": shape_list[7],
                                        "src": mix_list[7][0]
                                    },
                                    {
                                        "order": 9,
                                        "type": mix_list[8][1],
                                        "shape": shape_list[8],
                                        "src": mix_list[8][0]
                                    },
                                ],  # 提供三种水果类型和资源路径
                                "type": "au-classify-byshape"  # 组件名
                            }
                        ],
                         "answers": "{{"+str(answer_fruit_list1[0])+";"+str(answer_fruit_list1[1])+";"+str(answer_fruit_list1[2])+"};{"+str(answer_fruit_list2[0])+";"+str(answer_fruit_list2[1])+";"+str(answer_fruit_list2[2])+"};{"+str(answer_fruit_list3[0])+";"+str(answer_fruit_list3[1])+";"+str(answer_fruit_list3[2])+"}}",
                        "knowledges": [
                            "按不同的标准分类"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "操作",  # 题型
                        "explain": "explain",
                        "level": "3",  # 难度
                        "number": "1-4-2-4"  # 题型编号
                    }
                ]


            all_questions.extend(questions)
            print("===========================================\n",questions)
        return all_questions

    #todo 1-4-2-4  按形状分类
    def ClassifyShape(self):

        all_questions = []
        for i in range(18):
            mix_list=[]
            mid_list=[]

            answer_fruit_list1=[]
            answer_fruit_list2=[]
            answer_fruit_list3=[]
            answer_shape_list1=[]
            answer_shape_list2=[]
            answer_shape_list3=[]
            comparison_shape_list=["circle","square","triangle"]
            cardShape_list=["cardShape","fruitType"]
            shape_list=["circle","square","triangle","circle","square","triangle","circle","square","triangle"]
            random.shuffle(shape_list)
            images_fruit_url = q_CreatImgs.UpImages().FruitShape()
            mid_list.extend(random.sample(images_fruit_url,3))
            mix_list.extend(random.sample(mid_list,3))
            mix_list.extend(random.sample(mid_list,3))
            mix_list.extend(random.sample(mid_list,3))
            random.shuffle(mix_list)
            print("len_mix_list",len(mix_list))

            for m in range(len(mix_list)):
                if mix_list[m][1]==mid_list[0][1]:
                    answer_fruit_list1.append(m+1)
                elif mix_list[m][1]==mid_list[1][1]:
                    answer_fruit_list2.append(m+1)
                elif mix_list[m][1]==mid_list[2][1]:
                    answer_fruit_list3.append(m+1)
            for comp in range(len(shape_list)):
                if shape_list[comp]==comparison_shape_list[0]:
                    answer_shape_list1.append(comp+1)
                elif shape_list[comp]==comparison_shape_list[1]:
                    answer_shape_list2.append(comp+1)
                elif shape_list[comp]==comparison_shape_list[2]:
                    answer_shape_list3.append(comp+1)

            print("mid_list", mid_list)
            print("mix_list",mix_list)
            print("answer_fruit_list1",answer_fruit_list1)
            print("answer_fruit_list2",answer_fruit_list2)
            print("answer_fruit_list3",answer_fruit_list3)
            print("answer_shape_list1",answer_shape_list1)
            print("answer_shape_list2",answer_shape_list2)
            print("answer_shape_list3",answer_shape_list3)


            card=random.choice(cardShape_list)

            questions = [
                    {
                        "body": [
                            {
                                "title": "拖拽分类",
                                "stem": "按形状/水果种类分类。",  # 与classifyType字段值对应
                                "classifyType": "cardShape",  # 分类标准（2 种） 根据卡片形状：cardShape、水果种类：fruitType
                                "typeList": [
                                    {
                                        "order": 1,
                                        "type": mix_list[0][1],  # 水果类型任意三种（此处   苹果: apple 、草莓：berry、菠萝：pineapple）
                                        "shape": shape_list[0],
                                        "src": mix_list[0][0]  # 图片路径
                                    },
                                    {
                                        "order": 2,
                                        "type": mix_list[1][1],
                                        "shape": shape_list[1],
                                        "src": mix_list[1][0]
                                    },
                                    {
                                        "order": 3,
                                        "type": mix_list[2][1],
                                        "shape": shape_list[2],
                                        "src": mix_list[2][0]
                                    },
                                    {
                                        "order": 4,
                                        "type": mix_list[3][1],  # 水果类型任意三种（此处   苹果: apple 、草莓：berry、菠萝：pineapple）
                                        "shape": shape_list[3],
                                        "src": mix_list[3][0]  # 图片路径
                                    },
                                    {
                                        "order": 5,
                                        "type": mix_list[4][1],
                                        "shape": shape_list[4],
                                        "src": mix_list[4][0]
                                    },
                                    {
                                        "order": 6,
                                        "type": mix_list[5][1],
                                        "shape": shape_list[5],
                                        "src": mix_list[5][0]
                                    },
                                    {
                                        "order": 7,
                                        "type": mix_list[6][1],  # 水果类型任意三种（此处   苹果: apple 、草莓：berry、菠萝：pineapple）
                                        "shape": shape_list[6],
                                        "src": mix_list[6][0]  # 图片路径
                                    },
                                    {
                                        "order": 8,
                                        "type": mix_list[7][1],
                                        "shape": shape_list[7],
                                        "src": mix_list[7][0]
                                    },
                                    {
                                        "order": 9,
                                        "type": mix_list[8][1],
                                        "shape": shape_list[8],
                                        "src": mix_list[8][0]
                                    },
                                ],  # 提供三种水果类型和资源路径
                                "type": "au-classify-byshape"  # 组件名
                            }
                        ],
                        "answers": "({{"+str(answer_shape_list1[0])+";"+str(answer_shape_list1[1])+";"+str(answer_shape_list1[2])+"};{"+str(answer_shape_list2[0])+";"+str(answer_shape_list2[1])+";"+str(answer_shape_list2[2])+"};{"+str(answer_shape_list3[0])+";"+str(answer_shape_list3[1])+";"+str(answer_shape_list3[2])+"}}|{{"+str(answer_fruit_list1[0])+";"+str(answer_fruit_list1[1])+";"+str(answer_fruit_list1[2])+"};{"+str(answer_fruit_list2[0])+";"+str(answer_fruit_list2[1])+";"+str(answer_fruit_list2[2])+"};{"+str(answer_fruit_list3[0])+";"+str(answer_fruit_list3[1])+";"+str(answer_fruit_list3[2])+"}})",
                        "knowledges": [
                            "按不同的标准分类"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "操作",  # 题型
                        "explain": "explain",
                        "level": "3",  # 难度
                        "number": "1-4-2-4"  # 题型编号
                    }
                ]



            all_questions.extend(questions)
            print("===========================================\n",questions)
        return all_questions

    # todo 1-4-2-5   按算式结果分类
    def CalculationResultSelect(self):
        all_questions=[]
        for i in range(18):
            all_result=[]
            mix_list=[]
            less_fif_list=[]
            than_fif_list=[]
            One, Two, Thire, Four, Fif, Six, Seven, Eight, Nine = q_CreatImgs.UpImages().CalculationClssify()
            all_result.extend(One)
            all_result.extend(Two)
            all_result.extend(Thire)
            all_result.extend(Four)
            all_result.extend(Six)
            all_result.extend(Eight)
            all_result.extend(Nine)
            mix_list.extend(random.sample(all_result,12))
            for mix in mix_list:
                if mix[1]<5:
                    less_fif_list.append(mix[0])
                else:
                    than_fif_list.append(mix[0])

            print("less_fif_list",less_fif_list)
            print("than_fif_list",than_fif_list)
            if len(than_fif_list)==1:
                questions=[
                    {
                        "body": [
                            {
                                "title": "分类",
                                "stem": "按要求分类。",
                                "num": "5", # 拖入框的界限数字
                            "questionItem": [
                                               mix_list[0][0],
                                               mix_list[1][0],
                                               mix_list[2][0],
                                               mix_list[3][0],
                                               mix_list[4][0],
                                               mix_list[5][0],
                                               mix_list[6][0],
                                               mix_list[7][0],
                                               mix_list[8][0],
                                               mix_list[9][0],
                                               mix_list[10][0],
                                               mix_list[11][0],


                                            ], # 算式列表(注意：算式中不能出现运算结果等于界限数字的算式，比如此题中算式结果不能等于5)
                "type": "au-equation-drag2" # 组件名
                }
                ],
                "answers": [
                    [
                        than_fif_list[0],
                    ],
                    [
                        less_fif_list[0],
                        less_fif_list[1],
                        less_fif_list[2],
                        less_fif_list[3],
                        less_fif_list[4],
                        less_fif_list[5],
                        less_fif_list[6],
                        less_fif_list[7],
                    ]
                ], # 答案集合项
                "knowledges": [
                    "按不同的标准分类"
                ], # 知识点
                "resource": "resource",
                "type": "操作", # 题型
                "explain": "explain",
                "level": "3", # 难度
                "number": "1-4-2-5" # 题型编号
                }
                ]

            if len(than_fif_list) == 2:
                questions = [
                    {
                        "body": [
                            {
                                "title": "分类",
                                "stem": "按要求分类。",
                                "num": "5",  # 拖入框的界限数字
                                "questionItem": [
                                    mix_list[0][0],
                                    mix_list[1][0],
                                    mix_list[2][0],
                                    mix_list[3][0],
                                    mix_list[4][0],
                                    mix_list[5][0],
                                    mix_list[6][0],
                                    mix_list[7][0],
                                    mix_list[8][0],
                                    mix_list[9][0],
                                    mix_list[10][0],
                                    mix_list[11][0],

                                ],  # 算式列表(注意：算式中不能出现运算结果等于界限数字的算式，比如此题中算式结果不能等于5)
                                "type": "au-equation-drag2"  # 组件名
                            }
                        ],
                        "answers": [
                            [
                                than_fif_list[0],
                                than_fif_list[1],
                            ],
                            [
                                less_fif_list[0],
                                less_fif_list[1],
                                less_fif_list[2],
                                less_fif_list[3],
                                less_fif_list[4],
                                less_fif_list[5],
                                less_fif_list[6],
                            ]
                        ],  # 答案集合项
                        "knowledges": [
                            "按不同的标准分类"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "操作",  # 题型
                        "explain": "explain",
                        "level": "3",  # 难度
                        "number": "1-4-2-5"  # 题型编号
                    }
                ]

            if len(than_fif_list) == 3:
                questions = [
                    {
                        "body": [
                            {
                                "title": "分类",
                                "stem": "按要求分类。",
                                "num": "5",  # 拖入框的界限数字
                                "questionItem": [
                                    mix_list[0][0],
                                    mix_list[1][0],
                                    mix_list[2][0],
                                    mix_list[3][0],
                                    mix_list[4][0],
                                    mix_list[5][0],
                                    mix_list[6][0],
                                    mix_list[7][0],
                                    mix_list[8][0],
                                    mix_list[9][0],
                                    mix_list[10][0],
                                    mix_list[11][0],

                                ],  # 算式列表(注意：算式中不能出现运算结果等于界限数字的算式，比如此题中算式结果不能等于5)
                                "type": "au-equation-drag2"  # 组件名
                            }
                        ],
                        "answers": [
                            [
                                than_fif_list[0],
                                than_fif_list[1],
                                than_fif_list[2],
                            ],
                            [
                                less_fif_list[0],
                                less_fif_list[1],
                                less_fif_list[2],
                                less_fif_list[3],
                                less_fif_list[4],
                                less_fif_list[5],

                            ]
                        ],  # 答案集合项
                        "knowledges": [
                            "按不同的标准分类"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "操作",  # 题型
                        "explain": "explain",
                        "level": "3",  # 难度
                        "number": "1-4-2-5"  # 题型编号
                    }
                ]

            if len(than_fif_list) == 4:
                questions = [
                    {
                        "body": [
                            {
                                "title": "分类",
                                "stem": "按要求分类。",
                                "num": "5",  # 拖入框的界限数字
                                "questionItem": [
                                    mix_list[0][0],
                                    mix_list[1][0],
                                    mix_list[2][0],
                                    mix_list[3][0],
                                    mix_list[4][0],
                                    mix_list[5][0],
                                    mix_list[6][0],
                                    mix_list[7][0],
                                    mix_list[8][0],
                                    mix_list[9][0],
                                    mix_list[10][0],
                                    mix_list[11][0],

                                ],  # 算式列表(注意：算式中不能出现运算结果等于界限数字的算式，比如此题中算式结果不能等于5)
                                "type": "au-equation-drag2"  # 组件名
                            }
                        ],
                        "answers": [
                            [
                                than_fif_list[0],
                                than_fif_list[1],
                                than_fif_list[2],
                                than_fif_list[3],
                            ],
                            [
                                less_fif_list[0],
                                less_fif_list[1],
                                less_fif_list[2],
                                less_fif_list[3],
                                less_fif_list[4],


                            ]
                        ],  # 答案集合项
                        "knowledges": [
                            "按不同的标准分类"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "操作",  # 题型
                        "explain": "explain",
                        "level": "3",  # 难度
                        "number": "1-4-2-5"  # 题型编号
                    }
                ]

            if len(than_fif_list) == 5:
                questions = [
                    {
                        "body": [
                            {
                                "title": "分类",
                                "stem": "按要求分类。",
                                "num": "5",  # 拖入框的界限数字
                                "questionItem": [
                                    mix_list[0][0],
                                    mix_list[1][0],
                                    mix_list[2][0],
                                    mix_list[3][0],
                                    mix_list[4][0],
                                    mix_list[5][0],
                                    mix_list[6][0],
                                    mix_list[7][0],
                                    mix_list[8][0],
                                    mix_list[9][0],
                                    mix_list[10][0],
                                    mix_list[11][0],

                                ],  # 算式列表(注意：算式中不能出现运算结果等于界限数字的算式，比如此题中算式结果不能等于5)
                                "type": "au-equation-drag2"  # 组件名
                            }
                        ],
                        "answers": [
                            [
                                than_fif_list[0],
                                than_fif_list[1],
                                than_fif_list[2],
                                than_fif_list[3],
                                than_fif_list[4],
                            ],
                            [
                                less_fif_list[0],
                                less_fif_list[1],
                                less_fif_list[2],
                                less_fif_list[3],

                            ]
                        ],  # 答案集合项
                        "knowledges": [
                            "按不同的标准分类"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "操作",  # 题型
                        "explain": "explain",
                        "level": "3",  # 难度
                        "number": "1-4-2-5"  # 题型编号
                    }
                ]

            if len(than_fif_list) == 6:
                questions = [
                    {
                        "body": [
                            {
                                "title": "分类",
                                "stem": "按要求分类。",
                                "num": "5",  # 拖入框的界限数字
                                "questionItem": [
                                    mix_list[0][0],
                                    mix_list[1][0],
                                    mix_list[2][0],
                                    mix_list[3][0],
                                    mix_list[4][0],
                                    mix_list[5][0],
                                    mix_list[6][0],
                                    mix_list[7][0],
                                    mix_list[8][0],
                                    mix_list[9][0],
                                    mix_list[10][0],
                                    mix_list[11][0],

                                ],  # 算式列表(注意：算式中不能出现运算结果等于界限数字的算式，比如此题中算式结果不能等于5)
                                "type": "au-equation-drag2"  # 组件名
                            }
                        ],
                        "answers": [
                            [
                                than_fif_list[0],
                                than_fif_list[1],
                                than_fif_list[2],
                                than_fif_list[3],
                                than_fif_list[4],
                                than_fif_list[5],
                            ],
                            [
                                less_fif_list[0],
                                less_fif_list[1],
                                less_fif_list[2],

                            ]
                        ],  # 答案集合项
                        "knowledges": [
                            "按不同的标准分类"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "操作",  # 题型
                        "explain": "explain",
                        "level": "3",  # 难度
                        "number": "1-4-2-5"  # 题型编号
                    }
                ]

            if len(than_fif_list) == 7:
                questions = [
                    {
                        "body": [
                            {
                                "title": "分类",
                                "stem": "按要求分类。",
                                "num": "5",  # 拖入框的界限数字
                                "questionItem": [
                                    mix_list[0][0],
                                    mix_list[1][0],
                                    mix_list[2][0],
                                    mix_list[3][0],
                                    mix_list[4][0],
                                    mix_list[5][0],
                                    mix_list[6][0],
                                    mix_list[7][0],
                                    mix_list[8][0],
                                    mix_list[9][0],
                                    mix_list[10][0],
                                    mix_list[11][0],

                                ],  # 算式列表(注意：算式中不能出现运算结果等于界限数字的算式，比如此题中算式结果不能等于5)
                                "type": "au-equation-drag2"  # 组件名
                            }
                        ],
                        "answers": [
                            [
                                than_fif_list[0],
                                than_fif_list[1],
                                than_fif_list[2],
                                than_fif_list[3],
                                than_fif_list[4],
                                than_fif_list[5],
                                than_fif_list[6],
                            ],
                            [
                                less_fif_list[0],
                                less_fif_list[1],


                            ]
                        ],  # 答案集合项
                        "knowledges": [
                            "按不同的标准分类"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "操作",  # 题型
                        "explain": "explain",
                        "level": "3",  # 难度
                        "number": "1-4-2-5"  # 题型编号
                    }
                ]

            if len(than_fif_list) == 8:
                questions = [
                    {
                        "body": [
                            {
                                "title": "分类",
                                "stem": "按要求分类。",
                                "num": "5",  # 拖入框的界限数字
                                "questionItem": [
                                    mix_list[0][0],
                                    mix_list[1][0],
                                    mix_list[2][0],
                                    mix_list[3][0],
                                    mix_list[4][0],
                                    mix_list[5][0],
                                    mix_list[6][0],
                                    mix_list[7][0],
                                    mix_list[8][0],
                                    mix_list[9][0],
                                    mix_list[10][0],
                                    mix_list[11][0],

                                ],  # 算式列表(注意：算式中不能出现运算结果等于界限数字的算式，比如此题中算式结果不能等于5)
                                "type": "au-equation-drag2"  # 组件名
                            }
                        ],
                        "answers": [
                            [
                                than_fif_list[0],
                                than_fif_list[1],
                                than_fif_list[2],
                                than_fif_list[3],
                                than_fif_list[4],
                                than_fif_list[5],
                                than_fif_list[6],
                                than_fif_list[7],
                            ],
                            [
                                less_fif_list[0],


                            ]
                        ],  # 答案集合项
                        "knowledges": [
                            "按不同的标准分类"
                        ],  # 知识点
                        "resource": "resource",
                        "type": "操作",  # 题型
                        "explain": "explain",
                        "level": "3",  # 难度
                        "number": "1-4-2-5"  # 题型编号
                    }
                ]

            all_questions.extend(questions)
        return all_questions

    #todo 1-4-2-6 把和左边同类的选出来
    def Inhomogeneity(self):
        all_questions=[]
        for i in range(18):
            swim_run_list=[]
            stationery_sportEquipment_list=[]
            shoes_skirt_list=[]
            mix_list=[]
            answer_list=[]
            images_fly_url,images_swim_url,images_run_url = q_CreatImgs.UpImages().FlyAndSwimAndRun()
            images_toy_url,images_stationery_url,images_clothing_url,images_sportEquipment_url = q_CreatImgs.UpImages().ToyAndStationeryEC()
            images_hat_url,images_surface_url,images_skirt_url,images_socks_url,images_shoes_url = q_CreatImgs.UpImages().Clothingclssify()
            swim_run_list.extend(random.sample(images_swim_url,2))
            swim_run_list.extend(random.sample(images_run_url,2))
            stationery_sportEquipment_list.extend(random.sample(images_stationery_url,2))
            stationery_sportEquipment_list.extend(random.sample(images_sportEquipment_url,2))
            shoes_skirt_list.extend(random.sample(images_shoes_url,2))
            shoes_skirt_list.extend(random.sample(images_skirt_url,2))
            random.shuffle(swim_run_list)
            swim_run_list.extend(random.sample(images_fly_url,1))
            random.shuffle(stationery_sportEquipment_list)
            stationery_sportEquipment_list.extend(random.sample(images_toy_url,1))
            random.shuffle(shoes_skirt_list)
            shoes_skirt_list.extend(random.sample(images_socks_url,1))
            for swim in range(4):
                if swim==0:
                    answer_list.append(swim_run_list[swim][1])
                    answer_list.append(stationery_sportEquipment_list[swim][1])
                    answer_list.append(shoes_skirt_list[swim][1])
                if swim_run_list[swim][1] in answer_list and swim>0:
                    answer_list.insert(3,[swim_run_list[swim][1],swim])
                if stationery_sportEquipment_list[swim][1] in answer_list and swim>0:
                    answer_list.insert(4,[stationery_sportEquipment_list[swim][1],swim])
                if shoes_skirt_list[swim][1] in answer_list and swim>0:
                    answer_list.insert(5,[shoes_skirt_list[swim][1],swim])




            print("swim_run_list",swim_run_list)
            print("stationery_sportEquipment_list",stationery_sportEquipment_list)
            print("shoes_skirt_list",shoes_skirt_list)
            print("answer_list",answer_list)
            questions=[
                {
                    "body": [
                        {
                            "title": "分类选择",
                            "stem": "把和左边同类的选出来。",
                            "selectType": "1", # 选择类型：1代表选与左边相同类型（1 - 2 - 2 - 06 组件）， 2代表所有项选不同（1 - 2 - 2 - 07 组件）
            "content": [ # 此数组里放置三组图片，每组皆为单选
            [
                {
                    "type": swim_run_list[0][1], # 图片类型      可随意定义
            "src": swim_run_list[0][0]
            },
            {
                "type": swim_run_list[1][1], # 图片类型      可随意定义
            "src": swim_run_list[1][0]
            },
            {
                "type": swim_run_list[2][1], # 图片类型      可随意定义
            "src": swim_run_list[2][0]
            },
            {
                "type": swim_run_list[3][1],  # 图片类型      可随意定义
                "src": swim_run_list[3][0]
            },
            {
                "type": swim_run_list[4][1],  # 图片类型      可随意定义
                "src": swim_run_list[4][0]
            }
            ], # 第一组， 当selectType值为1时，为选同题型：代表同组后面四个图片只能有一个与它同类型
                                             # 当selectType值为2时，为选不同题型：代表全组五个图片有一类图片只有一项
       [
           {
               "type": stationery_sportEquipment_list[0][1],
               "src": stationery_sportEquipment_list[0][0]
           },
           {
               "type": stationery_sportEquipment_list[1][1],
               "src": stationery_sportEquipment_list[1][0]
           },
           {
               "type": stationery_sportEquipment_list[2][1],
               "src": stationery_sportEquipment_list[2][0]
           },
           {
               "type": stationery_sportEquipment_list[3][1],
               "src": stationery_sportEquipment_list[3][0]
           },
           {
               "type": stationery_sportEquipment_list[4][1],
               "src": stationery_sportEquipment_list[4][0]
           }
       ], # 第二组
             [
                 {
                     "type": shoes_skirt_list[0][1],
                     "src": shoes_skirt_list[0][0]
                 },
                 {
                     "type": shoes_skirt_list[1][1],
                     "src": shoes_skirt_list[1][0]
                 },
                 {
                      "type": shoes_skirt_list[2][1],
                     "src": shoes_skirt_list[2][0]
                 },
                 {
                     "type": shoes_skirt_list[3][1],
                     "src": shoes_skirt_list[3][0]
                 },
                 {
                     "type": shoes_skirt_list[4][1],
                     "src": shoes_skirt_list[4][0]
                 }
             ] # 第三组
            ],
            "type": "au-classify-similar" # 组件名
            }
            ],
            "answers": [
                answer_list[3][1],
                answer_list[4][1],
                answer_list[5][1],

            ], # 正确答案，每组正确位置的下标
            "knowledges": [
                "按不同的标准分类"
            ], # 知识点
            "resource": "resource",
            "type": "操作",
            "explain": "explain",
            "level": "2", # 难度
            "number": "1-4-2-6" # 题型编号  selectType值为2时对应1 - 4 - 2 - 07
            }
            ]
            all_questions.extend(questions)

        return all_questions


    #todo 1-4-2-7 选不同类
    def InhomogeneitySelectT(self):
        all_questions=[]
        for i in range(18):
            swim_run_list=[]
            stationery_sportEquipment_list=[]
            shoes_skirt_list=[]
            all_swim_run_list=[]
            all_stationery_sportEquipment_list=[]
            all_shoes_skirt_list=[]
            mix_list=[]
            answer_list=[]
            images_fly_url,images_swim_url,images_run_url = q_CreatImgs.UpImages().FlyAndSwimAndRun()
            images_toy_url,images_stationery_url,images_clothing_url,images_sportEquipment_url = q_CreatImgs.UpImages().ToyAndStationeryEC()
            images_hat_url,images_surface_url,images_skirt_url,images_socks_url,images_shoes_url = q_CreatImgs.UpImages().Clothingclssify()
            all_swim_run_list.extend(images_fly_url)
            all_swim_run_list.extend(images_swim_url)
            # all_swim_run_list.extend(images_run_url)

            fsr=random.sample(all_swim_run_list,1)
            print("fsr",fsr)
            if fsr[0][1]=="fly":
                swim_run_list.extend(fsr)
                swim_run_list.extend(random.sample(images_swim_url,4))
            if fsr[0][1]=="swim":
                swim_run_list.extend(fsr)
                swim_run_list.extend(random.sample(images_run_url,4))
            # if fsr[0][1]=="run":
            #     swim_run_list.extend(fsr)
            #     swim_run_list.extend(random.sample(images_fly_url,4))

            all_stationery_sportEquipment_list.extend(images_stationery_url)
            all_stationery_sportEquipment_list.extend(images_clothing_url)
            all_stationery_sportEquipment_list.extend(images_sportEquipment_url)
            scs=random.sample(all_stationery_sportEquipment_list,1)
            stationery_sportEquipment_list.extend(scs)
            print("scs",scs)
            if scs[0][1]=="stationery":

                stationery_sportEquipment_list.extend(random.sample(images_clothing_url,4))
            if scs[0][1]=="clothing":

                stationery_sportEquipment_list.extend(random.sample(images_sportEquipment_url,4))
            if scs[0][1]=="sportEquipment":

                stationery_sportEquipment_list.extend(random.sample(images_stationery_url,4))

            all_shoes_skirt_list.extend(images_hat_url)
            all_shoes_skirt_list.extend(images_surface_url)
            all_shoes_skirt_list.extend(images_skirt_url)
            shs = random.sample(all_shoes_skirt_list, 1)
            shoes_skirt_list.extend(shs)
            print("shs",shs)

            if shs[0][1] == "hat":

                shoes_skirt_list.extend(random.sample(images_surface_url, 4))
            if shs[0][1] == "surface":

                shoes_skirt_list.extend(random.sample(images_skirt_url, 4))
            if shs[0][1] == "skirt":

                shoes_skirt_list.extend(random.sample(images_hat_url, 4))

            random.shuffle(swim_run_list)
            random.shuffle(stationery_sportEquipment_list)
            random.shuffle(shoes_skirt_list)
            print("swim_run_list",swim_run_list)
            print("stationery_sportEquipment_list",stationery_sportEquipment_list)
            print("shoes_skirt_list",shoes_skirt_list)


            first_swim=swim_run_list[0][1]
            for swim in range(1,4):
                if swim_run_list[swim][1]!=first_swim and swim_run_list[swim+1][1]!=first_swim:
                    answer_list.extend([first_swim,0])
                    break
                elif swim_run_list[swim][1]!=first_swim and swim_run_list[swim+1][1]==first_swim:
                    answer_list.extend([swim_run_list[swim][1],swim])
                    break
                elif swim_run_list[swim][1]==first_swim and swim_run_list[swim+1][1]!=first_swim:
                    answer_list.extend([swim_run_list[swim+1][1], swim+1])
                    break



            first_stationery = stationery_sportEquipment_list[0][1]
            for stationery in range(1, 4):
                if stationery_sportEquipment_list[stationery][1] != first_stationery and stationery_sportEquipment_list[stationery + 1][1] != first_stationery:
                    answer_list.extend([first_stationery, 0])
                    break
                elif stationery_sportEquipment_list[stationery][1] != first_stationery and stationery_sportEquipment_list[stationery + 1][1] == first_stationery:
                    answer_list.extend([stationery_sportEquipment_list[stationery][1], stationery])
                    break
                elif stationery_sportEquipment_list[stationery][1] == first_stationery and stationery_sportEquipment_list[stationery + 1][1] != first_stationery:
                    answer_list.extend([stationery_sportEquipment_list[stationery + 1][1], stationery + 1])
                    break

            first_shoes = shoes_skirt_list[0][1]

            for shoes in range(1, 4):

                if shoes_skirt_list[shoes][1] != first_shoes and \
                        shoes_skirt_list[shoes + 1][1] != first_shoes:
                    answer_list.extend([first_shoes, 0])
                    break
                elif shoes_skirt_list[shoes][1] != first_shoes and \
                        shoes_skirt_list[shoes + 1][1] == first_shoes:
                    answer_list.extend([shoes_skirt_list[shoes][1], shoes])
                    break
                elif shoes_skirt_list[shoes][1] == first_shoes and \
                        shoes_skirt_list[shoes + 1][1] != first_shoes:

                    answer_list.extend([shoes_skirt_list[shoes + 1][1], shoes + 1])
                    break

            print("answer_list", answer_list)



            questions=[
                {
                    "body": [
                        {
                            "title": "分类选择",
                            "stem": "选择一个和其他不是同类的。",
                            "selectType": "2", # 选择类型：1代表选与左边相同类型（1 - 2 - 2 - 06 组件）， 2代表所有项选不同（1 - 2 - 2 - 07 组件）
            "content": [ # 此数组里放置三组图片，每组皆为单选
            [
                {
                    "type": swim_run_list[0][1], # 图片类型      可随意定义
            "src": swim_run_list[0][0]
            },
            {
                "type": swim_run_list[1][1], # 图片类型      可随意定义
            "src": swim_run_list[1][0]
            },
            {
                "type": swim_run_list[2][1], # 图片类型      可随意定义
            "src": swim_run_list[2][0]
            },
            {
                "type": swim_run_list[3][1],  # 图片类型      可随意定义
                "src": swim_run_list[3][0]
            },
            {
                "type": swim_run_list[4][1],  # 图片类型      可随意定义
                "src": swim_run_list[4][0]
            }
            ], # 第一组， 当selectType值为1时，为选同题型：代表同组后面四个图片只能有一个与它同类型
                                             # 当selectType值为2时，为选不同题型：代表全组五个图片有一类图片只有一项
       [
           {
               "type": stationery_sportEquipment_list[0][1],
               "src": stationery_sportEquipment_list[0][0]
           },
           {
               "type": stationery_sportEquipment_list[1][1],
               "src": stationery_sportEquipment_list[1][0]
           },
           {
               "type": stationery_sportEquipment_list[2][1],
               "src": stationery_sportEquipment_list[2][0]
           },
           {
               "type": stationery_sportEquipment_list[3][1],
               "src": stationery_sportEquipment_list[3][0]
           },
           {
               "type": stationery_sportEquipment_list[4][1],
               "src": stationery_sportEquipment_list[4][0]
           }
       ], # 第二组
             [
                 {
                     "type": shoes_skirt_list[0][1],
                     "src": shoes_skirt_list[0][0]
                 },
                 {
                     "type": shoes_skirt_list[1][1],
                     "src": shoes_skirt_list[1][0]
                 },
                 {
                      "type": shoes_skirt_list[2][1],
                     "src": shoes_skirt_list[2][0]
                 },
                 {
                     "type": shoes_skirt_list[3][1],
                     "src": shoes_skirt_list[3][0]
                 },
                 {
                     "type": shoes_skirt_list[4][1],
                     "src": shoes_skirt_list[4][0]
                 }
             ] # 第三组
            ],
            "type": "au-classify-similar" # 组件名
            }
            ],
            "answers": [
                answer_list[1],
                answer_list[3],
                answer_list[5],


            ], # 正确答案，每组正确位置的下标
            "knowledges": [
                "按不同的标准分类"
            ], # 知识点
            "resource": "resource",
            "type": "操作",
            "explain": "explain",
            "level": "2", # 难度
            "number": "1-4-2-6" # 题型编号  selectType值为2时对应1 - 4 - 2 - 07
            }
            ]
            all_questions.extend(questions)

        return all_questions

    # todo 1-4-2-7 选不同类
    def InhomogeneitySelect(self):
        all_questions = []
        for i in range(18):
            swim_run_list = []
            stationery_sportEquipment_list = []
            shoes_skirt_list = []
            all_swim_run_list = []
            all_stationery_sportEquipment_list = []
            all_shoes_skirt_list = []
            mix_list = []
            answer_list = []
            images_fly_url, images_swim_url, images_run_url = q_CreatImgs.UpImages().FlyAndSwimAndRun()
            images_toy_url, images_stationery_url, images_clothing_url, images_sportEquipment_url = q_CreatImgs.UpImages().ToyAndStationeryEC()
            images_hat_url, images_surface_url, images_skirt_url, images_socks_url, images_shoes_url = q_CreatImgs.UpImages().Clothingclssify()
            all_swim_run_list.extend(images_fly_url)
            all_swim_run_list.extend(images_swim_url)
            # all_swim_run_list.extend(images_run_url)

            fsr = random.sample(all_swim_run_list, 1)
            print("fsr", fsr)
            if fsr[0][1] == "fly":
                swim_run_list.extend(fsr)
                swim_run_list.extend(random.sample(images_swim_url, 4))
            if fsr[0][1] == "swim":
                swim_run_list.extend(fsr)
                swim_run_list.extend(random.sample(images_run_url, 4))
            # if fsr[0][1]=="run":
            #     swim_run_list.extend(fsr)
            #     swim_run_list.extend(random.sample(images_fly_url,4))

            all_stationery_sportEquipment_list.extend(images_stationery_url)
            # all_stationery_sportEquipment_list.extend(images_clothing_url)
            all_stationery_sportEquipment_list.extend(images_sportEquipment_url)
            scs = random.sample(all_stationery_sportEquipment_list, 1)
            stationery_sportEquipment_list.extend(scs)
            print("scs", scs)
            if scs[0][1] == "stationery":
                stationery_sportEquipment_list.extend(random.sample(images_sportEquipment_url, 4))
            # if scs[0][1] == "clothing":
            #     stationery_sportEquipment_list.extend(random.sample(images_sportEquipment_url, 4))
            if scs[0][1] == "sportEquipment":
                stationery_sportEquipment_list.extend(random.sample(images_stationery_url, 4))

            all_shoes_skirt_list.extend(images_hat_url)
            all_shoes_skirt_list.extend(images_surface_url)
            all_shoes_skirt_list.extend(images_skirt_url)
            shs = random.sample(all_shoes_skirt_list, 1)
            shoes_skirt_list.extend(shs)
            print("shs", shs)

            if shs[0][1] == "hat":
                shoes_skirt_list.extend(random.sample(images_surface_url, 4))
            if shs[0][1] == "surface":
                shoes_skirt_list.extend(random.sample(images_skirt_url, 4))
            if shs[0][1] == "skirt":
                shoes_skirt_list.extend(random.sample(images_hat_url, 4))

            random.shuffle(swim_run_list)
            random.shuffle(stationery_sportEquipment_list)
            random.shuffle(shoes_skirt_list)
            print("swim_run_list", swim_run_list)
            print("stationery_sportEquipment_list", stationery_sportEquipment_list)
            print("shoes_skirt_list", shoes_skirt_list)

            first_swim = swim_run_list[0][1]
            for swim in range(1, 4):
                if swim_run_list[swim][1] != first_swim and swim_run_list[swim + 1][1] != first_swim:
                    answer_list.extend([first_swim, 0])
                    break
                elif swim_run_list[swim][1] != first_swim and swim_run_list[swim + 1][1] == first_swim:
                    answer_list.extend([swim_run_list[swim][1], swim])
                    break
                elif swim_run_list[swim][1] == first_swim and swim_run_list[swim + 1][1] != first_swim:
                    answer_list.extend([swim_run_list[swim + 1][1], swim + 1])
                    break

            first_stationery = stationery_sportEquipment_list[0][1]
            for stationery in range(1, 4):
                if stationery_sportEquipment_list[stationery][1] != first_stationery and \
                        stationery_sportEquipment_list[stationery + 1][1] != first_stationery:
                    answer_list.extend([first_stationery, 0])
                    break
                elif stationery_sportEquipment_list[stationery][1] != first_stationery and \
                        stationery_sportEquipment_list[stationery + 1][1] == first_stationery:
                    answer_list.extend([stationery_sportEquipment_list[stationery][1], stationery])
                    break
                elif stationery_sportEquipment_list[stationery][1] == first_stationery and \
                        stationery_sportEquipment_list[stationery + 1][1] != first_stationery:
                    answer_list.extend([stationery_sportEquipment_list[stationery + 1][1], stationery + 1])
                    break

            first_shoes = shoes_skirt_list[0][1]

            for shoes in range(1, 4):

                if shoes_skirt_list[shoes][1] != first_shoes and \
                        shoes_skirt_list[shoes + 1][1] != first_shoes:
                    answer_list.extend([first_shoes, 0])
                    break
                elif shoes_skirt_list[shoes][1] != first_shoes and \
                        shoes_skirt_list[shoes + 1][1] == first_shoes:
                    answer_list.extend([shoes_skirt_list[shoes][1], shoes])
                    break
                elif shoes_skirt_list[shoes][1] == first_shoes and \
                        shoes_skirt_list[shoes + 1][1] != first_shoes:

                    answer_list.extend([shoes_skirt_list[shoes + 1][1], shoes + 1])
                    break

            print("answer_list", answer_list)

            questions = [
                {
                    "body": [
                        {
                            "title": "分类选择",
                            "stem": "选择一个和其他不是同类的。",
                            "selectType": "2",  # 选择类型：1代表选与左边相同类型（1 - 2 - 2 - 06 组件）， 2代表所有项选不同（1 - 2 - 2 - 07 组件）
                            "content": [  # 此数组里放置三组图片，每组皆为单选
                                [
                                    {
                                        "type": swim_run_list[0][1],  # 图片类型      可随意定义
                                        "src": swim_run_list[0][0]
                                    },
                                    {
                                        "type": swim_run_list[1][1],  # 图片类型      可随意定义
                                        "src": swim_run_list[1][0]
                                    },
                                    {
                                        "type": swim_run_list[2][1],  # 图片类型      可随意定义
                                        "src": swim_run_list[2][0]
                                    },
                                    {
                                        "type": swim_run_list[3][1],  # 图片类型      可随意定义
                                        "src": swim_run_list[3][0]
                                    },
                                    {
                                        "type": swim_run_list[4][1],  # 图片类型      可随意定义
                                        "src": swim_run_list[4][0]
                                    }
                                ],  # 第一组， 当selectType值为1时，为选同题型：代表同组后面四个图片只能有一个与它同类型
                                # 当selectType值为2时，为选不同题型：代表全组五个图片有一类图片只有一项
                                [
                                    {
                                        "type": stationery_sportEquipment_list[0][1],
                                        "src": stationery_sportEquipment_list[0][0]
                                    },
                                    {
                                        "type": stationery_sportEquipment_list[1][1],
                                        "src": stationery_sportEquipment_list[1][0]
                                    },
                                    {
                                        "type": stationery_sportEquipment_list[2][1],
                                        "src": stationery_sportEquipment_list[2][0]
                                    },
                                    {
                                        "type": stationery_sportEquipment_list[3][1],
                                        "src": stationery_sportEquipment_list[3][0]
                                    },
                                    {
                                        "type": stationery_sportEquipment_list[4][1],
                                        "src": stationery_sportEquipment_list[4][0]
                                    }
                                ],  # 第二组
                                [
                                    {
                                        "type": shoes_skirt_list[0][1],
                                        "src": shoes_skirt_list[0][0]
                                    },
                                    {
                                        "type": shoes_skirt_list[1][1],
                                        "src": shoes_skirt_list[1][0]
                                    },
                                    {
                                        "type": shoes_skirt_list[2][1],
                                        "src": shoes_skirt_list[2][0]
                                    },
                                    {
                                        "type": shoes_skirt_list[3][1],
                                        "src": shoes_skirt_list[3][0]
                                    },
                                    {
                                        "type": shoes_skirt_list[4][1],
                                        "src": shoes_skirt_list[4][0]
                                    }
                                ]  # 第三组
                            ],
                            "type": "au-classify-similar"  # 组件名
                        }
                    ],
                    "answers": [
                        answer_list[1],
                        answer_list[3],
                        answer_list[5],

                    ],  # 正确答案，每组正确位置的下标
                    "knowledges": [
                        "按不同的标准分类"
                    ],  # 知识点
                    "resource": "resource",
                    "type": "操作",
                    "explain": "explain",
                    "level": "2",  # 难度
                    "number": "1-4-2-6"  # 题型编号  selectType值为2时对应1 - 4 - 2 - 07
                }
            ]
            all_questions.extend(questions)

        return all_questions



# 完成第四单元18个题的生成工作：
# 【编号】1-4-1-01  把动物选出来
# 选一选，给会飞的动物涂上颜色
# 选一选，给会飞的动物涂上颜色
# 1-4-1-04 在蔬菜下面输入“0”，在水果下面输入“1”
# 天上飞的输入“0”，水里游的输入“1”，地上跑的输入“2”
# 拖一拖﹐把下面生活用品分为三类
# 1-4-1-07 拖一拖﹐把下面生活用品分为三类
# 1-4-1-08 算一算，将得数相同的算式拖入到相同的框里
# 1-4-1-10 把会飞的动物选出来，再填一填
# 1-4-1-09 把学习文具选出来﹐再填—填
# 1-4-1-11 分一分﹐填―填
# 1-4-2-3 拖一拖﹐把下面生活用品分为三类
# 1-4-2-1 选择同类﹐涂上相同的颜色
# 1-4-2-2 选择同类﹐涂上相同的颜色
# 1-4-2-4  按形状分类
# 1-4-2-5   按算式结果分类
# 1-4-2-6 把和左边同类的选出来
# 1-4-2-7 选不同类

if __name__ == '__main__':
    cal=CalculNum()
    # cal.NumAdd1()
    # cal.AnimalSelect()
    # content=cal.ImageClass()
    # question=cal.AnimalColoring()
    # question=cal.FruitVegetableSelect()
    # question=cal.FlyAndSwimAndRunSelect()
    # question=cal.ToyAndStationerySelect()
    # question=cal.EquationClassifySelect()
    # question=cal.FlyAnimalSelect()
    # question=cal.TransportSelect()
    # question=cal.ClothingclssifySelect()
    # question=cal.ClassifyTintageSelect()
    # question=cal.ClassifyTintageSelect2()
    # question=cal.CalculationResultSelect()
    # question=cal.Inhomogeneity()
    # question=cal.InhomogeneitySelect()
    question=cal.ClassifyShape()
    # print(question)