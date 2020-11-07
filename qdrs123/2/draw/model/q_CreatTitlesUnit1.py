from model import NumCalculation
from draw import q_CreatDatas


class AnimalKnow(object):

    # todo 1-4-1-01 把动物选出来
    def AnimalSelect(self,  url_name1, url_name2, json_path, creat_json=False, json_name=None):

        questions_all= NumCalculation.CalculNum().AnimalSelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)



    # todo 1-4-1-01 选一选，给会飞的动物涂上颜色
    def AnimalColoring(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all= NumCalculation.CalculNum().AnimalColoring()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    # todo 1-4-1-01 选一选，给会飞的动物涂上颜色
    def AnimalColoringSelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all= NumCalculation.CalculNum().AnimalColoringSelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    #todo 1-4-1-04 在蔬菜下面输入“0”，在水果下面输入“1”
    def FruitVegetableSelectMid(self,url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = NumCalculation.CalculNum().FruitVegetableSelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    # todo 天上飞的输入“0”，水里游的输入“1”，地上跑的输入“2”
    def FlyAndSwimAndRunSelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = NumCalculation.CalculNum().FlyAndSwimAndRunSelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


    # todo 拖一拖﹐把下面生活用品分为三类
    def ToyAndStationerySelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = NumCalculation.CalculNum().ToyAndStationerySelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    # todo 拖一拖﹐把下面生活用品分为三类
    def ToyAndSportEquipmentSelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = NumCalculation.CalculNum().ToyAndSportEquipmentSelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)


        # todo 1-4-1-08 算一算，将得数相同的算式拖入到相同的框里
    def EquationClassifySelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = NumCalculation.CalculNum().EquationClassifySelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)

        #todo 1-4-1-10 把会飞的动物选出来，再填一填
    def FlyAnimalSelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = NumCalculation.CalculNum().FlyAnimalSelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    #todo 1-4-1-09 把学习文具选出来﹐再填—填
    def StationerySelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = NumCalculation.CalculNum().StationerySelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)

     # todo 1-4-1-11 分一分﹐填―填
    def TransportSelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = NumCalculation.CalculNum().TransportSelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    #todo 1-4-2-3 拖一拖﹐把下面生活用品分为三类
    def ClothingclssifySelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = NumCalculation.CalculNum().ClothingclssifySelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    #todo 1-4-2-1 选择同类﹐涂上相同的颜色
    def ClassifyTintageSelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = NumCalculation.CalculNum().ClassifyTintageSelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    #todo 1-4-2-2 选择同类﹐涂上相同的颜色
    def ClassifyTintageSelect2Mid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = NumCalculation.CalculNum().ClassifyTintageSelect2()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    #todo 1-4-2-4  按形状分类
    def ClassifyShapeMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = NumCalculation.CalculNum().ClassifyShape()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    # todo 1-4-2-5   按算式结果分类
    def CalculationResultSelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = NumCalculation.CalculNum().CalculationResultSelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    #todo 1-4-2-6 把和左边同类的选出来
    def InhomogeneityMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = NumCalculation.CalculNum().Inhomogeneity()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    # todo 1-4-2-7 选不同类
    def InhomogeneitySelectMid(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = NumCalculation.CalculNum().InhomogeneitySelect()

        if creat_json:
            q_CreatDatas.CreatDatas(questions_all).creatJson(json_path, json_name,url_name2)
        q_CreatDatas.CreatDatas(questions_all).creatUrl(url_name1, url_name2)