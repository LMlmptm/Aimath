from models import CreatTitlesUnit7


def main(creat_json=True):
    # todo 一、20以内数的认识

    # todo 二、20以内数的组成
    CreatTitlesUnit7.ComposnumbersWithin20().compos_numbers_within_20_4(
        num_max=20, url_name1='compos_numbers_within_20_4', url_name2='1-7-2-04', json_path='./data/title_json/',
        creat_json=creat_json, json_name='20以内数的组成_4'
    )

    # todo 三、个位,十位的认识

    # todo 四、20以内数的大小比较

    # todo 五、20以内数的排序

    # todo 六、20以内的不进位加法
    CreatTitlesUnit7.AddWithoutCarryWithin20().add_without_carry_within_20_15(
        num_max=20, url_name1='add_without_carry_within_20_15', url_name2='1-7-6-15', json_path='./data/title_json/',
        creat_json=creat_json, json_name='20以内的不进位加法_15'
    )

    # todo 七、20以内的不进位加法应用

    # todo 八、20以内的进位加法
    CreatTitlesUnit7.AddWithCarryWithin20().add_with_carry_within_20_1(
        num_max=20, url_name1='add_with_carry_within_20_1', url_name2='1-7-8-01', json_path='./data/title_json/',
        creat_json=creat_json, json_name='20以内的进位加法_1'
    )

    CreatTitlesUnit7.AddWithCarryWithin20().add_with_carry_within_20_18(
        num_max=20, url_name1='add_with_carry_within_20_18', url_name2='1-7-8-18', json_path='./data/title_json/',
        creat_json=creat_json, json_name='20以内的进位加法_18'
    )

    # todo 九、20以内的进位加法应用
    CreatTitlesUnit7.AppCarryAddWithin20().app_carry_add_within_20_8(
        num_max=20, url_name1='app_carry_add_within_20_8', url_name2='1-7-9-08', json_path='./data/title_json/',
        creat_json=creat_json, json_name='20以内的进位加法应用_8'
    )

    CreatTitlesUnit7.AppCarryAddWithin20().app_carry_add_within_20_9(
        num_max=20, url_name1='app_carry_add_within_20_9', url_name2='1-7-9-09', json_path='./data/title_json/',
        creat_json=creat_json, json_name='20以内的进位加法应用_9'
    )

    # todo 十、20以内的不退位减法

    # todo 十一、20以内的不退位减法应用


if __name__ == "__main__":
    main()
