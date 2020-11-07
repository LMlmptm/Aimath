import os
import json
from aimath.sdk import QuestionAPI


class CreatDatas(object):
    def __init__(self, questions_all):
        self.questions_all = questions_all

    # 输出json数据
    def creatJson(self, url_path, json_name):


        if not os.path.exists(url_path):
            os.makedirs(url_path)
        with open(os.path.join(url_path, '{}.json'.format(json_name)), 'w', encoding='utf_8') as w:
            json.dump(self.questions_all, w, ensure_ascii=False)

    # 输出url
    def creatUrl(self, url_name1, url_name2):
        result = QuestionAPI.post(["{}".format(url_name1)], "{}".format(url_name2), self.questions_all)
        print(result["state"], result["data"]["url"] if result["state"] == 1 else result["msg"])
