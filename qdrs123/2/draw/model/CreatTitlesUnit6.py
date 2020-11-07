from model import CreateQuestionUnit6
from draw import q_CreatDatas

class SolidFigture():

    # todo 1-6-1-01 这是什么形状?
    def ShapeSelectMid(self,  url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all= CreateQuestionUnit6.SoildQuestions().ShapeSelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    # todo 1-6-1-02 选一选,正方体是那个形状?
    def CubeShapeSelectMid(self,  url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all= CreateQuestionUnit6.SoildQuestions().CubeShapeSelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    # todo 1-6-1-03 想一想，拖一拖。正方体下面拖入o 不是的下面拖入√
    def RightAndWrongMid(self,  url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all= CreateQuestionUnit6.SoildQuestions().RightAndWrong()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


        #todo 1-6-2-01 这是什么形状？
    def CuboidSelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all = CreateQuestionUnit6.SoildQuestions().CuboidSelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


        #todo 1-6-2-02 那个物品放错地方了，请把它选出来
    def LifeSolidSelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all = CreateQuestionUnit6.SoildQuestions().LifeSolidSelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)

        #todo 1-6-2-03 那个物品放错地方了，请把它选出来
    def LifeSolid2SelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all = CreateQuestionUnit6.SoildQuestions().LifeSolid2Select()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    # todo 1-6-2-04 想一想，拖一拖。正方体下面拖入o 不是的下面拖入√
    def RightAndWrongSelectMid(self,  url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all= CreateQuestionUnit6.SoildQuestions().RightAndWrongSelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


        #todo 1-6-3-01 这是什么形状？
    def CylinderSelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all = CreateQuestionUnit6.SoildQuestions().CylinderSelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    # todo 1-6-3-02 选一选，圆柱体是那个形状？
    def CylinderShapeSelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all = CreateQuestionUnit6.SoildQuestions().CylinderShapeSelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    #todo 1-6-2-03 那个物品放错地方了，请把它选出来
    def LifeCylinderSelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all = CreateQuestionUnit6.SoildQuestions().LifeCylinderSelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    # todo 1-6-2-04 想一想，拖一拖。长方体下面拖入o 不是的下面拖入√
    def RightAndWrongCylinderSelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all = CreateQuestionUnit6.SoildQuestions().RightAndWrongCylinderSelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    # todo 1-6-4-01 选一选,球体是那个形状?
    def GlobeShapeSelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all = CreateQuestionUnit6.SoildQuestions().GlobeShapeSelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


        #todo 1-6-4-02 那个物品放错地方了，请把它选出来
    def LifeGlobeSelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all = CreateQuestionUnit6.SoildQuestions().LifeGlobeSelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    #todo 1-6-5-01 找朋友
    def FindCompanySelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all = CreateQuestionUnit6.SoildQuestions().FindCompanySelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    #todo 1-6-5-02 数一数 填一填
    def SynthesizeSelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all = CreateQuestionUnit6.SoildQuestions().SynthesizeSelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    # todo 1-6-5-03 数一数
    def CountOneByOneMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all = CreateQuestionUnit6.SoildQuestions().CountOneByOne()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    # todo 1-6-5-04 数一数 填一填
    def SynthesizeSelect2Mid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all = CreateQuestionUnit6.SoildQuestions().SynthesizeSelect2()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    #todo 1-6-5-05 数一数 填一填
    def SynthesizeSelect3Mid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all = CreateQuestionUnit6.SoildQuestions().SynthesizeSelect3()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)



    #todo 1-6-5-06  数一数 填一填
    def SynthesizeSelect4Mid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all = CreateQuestionUnit6.SoildQuestions().SynthesizeSelect4()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)



    # todo 1-6-5-07  数一数 填一填
    def SynthesizeSelect5Mid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all = CreateQuestionUnit6.SoildQuestions().SynthesizeSelect5()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    # todo 1-6-6-01 数一数，填一填。
    def SynthesizeSelect6Mid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all = CreateQuestionUnit6.SoildQuestions().SynthesizeSelect6()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    #todo 1-6-6-02 选出可以滚动的图形
    def RollDiagramSelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all = CreateQuestionUnit6.SoildQuestions().RollDiagramSelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    # todo 1-6-6-03 想一想，拖一拖。容易滚动的拖入o ，不能滚动的拖入√
    def RightAndWrongRollSelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all = CreateQuestionUnit6.SoildQuestions().RightAndWrongRollSelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    # todo 1-6-6-04 连一连，你能帮他们选择合适的包装盒吗？
    def GiftBoxSelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all = CreateQuestionUnit6.SoildQuestions().GiftBoxSelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    #todo 1-6-7-01 想一想,拖一拖。能放稳的拖入√
    def SteadySolidSelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all = CreateQuestionUnit6.SoildQuestions().SteadySolidSelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    #todo 1-6-7-02 摆这个图形用到了那些图片？请选出来
    def PictureDiscernSelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all = CreateQuestionUnit6.SoildQuestions().PictureDiscernSelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


        # todo 1-6-7-03 摆对的拖入√，摆错的拖入O。
    def CombinationLoationSelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all = CreateQuestionUnit6.SoildQuestions().CombinationLoationSelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


        # todo 1-6-7-04 连一连，找出相同积木搭起来的图形。
    def SplitFindCombineSelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all = CreateQuestionUnit6.SoildQuestions().SplitFindCombineSelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    # todo 1-6-7-05 连一连，找出相同积木搭起来的图形。
    def BrickConstractSelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all = CreateQuestionUnit6.SoildQuestions().BrickConstractSelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    # todo 1-6-7-06 那两堆可以拼成下面的图形？用线连起来。
    def PatchPictureSelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all = CreateQuestionUnit6.SoildQuestions().PatchPictureSelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    #todo 1-6-7-07  下面图形中分别有几个小正方形？
    def CalculationCubeMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all = CreateQuestionUnit6.SoildQuestions().CalculationCube()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    #todo 1-6-7-08  下面的大长方体是几个相同的小长方体组成吗?
    def ConstituteCuboidMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all = CreateQuestionUnit6.SoildQuestions().ConstituteCuboid()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    # todo 1-6-7-09 摆成一个长方体，最少要用多少个相同的正方体？
    def ConstituteCuboid2Mid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all = CreateQuestionUnit6.SoildQuestions().ConstituteCuboid2()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    # todo 1-6-7-10 小亮和小红用正方体分别搭了一个立体图形，小亮给小红几块积木，两个人就一样多了
    def ThanHowMuchMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all = CreateQuestionUnit6.SoildQuestions().ThanHowMuch()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    #todo 1-6-7-11 接着摆什么？选一选。
    def SequencingSelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all = CreateQuestionUnit6.SoildQuestions().SequencingSelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name, url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)