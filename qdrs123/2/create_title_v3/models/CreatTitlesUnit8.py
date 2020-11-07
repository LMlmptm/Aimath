from models.CreatNumbers import CreatNumbers
from models.CreatImgs import CreatImgs
from models import CreatQuestionUnit8
from models.CreatDatas import CreatDatas


# todo 一、整时
class IntegralTime(object):
    def integral_time_1(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        questions_all = CreatQuestionUnit8.IntegralTime.integral_time_1()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def integral_time_2_1(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        imgs = CreatImgs().creatImgs13()
        questions_all = CreatQuestionUnit8.IntegralTime.integral_time_2_1(imgs)
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def integral_time_2_2(self, num_max, url_name1, url_name2, json_path, creat_json=False, json_name=None):
        imgs = CreatImgs().creatImgs14()
        questions_all = CreatQuestionUnit8.IntegralTime.integral_time_2_2(imgs)
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)


# todo 二、半时


# todo 三、整时、半时的应用
class AppOfIntegralAndHalfTime(object):
    def app_of_integral_and_half_time_5_1(self, num_max, url_name1, url_name2, json_path, creat_json=False,
                                          json_name=None):
        nums = CreatNumbers(num_max).creatNumbersWithinTen15()
        questions_all = CreatQuestionUnit8.AppOfIntegralAndHalfTime(nums).app_of_integral_and_half_time_5_1()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)

    def app_of_integral_and_half_time_5_2(self, num_max, url_name1, url_name2, json_path, creat_json=False,
                                          json_name=None):
        nums = CreatNumbers(num_max).creatNumbersWithinTen15()
        questions_all = CreatQuestionUnit8.AppOfIntegralAndHalfTime(nums).app_of_integral_and_half_time_5_2()
        if creat_json:
            CreatDatas(questions_all).creatJson(json_path, json_name)
        CreatDatas(questions_all).creatUrl(url_name1, url_name2)


# todo 四、整时、半时的综合认识


if __name__ == "__main__":
    pass
