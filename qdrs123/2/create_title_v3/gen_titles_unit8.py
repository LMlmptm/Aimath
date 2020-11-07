from models import CreatTitlesUnit8


def main(creat_json=True):
    # todo 一、整时
    CreatTitlesUnit8.IntegralTime().integral_time_1(
        num_max=12, url_name1='integral_time_1', url_name2='1-8-1-01', json_path='./data/title_json/',
        creat_json=creat_json, json_name='整时_1'
    )

    CreatTitlesUnit8.IntegralTime().integral_time_2_1(
        num_max=12, url_name1='integral_time_2_1', url_name2='1-8-1-02', json_path='./data/title_json/',
        creat_json=creat_json, json_name='整时_2_1'
    )

    CreatTitlesUnit8.IntegralTime().integral_time_2_2(
        num_max=12, url_name1='integral_time_2_2', url_name2='1-8-1-02', json_path='./data/title_json/',
        creat_json=creat_json, json_name='整时_2_2'
    )

    # todo 二、半时

    # todo 三、整时、半时的应用
    CreatTitlesUnit8.AppOfIntegralAndHalfTime().app_of_integral_and_half_time_5_1(
        num_max=12, url_name1='app_of_integral_and_half_time_5_1', url_name2='1-8-3-05', json_path='./data/title_json/',
        creat_json=creat_json, json_name='整时半时的应用_5_1'
    )

    CreatTitlesUnit8.AppOfIntegralAndHalfTime().app_of_integral_and_half_time_5_2(
        num_max=12, url_name1='app_of_integral_and_half_time_5_2', url_name2='1-8-3-05', json_path='./data/title_json/',
        creat_json=creat_json, json_name='整时半时的应用_5_2'
    )

    # todo 四、整时、半时的综合认识


if __name__ == "__main__":
    main()
