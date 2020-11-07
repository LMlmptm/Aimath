from models.CreatNumbers import CreatNumbers
from models.CreatImgs import CreatImgs
from models import CreatQuestionUnit7
from models.CreatDatas import CreatDatas


# todo 一、20以内数的认识


# todo 二、20以内数的组成
class ComposnumbersWithin20(object):
    def compos_numbers_within_20_4(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatNumbersWithTwenty1()
        questions_all = CreatQuestionUnit7.ComposnumbersWithin20(nums).compos_numbers_within_20_4()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)


# todo 三、个位,十位的认识


# todo 四、20以内数的大小比较


# todo 五、20以内数的排序


# todo 六、20以内的不进位加法
class AddWithoutCarryWithin20(object):
    def add_without_carry_within_20_15(self, num_max, url_name1, url_name2, json_path, creat_json=False,
                                       json_name=None):
        nums = CreatNumbers(num_max).creatAddSubWithinTwenty1()
        questions_all = CreatQuestionUnit7.AddWithoutCarryWithin20(nums).add_without_carry_within_20_15()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)


# todo 七、20以内的不进位加法应用


# todo 八、20以内的进位加法
class AddWithCarryWithin20(object):
    def add_with_carry_within_20_1(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatAddSubWithinTwenty2()
        questions_all = CreatQuestionUnit7.AddWithCarryWithin20(nums).add_with_carry_within_20_1()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def add_with_carry_within_20_18(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatAddSubWithinTwenty3()
        questions_all = CreatQuestionUnit7.AddWithCarryWithin20(nums).add_with_carry_within_20_18()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)


# todo 九、20以内的进位加法应用
class AppCarryAddWithin20(object):
    def app_carry_add_within_20_8(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatAddSubWithinTwenty2()
        questions_all = CreatQuestionUnit7.AppCarryAddWithin20(nums).app_carry_add_within_20_8()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def app_carry_add_within_20_9(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatAddSubWithinTwenty2()
        questions_all = CreatQuestionUnit7.AppCarryAddWithin20(nums).app_carry_add_within_20_9()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)


# todo 十、20以内的不退位减法


# todo 十一、20以内的不退位减法应用


if __name__ == "__main__":
    pass
