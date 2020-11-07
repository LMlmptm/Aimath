from model import CreateQuestionUnit5
from draw import q_CreatDatas


class LoationTitles(object):

    #todo 1-5-1-01 看图填一填
    def CognitionFrontAndBackMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreateQuestionUnit5.LoationQuestions().CognitionFrontAndBack()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    #todo 1-5-1-02 看图填一填
    def CognitionFrontAndBack2Mid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreateQuestionUnit5.LoationQuestions().CognitionFrontAndBack2()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    #todo 1-5-1-03 看图选一选
    def CognitionFrontAndBack3Mid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreateQuestionUnit5.LoationQuestions().CognitionFrontAndBack3()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    # todo 1-5-1-04 看图填一填
    def CognitionFrontAndBack4Mid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreateQuestionUnit5.LoationQuestions().CognitionFrontAndBack4()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    #todo 1-5-1-05 看图选一选
    def CognitionFrontAndBack5Mid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreateQuestionUnit5.LoationQuestions().CognitionFrontAndBack5()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    #todo  1-5-1-06 看图填一填
    def CognitionFrontAndBack6Mid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreateQuestionUnit5.LoationQuestions().CognitionFrontAndBack6()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)



    # todo 1-5-1-07  拖一拖，排排序
    def CognitionFrontAndBack7Mid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreateQuestionUnit5.LoationQuestions().CognitionFrontAndBack7()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)



    # todo 1-5-1-08  拖一拖，排排序
    def CognitionFrontAndBack8Mid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreateQuestionUnit5.LoationQuestions().CognitionFrontAndBack8()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)



    #todo 1-5-1-09 拖一拖，排排序
    def CognitionFrontAndBack9Mid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreateQuestionUnit5.LoationQuestions().CognitionFrontAndBack9()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    # todo 1-5-1-10 看图填一填
    def CognitionFrontAndBack10Mid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreateQuestionUnit5.LoationQuestions().CognitionFrontAndBack10()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    # todo 1-5-1-11 填一填
    def CognitionFrontAndBack11Mid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreateQuestionUnit5.LoationQuestions().CognitionFrontAndBack11()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    #todo 1-5-2-01 选一选
    def ToChoiceAMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreateQuestionUnit5.LoationQuestions().ToChoiceA()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    #todo 1-5-2-02 选一选
    def ToChoiceA1Mid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreateQuestionUnit5.LoationQuestions().ToChoiceA1()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    #todo 1-5-2-03 填一填
    def ToChoiceA2Mid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreateQuestionUnit5.LoationQuestions().ToChoiceA2()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    #todo 1-5-2-04 填一填
    def ToChoiceA3Mid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreateQuestionUnit5.LoationQuestions().ToChoiceA3()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    #todo 1-5-2-05 填一填
    def ToChoiceA4Mid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreateQuestionUnit5.LoationQuestions().ToChoiceA4()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    #todo 1-5-2-06 填一填
    def ToChoiceA5Mid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreateQuestionUnit5.LoationQuestions().ToChoiceA5()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    #todo 1-5-2-07 填一填
    def ToChoiceA6Mid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreateQuestionUnit5.LoationQuestions().ToChoiceA6()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    #todo 1-5-2-10 选一选
    def ToChoiceA7Mid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreateQuestionUnit5.LoationQuestions().ToChoiceA7()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    #todo 1-5-1-11 看图填一填
    def ToChoiceA8Mid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreateQuestionUnit5.LoationQuestions().ToChoiceA8()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    #todo 1-5-3-01 看图选一选
    def LeftAndRightMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreateQuestionUnit5.LoationQuestions().LeftAndRight()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    #todo 1-5-3-02 看图选一选
    def LeftAndRight1Mid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreateQuestionUnit5.LoationQuestions().LeftAndRight1()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)



    #todo 1-5-3-03 看图填一填
    def LeftAndRight2Mid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreateQuestionUnit5.LoationQuestions().LeftAndRight2()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)



    #todo 1-5-3-06 连一连
    def LeftAndRight3Mid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreateQuestionUnit5.LoationQuestions().LeftAndRight3()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    # todo 1-5-3-07 连一连
    def LeftAndRight4Mid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreateQuestionUnit5.LoationQuestions().LeftAndRight4()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    #todo 1-5-3-08 选一选
    def LeftAndRight5Mid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreateQuestionUnit5.LoationQuestions().LeftAndRight5()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    #todo 1-5-3-09 拖一拖
    def LeftAndRight6Mid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreateQuestionUnit5.LoationQuestions().LeftAndRight6()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)

