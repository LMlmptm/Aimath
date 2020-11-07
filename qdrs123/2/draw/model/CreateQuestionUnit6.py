from draw import q_CreatImgs
import random


class SoildQuestions(object):
    def __init__(self):
        self.count = 0

    # todo 1-6-1-01 这是什么形状？
    def ShapeSelect(self):
        all_questions = []
        for i in range(10):
            mix_list = []
            answer_sequence_list = []
            question_type_list = []
            question_image_addr_list = []
            answer_shuffle_index_list = []
            images_cube_url, images_solid_url = q_CreatImgs.UpImages().CubeDiscern()
            mix_list.extend(random.sample(images_cube_url, 2))
            answer_sequence_list.append(mix_list[0][2])
            question_type_list.append(mix_list[0][1])
            question_image_addr_list.append(mix_list[0][0])
            print("answer_sequence_list", answer_sequence_list)
            print("question_type_list", question_type_list)
            print("question_image_addr_list", question_image_addr_list)
            random.shuffle(mix_list)
            for m in mix_list:
                if m[2] == answer_sequence_list[0]:
                    answer_shuffle_index_list.append(mix_list.index(m))
            print("answer_shuffle_index_list", answer_shuffle_index_list)

            questions = [
                {
                    "body": [
                        {
                            "type": "know-cube-select",
                            "title": "这是什么形状？",
                            "imgSrc": question_image_addr_list[0],  # 顶部图片资源
                            "list": [  # 列表文字选项
                                {
                                    "desc": mix_list[0][2]
                                },
                                {
                                    "desc": "长方体"
                                }
                            ]
                        }
                    ],
                    "answers": [answer_shuffle_index_list[0]],
                    "resource": "resource",
                    "explain": "explain",
                    "knowledges": [
                        "认识" + str(answer_sequence_list[0])
                    ],
                    "level": "1",
                    "type": "选择",
                    "number": "1-6-1-01"
                }
            ]
            print(questions)
            all_questions.extend(questions)
        return all_questions

    # todo 1-6-1-02 选一选,正方体是那个形状?
    def CubeShapeSelect(self):
        all_questions = []
        dup_questions=[]
        for i in range(6):
            mix_list = []
            answer_index_list = []
            images_cube_url, other_solid_url = q_CreatImgs.UpImages().CubeShape()
            mix_list.extend(random.sample(images_cube_url, 1))
            mix_list.extend(random.sample(other_solid_url, 1))
            random.shuffle(mix_list)
            for m in mix_list:
                if m[1] == "cube":
                    answer_index_list.append(mix_list.index(m))
            print("mix_list", mix_list)
            print("answer_index_list", answer_index_list)
            questions = [
                {
                    "body": [
                        {
                            "type": "know-cube-select",
                            "imgSrc": "",
                            "title": "选一选，正方体是那个形状？",
                            "list": [  # 列表图片选项
                                {
                                    "src": mix_list[0][0]
                                },
                                {
                                    "src": mix_list[1][0]
                                }
                            ]
                        }
                    ],
                    "answers": answer_index_list,
                    "resource": "resource",
                    "explain": "explain",
                    "knowledges": [
                        "认识正方体"
                    ],
                    "level": "1",
                    "type": "选择",
                    "number": "1-6-1-02"
                }
            ]
            print("questions", questions)
            dup_questions.extend(questions)
        for dup in dup_questions:
            if dup not in all_questions:
                all_questions.append(dup)
        return all_questions

    # todo 1-6-1-03 想一想，拖一拖。正方体下面拖入o 不是的下面拖入√
    def RightAndWrong(self):
        all_questions = []
        for i in range(18):
            mix_list = []
            answer_replace_list = []
            images_cube_url, other_solid_url = q_CreatImgs.UpImages().CubeShape()
            mix_list.extend(random.sample(images_cube_url, 1))
            mix_list.extend(random.sample(other_solid_url, 3))
            random.shuffle(mix_list)
            for m in mix_list:
                if m[1] == "cube":
                    answer_replace_list.append(2)
                else:
                    answer_replace_list.append(1)
            print("mix_list", mix_list)
            print("answer_replace_list", answer_replace_list)
            questions = [
                {
                    "body": [
                        {
                            "type": "know-cube-drag",
                            "title": "拖一拖",
                            "titleList": [  # 头部文字描述列表
                                {
                                    "type": "text",  # 文本类型
                                    "value": "想一想，拖一拖。正方体下面拖入"
                                },
                                {
                                    "type": "image",  # 符号类型
                                    "src": "/v2/通用/对错符号/圈.svg",
                                    "value": '圆圈'
                                },
                                {
                                    "type": "text",
                                    "value": "，不是的下面拖入"
                                },
                                {
                                    "type": "image",
                                    "src": "/v2/通用/对错符号/对号.svg",
                                    "value": '对号'
                                },
                                {
                                    "type": "text",
                                    "value": "。"
                                }
                            ],
                            "content": [  # 内容列表
                                {
                                    "src": mix_list[0][0],
                                    "val": ""
                                },
                                {
                                    "src": mix_list[1][0],
                                    "val": ""
                                },
                                {
                                    "src": mix_list[2][0],
                                    "val": ""
                                },
                                {
                                    "src": mix_list[3][0],
                                    "val": ""
                                }
                            ],
                            "options": [  # 符号列表
                                {
                                    "type": "1",  # 用于返回答案，
                                    "src": "/v2/通用/对错符号/对号.svg"
                                },
                                {
                                    "type": "2",  # 用于返回答案，
                                    "src": "/v2/通用/对错符号/圈.svg"
                                }
                            ],
                            "type": "know-cube-drag"
                        }
                    ],
                    "answers": answer_replace_list,  # 根据option里的type类型，没有对应为  '',
                    "knowledges": [
                        "认识正方体"
                    ],
                    "resource": "resource",
                    "type": "选择",
                    "explain": "explain",
                    "level": "2",
                    "number": "1-6-1-03",
                }
            ]
            print("questions", questions)
            all_questions.extend(questions)
        return all_questions

    # todo 1-6-2-01 这是什么形状？
    def CuboidSelect(self):
        all_questions = []
        for i in range(10):
            mix_list = []
            answer_index_list = []
            all_solid_list, images_cuboid_url = q_CreatImgs.UpImages().ChinaDescriptionSolid()
            mix_list.extend(random.sample(images_cuboid_url, 1))
            random.shuffle(all_solid_list)
            for a in all_solid_list:
                if a == "长方体":
                    answer_index_list.append(all_solid_list.index(a))
            print("all_solid_list", all_solid_list)
            print("answer_index_list", answer_index_list)
            questions = [
                {
                    "body": [
                        {
                            "type": "know-cube-select",
                            "imgSrc": mix_list[0][0],
                            "title": "这是什么形状？",
                            "list": [  # 选项列表
                                {
                                    "desc": all_solid_list[0]
                                },
                                {
                                    "desc": all_solid_list[1]
                                },
                                {
                                    "desc": all_solid_list[2]
                                },
                                {
                                    "desc": all_solid_list[3]
                                }
                            ]
                        }
                    ],
                    "answers": answer_index_list,
                    "resource": "resource",
                    "explain": "explain",
                    "knowledges": [
                        "认识长方体"
                    ],
                    "level": "1",
                    "type": "选择",
                    "number": "1-6-2-01"
                }
            ]
            print("questions", questions)
            all_questions.extend(questions)
        return all_questions

    # todo 1-6-2-02 那个物品放错地方了，请把它选出来
    def LifeSolidSelect(self):
        all_questions = []
        for i in range(16):
            mix_list = []
            answer_list = []
            life_cube_url, life_cuboid_url, life_globe_url, life_cylinder_url = q_CreatImgs.UpImages().LifeSolid()
            mix_list.extend(random.sample(life_cube_url, 3))
            mix_list.extend(random.sample(life_cuboid_url, 1))
            random.shuffle(mix_list)
            for m in mix_list:
                if m[1] == "cuboid":
                    answer_list.append(mix_list.index(m))
            print("mix_list", mix_list)
            print("answer_list", answer_list)
            questions = [
                {
                    "body": [
                        {
                            "type": "know-cube-select",
                            "imgSrc": "",
                            "title": "那个物品放错地方了，请把它选出来。",
                            "list": [
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
                                }
                            ]
                        }
                    ],
                    "answers": answer_list,
                    "resource": "resource",
                    "explain": "explain",
                    "knowledges": [
                        "认识长方体"
                    ],
                    "level": "1",
                    "type": "选择",
                    "number": "1-6-2-02"
                }
            ]
            print("questions", questions)
            all_questions.extend(questions)
        return all_questions

    # todo 1-6-2-03 那个物品放错地方了，请把它选出来
    def LifeSolid2Select(self):
        all_questions = []
        for i in range(16):
            mix_list = []
            answer_list = []
            life_cube_url, life_cuboid_url, life_globe_url, life_cylinder_url = q_CreatImgs.UpImages().LifeSolid()
            mix_list.extend(random.sample(life_globe_url, 3))
            mix_list.extend(random.sample(life_cuboid_url, 1))
            random.shuffle(mix_list)
            for m in mix_list:
                if m[1] == "cuboid":
                    answer_list.append(mix_list.index(m))
            print("mix_list", mix_list)
            print("answer_list", answer_list)
            questions = [
                {
                    "body": [
                        {
                            "type": "know-cube-select",
                            "imgSrc": "",
                            "title": "那个物品放错地方了，请把它选出来。",
                            "list": [
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
                                }
                            ]
                        }
                    ],
                    "answers": answer_list,
                    "resource": "resource",
                    "explain": "explain",
                    "knowledges": [
                        "认识长方体"
                    ],
                    "level": "1",
                    "type": "选择",
                    "number": "1-6-2-02"
                }
            ]
            print("questions", questions)
            all_questions.extend(questions)

        return all_questions

    # todo 1-6-2-04 想一想，拖一拖。长方体下面拖入o 不是的下面拖入√
    def RightAndWrongSelect(self):
        all_questions = []
        for i in range(18):
            mix_list = []
            answer_replace_list = []
            images_cube_url, other_solid_url = q_CreatImgs.UpImages().CuboidShape()
            mix_list.extend(random.sample(images_cube_url, 1))
            mix_list.extend(random.sample(other_solid_url, 3))
            random.shuffle(mix_list)
            for m in mix_list:
                if m[1] == "cuboid":
                    answer_replace_list.append(2)
                else:
                    answer_replace_list.append(1)
            print("mix_list", mix_list)
            print("answer_replace_list", answer_replace_list)
            questions = [
                {
                    "body": [
                        {
                            "title": "拖一拖",
                            "titleList": [  # 头部文字描述列表
                                {
                                    "type": "text",  # 文本类型
                                    "value": "想一想，拖一拖。长方体下面拖入 "
                                },
                                {
                                    "type": "image",  # 符号类型
                                    "src": "/v2/通用/对错符号/圈.svg",
                                    "value": '圆圈'
                                },
                                {
                                    "type": "text",
                                    "value": "，不是的下面拖入 "
                                },
                                {
                                    "type": "image",
                                    "src": "/v2/通用/对错符号/对号.svg",
                                    "value": '对号'
                                },
                                {
                                    "type": "text",
                                    "value": "。"
                                }
                            ],
                            "content": [  # 内容列表
                                {
                                    "src": mix_list[0][0],
                                    "val": ""
                                },
                                {
                                    "src": mix_list[1][0],
                                    "val": ""
                                },
                                {
                                    "src": mix_list[2][0],
                                    "val": ""
                                },
                                {
                                    "src": mix_list[3][0],
                                    "val": ""
                                }
                            ],
                            "options": [  # 符号列表
                                {
                                    "type": "1",  # 用于返回答案，
                                    "src": "/v2/通用/对错符号/对号.svg"
                                },
                                {
                                    "type": "2",  # 用于返回答案，
                                    "src": "/v2/通用/对错符号/圈.svg"
                                }
                            ],
                            "type": "know-cube-drag"
                        }
                    ],
                    "answers": answer_replace_list,  # 根据option里的type类型，没有对应为  '',
                    "knowledges": [
                        "认识长方体"
                    ],
                    "resource": "resource",
                    "type": "选择",
                    "explain": "explain",
                    "level": "2",
                    "number": "1-6-1-03",
                }
            ]
            print("questions", questions)
            all_questions.extend(questions)
        return all_questions

    # todo 1-6-3-01 这是什么形状？
    def CylinderSelect(self):
        all_questions = []
        for i in range(8):
            mix_list = []
            answer_list = []
            all_solid_list, images_cylinder_url = q_CreatImgs.UpImages().CylinderShape()
            mix_list.extend(random.sample(images_cylinder_url, 1))
            random.shuffle(all_solid_list)
            for s in all_solid_list:
                if s == "圆柱体":
                    answer_list.append(all_solid_list.index(s))
            print("all_solid_list", all_solid_list)
            print("answer_list", answer_list)
            questions = [
                {
                    "body": [
                        {
                            "type": "know-cube-select",
                            "imgSrc": mix_list[0][0],
                            "title": "这是什么形状？",
                            "list": [  # 选项列表
                                {
                                    "desc": all_solid_list[0]
                                },
                                {
                                    "desc": all_solid_list[1]
                                },
                                {
                                    "desc": all_solid_list[2]
                                },
                                {
                                    "desc": all_solid_list[3]
                                }
                            ]
                        }
                    ],
                    "answers": answer_list,
                    "resource": "resource",
                    "explain": "explain",
                    "knowledges": [
                        "认识圆柱体"
                    ],
                    "level": "1",
                    "type": "选择",
                    "number": "1-6-3-01"
                }
            ]
            print("questions", questions)
            all_questions.extend(questions)
        return all_questions

    # todo 1-6-3-02 选一选，圆柱体是那个形状？
    def CylinderShapeSelect(self):
        all_questions = []
        for i in range(6):
            mix_list = []
            answer_index_list = []
            all_solid_list, images_cylinder_url = q_CreatImgs.UpImages().CylinderShapeDiscern()
            mix_list.extend(random.sample(all_solid_list, 1))
            mix_list.extend(random.sample(images_cylinder_url, 1))
            random.shuffle(mix_list)
            for m in mix_list:
                if m[1] == "cylinder":
                    answer_index_list.append(mix_list.index(m))
            print("mix_list", mix_list)
            print("answer_index_list", answer_index_list)
            questions = [
                {
                    "body": [
                        {
                            "type": "know-cube-select",
                            "imgSrc": "",
                            "title": "选一选，圆柱体是那个形状？",
                            "list": [  # 列表图片选项
                                {
                                    "src": mix_list[0][0]
                                },
                                {
                                    "src": mix_list[1][0]
                                }
                            ]
                        }
                    ],
                    "answers": answer_index_list,
                    "resource": "resource",
                    "explain": "explain",
                    "knowledges": [
                        "认识圆柱体"
                    ],
                    "level": "1",
                    "type": "选择",
                    "number": "1-6-3-02"
                }
            ]
            print("questions", questions)
            all_questions.extend(questions)
        return all_questions

    # todo 1-6-3-03 那个物品放错地方了，请把它选出来
    def LifeCylinderSelect(self):
        all_questions = []
        for i in range(16):
            mix_list = []
            answer_list = []
            life_cube_url, life_cuboid_url, life_globe_url, life_cylinder_url = q_CreatImgs.UpImages().LifeSolid()
            mix_list.extend(random.sample(life_globe_url, 3))
            mix_list.extend(random.sample(life_cylinder_url, 1))
            random.shuffle(mix_list)
            for m in mix_list:
                if m[1] == "cylinder":
                    answer_list.append(mix_list.index(m))
            print("mix_list", mix_list)
            print("answer_list", answer_list)
            questions = [
                {
                    "body": [
                        {
                            "type": "know-cube-select",
                            "imgSrc": "",
                            "title": "那个物品放错地方了，请把它选出来。",
                            "list": [
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
                                }
                            ]
                        }
                    ],
                    "answers": answer_list,
                    "resource": "resource",
                    "explain": "explain",
                    "knowledges": [
                        "认识圆柱体"
                    ],
                    "level": "1",
                    "type": "选择",
                    "number": "1-6-3-03"
                }
            ]
            print("questions", questions)
            all_questions.extend(questions)

        return all_questions

    # todo 1-6-3-04 想一想，拖一拖。长方体下面拖入o 不是的下面拖入√
    def RightAndWrongCylinderSelect(self):
        all_questions = []
        for i in range(18):
            mix_list = []
            answer_replace_list = []
            all_solid_list, images_cylinder_url = q_CreatImgs.UpImages().CylinderShapeDiscern()
            mix_list.extend(random.sample(images_cylinder_url, 1))
            mix_list.extend(random.sample(all_solid_list, 3))
            random.shuffle(mix_list)
            for m in mix_list:
                if m[1] == "cylinder":
                    answer_replace_list.append(2)
                else:
                    answer_replace_list.append(1)
            print("mix_list", mix_list)
            print("answer_replace_list", answer_replace_list)
            questions = [
                {
                    "body": [
                        {
                            "title": "拖一拖",
                            "titleList": [  # 头部文字描述列表
                                {
                                    "type": "text",  # 文本类型
                                    "value": "想一想，拖一拖。圆柱体下面拖入"
                                },
                                {
                                    "type": "image",  # 符号类型
                                    "src": "/v2/通用/对错符号/圈.svg",
                                    "value": '圆圈'
                                },
                                {
                                    "type": "text",
                                    "value": "，不是的下面拖入"
                                },
                                {
                                    "type": "image",
                                    "src": "/v2/通用/对错符号/对号.svg",
                                    "value": '对号'
                                },
                                {
                                    "type": "text",
                                    "value": "。"
                                }
                            ],
                            "content": [  # 内容列表
                                {
                                    "src": mix_list[0][0],
                                    "val": ""
                                },
                                {
                                    "src": mix_list[1][0],
                                    "val": ""
                                },
                                {
                                    "src": mix_list[2][0],
                                    "val": ""
                                },
                                {
                                    "src": mix_list[3][0],
                                    "val": ""
                                }
                            ],
                            "options": [  # 符号列表
                                {
                                    "type": "1",  # 用于返回答案，
                                    "src": "/v2/通用/对错符号/对号.svg"
                                },
                                {
                                    "type": "2",  # 用于返回答案，
                                    "src": "/v2/通用/对错符号/圈.svg"
                                }
                            ],
                            "type": "know-cube-drag"
                        }
                    ],
                    "answers": answer_replace_list,  # 根据option里的type类型，没有对应为  '',
                    "knowledges": [
                        "认识圆柱"
                    ],
                    "resource": "resource",
                    "type": "选择",
                    "explain": "explain",
                    "level": "2",
                    "number": "1-6-3-04"
                }
            ]
            print("questions", questions)
            all_questions.extend(questions)
        return all_questions

    # todo 1-6-4-01 选一选,球体是那个形状?
    def GlobeShapeSelect(self):
        all_questions = []
        for i in range(6):
            mix_list = []
            answer_index_list = []
            all_solid_list, images_globe_url = q_CreatImgs.UpImages().GlobeShape()
            mix_list.extend(random.sample(all_solid_list, 1))
            mix_list.extend(random.sample(images_globe_url, 1))
            random.shuffle(mix_list)
            for m in mix_list:
                if m[1] == "globe":
                    answer_index_list.append(mix_list.index(m))
            print("mix_list", mix_list)
            print("answer_index_list", answer_index_list)
            questions = [
                {
                    "body": [
                        {
                            "type": "know-cube-select",
                            "imgSrc": "",
                            "title": "选一选，球体是那个形状？",
                            "list": [  # 列表图片选项
                                {
                                    "src": mix_list[0][0]
                                },
                                {
                                    "src": mix_list[1][0]
                                }
                            ]
                        }
                    ],
                    "answers": answer_index_list,
                    "resource": "resource",
                    "explain": "explain",
                    "knowledges": [
                        "认识球体"
                    ],
                    "level": "1",
                    "type": "选择",
                    "number": "1-6-4-01"
                }
            ]
            print("questions", questions)
            all_questions.extend(questions)
        return all_questions

    # todo 1-6-4-02 那个物品放错地方了，请把它选出来
    def LifeGlobeSelect(self):
        all_questions = []
        for i in range(16):
            mix_list = []
            answer_list = []
            life_cube_url, life_cuboid_url, life_globe_url, life_cylinder_url = q_CreatImgs.UpImages().LifeSolid()
            mix_list.extend(random.sample(life_cylinder_url, 3))
            mix_list.extend(random.sample(life_globe_url, 1))
            random.shuffle(mix_list)
            for m in mix_list:
                if m[1] == "orb":
                    answer_list.append(mix_list.index(m))
            print("mix_list", mix_list)
            print("answer_list", answer_list)
            questions = [
                {
                    "body": [
                        {
                            "type": "know-cube-select",
                            "imgSrc": "",
                            "title": "那个物品放错地方了，请把它选出来。",
                            "list": [
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
                                }
                            ]
                        }
                    ],
                    "answers": answer_list,
                    "resource": "resource",
                    "explain": "explain",
                    "knowledges": [
                        "认识球体"
                    ],
                    "level": "2",
                    "type": "选择",
                    "number": "1-6-4-02"
                }
            ]
            print("questions", questions)
            all_questions.extend(questions)

        return all_questions

    # todo 1-6-5-01 找朋友
    def FindCompanySelect(self):
        all_questions = []
        for i in range(18):
            mix_list = []
            answer_list = []
            life_cube_url, life_cuboid_url, life_globe_url, life_cylinder_url = q_CreatImgs.UpImages().LifeSolid()
            mix_list.extend(random.sample(life_cube_url, 2))
            mix_list.extend(random.sample(life_cuboid_url, 2))
            mix_list.extend(random.sample(life_globe_url, 2))
            mix_list.extend(random.sample(life_cylinder_url, 1))
            random.shuffle(mix_list)
            for m in mix_list:
                if m[1] == "orb":
                    answer_list.append([mix_list.index(m), 0])
                elif m[1] == "cube":
                    answer_list.append([mix_list.index(m), 1])
                elif m[1] == "cylinder":
                    answer_list.append([mix_list.index(m), 2])
                else:
                    answer_list.append([mix_list.index(m), 3])
            print("mix_list", mix_list)
            print("answer_list", answer_list)
            questions = [
                {
                    "body": [{
                        "stem": "找朋友。",
                        "content": [
                            [{
                                "src": mix_list[0][0],
                                "type": mix_list[0][1]
                            },
                                {
                                    "src": mix_list[1][0],
                                    "type": mix_list[1][1]
                                },
                                {
                                    "src": mix_list[2][0],
                                    "type": mix_list[2][1]
                                },
                                {
                                    "src": mix_list[3][0],
                                    "type": mix_list[3][1]
                                },
                                {
                                    "src": mix_list[4][0],
                                    "type": mix_list[4][1]
                                },
                                {
                                    "src": mix_list[5][0],
                                    "type": mix_list[5][1]
                                },
                                {
                                    "src": mix_list[6][0],
                                    "type": mix_list[6][1]
                                }
                            ],
                            [{
                                "src": "v2/通用/基本立体图形/球体_8.svg",
                                "type": "orb"
                            },
                                {
                                    "src": "v2/通用/基本立体图形/正方体_5.svg",
                                    "type": "cube"
                                },
                                {
                                    "src": "v2/通用/基本立体图形/圆柱体-2.svg",
                                    "type": "cylinder"
                                },
                                {
                                    "src": "v2/通用/基本立体图形/长方体_1.svg",
                                    "type": "cuboid"
                                }
                            ]
                        ],
                        "type": "know-cube-connect"
                    }],
                    "answers": answer_list,
                    "knowledges": [
                        "认识立体图形"
                    ],
                    "resource": "resource",
                    "type": "操作",
                    "explain": "explain",
                    "level": "2",
                    "number": "1-6-5-01"
                }
            ]
            print("questions", questions)
            all_questions.extend(questions)
        return all_questions

    # todo 1-6-5-02 数一数 填一填
    def SynthesizeSelect(self):
        all_questions = []
        for i in range(30):
            mix_list = []
            showType_list = [0, 1, 2]
            answer_list1 = []
            answer_list2 = []
            answer_list3 = []
            images_cuboid_url = q_CreatImgs.UpImages().CuboidDiscern()
            mix_list.extend(images_cuboid_url)
            random.shuffle(mix_list)
            for m in mix_list:
                if m[2] == "圆柱体":
                    answer_list1.append("1")
                else:
                    answer_list1.append("0")
            for m1 in mix_list:
                if m1[2] == "球体":
                    answer_list2.append(mix_list.index(m1) + 1)
                    for m2 in mix_list:
                        if m2[2] == "正方体":
                            answer_list2.append(mix_list.index(m2) + 1)
            for m3 in mix_list:
                if m3[2] == "长方体":
                    answer_list3.append(mix_list.index(m3) + 1)

            print("mix_list", mix_list)
            print("answer_list1", answer_list1)
            print("answer_list2", answer_list2)
            print("answer_list3", answer_list3)
            showType = random.choice(showType_list)
            print("showType", showType)
            if showType == 0:
                questions = [
                    {
                        "body": [
                            {
                                "type": "know-cube-color",
                                "showType": showType,  # 共用组件 # 表示题型操作类型，0  需要显示上色，1：正常无上色，无选择，2：表示图片可选择
                                "stem": "数一数，填一填。",
                                "colorList": [
                                    {
                                        'type': 'blue',
                                        'desc': '蓝色',
                                        'src': '/v2/组件/分类与整理/1-4-2-2/蓝色刷子.svg'
                                    },
                                    {
                                        'type': 'yellow',
                                        'desc': '黄色',
                                        'src': '/v2/组件/分类与整理/1-4-2-2/黄色刷子.svg'
                                    },
                                ],
                                "brushImg": '/v2/组件/分类与整理/1-4-2-2/橡皮.svg',
                                "brushDesc": '橡皮',
                                "actionTips": '（拖动到对应图形）',
                                "content": [
                                    {
                                        "type": mix_list[0][1],  # 图片类型：cylinder 圆柱体、 orb 球体、cube正方体、 cuboid 长方体
                                        "src": mix_list[0][0],
                                        "blueSrc": mix_list[0][3],
                                        "yellowSrc": mix_list[0][4],
                                    },
                                    {
                                        "type": mix_list[1][1],
                                        "src": mix_list[1][0],
                                        "blueSrc": mix_list[1][3],
                                        "yellowSrc": mix_list[1][4],
                                    },
                                    {
                                        "type": mix_list[2][1],
                                        "src": mix_list[2][0],
                                        "blueSrc": mix_list[2][3],
                                        "yellowSrc": mix_list[2][4],
                                    },
                                    {
                                        "type": mix_list[3][1],
                                        "src": mix_list[3][0],
                                        "blueSrc": mix_list[3][3],
                                        "yellowSrc": mix_list[3][4],
                                    },
                                    {
                                        "type": mix_list[4][1],
                                        "src": mix_list[4][0],
                                        "blueSrc": mix_list[4][3],
                                        "yellowSrc": mix_list[4][4],
                                    },
                                ],
                                "textList": [
                                    {
                                        "desc": '一共有',
                                        "type": 'text'
                                    }, {
                                        "desc": '',
                                        "type": 'input'
                                    }, {
                                        "desc": '个图形，给圆柱体涂上你喜欢的颜色。',
                                        "type": 'text'
                                    },
                                ],
                            }
                        ],
                        "answers": [['5'], answer_list1],  # showType: 1 時只可填
                        # answers: [['3'], ['', '', 'yellow', '', '']]
                        # showType: 0
                        # 可填也需上色时, 第一个数组表示所填答案，第二个表示对应下标所上颜色
                        #                      # answers: [['3'], [2, 3, 4]]
                        # showType: 2
                        # 可填也可选择时, 第一个数组表示所填答案，第二个表示选中图形的对应下标
                        "knowledges": "认识左右、5以内数的排序、认识长方体、认识正方体、认识球体、认识圆柱体、5以内的数",
                        "resource": "resource",
                        "type": "填空&操作",
                        "explain": "explain",
                        "level": "3",
                        "number": "1-6-5-05"
                    }

                ]
            if showType == 1:
                questions = [
                    {
                        "body": [
                            {
                                "type": "know-cube-color",
                                "showType": showType,  # 共用组件 # 表示题型操作类型，0  需要显示上色，1：正常无上色，无选择，2：表示图片可选择
                                "stem": "数一数，填一填。",

                                "content": [
                                    {
                                        "type": mix_list[0][1],  # 图片类型：cylinder 圆柱体、 orb 球体、cube正方体、 cuboid 长方体
                                        "src": mix_list[0][0],
                                    },
                                    {
                                        "type": mix_list[1][1],
                                        "src": mix_list[1][0],
                                    },
                                    {
                                        "type": mix_list[2][1],
                                        "src": mix_list[2][0],
                                    },
                                    {
                                        "type": mix_list[3][1],
                                        "src": mix_list[3][0],
                                    },
                                    {
                                        "type": mix_list[4][1],
                                        "src": mix_list[4][0],
                                    },
                                ],
                                "textList": [  # 文字描述列表
                                    {
                                        "desc": '从左边数，第',
                                        "type": 'text'  # 文字
                                    }, {
                                        "desc": '',
                                        "type": 'input'  # 输入框
                                    }, {
                                        "desc": '个是球，第',
                                        "type": 'text'
                                    }, {
                                        "desc": '',
                                        "type": 'input'
                                    }, {
                                        "desc": '个和第',
                                        "type": 'text'
                                    }, {
                                        "desc": '',
                                        "type": 'input'
                                    }, {
                                        "desc": '个是正方体。',
                                        "type": 'text'
                                    },
                                ],
                            }
                        ],
                        "answers": answer_list2,  # showType: 1 時只可填
                        # answers: [['3'], ['', '', 'yellow', '', '']]
                        # showType: 0
                        # 可填也需上色时, 第一个数组表示所填答案，第二个表示对应下标所上颜色
                        #                      # answers: [['3'], [2, 3, 4]]
                        # showType: 2
                        # 可填也可选择时, 第一个数组表示所填答案，第二个表示选中图形的对应下标
                        "knowledges": "认识左右、5以内数的排序、认识长方体、认识正方体、认识球体、认识圆柱体、5以内的数",
                        "resource": "resource",
                        "type": "填空&操作",
                        "explain": "explain",
                        "level": "3",
                        "number": "1-6-5-05"
                    }

                ]
            if showType == 2:
                questions = [
                    {
                        "body": [
                            {
                                "type": "know-cube-color",
                                "showType": showType,  # 共用组件 # 表示题型操作类型，0  需要显示上色，1：正常无上色，无选择，2：表示图片可选择
                                "stem": "数一数，填一填。",
                                "content": [
                                    {
                                        "type": mix_list[0][1],  # 图片类型：cylinder 圆柱体、 orb 球体、cube正方体、 cuboid 长方体
                                        "src": mix_list[0][0],
                                    },
                                    {
                                        "type": mix_list[1][1],
                                        "src": mix_list[1][0],
                                    },
                                    {
                                        "type": mix_list[2][1],
                                        "src": mix_list[2][0],
                                    },
                                    {
                                        "type": mix_list[3][1],
                                        "src": mix_list[3][0],
                                    },
                                    {
                                        "type": mix_list[4][1],
                                        "src": mix_list[4][0],
                                    },
                                ],
                                "textList": [
                                    {
                                        "desc": '从左边数，第',
                                        "type": 'text'
                                    }, {
                                        "desc": '',
                                        "type": 'input'
                                    }, {
                                        "desc": '个是长方体，选择右边的3个图形。',
                                        "type": 'text'
                                    },
                                ]
                            }
                        ],
                        "answers": [answer_list3, [2, 3, 4]],  # showType: 1 時只可填
                        # answers: [['3'], ['', '', 'yellow', '', '']]
                        # showType: 0
                        # 可填也需上色时, 第一个数组表示所填答案，第二个表示对应下标所上颜色
                        #                      # answers: [['3'], [2, 3, 4]]
                        # showType: 2
                        # 可填也可选择时, 第一个数组表示所填答案，第二个表示选中图形的对应下标
                        "knowledges": "认识左右、5以内数的排序、认识长方体、认识正方体、认识球体、认识圆柱体、5以内的数",
                        "resource": "resource",
                        "type": "填空&操作",
                        "explain": "explain",
                        "level": "3",
                        "number": "1-6-5-05"
                    }

                ]
            print("questions", questions)
            all_questions.extend(questions)
        return all_questions

    # todo 1-6-5-03 数一数
    def CountOneByOne(self):
        all_questions = []
        for i in range(18):
            mix_list = []
            answer_orb_list = []
            answer_cube_list = []
            answer_cuboid_list = []
            answer_cylinder_list = []
            all_life_instrument = []
            life_cube_url, life_cuboid_url, life_globe_url, life_cylinder_url = q_CreatImgs.UpImages().LifeSolid()
            mix_list.extend(random.sample(life_cube_url, 1))
            mix_list.extend(random.sample(life_cuboid_url, 1))
            mix_list.extend(random.sample(life_globe_url, 1))
            mix_list.extend(random.sample(life_cylinder_url, 1))

            all_life_instrument.extend(life_cube_url)
            all_life_instrument.extend(life_cuboid_url)
            all_life_instrument.extend(life_globe_url)
            all_life_instrument.extend(life_cylinder_url)
            while True:
                l = random.choice(all_life_instrument)

                if l not in mix_list:
                    print("l", l)
                    mix_list.append(l)
                if len(mix_list) == 12:
                    break
            print("mix_list", mix_list)
            print("mix_list_len", len(mix_list))
            for m in mix_list:
                if m[1] == "orb":
                    answer_orb_list.append("orb")
                elif m[1] == "cube":
                    answer_cube_list.append("cube")
                elif m[1] == "cuboid":
                    answer_cuboid_list.append("cuboid")
                else:
                    answer_cylinder_list.append("cylinder")

            questions = [
                {
                    "body": [
                        {
                            "title": "数一数，填一填",
                            "stem": "数一数，填一填。",
                            "classifyType": "cardShape",
                            "content": [
                                {
                                    "type": mix_list[0][1],  # 图片类型：cylinder  圆柱体、 orb球体、cube 正方体、 cuboid长方体, 前端用于提交答案
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
                            "typeList": [  # 基本图片类型
                                {
                                    "type": "orb",  # 图片类型：cylinder 圆柱体、 orb 球体、cube正方体、 cuboid 长方体
                                    "src": "v2/通用/基本立体图形/球体_8.svg"
                                },
                                {
                                    "type": "cube",
                                    "src": "v2/通用/基本立体图形/正方体_5.svg"
                                },
                                {
                                    "type": "cuboid",
                                    "src": "v2/通用/基本立体图形/圆柱体-2.svg"
                                },
                                {
                                    "type": "cylinder",
                                    "src": "v2/通用/基本立体图形/长方体_7.svg"
                                }
                            ],
                            "type": "know-cube-drag2"
                        }
                    ],
                    "answers": [answer_orb_list, answer_cube_list, answer_cylinder_list, answer_cuboid_list],
                    # 对应基本图形所拖动的图形类型
                    "knowledges": [
                        "认识长方体、认识正方体、认识球体、认识圆柱体"
                    ],
                    "resource": "resource",
                    "type": "操作",
                    "explain": "explain",
                    "level": "2",
                    "number": "1-6-5-03"
                }
            ]
            print("questions", questions)
            all_questions.extend(questions)
        return all_questions

    # todo 1-6-5-04 数一数 填一填
    def SynthesizeSelect2(self):
        all_questions = []
        for i in range(24):
            mix_list = []
            answer_orb_list = []
            answer_cube_list = []
            answer_cuboid_list = []
            answer_cylinder_list = []
            all_life_instrument = []
            life_cube_url, life_cuboid_url, life_globe_url, life_cylinder_url = q_CreatImgs.UpImages().LifeSolid()
            mix_list.extend(random.sample(life_cube_url, 1))
            mix_list.extend(random.sample(life_cuboid_url, 1))
            mix_list.extend(random.sample(life_globe_url, 1))
            mix_list.extend(random.sample(life_cylinder_url, 1))

            all_life_instrument.extend(life_cube_url)
            all_life_instrument.extend(life_cuboid_url)
            all_life_instrument.extend(life_globe_url)
            all_life_instrument.extend(life_cylinder_url)
            while True:
                l = random.choice(all_life_instrument)

                if l not in mix_list:
                    print("l", l)
                    mix_list.append(l)
                if len(mix_list) == 7:
                    break
            print("mix_list", mix_list)
            print("mix_list_len", len(mix_list))
            for m in mix_list:
                if m[1] == "orb":
                    answer_orb_list.append("orb")
                elif m[1] == "cube":
                    answer_cube_list.append("cube")
                elif m[1] == "cuboid":
                    answer_cuboid_list.append("cuboid")
                else:
                    answer_cylinder_list.append("cylinder")

            questions = [
                {
                    "body": [
                        {
                            "type": "know-cube-input",
                            "title": "填一填",
                            "stem": "数一数，填一填。",
                            "unit": "个",  # 单位
                            "dom": i,  # 节点唯一标识
                            "content": [
                                {  # type与typeList里的type相对应
                                    "type": mix_list[0][1],  # 图片类型：cylinder 圆柱体、 orb球体、cube 正方体、 cuboid 长方体
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
                            ],
                            "typeList": [  # 基本图片类型
                                {
                                    "type": "orb",
                                    "src": "v2/通用/基本立体图形/球体_8.svg"
                                },
                                {
                                    "type": "cube",
                                    "src": "v2/通用/基本立体图形/正方体_5.svg"
                                },
                                {
                                    "type": "cuboid",
                                    "src": "v2/通用/基本立体图形/圆柱体-2.svg"
                                },
                                {
                                    "type": "cylinder",
                                    "src": "v2/通用/基本立体图形/长方体_7.svg"
                                }
                            ]
                        }
                    ],
                    "answers": [str(len(answer_orb_list)), str(len(answer_cube_list)), str(len(answer_cylinder_list)),
                                str(len(answer_cuboid_list))],
                    "resource": "resource",
                    "explain": "explain",
                    "knowledges": [
                        "5以内 的数、认识长方体、认识正方体、认识球体、认识圆柱体"
                    ],
                    "level": "2",
                    "type": "填空",
                    "number": "1-6-5-04"
                }
            ]
            print("questions", questions)
            all_questions.extend(questions)
        return all_questions

    # todo 1-6-5-05 数一数 填一填
    def SynthesizeSelect3(self):
        all_questions = []
        for i in range(24):
            mix_list = []
            answer_orb_cuboid_list = []
            answer_cylinder_list = []
            reverse_answer_cylinder_list = []
            answer_orb_cylinder_list = []  # 多少球体多少圆柱
            showType_list = [1, 2, 3, 4]
            images_orb_url = q_CreatImgs.UpImages().OrbDiscern()
            mix_list.extend(images_orb_url)
            random.shuffle(mix_list)
            print("mix_list", mix_list)
            showType = random.choice(showType_list)
            if showType == 1:
                for m1 in mix_list:
                    if m1[1] == "orb":
                        answer_orb_cuboid_list.append(mix_list.index(m1) + 1)
                        for m11 in mix_list:
                            if m11[1] == "cuboid":
                                answer_orb_cuboid_list.append(mix_list.index(m11) + 1)

                print("answer_orb_cuboid_list", answer_orb_cuboid_list)
                questions = [
                    {
                        "body": [
                            {
                                "type": "know-cube-color",
                                "showType": "1",  # 共用组件 # 表示题型操作类型，0 需要显示上色，1：正常无上色，无选择，2：表示图片可选择
                                "stem": "数一数，填一填。",
                                "content": [
                                    {
                                        "type": mix_list[0][1],  # 图片类型：cylinder 圆柱体、 orb 球体、cube  正方体、 cuboi   长方体
                                        "src": mix_list[0][0],
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
                                ],
                                "textList": [  # 文字描述列表
                                    {
                                        "desc": '从左边数，第',
                                        "type": 'text'
                                    }, {
                                        "desc": '',
                                        "type": 'input'
                                    }, {
                                        "desc": '个是球，第',
                                        "type": 'text'
                                    }, {
                                        "desc": '',
                                        "type": 'input'
                                    }, {
                                        "desc": '个和第',
                                        "type": 'text'
                                    }, {
                                        "desc": '',
                                        "type": 'input'
                                    }, {
                                        "desc": '个是长方体。',
                                        "type": 'text'
                                    },
                                ],
                            }
                        ],
                        "answers": answer_orb_cuboid_list,
                        "knowledges": "认识左右、5以内数的排序、认识长方体、认识正方体、认识球体、认识圆柱体、5以内的数",
                        "resource": "resource",
                        "type": "填空&操作",
                        "explain": "explain",
                        "level": "3",
                        "number": "1-6-5-05"
                    }
                ]

            if showType == 3:
                for m2 in mix_list:
                    if m2[1] == "cylinder":
                        answer_cylinder_list.append(mix_list.index(m2) + 1)

                print("answer_cylinder_list", answer_cylinder_list)
                questions = [
                    {
                        "body": [
                            {
                                "type": "know-cube-color",
                                "showType": "1",  # 共用组件 # 表示题型操作类型，0 需要显示上色，1：正常无上色，无选择，2：表示图片可选择
                                "stem": "数一数，填一填",
                                "content": [
                                    {
                                        "type": mix_list[0][1],  # 图片类型：cylinder 圆柱体、 orb 球体、cube  正方体、 cuboi   长方体
                                        "src": mix_list[0][0],
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
                                ],
                                "textList": [  # 文字描述列表
                                    {
                                        "desc": '从左边数，第',
                                        "type": 'text'
                                    }, {
                                        "desc": '',
                                        "type": 'input'
                                    }, {
                                        "desc": '个，第',
                                        "type": 'text'
                                    }, {
                                        "desc": '',
                                        "type": 'input'
                                    }, {
                                        "desc": '个和第',
                                        "type": 'text'
                                    }, {
                                        "desc": '',
                                        "type": 'input'
                                    }, {
                                        "desc": '个是圆柱体。',
                                        "type": 'text'
                                    },
                                ],
                            }
                        ],
                        "answers": answer_cylinder_list,
                        "knowledges": "认识左右、5以内数的排序、认识长方体、认识正方体、认识球体、认识圆柱体、5以内的数",
                        "resource": "resource",
                        "type": "填空&操作",
                        "explain": "explain",
                        "level": "3",
                        "number": "1-6-5-05"
                    }
                ]

            if showType == 4:
                o = 0
                cy = 0
                for m3 in mix_list:
                    if m3[1] == "orb":
                        o += 1

                    if m3[1] == "cylinder":
                        cy += 1
                answer_orb_cylinder_list.append(o)
                answer_orb_cylinder_list.append(cy)
                print("answer_orb_cylinder_list", answer_orb_cylinder_list)
                questions = [
                    {
                        "body": [
                            {
                                "type": "know-cube-color",
                                "showType": "1",  # 共用组件 # 表示题型操作类型，0 需要显示上色，1：正常无上色，无选择，2：表示图片可选择
                                "stem": "数一数，填一填",
                                "content": [
                                    {
                                        "type": mix_list[0][1],  # 图片类型：cylinder 圆柱体、 orb 球体、cube  正方体、 cuboi   长方体
                                        "src": mix_list[0][0],
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
                                ],
                                "textList": [  # 文字描述列表
                                    {
                                        "desc": '一共有',
                                        "type": 'text'
                                    }, {
                                        "desc": '',
                                        "type": 'input'
                                    }, {
                                        "desc": '个球，一共有',
                                        "type": 'text'
                                    }, {
                                        "desc": '',
                                        "type": 'input'
                                    }, {
                                        "desc": '个圆柱体',
                                        "type": 'text'
                                    },
                                ],
                            }
                        ],
                        "answers": answer_orb_cylinder_list,
                        "knowledges": "认识左右、5以内数的排序、认识长方体、认识正方体、认识球体、认识圆柱体、5以内的数",
                        "resource": "resource",
                        "type": "填空&操作",
                        "explain": "explain",
                        "level": "3",
                        "number": "1-6-5-05"
                    }
                ]

            if showType == 2:
                reverse_mix_list = list(reversed(mix_list))
                for m4 in reverse_mix_list:
                    if m4[1] == "cylinder":
                        reverse_answer_cylinder_list.append(reverse_mix_list.index(m4) + 1)

                print("answer_cylinder_list", answer_cylinder_list)
                print("reverse_answer_cylinder_list", reverse_answer_cylinder_list)
                questions = [
                    {
                        "body": [
                            {
                                "type": "know-cube-color",
                                "showType": "1",  # 共用组件 # 表示题型操作类型，0 需要显示上色，1：正常无上色，无选择，2：表示图片可选择
                                "stem": "数一数，填一填",
                                "content": [
                                    {
                                        "type": mix_list[0][1],  # 图片类型：cylinder 圆柱体、 orb 球体、cube  正方体、 cuboi   长方体
                                        "src": mix_list[0][0],
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
                                ],
                                "textList": [  # 文字描述列表
                                    {
                                        "desc": '从右边数，第',
                                        "type": 'text'
                                    }, {
                                        "desc": '',
                                        "type": 'input'
                                    }, {
                                        "desc": '个，第',
                                        "type": 'text'
                                    }, {
                                        "desc": '',
                                        "type": 'input'
                                    }, {
                                        "desc": '个和第',
                                        "type": 'text'
                                    }, {
                                        "desc": '',
                                        "type": 'input'
                                    }, {
                                        "desc": '个是圆柱体。',
                                        "type": 'text'
                                    },
                                ],
                            }
                        ],
                        "answers": reverse_answer_cylinder_list,
                        "knowledges": "认识左右、5以内数的排序、认识长方体、认识正方体、认识球体、认识圆柱体、5以内的数",
                        "resource": "resource",
                        "type": "填空&操作",
                        "explain": "explain",
                        "level": "3",
                        "number": "1-6-5-05"
                    }
                ]

            print("questions", questions)
            all_questions.extend(questions)
        return all_questions

    # todo 1-6-5-06  数一数 填一填
    def SynthesizeSelect4(self):
        all_questions = []
        for i in range(24):
            mix_list = []
            stereo_combination_url = q_CreatImgs.UpImages().ComplexStereoCombination()
            mix_list.extend(random.choice(stereo_combination_url))
            print("mix_list", mix_list)
            print("mix_0", mix_list[0])
            print("mix_1", mix_list[1])
            questions = [
                {
                    "body": [
                        {
                            "type": "know-cube-input",
                            "title": "填一填",
                            "stem": "数一数，填一填。",
                            "unit": "个",  # 单位
                            "imgSrc": mix_list[0],
                            "typeList": [  # 基本图形列表
                                {
                                    "type": "orb",
                                    "src": "v2/通用/基本立体图形/球体_8.svg"
                                },
                                {
                                    "type": "cylinder",
                                    "src": "v2/通用/基本立体图形/圆柱体-2.svg"
                                },

                                {
                                    "type": "cube",
                                    "src": "v2/通用/基本立体图形/正方体_5.svg"
                                },
                                {
                                    "type": "cuboid",
                                    "src": "v2/通用/基本立体图形/长方体_7.svg"
                                },

                            ]
                        }
                    ],
                    "answers": mix_list[1],
                    "resource": "resource",
                    "explain": "explain",
                    "knowledges": [
                        "5以内 的数、认识长方体、认识正方体、认识球体、认识圆柱体"
                    ],
                    "level": "3",
                    "type": "填空",
                    "number": "1-6-5-06"
                }
            ]
            print("questions", questions)
            all_questions.extend(questions)
        return all_questions

    # todo 1-6-5-07  数一数 填一填
    def SynthesizeSelect5(self):
        all_questions = []
        for i in range(30):
            mix_list = []
            # cube and cuboid equal to    orb and cylinder equal to     cuboid than cube or cube than cuboid          orb than cylinder or cylinder than orb
            showtype_list = [1, 2, 3, 4]
            answer_list = []
            stereo_combination_url = q_CreatImgs.UpImages().ComplexStereoCombination()
            mix_list.extend(random.choice(stereo_combination_url))
            # print("mix_list", mix_list)

            showtype = random.choice(showtype_list)
            if showtype == 1:
                answer_list.append(mix_list[1][2] + mix_list[1][3])
                print("mix_cube", mix_list[1][2])
                print("mix_cuboid", mix_list[1][3])
                print("showtype1", answer_list)
                questions = [
                    {
                        "body": [
                            {
                                "type": "know-cube-input",
                                "title": "填一填",
                                "stem": "数一数，填一填。",
                                "imgSrc": mix_list[0],  # 头部大图片
                                "textList": [  # 下方文字描述列表
                                    {
                                        "desc": '图中所有长方体数目加所有正方体数目一共有',
                                        "type": 'text'
                                    }, {
                                        "desc": '',
                                        "type": 'input'
                                    }, {
                                        "desc": '个',
                                        "type": 'text'
                                    }
                                ]
                            }
                        ],
                        "answers": answer_list,
                        "resource": "resource",
                        "explain": "explain",
                        "knowledges": [
                            "5以内的数、比多少、5以内数的加法、5以内数的减法、认识长方体、认识正方体、认识球体、认识圆柱体"
                        ],
                        "level": "3",
                        "type": "填空",
                        "number": "1-6-5-06"
                    }
                ]

            if showtype == 2:
                answer_list.append(mix_list[1][0] + mix_list[1][1])
                print("mix_orb", mix_list[1][0])
                print("mix_cylinder", mix_list[1][1])
                print("showtype2", answer_list)
                questions = [
                    {
                        "body": [
                            {
                                "type": "know-cube-input",
                                "title": "填一填",
                                "stem": "数一数，填一填。",
                                "imgSrc": mix_list[0],  # 头部大图片
                                "textList": [  # 下方文字描述列表
                                    {
                                        "desc": '图中所有球体数目加所有圆柱体数目一共有',
                                        "type": 'text'
                                    }, {
                                        "desc": '',
                                        "type": 'input'
                                    }, {
                                        "desc": '个',
                                        "type": 'text'
                                    }
                                ]
                            }
                        ],
                        "answers": answer_list,
                        "resource": "resource",
                        "explain": "explain",
                        "knowledges": [
                            "5以内的数、比多少、5以内数的加法、5以内数的减法、认识长方体、认识正方体、认识球体、认识圆柱体"
                        ],
                        "level": "3",
                        "type": "填空",
                        "number": "1-6-5-06"
                    }
                ]

            if showtype == 3:
                if mix_list[1][2] > mix_list[1][3]:
                    answer_list.append(mix_list[1][2] - mix_list[1][3])
                    print("cube than cuboid", answer_list)
                    questions = [
                        {
                            "body": [
                                {
                                    "type": "know-cube-input",
                                    "title": "填一填",
                                    "stem": "数一数，填一填。",
                                    "imgSrc": mix_list[0],  # 头部大图片
                                    "textList": [  # 下方文字描述列表
                                        {
                                            "desc": '图中正方体数目比长方体数目多',
                                            "type": 'text'
                                        }, {
                                            "desc": '',
                                            "type": 'input'
                                        }, {
                                            "desc": '个',
                                            "type": 'text'
                                        }
                                    ]
                                }
                            ],
                            "answers": answer_list,
                            "resource": "resource",
                            "explain": "explain",
                            "knowledges": [
                                "5以内的数、比多少、5以内数的加法、5以内数的减法、认识长方体、认识正方体、认识球体、认识圆柱体"
                            ],
                            "level": "3",
                            "type": "填空",
                            "number": "1-6-5-06"
                        }
                    ]
                elif mix_list[1][3] > mix_list[1][2]:
                    answer_list.append(mix_list[1][3] - mix_list[1][2])
                    print("cuboid than cube", answer_list)
                    questions = [
                        {
                            "body": [
                                {
                                    "type": "know-cube-input",
                                    "title": "填一填",
                                    "stem": "数一数，填一填。",
                                    "imgSrc": mix_list[0],  # 头部大图片
                                    "textList": [  # 下方文字描述列表
                                        {
                                            "desc": '图中长方体数目比正方体数目多',
                                            "type": 'text'
                                        }, {
                                            "desc": '',
                                            "type": 'input'
                                        }, {
                                            "desc": '个',
                                            "type": 'text'
                                        }
                                    ]
                                }
                            ],
                            "answers": answer_list,
                            "resource": "resource",
                            "explain": "explain",
                            "knowledges": [
                                "5以内的数、比多少、5以内数的加法、5以内数的减法、认识长方体、认识正方体、认识球体、认识圆柱体"
                            ],
                            "level": "3",
                            "type": "填空",
                            "number": "1-6-5-06"
                        }
                    ]

            if showtype == 4:
                if mix_list[1][0] > mix_list[1][1]:
                    answer_list.append(mix_list[1][0] - mix_list[1][1])
                    print("orb than cylinder", answer_list)
                    questions = [
                        {
                            "body": [
                                {
                                    "type": "know-cube-input",
                                    "title": "填一填",
                                    "stem": "数一数，填一填。",
                                    "imgSrc": mix_list[0],  # 头部大图片
                                    "textList": [  # 下方文字描述列表
                                        {
                                            "desc": '图中球体数目比圆柱体数目多',
                                            "type": 'text'
                                        }, {
                                            "desc": '',
                                            "type": 'input'
                                        }, {
                                            "desc": '个',
                                            "type": 'text'
                                        }
                                    ]
                                }
                            ],
                            "answers": answer_list,
                            "resource": "resource",
                            "explain": "explain",
                            "knowledges": [
                                "5以内的数、比多少、5以内数的加法、5以内数的减法、认识长方体、认识正方体、认识球体、认识圆柱体"
                            ],
                            "level": "3",
                            "type": "填空",
                            "number": "1-6-5-06"
                        }
                    ]
                elif mix_list[1][1] > mix_list[1][0]:
                    answer_list.append(mix_list[1][1] - mix_list[1][0])
                    print("cylinder than orb", answer_list)
                    questions = [
                        {
                            "body": [
                                {
                                    "type": "know-cube-input",
                                    "title": "填一填",
                                    "stem": "数一数，填一填。",
                                    "imgSrc": mix_list[0],  # 头部大图片
                                    "textList": [  # 下方文字描述列表
                                        {
                                            "desc": '图中圆柱体数目比球体数目多',
                                            "type": 'text'
                                        }, {
                                            "desc": '',
                                            "type": 'input'
                                        }, {
                                            "desc": '个',
                                            "type": 'text'
                                        }
                                    ]
                                }
                            ],
                            "answers": answer_list,
                            "resource": "resource",
                            "explain": "explain",
                            "knowledges": [
                                "5以内的数、比多少、5以内数的加法、5以内数的减法、认识长方体、认识正方体、认识球体、认识圆柱体"
                            ],
                            "level": "3",
                            "type": "填空",
                            "number": "1-6-5-06"
                        }
                    ]

            print("questions", questions)
            all_questions.extend(questions)
        return all_questions

    # todo 1-6-6-01 数一数，填一填。
    def SynthesizeSelect6(self):
        all_questions = []
        for i in range(22):
            mix_list = []
            # only roll     only drag   orb   cube   cuboid cylinder
            showtype_list = [1, 2, 3, 4]
            answer_roll_list = []
            answer_drag_list = []
            answer_orb_list = []
            answer_cube_list = []
            answer_cuboid_list = []
            answer_cylinder_list = []
            life_cube_url, life_cuboid_url, life_globe_url, life_cylinder_url = q_CreatImgs.UpImages().LifeSolid()
            mix_list.extend(random.sample(life_cube_url, 1))
            mix_list.extend(random.sample(life_cuboid_url, 1))
            mix_list.extend(random.sample(life_globe_url, 1))
            mix_list.extend(random.sample(life_cylinder_url, 1))
            random.shuffle(mix_list)
            for m in mix_list:
                if m[1] == "orb" or m[1] == "cylinder":
                    answer_roll_list.append(mix_list.index(m) + 1)
                else:
                    answer_drag_list.append(mix_list.index(m) + 1)
            for m in mix_list:
                if m[1] == "orb":
                    answer_orb_list.append(mix_list.index(m) + 1)
                elif m[1] == "cube":
                    answer_cube_list.append(mix_list.index(m) + 1)
                elif m[1] == "cuboid":
                    answer_cuboid_list.append(mix_list.index(m) + 1)
                else:
                    answer_cylinder_list.append(mix_list.index(m) + 1)

            print("mix_list", mix_list)
            print("answer_roll_list", answer_roll_list)
            print("answer_drag_list", answer_drag_list)
            showtype = random.choice(showtype_list)
            if showtype == 1:
                questions = [
                    {
                        "body": [
                            {
                                "type": "know-cube-input2",
                                "title": "填一填",
                                "stem": "数一数，填一填。",
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
                                    }
                                ],
                                "textList": [  # 文字描述列表
                                    {
                                        "desc": "容易滚动的是",
                                        "type": "text"  # text：文字，input：输入框
                                    },
                                    {
                                        "desc": "",
                                        "type": "input"
                                    },
                                    {
                                        "desc": "和",
                                        "type": "text"
                                    },
                                    {
                                        "desc": "",
                                        "type": "input"
                                    }
                                ]
                            }
                        ],
                        "answers": answer_roll_list,
                        "resource": "resource",
                        "explain": "explain",
                        "knowledges": [
                            "立体图形的特征"
                        ],
                        "level": "1",
                        "type": "填空",
                        "number": "1-6-6-01"
                    }
                ]

            if showtype == 2:
                questions = [
                    {
                        "body": [
                            {
                                "type": "know-cube-input2",
                                "title": "填一填",
                                "stem": "数一数，填一填。",
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
                                    }
                                ],
                                "textList": [  # 文字描述列表
                                    {
                                        "desc": "不容易滚动的，只能拖动是",
                                        "type": "text"  # text：文字，input：输入框
                                    },
                                    {
                                        "desc": "",
                                        "type": "input"
                                    },
                                    {
                                        "desc": "和",
                                        "type": "text"
                                    },
                                    {
                                        "desc": "",
                                        "type": "input"
                                    }
                                ]
                            }
                        ],
                        "answers": answer_drag_list,
                        "resource": "resource",
                        "explain": "explain",
                        "knowledges": [
                            "立体图形的特征"
                        ],
                        "level": "1",
                        "type": "填空",
                        "number": "1-6-6-01"
                    }
                ]

            if showtype == 3:
                questions = [
                    {
                        "body": [
                            {
                                "type": "know-cube-input2",
                                "title": "填一填",
                                "stem": "数一数，填一填。",
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
                                    }
                                ],
                                "textList": [  # 文字描述列表
                                    {
                                        "desc": "上图生活用品中形状类似正方体的编号是",
                                        "type": "text"  # text：文字，input：输入框
                                    },
                                    {
                                        "desc": "",
                                        "type": "input"
                                    },
                                    {
                                        "desc": " ,  ",
                                        "type": "text"
                                    },
                                    {
                                        "desc": "上图生活用品中形状类似长方体的编号是",
                                        "type": "text"  # text：文字，input：输入框
                                    },
                                    {
                                        "desc": "",
                                        "type": "input"
                                    },

                                ]
                            }
                        ],
                        "answers": [answer_cube_list[0], answer_cuboid_list[0]],
                        "resource": "resource",
                        "explain": "explain",
                        "knowledges": [
                            "立体图形的特征"
                        ],
                        "level": "1",
                        "type": "填空",
                        "number": "1-6-6-01"
                    }
                ]

            if showtype == 4:
                questions = [
                    {
                        "body": [
                            {
                                "type": "know-cube-input2",
                                "title": "填一填",
                                "stem": "数一数，填一填。",
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
                                    }
                                ],
                                "textList": [  # 文字描述列表
                                    {
                                        "desc": "上图生活用品中形状类似球体的编号是",
                                        "type": "text"  # text：文字，input：输入框
                                    },
                                    {
                                        "desc": "",
                                        "type": "input"
                                    },
                                    {
                                        "desc": "，",
                                        "type": "text"
                                    },
                                    {
                                        "desc": "上图生活用品中形状类似圆柱体的编号是",
                                        "type": "text"  # text：文字，input：输入框
                                    },
                                    {
                                        "desc": "",
                                        "type": "input"
                                    },

                                ]
                            }
                        ],
                        "answers": [answer_orb_list[0], answer_cylinder_list[0]],
                        "resource": "resource",
                        "explain": "explain",
                        "knowledges": [
                            "立体图形的特征"
                        ],
                        "level": "1",
                        "type": "填空",
                        "number": "1-6-6-01"
                    }
                ]

            all_questions.extend(questions)
            print("questions", questions)
        return all_questions

    # todo 1-6-6-02 选出可以滚动的图形
    def RollDiagramSelect(self):
        all_questions = []
        for i in range(18):
            mix_list = []
            mid_list = []
            answer_list = []
            maybe_roll_url, not_roll_url = q_CreatImgs.UpImages().RollDiagram()
            mix_list.extend(random.sample(maybe_roll_url, 1))
            mid_list.extend(maybe_roll_url)
            mid_list.extend(not_roll_url)
            while True:
                mid = random.choice(mid_list)
                if mid not in mix_list:
                    mix_list.append(mid)
                if len(mix_list) == 8:
                    break
            random.shuffle(mix_list)
            print("mix_list", mix_list)
            for mix in mix_list:
                if mix[1] == "orb" or mix[1] == "cylinder" or mix[1] == "cone":
                    answer_list.append(mix_list.index(mix))
            print("answer_list", answer_list)
            questions = [
                {
                    "body": [
                        {
                            "type": "know-cube-select2",
                            "title": "选出可以滚动的图形。",
                            "content": [
                                {
                                    "src": mix_list[0][0],
                                    "type": mix_list[0][1]  # 图片类型：cylinder 圆柱体、 orb 球体、cube 正方体、 cuboid   长方体
                                },
                                {
                                    "src": mix_list[1][0],
                                    "type": mix_list[1][1]
                                },
                                {
                                    "src": mix_list[2][0],
                                    "type": mix_list[2][1]
                                },
                                {
                                    "src": mix_list[3][0],
                                    "type": mix_list[3][1]
                                },
                                {
                                    "src": mix_list[4][0],
                                    "type": mix_list[4][1]
                                },
                                {
                                    "src": mix_list[5][0],
                                    "type": mix_list[5][1]
                                },
                                {
                                    "src": mix_list[6][0],
                                    "type": mix_list[6][1]
                                },
                                {
                                    "src": mix_list[7][0],
                                    "type": mix_list[7][1]
                                }
                            ]
                        }
                    ],
                    "answers": answer_list,
                    "resource": "resource",
                    "explain": "explain",
                    "knowledges": [
                        "立体图形的特征"
                    ],
                    "level": "2",
                    "type": "选择",
                    "number": "1-6-6-02"
                }
            ]
            print("questions", questions)
            all_questions.extend(questions)
        return all_questions

    # todo 1-6-6-03 想一想，拖一拖。容易滚动的拖入o ，不能滚动的拖入√
    def RightAndWrongRollSelect(self):
        all_questions = []
        for i in range(18):
            mix_list = []
            answer_replace_list = []
            maybe_roll_url, not_roll_url = q_CreatImgs.UpImages().RollDiagram()
            mix_list.extend(random.sample(maybe_roll_url, 2))
            mix_list.extend(random.sample(not_roll_url, 2))
            random.shuffle(mix_list)
            for m in mix_list:
                if m[1] == "cuboid" or m[1] == "cylinder":
                    answer_replace_list.append(2)
                else:
                    answer_replace_list.append(1)
            print("mix_list", mix_list)
            print("answer_replace_list", answer_replace_list)
            questions = [
                {
                    "body": [
                        {
                            "title": "拖一拖",
                            "titleList": [  # 头部文字描述列表
                                {
                                    "type": "text",  # 文本类型
                                    "value": "想一想，拖一拖。容易滚动的拖入"
                                },
                                {
                                    "type": "image",  # 符号类型
                                    "src": "/v2/通用/对错符号/圈.svg",
                                    "value": '圆圈'
                                },
                                {
                                    "type": "text",
                                    "value": "，不能滚动的拖入"
                                },
                                {
                                    "type": "image",
                                    "src": "/v2/通用/对错符号/对号.svg",
                                    "value": '对号'
                                },
                                {
                                    "type": "text",
                                    "value": "。"
                                }
                            ],
                            "content": [  # 内容列表
                                {
                                    "src": mix_list[0][0],
                                    "val": ""
                                },
                                {
                                    "src": mix_list[1][0],
                                    "val": ""
                                },
                                {
                                    "src": mix_list[2][0],
                                    "val": ""
                                },
                                {
                                    "src": mix_list[3][0],
                                    "val": ""
                                }
                            ],
                            "options": [  # 符号列表
                                {
                                    "type": "1",  # 用于返回答案，
                                    "src": "/v2/通用/对错符号/对号.svg"
                                },
                                {
                                    "type": "2",  # 用于返回答案，
                                    "src": "/v2/通用/对错符号/圈.svg"
                                }
                            ],
                            "type": "know-cube-drag"
                        }
                    ],
                    "answers": answer_replace_list,  # 根据option里的type类型，没有对应为  '',
                    "knowledges": [
                        "立体图形的特征"
                    ],
                    "resource": "resource",
                    "type": "操作",
                    "explain": "explain",
                    "level": "2",
                    "number": "1-6-6-03"
                }
            ]
            print("questions", questions)
            all_questions.extend(questions)
        return all_questions

    # todo 1-6-6-04 连一连，你能帮他们选择合适的包装盒吗？
    def GiftBoxSelect(self):
        all_questions = []
        for i in range(16):
            mix_list = []
            gift_list = []
            box_list = []
            answer_list = []
            images_gift_orb_url, images_gift_cuboid_url, images_gift_cylinder_url, images_box_url = q_CreatImgs.UpImages().GiftBox()
            gift_list.extend(random.sample(images_gift_orb_url, 1))
            gift_list.extend(random.sample(images_gift_cylinder_url, 1))
            gift_list.extend(random.sample(images_gift_cuboid_url, 1))
            box_list.extend(random.sample(images_box_url, 3))
            random.shuffle(gift_list)
            random.shuffle(box_list)
            for gift in gift_list:
                for box in box_list:
                    if gift[1] == "orb" and box[3] == "globe":
                        answer_list.append([gift_list.index(gift), box_list.index(box)])
                    elif gift[1] == "cylinder" and box[3] == "max":
                        answer_list.append([gift_list.index(gift), box_list.index(box)])
                    elif gift[1] == "cuboid" and box[3] == "min":
                        answer_list.append([gift_list.index(gift), box_list.index(box)])
            print("gift_list", gift_list)
            print("box_list", box_list)
            print("answer_list", answer_list)
            questions = [
                {
                    "body": [
                        {
                            "stem": "连一连，你能帮他们选择合适的包装盒吗？",
                            "imgSrc": "v2/通用/人物/人物头像系列/男孩/8.svg",
                            "content": [
                                [
                                    {
                                        "src": gift_list[0][0],
                                        "type": gift_list[0][1]
                                    },
                                    {
                                        "src": gift_list[1][0],
                                        "type": gift_list[1][1]
                                    },
                                    {
                                        "src": gift_list[2][0],
                                        "type": gift_list[2][1]
                                    }
                                ],
                                [
                                    {
                                        "src": box_list[0][0],
                                        "type": box_list[0][1]
                                    },
                                    {
                                        "src": box_list[1][0],
                                        "type": box_list[1][1]
                                    },
                                    {
                                        "src": box_list[2][0],
                                        "type": box_list[2][1]
                                    }
                                ]
                            ],
                            "type": "know-cube-connect2"
                        }
                    ],
                    "answers": answer_list,
                    "knowledges": [
                        "立体图形的特征"
                    ],
                    "resource": "resource",
                    "type": "操作",
                    "explain": "explain",
                    "level": "1",
                    "number": "1-6-6-04"
                }
            ]
            print("questions", questions)
            all_questions.extend(questions)
        return all_questions

    # todo 1-6-7-01 想一想,拖一拖。能放稳的拖入√
    def SteadySolidSelect(self):
        all_questions = []
        for i in range(18):
            mix_list = []
            mid_list = []
            answer_list = []
            steady_solid_url, swaying_solid_url = q_CreatImgs.UpImages().SteadySolid()
            mix_list.extend(random.sample(steady_solid_url, 1))
            mid_list.extend(steady_solid_url)
            mid_list.extend(swaying_solid_url)
            while True:
                mid = random.choice(mid_list)
                if mid not in mix_list:
                    mix_list.append(mid)
                if len(mix_list) == 4:
                    break
            random.shuffle(mix_list)
            for mix in mix_list:
                if mix[1] == "steady":
                    answer_list.append("1")
                else:
                    answer_list.append("")
            print("mix_list", mix_list)
            print("answer_list", answer_list)
            questions = [
                {
                    "body": [
                        {
                            "title": "拖一拖",
                            "titleList": [  # 头部文字和图标描述列表
                                {
                                    "type": "text",
                                    "value": "想一想，拖一拖。能放稳的拖入"
                                },
                                {
                                    "type": "image",
                                    "src": "/v2/通用/对错符号/对号.svg",
                                    "value": '对号'  # 图片描述文字，可用于文字转语音
                                },
                                {
                                    "type": "text",
                                    "value": "。"
                                }
                            ],
                            "content": [  # 组合图形列表
                                {
                                    "src": mix_list[0][0],
                                },
                                {
                                    "src": mix_list[1][0],
                                },
                                {
                                    "src": mix_list[2][0],
                                },
                                {
                                    "src": mix_list[3][0],
                                }
                            ],
                            "options": [  # 对圈符号
                                {
                                    "type": "1",  # 用于前端传值
                                    "src": "/v2/通用/对错符号/对号.svg"
                                },
                                {
                                    "type": "2",
                                    "src": "/v2/通用/对错符号/圈.svg"
                                }
                            ],
                            "type": "know-cube-drag"
                        }
                    ],
                    "answers": answer_list,  # 与options里的type对应，数组的第一项和第三项对应为1就为正确答案
                    "knowledges": [
                        "立体图形的拼组"
                    ],
                    "resource": "resource",
                    "type": "操作",
                    "explain": "explain",
                    "level": "2",
                    "number": "1-6-7-01"
                }
            ]
            print("questions", questions)
            all_questions.extend(questions)
        return all_questions

    # todo 1-6-7-02 摆这个图形用到了那些图片？请选出来
    def PictureDiscernSelect(self):
        all_questions = []
        mid_list = []
        combination_solid_url = q_CreatImgs.UpImages().CombinationDiscern()
        mid_list.extend(combination_solid_url)
        for i in range(10):
            mix_list = []
            picture_list = ["orb", "cuboid", "cylinder", "cube"]
            answer_list = []

            choice=random.choice(mid_list)
            mid_list.remove(choice)
            # mix_list.extend(random.sample(combination_solid_url, 1))
            mix_list.append(choice)
            print(mix_list)
            for pic in picture_list:
                if pic in mix_list[0][2]:
                    answer_list.append(picture_list.index(pic))
            print("mix_list", mix_list)
            print("answer_list", answer_list)
            questions = [
                {
                    "body": [
                        {
                            "type": 'know-cube-select2',
                            "textList": [  # 头部文字与图片描述列表
                                {
                                    "type": "text",
                                    "value": "摆"
                                },
                                {
                                    "type": "image",
                                    "src": mix_list[0][0],
                                    "value": '组合图形',  # 图片也需加value，可能用于过后文字转语音功能
                                },
                                {
                                    "type": "text",
                                    "value": "，用到了哪些形状？请选出来。"
                                }
                            ],
                            "content": [  # 基本图形列表
                                {
                                    "src": "v2/通用/基本立体图形/球体_8.svg",
                                    "type": "orb"  # 类型: text:文字，image：图片，input: 输入框。前端根据type值决定显示内容
                                },
                                {
                                    "src": "v2/通用/基本立体图形/长方体_8.svg",
                                    "type": "cuboid"
                                },
                                {
                                    "src": "v2/通用/基本立体图形/圆柱体-2.svg",
                                    "type": "cylinder"
                                },
                                {
                                    "src": "v2/通用/基本立体图形/正方体_5.svg",
                                    "type": "cube"
                                }
                            ]
                        }
                    ],
                    "answers": answer_list,
                    "resource": "resource",
                    "explain": "explain",
                    "knowledges": [
                        "立体图形的拼组"
                    ],
                    "level": "2",
                    "type": "选择",
                    "number": "1-6-7-02"
                }
            ]
            print("questions", questions)
            all_questions.extend(questions)
        return all_questions

    # todo 1-6-7-03 摆对的拖入√，摆错的拖入O。
    def CombinationLoationSelect(self):
        all_questions = []
        for i in range(18):
            mix_list = []
            left_right_list = []
            abstract_list = []
            answer_list = []
            swaying_solid_url, images_solid_url = q_CreatImgs.UpImages().CombinationLoation()
            mix_list.extend(random.sample(swaying_solid_url, 2))
            left_right_list.extend([random.sample(images_solid_url, 2)])
            left_right_list.extend([random.sample(images_solid_url, 2)])

            print("mix_list", mix_list)
            print("left_right_List", left_right_list)
            lr = random.choice(left_right_list)
            if left_right_list.index(lr) == 1:
                abstract_list.append(lr)
                abstract_list.append(mix_list[1])
                answer_list.extend([1, 2])
            else:
                abstract_list.append(lr)
                abstract_list.append(mix_list[0])
                answer_list.extend([2, 1])
            print("abstract_list", abstract_list)

            questions = [
                {
                    "body": [
                        {
                            "title": "拖一拖",
                            "imgSrc": "v2/通用/人物/人物头像系列/男孩/8.svg",  # 人物图片
                            "stem": "先放一个" + str(abstract_list[1][2][0]) + "，在它上面放一个" + str(
                                abstract_list[1][2][1]) + "，左边放" + str(abstract_list[0][0][2]) + "，右边放一个" + str(
                                abstract_list[0][1][2]) + "。",  # 文字提示
                            "titleList": [  # 头部文字与图标列表
                                {
                                    "type": "text",
                                    "value": "摆对的拖入"
                                },
                                {
                                    "type": "symbol",
                                    "src": "/v2/通用/对错符号/圈.svg",
                                    "value": '圆圈'
                                },
                                {
                                    "type": "text",
                                    "value": "，摆错的拖入"
                                },
                                {
                                    "type": "symbol",
                                    "src": "/v2/通用/对错符号/对号.svg",
                                    "value": '对号'
                                },
                                {
                                    "type": "text",
                                    "value": "。"
                                }
                            ],
                            "content": [  # 组合图形与基本图形列表
                                [
                                    {
                                        "src": left_right_list[0][0][0],
                                        "type": "basic"
                                    },
                                    {
                                        "src": mix_list[0][0],
                                        "type": "compose"
                                    },
                                    {
                                        "src": left_right_list[0][1][0],
                                        "type": "basic"
                                    }
                                ],
                                [
                                    {
                                        "src": left_right_list[1][0][0],
                                        "type": "basic"
                                    },
                                    {
                                        "src": mix_list[1][0],
                                        "type": "compose"
                                    },
                                    {
                                        "src": left_right_list[1][1][0],
                                        "type": "basic"
                                    }
                                ]
                            ],
                            "options": [  # 符号图片资源列表
                                {
                                    "type": "1",
                                    "src": "/v2/通用/对错符号/对号.svg"
                                },
                                {
                                    "type": "2",
                                    "src": "/v2/通用/对错符号/圈.svg"
                                }
                            ],
                            "type": "know-cube-drag3"
                        }
                    ],
                    "answers": answer_list,  # 与options里的type对应
                    "knowledges": [
                        "立体图形的拼组"
                    ],
                    "resource": "resource",
                    "type": "操作",
                    "explain": "explain",
                    "level": "2",
                    "number": "1-6-7-03"
                }
            ]
            print("questions", questions)
            all_questions.extend(questions)
        return all_questions

    # todo 1-6-7-04 连一连，找出相同积木搭起来的图形。
    def SplitFindCombineSelect(self):
        all_questions = []
        for i in range(16):
            mix_list = []
            split_list = []
            answer_list = []
            images_combine_url = q_CreatImgs.UpImages().SplitFindCombine()
            mix_list.extend(images_combine_url)
            for mix in mix_list:
                split_list.append(mix[1])
            random.shuffle(mix_list)
            for split in split_list:
                if split == mix_list[0][1]:
                    answer_list.append([split_list.index(split), 0])

                elif split == mix_list[1][1]:
                    answer_list.append([split_list.index(split), 1])

                elif split == mix_list[2][1]:
                    answer_list.append([split_list.index(split), 2])

            print("mix_list", mix_list)
            print("split_list", split_list)
            print("answer_list", answer_list)
            questions = [

                {
                    "body": [
                        {
                            "stem": "连一连，找出相同积木搭起来的图形。",
                            "content": [  # 左边散图
                                [{  # 左边内容
                                    "src": split_list[0],  # 图片资源路径
                                    "val": '0'  # 前端用于计算正确值
                                },
                                    {
                                        "src": split_list[1],  # 图片资源路径
                                        "val": '1'
                                    },
                                    {
                                        "src": split_list[2],  # 图片资源路径
                                        "val": '2'
                                    }], [  # 右边内容
                                    {
                                        "src": mix_list[0][0],  # 图片资源路径
                                        "val": '0'
                                    },
                                    {
                                        "src": mix_list[1][0],  # 图片资源路径
                                        "val": '1'
                                    },
                                    {
                                        "src": mix_list[2][0],  # 图片资源路径
                                        "val": '2'
                                    },
                                ]
                            ],
                            "type": "know-cube-connect3"
                        }
                    ],
                    "answers": answer_list,  # 对应连线的下标值，需val相同
                    "knowledges": [
                        "立体图形的拼组"
                    ],
                    "resource": "resource",
                    "type": "操作",
                    "explain": "explain",
                    "level": "3",
                    "number": "1-6-7-04"
                }
            ]
            all_questions.extend(questions)
            print("questions", questions)
        return all_questions

    # todo 1-6-7-05 连一连，找出相同积木搭起来的图形。
    def BrickConstractSelect(self):
        all_questions = []
        for i in range(16):
            mix_list = []
            constract_list = []
            answer_list = []
            images_combine_url = q_CreatImgs.UpImages().BrickConstract()
            mix_list.extend(images_combine_url)
            for mix in mix_list:
                constract_list.append(mix[0])
            random.shuffle(mix_list)
            for constract in constract_list:
                if constract == mix_list[0][0]:
                    answer_list.append([constract_list.index(constract), 0])
                elif constract == mix_list[1][0]:
                    answer_list.append([constract_list.index(constract), 1])
                elif constract == mix_list[2][0]:
                    answer_list.append([constract_list.index(constract), 2])
                elif constract == mix_list[3][0]:
                    answer_list.append([constract_list.index(constract), 3])
            print("mix_list", mix_list)
            print("constract_list", constract_list)
            print("answer_list", answer_list)
            questions = [
                {
                    "body": [
                        {
                            "stem": "连一连，找出相同积木搭起来的图形。",
                            "content": [
                                [  # 左边组合过程图片资源
                                    {
                                        "src": constract_list[0]
                                    },
                                    {
                                        "src": constract_list[1]
                                    },
                                    {
                                        "src": constract_list[2]
                                    },
                                    {
                                        "src": constract_list[3]
                                    }
                                ],
                                [  # 组合图形资源
                                    {
                                        "src": mix_list[0][1]
                                    },
                                    {
                                        "src": mix_list[1][1]
                                    },
                                    {
                                        "src": mix_list[2][1]
                                    },
                                    {
                                        "src": mix_list[3][1]
                                    }
                                ]
                            ],
                            "type": "know-cube-connect4"
                        }
                    ],
                    "answers": answer_list,  # 对应连线的下标值，需val相同
                    "knowledges": [
                        "立体图形的拼组"
                    ],
                    "resource": "resource",
                    "type": "操作",
                    "explain": "explain",
                    "level": "2",
                    "number": "1-6-7-05"
                }
            ]
            print("questions", questions)
            all_questions.extend(questions)
        return all_questions

    # todo 1-6-7-06 那两堆可以拼成下面的图形？用线连起来。
    def PatchPictureSelect(self):
        all_questions = []
        for i in range(16):
            mix_list = []
            left_list=[]
            right_list=[]
            answer_list=[]
            images_brick_url = q_CreatImgs.UpImages().CombineFindSplit()
            mix_list.extend(images_brick_url)
            for mix in mix_list:
                left_list.append(mix[1])
                right_list.append(mix[2])

            random.shuffle(left_list)
            random.shuffle(right_list)
            for left in left_list:
                for right in right_list:
                    if left==mix_list[0][1] and right==mix_list[0][2]:
                        answer_list.append([left_list.index(left),right_list.index(right)])
                    elif left==mix_list[1][1] and right==mix_list[1][2]:
                        answer_list.append([left_list.index(left),right_list.index(right)])
                    elif left == mix_list[2][1] and right == mix_list[2][2]:
                        answer_list.append([left_list.index(left), right_list.index(right)])


            print("mix_list",mix_list)
            print("left_list",left_list)
            print("right_list",right_list)
            print("answer_list",answer_list)
            questions=[
                {
                    "body": [
                        {
                            "stem": "那两堆可以拼成下面的图形？用线连起来。",
                            "imgSrc": "v2/通用/基本立体图形/积木/积木5.svg",
                            "content": [
                                [
                                    {
                                        "src": left_list[0]
                                    },
                                    {
                                        "src": left_list[1]
                                    },
                                    {
                                        "src": left_list[2]
                                    }
                                ],
                                [
                                    {
                                        "src": right_list[0]
                                    },
                                    {
                                        "src": right_list[1]
                                    },
                                    {
                                        "src": right_list[2]
                                    }
                                ]
                            ],
                            "type": "know-cube-connect4"
                        }
                    ],
                    "answers": answer_list, # 对应连线的下标值，需val相同
            "knowledges": [
                "立体图形的拼组"
            ],
            "resource": "resource",
            "type": "操作",
            "explain": "explain",
            "level": "2",
            "number": "1-6-7-05"
            }
            ]
            print("questions",questions)
            all_questions.extend(questions)
        return all_questions


    #todo 1-6-7-07  下面图形中分别有几个小正方形？
    def CalculationCube(self):
        all_questions=[]
        for i in range(18):
            mix_list=[]
            images_cube_url=q_CreatImgs.UpImages().CalculationCube()
            mix_list.extend(random.sample(images_cube_url,4))
            questions=[
                {
                    "body": [
                        {
                            "type": "know-cube-input4",
                            "title": "填一填",
                            "stem": "下面图形中分别有几个小正方形？",
                            "unit": "个", # 单位
                        "content": [ # 图片资源列表
            {
                "num": mix_list[0][1],
                "src": mix_list[0][0]
            },
            {
                 "num": mix_list[1][1],
                "src": mix_list[1][0]
            },
            {
                 "num": mix_list[2][1],
                "src": mix_list[2][0]
            },
            {
                 "num": mix_list[3][1],
                "src": mix_list[3][0]
            }
            ]
            }
            ],
            "answers": [mix_list[0][1], mix_list[1][1], mix_list[2][1], mix_list[3][1]],
            "resource": "resource",
            "explain": "explain",
            "knowledges": [
                "立体图形的拼组", "5以内的数(或10以内的数)", "数一数"
            ],
            "level": "2",
            "type": "填空",
            "number": "1-6-7-07"
            }
            ]
            print("questions",questions)
            all_questions.extend(questions)
        return questions


    #todo 1-6-7-08  下面的大长方体是几个相同的小长方体组成吗?
    def ConstituteCuboid(self):
        all_questions=[]
        for i in range(8):
            mix_list=[]
            questions=[
            {
                "body": [
                    {
                        "type": "know-cube-input5",
                        "imgList": [ # 图片列表, 可能只有一个
                        {
                            "src": "v2/通用/基本立体图形/积木/积木12.svg",
                            "desc": '积木' # 图片描述
                        }
                ],
                "textList": [
                    {
                        "type": "text", # 显示类型，type：text文字，input输入框, image图片
        "desc": "下面的大长方体是"
        },
        {
            "type": "input",
            "desc": "个" # 输入框描述，如果类型时image时也需添加图片描述文字
        },
        {
            "type": "text",
            "desc": "个相同的小长方体组成的。"
        }
        ]
        }
        ],
        "answers": ["10", ],
        "resource": "resource",
        "explain": "explain",
        "knowledges": [
            "立体图形的拼组、5以内的数(或10以内的数)、数一数"
        ],
        "level": "2",
        "type": "填空",
        "number": "1-6-7-08"
        }
        ]
            all_questions.extend(questions)
        return all_questions


    # todo 1-6-7-09 摆成一个长方体，最少要用多少个相同的正方体？
    def ConstituteCuboid2(self):
        all_questions=[]
        for i in range(12):
            mix_list=[]
            choice_list=[1,2]
            choice=random.choice(choice_list)
            if choice==1:
                questions=[
                    {
                        "body": [
                            {
                                "type": "know-cube-input5",
                                "textList": [
                                    {
                                        "type": "text",
                                        "desc": "摆成一个长方体，最少要用"
                                    },
                                    {
                                        "type": "input",
                                        "desc": "个"
                                    },
                                    {
                                        "type": "text",
                                        "desc": "个相同的正方体？"
                                    }
                                ]
                            }
                        ],
                        "answers": ['2'],
                        "resource": "resource",
                        "explain": "explain",
                        "knowledges": [
                            "立体图形的拼组", "5以内的数"
                        ],
                        "level": "2",
                        "type": "填空",
                        "number": "1-6-7-09"
                    }
                ]
            if choice==2:
                questions=[
                    {
                        "body": [
                            {
                                "type": "know-cube-input5",
                                "textList": [
                                    {
                                        "type": "text",
                                        "desc": "摆成一个大正方体，最少要用"
                                    },
                                    {
                                        "type": "input",
                                        "desc": "个"
                                    },
                                    {
                                        "type": "text",
                                        "desc": "个相同的小正方体？"
                                    }
                                ]
                            }
                        ],
                        "answers": ['4'],
                        "resource": "resource",
                        "explain": "explain",
                        "knowledges": [
                            "立体图形的拼组", "5以内的数"
                        ],
                        "level": "2",
                        "type": "填空",
                        "number": "1-6-7-09"
                    }
                ]
            all_questions.extend(questions)
        return all_questions


    # todo 1-6-7-10 小亮和小红用正方体分别搭了一个立体图形，小亮给小红几块积木，两个人就一样多了
    def ThanHowMuch(self):
        all_questions=[]
        for i in range(24):
            mid_list=[]
            mix_list=[]
            showtype_list=[1,2]
            images_cube_url=q_CreatImgs.UpImages().CalculationCube()
            mix_list.extend(random.sample(images_cube_url,2))
            while True:
                answer_verify = (mix_list[0][1] + mix_list[1][1]) % 2
                # print("answer_verify",answer_verify)
                if answer_verify!=0:
                    mix_list=[]
                    mix_list.extend(random.sample(images_cube_url, 2))
                else:
                    break

            if mix_list[0][1]>mix_list[1][1]:
                pass
            else:
                mix_list[0],mix_list[1]=mix_list[1],mix_list[0]
            print("mix_list",mix_list)

            showtype=random.choice(showtype_list)
            if showtype==1:
                answer1 = int(mix_list[0][1] - (mix_list[0][1] + mix_list[1][1]) / 2)
                print("answer1", answer1)
                questions=[
                    {
                        "body": [
                            {
                                "type": "know-cube-input5",
                                "imgList": [ # 图片列表
                                {
                                    "src": mix_list[0][0],
                                    "desc": "小亮"
                                },
                            {
                                "src": mix_list[1][0],
                                "desc": "小红" # 图片描述文字
                            }
                        ],
                        "textList": [ # 头部文字与输入框列表
                        {
                            "type": "text",
                            "desc": "小亮和小红用正方体分别搭了一个立体图形，小亮给小红"
                        },
                    {
                        "type": "input",
                        "desc": "个"
                    },
                    {
                        "type": "text",
                        "desc": "块积木，两个人就一样多了。"
                    }
                ]
                }
                ],
                "answers": [answer1],
                "resource": "resource",
                "explain": "explain",
                "knowledges": [
                    "立体图形的拼组", "5以内的数（或10以内的数）", "数一数"
                ],
                "level": "2",
                "type": "填空",
                "number": "1-6-7-08"
                }
                ]

            if showtype==2:
                answer2 = int(mix_list[0][1] - mix_list[1][1])
                print("answer2", answer2)
                questions = [
                {
                    "body": [
                        {
                            "type": "know-cube-input5",
                            "imgList": [  # 图片列表
                                {
                                    "src": mix_list[0][0],
                                    "desc": "小亮"
                                },
                                {
                                    "src": mix_list[1][0],
                                    "desc": "小红"  # 图片描述文字
                                }
                            ],
                            "textList": [  # 头部文字与输入框列表
                                {
                                    "type": "text",
                                    "desc": "小亮和小红用正方体分别搭了一个立体图形，小亮比小红多"
                                },
                                {
                                    "type": "input",
                                    "desc": "个"
                                },
                                {
                                    "type": "text",
                                    "desc": "块积木。"
                                }
                            ]
                        }
                    ],
                    "answers": [answer2],
                    "resource": "resource",
                    "explain": "explain",
                    "knowledges": [
                        "立体图形的拼组", "5以内的数（或10以内的数）", "数一数"
                    ],
                    "level": "2",
                    "type": "填空",
                    "number": "1-6-7-08"
                }
            ]

            print("questions",questions)
            all_questions.extend(questions)
        return all_questions


    #todo 1-6-7-11 接着摆什么？选一选。
    def SequencingSelect(self):
        all_questions=[]
        for i in range(18):
            mix_list=[]
            mid_list=[]
            answer_list=[]
            images_sequencing_url=q_CreatImgs.UpImages().SequencingShape()
            mid_list.extend(random.sample(images_sequencing_url,3))
            for seq in range(3):
                for mid in mid_list:
                    mix_list.append(mid)
            print("mix_list",mix_list)
            answer_list.append(mix_list[7][1])
            print("answer_list",answer_list)
            questions=[
                {
                    "body": [
                        {
                            "type": "know-cube-select3",
                            "title": "接着摆什么？选一选。",
                            "content": [
                                {
                                    "src": mix_list[0][0],
                                    "type": mix_list[0][1] # 图片类型：cylinder 圆柱体、 orb球体、cube正方体、 cuboid长方体
            },
            {
                "src": mix_list[1][0],
                "type": mix_list[1][1]
            },
            {
                "src": mix_list[2][0],
                "type": mix_list[2][1]
            },
            {
                  "src": mix_list[3][0],
                "type": mix_list[3][1]
            },
            {
                  "src": mix_list[4][0],
                "type": mix_list[4][1]
            },
            {
                  "src": mix_list[5][0],
                "type": mix_list[5][1]
            },
            {
                  "src": mix_list[6][0],
                "type": mix_list[6][1]
            }
            ],
            "optionList": [
                {
                    "src": "v2/通用/基本立体图形/正方体_5.svg",
                    "type": "cube"
                },
                {
                    "src": "v2/通用/基本立体图形/长方体_1.svg",
                    "type": "cuboid"
                },
                {
                    "src": "v2/通用/基本立体图形/圆柱体-2.svg",
                    "type": "cylinder"
                },
                {
                    "src": "v2/通用/基本立体图形/球体_8.svg",
                    "type": "orb"
                }
            ]
            }
            ],
            "answers": answer_list, # 选中图形的类型，对应optionList里的type
            "resource": "resource",
            "explain": "explain",
            "knowledges": [
                "找规律"
            ],
            "level": "3",
            "type": "选择",
            "number": "1-6-7-11"
            }
            ]
            print("questions",questions)
            all_questions.extend(questions)
        return all_questions







if __name__ == '__main__':
    soildclass = SoildQuestions()
    # soildclass.ShapeSelect()
    # soildclass.CubeShapeSelect()
    # soildclass.RightAndWrong()
    # soildclass.CuboidSelect()
    # soildclass.LifeSolidSelect()
    # soildclass.CylinderSelect()
    # soildclass.CylinderShapeSelect()
    # soildclass.LifeCylinderSelect()
    # soildclass.RightAndWrongCylinderSelect()
    # soildclass.GlobeShapeSelect()
    # soildclass.LifeGlobeSelect()
    # soildclass.FindCompanySelect()
    # soildclass.SynthesizeSelect()
    # soildclass.CountOneByOne()
    # soildclass.SynthesizeSelect3()
    # soildclass.SynthesizeSelect4()
    # soildclass.SynthesizeSelect5()
    # soildclass.SynthesizeSelect6()
    # soildclass.RollDiagramSelect()
    # soildclass.GiftBoxSelect()
    # soildclass.SteadySolidSelect()
    # soildclass.PictureDiscernSelect()
    # soildclass.CombinationLoationSelect()
    # soildclass.SplitFindCombineSelect()
    # soildclass.PatchPictureSelect()
    soildclass.ThanHowMuch()
