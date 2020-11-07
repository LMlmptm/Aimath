from models.CreatNumbers import CreatNumbers
from models.CreatImgs import CreatImgs
from models import CreatQuestionUnit1
from models.CreatDatas import CreatDatas


# todo 一、数一数


# todo 二、比多少
class Comparison(object):
    def comparison_3(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatCompareNumbers14()
        imgs = CreatImgs().creatImgs4()
        questions_all = CreatQuestionUnit1.Comparison(nums).comparison_3(imgs)
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def comparison_8(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatCompareNumbers10()
        imgs = CreatImgs().creatImgs10()
        questions_all = CreatQuestionUnit1.Comparison(nums).comparison_8(imgs)
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)


# todo 三、5以内数的认识
class AnderstandNumbersWithin5(object):
    def anderstand_numbers_within_5_1(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatCompareNumbers5()
        imgs = CreatImgs().creatImgs4()
        questions_all = CreatQuestionUnit1.AnderstandNumbersWithin5(nums).anderstand_numbers_within_5_1(imgs)
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def anderstand_numbers_within_5_3(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatCompareNumbers5()
        imgs = CreatImgs().creatImgs4()
        questions_all = CreatQuestionUnit1.AnderstandNumbersWithin5(nums).anderstand_numbers_within_5_3(imgs)
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def anderstand_numbers_within_5_5(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatCompareNumbers20()
        imgs = CreatImgs().creatImgs4()
        questions_all = CreatQuestionUnit1.AnderstandNumbersWithin5(nums).anderstand_numbers_within_5_5(imgs)
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def anderstand_numbers_within_5_6(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatCompareNumbers5()
        questions_all = CreatQuestionUnit1.AnderstandNumbersWithin5(nums).anderstand_numbers_within_5_6()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)


# todo 四、比较符号的认识
class UnderstandComparativeSymbols(object):
    def understand_comparative_symbols_1(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreatQuestionUnit1.UnderstandComparativeSymbols().understand_comparative_symbols_1()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def understand_comparative_symbols_2(self, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreatQuestionUnit1.UnderstandComparativeSymbols().understand_comparative_symbols_2()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)


# todo 五、5以内数的大小比较
class ComparNumbersWithin5(object):
    def compar_numbers_within_5_2(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatCompareNumbers3()
        questions_all = CreatQuestionUnit1.ComparNumbersWithin5(nums).compar_numbers_within_5_2()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def compar_numbers_within_5_3(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatCompareNumbers3()
        questions_all = CreatQuestionUnit1.ComparNumbersWithin5(nums).compar_numbers_within_5_3()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def compar_numbers_within_5_8(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatCompareNumbers5()
        questions_all = CreatQuestionUnit1.ComparNumbersWithin5(nums).compar_numbers_within_5_8()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)


# todo 六、5以内数的排序
class SortNumbersWithin5(object):
    def sort_numbers_within_5_1(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatCompareNumbers9()
        questions_all = CreatQuestionUnit1.SortNumbersWithin5(nums).sort_numbers_within_5_1()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def sort_numbers_within_5_2_1(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatCompareNumbers5()
        imgs = CreatImgs().creatImgs4()
        questions_all = CreatQuestionUnit1.SortNumbersWithin5(nums).sort_numbers_within_5_2_1(imgs)
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def sort_numbers_within_5_2_2(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatCompareNumbers5()
        imgs = CreatImgs().creatImgs4()
        questions_all = CreatQuestionUnit1.SortNumbersWithin5(nums).sort_numbers_within_5_2_2(imgs)
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def sort_numbers_within_5_3(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatCompareNumbers5()
        questions_all = CreatQuestionUnit1.SortNumbersWithin5(nums).sort_numbers_within_5_3()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def sort_numbers_within_5_5_1(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatCompareNumbers15()
        questions_all = CreatQuestionUnit1.SortNumbersWithin5(nums).sort_numbers_within_5_5_1()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def sort_numbers_within_5_5_2(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatCompareNumbers16()
        questions_all = CreatQuestionUnit1.SortNumbersWithin5(nums).sort_numbers_within_5_5_2()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def sort_numbers_within_5_6(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatCompareNumbers12()
        questions_all = CreatQuestionUnit1.SortNumbersWithin5(nums).sort_numbers_within_5_6()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)


# todo 七、5以内数的合与分
class CombSepWithin5(object):
    def comb_sep_within_5_1(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatAddNumbers1()
        imgs = CreatImgs().creatImgs4()
        questions_all = CreatQuestionUnit1.CombSepWithin5(nums).comb_sep_within_5_1(imgs)
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def comb_sep_within_5_3(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatCompareNumbers17()
        questions_all = CreatQuestionUnit1.CombSepWithin5(nums).comb_sep_within_5_3()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def comb_sep_within_5_4(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatCompareNumbers18()
        imgs = CreatImgs().creatImgs2()
        questions_all = CreatQuestionUnit1.CombSepWithin5(nums).comb_sep_within_5_4(imgs)
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def comb_sep_within_5_5(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatCompareNumbers13()
        questions_all = CreatQuestionUnit1.CombSepWithin5(nums).comb_sep_within_5_5()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)


# todo 八、0的认识
class Anderstand0(object):
    def anderstand_0_1(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreatQuestionUnit1.Anderstand0.anderstand_0_1()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def anderstand_0_2(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatCompareNumbers19()
        imgs = CreatImgs().creatImgs2()
        questions_all = CreatQuestionUnit1.Anderstand0(nums).anderstand_0_2(imgs)
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def anderstand_0_3(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatAddNumbers3_1()
        questions_all = CreatQuestionUnit1.Anderstand0(nums).anderstand_0_3()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def anderstand_0_4_1(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreatQuestionUnit1.Anderstand0.anderstand_0_4_1()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def anderstand_0_4_2(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreatQuestionUnit1.Anderstand0.anderstand_0_4_2()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def anderstand_0_5(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatCompareNumbers11()
        questions_all = CreatQuestionUnit1.Anderstand0(nums).anderstand_0_5()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)


# todo 九、10以内数的认识
class AnderstandNumbersWithin10(object):
    def anderstand_numbers_within_10_1(self, num_max, url_name1, url_name2, json_path, creat_json=False,
                                       json_name=None):
        nums = CreatNumbers(num_max).creatNumbersWithinTen2()
        imgs = CreatImgs().creatImgs4()
        questions_all = CreatQuestionUnit1.AnderstandNumbersWithin10(nums).anderstand_numbers_within_10_1(imgs)
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def anderstand_numbers_within_10_2(self, num_max, url_name1, url_name2, json_path, creat_json=False,
                                       json_name=None):
        nums = CreatNumbers(num_max).creatNumbersWithinTen1()
        imgs = CreatImgs().creatImgs9()
        questions_all = CreatQuestionUnit1.AnderstandNumbersWithin10(nums).anderstand_numbers_within_10_2(imgs)
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def anderstand_numbers_within_10_3(self, num_max, url_name1, url_name2, json_path, creat_json=False,
                                       json_name=None):
        nums = CreatNumbers(num_max).creatNumbersWithinTen1()
        questions_all = CreatQuestionUnit1.AnderstandNumbersWithin10(nums).anderstand_numbers_within_10_3()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def anderstand_numbers_within_10_5_1(self, num_max, url_name1, url_name2, json_path, creat_json=False,
                                         json_name=None):
        nums = CreatNumbers(num_max).creatNumbersWithinTen1()
        questions_all = CreatQuestionUnit1.AnderstandNumbersWithin10(nums).anderstand_numbers_within_10_5_1()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def anderstand_numbers_within_10_5_2(self, num_max, url_name1, url_name2, json_path, creat_json=False,
                                         json_name=None):
        nums = CreatNumbers(num_max).creatNumbersWithinTen1()
        imgs = CreatImgs().creatImgs4()
        questions_all = CreatQuestionUnit1.AnderstandNumbersWithin10(nums).anderstand_numbers_within_10_5_2(imgs)
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def anderstand_numbers_within_10_6(self, num_max, url_name1, url_name2, json_path, creat_json=False,
                                       json_name=None):
        nums = CreatNumbers(num_max).creatNumbersWithinTen1()
        questions_all = CreatQuestionUnit1.AnderstandNumbersWithin10(nums).anderstand_numbers_within_10_6()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def anderstand_numbers_within_10_8(self, num_max, url_name1, url_name2, json_path, creat_json=False,
                                       json_name=None):
        nums = CreatNumbers(num_max).creatNumbersWithinTen12()
        questions_all = CreatQuestionUnit1.AnderstandNumbersWithin10(nums).anderstand_numbers_within_10_8()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def anderstand_numbers_within_10_9(self, num_max, url_name1, url_name2, json_path, creat_json=False,
                                       json_name=None):
        nums = CreatNumbers(num_max).creatNumbersWithinTen1()
        imgs = CreatImgs().creatImgs4()
        questions_all = CreatQuestionUnit1.AnderstandNumbersWithin10(nums).anderstand_numbers_within_10_9(imgs)
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def anderstand_numbers_within_10_10(self, num_max, url_name1, url_name2, json_path, creat_json=False,
                                        json_name=None):
        nums = CreatNumbers(num_max).creatNumbersWithinTen1()
        imgs = CreatImgs().creatImgs8()
        questions_all = CreatQuestionUnit1.AnderstandNumbersWithin10(nums).anderstand_numbers_within_10_10(imgs)
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)


# todo 十、10以内数的排序
class SortNumbersWithin10(object):
    def sort_numbers_within_10_2_1(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatNumbersWithinTen6()
        questions_all = CreatQuestionUnit1.SortNumbersWithin10(nums).sort_numbers_within_10_2_1()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def sort_numbers_within_10_2_2(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatNumbersWithinTen6()
        questions_all = CreatQuestionUnit1.SortNumbersWithin10(nums).sort_numbers_within_10_2_2()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def sort_numbers_within_10_2_3(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatNumbersWithinTen6()
        questions_all = CreatQuestionUnit1.SortNumbersWithin10(nums).sort_numbers_within_10_2_3()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def sort_numbers_within_10_2_4(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatNumbersWithinTen6()
        questions_all = CreatQuestionUnit1.SortNumbersWithin10(nums).sort_numbers_within_10_2_4()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def sort_numbers_within_10_3_1(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatNumbersWithinTen7()
        questions_all = CreatQuestionUnit1.SortNumbersWithin10(nums).sort_numbers_within_10_3_1()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def sort_numbers_within_10_3_2(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatNumbersWithinTen7()
        questions_all = CreatQuestionUnit1.SortNumbersWithin10(nums).sort_numbers_within_10_3_2()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def sort_numbers_within_10_4_1(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatNumbersWithinTen3()
        questions_all = CreatQuestionUnit1.SortNumbersWithin10(nums).sort_numbers_within_10_4_1()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def sort_numbers_within_10_4_2(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatNumbersWithinTen4()
        questions_all = CreatQuestionUnit1.SortNumbersWithin10(nums).sort_numbers_within_10_4_2()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def sort_numbers_within_10_6(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatNumbersWithinTen8()
        questions_all = CreatQuestionUnit1.SortNumbersWithin10(nums).sort_numbers_within_10_6()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def sort_numbers_within_10_7(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatNumbersWithinTen9()
        questions_all = CreatQuestionUnit1.SortNumbersWithin10(nums).sort_numbers_within_10_7()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def sort_numbers_within_10_8(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatNumbersWithinTen10()
        imgs = CreatImgs().creatImgs12()
        questions_all = CreatQuestionUnit1.SortNumbersWithin10(nums).sort_numbers_within_10_8(imgs)
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def sort_numbers_within_10_9(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatNumbersWithinTen11()
        questions_all = CreatQuestionUnit1.SortNumbersWithin10(nums).sort_numbers_within_10_9()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)


# todo 十一、10以内数的大小比较
class ComparNumbersWithin10(object):
    def compar_numbers_within_10_1(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatNumbersWithinTen13()
        imgs = CreatImgs().creatImgs8()
        questions_all = CreatQuestionUnit1.ComparNumbersWithin10(nums).compar_numbers_within_10_1(imgs)
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def compar_numbers_within_10_2(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatNumbersWithinTen2()
        questions_all = CreatQuestionUnit1.ComparNumbersWithin10(nums).compar_numbers_within_10_2()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def compar_numbers_within_10_3(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatNumbersWithinTen2()
        imgs = CreatImgs().creatImgs12()
        questions_all = CreatQuestionUnit1.ComparNumbersWithin10(nums).compar_numbers_within_10_3(imgs)
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)


# todo 十二、10以内数的合与分
class CombSepWithin10(object):
    def comb_sep_within_10_1(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatAddNumbersWithTen1()
        questions_all = CreatQuestionUnit1.CombSepWithin10(nums).comb_sep_within_10_1()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def comb_sep_within_10_3(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatNumbersWithinTen14()
        questions_all = CreatQuestionUnit1.CombSepWithin10(nums).comb_sep_within_10_3()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def comb_sep_within_10_8(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        nums = CreatNumbers(num_max).creatNumbersWithinTen5()
        imgs = CreatImgs().creatImgs8()
        questions_all = CreatQuestionUnit1.CombSepWithin10(nums).comb_sep_within_10_8(imgs)
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)


if __name__ == "__main__":
    pass
