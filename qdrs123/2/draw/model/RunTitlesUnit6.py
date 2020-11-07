from model import CreatTitlesUnit6

def main(creat_json=True):

    # # todo 1-6-1-01 这是什么形状?
    # CreatTitlesUnit6.SolidFigture().ShapeSelectMid(
    #     url_name1='know-cube-select_1-6', url_name2='1-6-1-01', json_path='./data/title_json/',
    #     creat_json=creat_json, json_name='这是什么形状'
    # )
    #
    # # todo 1-6-1-02 选一选,正方体是那个形状?
    # CreatTitlesUnit6.SolidFigture().CubeShapeSelectMid(
    #     url_name1='know-cube-select_1-6', url_name2='1-6-1-02', json_path='./data/title_json/',
    #     creat_json=creat_json, json_name='选一选,正方体是那个形状'
    # )

    # todo 1-6-1-03 想一想，拖一拖。正方体下面拖入o 不是的下面拖入√
    CreatTitlesUnit6.SolidFigture().RightAndWrongMid(
        url_name1='know-cube-drag_1-6', url_name2='1-6-1-03', json_path='./data/title_json/',
        creat_json=creat_json, json_name='想一想，拖一拖。正方体下面拖入o 不是的下面拖入√'
    )

    #todo 1-6-2-01 这是什么形状？
    CreatTitlesUnit6.SolidFigture().CuboidSelectMid(
        url_name1='know-cube-select_1-6', url_name2='1-6-2-01', json_path='./data/title_json/',
        creat_json=creat_json, json_name='这是什么形状'
    )

    #todo 1-6-2-02 那个物品放错地方了，请把它选出来
    CreatTitlesUnit6.SolidFigture().LifeSolidSelectMid(
        url_name1='know-cube-select_1-6', url_name2='1-6-2-02', json_path='./data/title_json/',
        creat_json=creat_json, json_name='那个物品放错地方了，请把它选出来'
    )


    #todo 1-6-2-03 那个物品放错地方了，请把它选出来
    CreatTitlesUnit6.SolidFigture().LifeSolid2SelectMid(
        url_name1='know-cube-select_1-6', url_name2='1-6-2-03', json_path='./data/title_json/',
        creat_json=creat_json, json_name='那个物品放错地方了，请把它选出来'
    )

    # todo 1-6-2-04 想一想，拖一拖。正方体下面拖入o 不是的下面拖入√
    CreatTitlesUnit6.SolidFigture().RightAndWrongSelectMid(
        url_name1='know-cube-drag_1-6', url_name2='1-6-2-04', json_path='./data/title_json/',
        creat_json=creat_json, json_name='想一想，拖一拖。正方体下面拖入o 不是的下面拖入√'
    )

    #todo 1-6-3-01 这是什么形状
    CreatTitlesUnit6.SolidFigture().CylinderSelectMid(
        url_name1='know-cube-select_1-6', url_name2='1-6-3-01', json_path='./data/title_json/',
        creat_json=creat_json, json_name='这是什么形状'
    )

    # todo 1-6-3-02 选一选，圆柱体是那个形状
    CreatTitlesUnit6.SolidFigture().CylinderShapeSelectMid(
        url_name1='know-cube-select_1-6', url_name2='1-6-3-02', json_path='./data/title_json/',
        creat_json=creat_json, json_name='选一选，圆柱体是那个形状'
    )

    # todo 1-6-3-03 那个物品放错地方了，请把它选出来
    CreatTitlesUnit6.SolidFigture().LifeCylinderSelectMid(
        url_name1='know-cube-select_1-6', url_name2='1-6-3-03', json_path='./data/title_json/',
        creat_json=creat_json, json_name='那个物品放错地方了，请把它选出来'
    )

    # todo 1-6-3-04 想一想，拖一拖。长方体下面拖入o 不是的下面拖入√
    CreatTitlesUnit6.SolidFigture().RightAndWrongCylinderSelectMid(
        url_name1='know-cube-drag_1-6', url_name2='1-6-3-04', json_path='./data/title_json/',
        creat_json=creat_json, json_name='想一想，拖一拖。长方体下面拖入o 不是的下面拖入√'
    )

    # todo 1-6-4-01 选一选,球体是那个形状
    CreatTitlesUnit6.SolidFigture().GlobeShapeSelectMid(
        url_name1='know-cube-select_1-6', url_name2='1-6-4-01', json_path='./data/title_json/',
        creat_json=creat_json, json_name='选一选,球体是那个形状'
    )

    # todo 1-6-4-02 那个物品放错地方了，请把它选出来
    CreatTitlesUnit6.SolidFigture().LifeGlobeSelectMid(
        url_name1='know-cube-select_1-6', url_name2='1-6-4-02', json_path='./data/title_json/',
        creat_json=creat_json, json_name='那个物品放错地方了，请把它选出来'
    )

    #todo 1-6-5-01 找朋友
    CreatTitlesUnit6.SolidFigture().FindCompanySelectMid(
        url_name1='know-cube-connect_1-6', url_name2='1-6-5-01', json_path='./data/title_json/',
        creat_json=creat_json, json_name='找朋友'
    )


    #todo 1-6-5-02 数一数 填一填
    CreatTitlesUnit6.SolidFigture().SynthesizeSelectMid(
        url_name1='know-cube-color_1-6', url_name2='1-6-5-02', json_path='./data/title_json/',
        creat_json=creat_json, json_name='数一数 填一填'
    )

    # todo 1-6-5-03 数一数
    CreatTitlesUnit6.SolidFigture().CountOneByOneMid(
        url_name1='know-cube-drag2_1-6', url_name2='1-6-5-03', json_path='./data/title_json/',
        creat_json=creat_json, json_name='数一数'
    )


    #todo 1-6-5-04 数一数 填一填
    CreatTitlesUnit6.SolidFigture().SynthesizeSelect2Mid(
        url_name1='know-cube-input_1-6', url_name2='1-6-5-04', json_path='./data/title_json/',
        creat_json=creat_json, json_name='数一数 填一填'
    )

    #todo 1-6-5-05 数一数 填一填
    CreatTitlesUnit6.SolidFigture().SynthesizeSelect3Mid(
        url_name1='know-cube-input_1-6', url_name2='1-6-5-05', json_path='./data/title_json/',
        creat_json=creat_json, json_name='数一数 填一填'
    )

    #todo 1-6-5-06  数一数 填一填
    CreatTitlesUnit6.SolidFigture().SynthesizeSelect4Mid(
        url_name1='know-cube-input_1-6', url_name2='1-6-5-06', json_path='./data/title_json/',
        creat_json=creat_json, json_name='数一数 填一填'
    )


    # todo 1-6-5-07  数一数 填一填
    CreatTitlesUnit6.SolidFigture().SynthesizeSelect5Mid(
        url_name1='know-cube-input_1-6', url_name2='1-6-5-07', json_path='./data/title_json/',
        creat_json=creat_json, json_name='数一数 填一填'
    )


    # todo 1-6-6-01 数一数，填一填。
    CreatTitlesUnit6.SolidFigture().SynthesizeSelect6Mid(
        url_name1='know-cube-input_1-6', url_name2='1-6-6-01', json_path='./data/title_json/',
        creat_json=creat_json, json_name='数一数 填一填'
    )

    #todo 1-6-6-02 选出可以滚动的图形
    CreatTitlesUnit6.SolidFigture().RollDiagramSelectMid(
        url_name1='know-cube-input_1-6', url_name2='1-6-6-02', json_path='./data/title_json/',
        creat_json=creat_json, json_name='选出可以滚动的图形'
    )

    # todo 1-6-6-03 想一想，拖一拖。容易滚动的拖入o ，不能滚动的拖入√
    CreatTitlesUnit6.SolidFigture().RightAndWrongRollSelectMid(
        url_name1='know-cube-drag_1-6', url_name2='1-6-6-03', json_path='./data/title_json/',
        creat_json=creat_json, json_name='想一想，拖一拖。容易滚动的拖入o ，不能滚动的拖入√'
    )

    # todo 1-6-6-04 连一连，你能帮他们选择合适的包装盒吗？
    CreatTitlesUnit6.SolidFigture().GiftBoxSelectMid(
        url_name1='know-cube-connect2_1-6', url_name2='1-6-6-04', json_path='./data/title_json/',
        creat_json=creat_json, json_name='连一连，你能帮他们选择合适的包装盒吗'
    )


    # todo 1-6-7-01 想一想,拖一拖。能放稳的拖入√
    CreatTitlesUnit6.SolidFigture().SteadySolidSelectMid(
        url_name1='know-cube-drag_1-6', url_name2='1-6-7-01', json_path='./data/title_json/',
        creat_json=creat_json, json_name='想一想,拖一拖。能放稳的拖入√'
    )


    #todo 1-6-7-02 摆这个图形用到了那些图片？请选出来
    CreatTitlesUnit6.SolidFigture().PictureDiscernSelectMid(
        url_name1='know-cube-select2_1-6', url_name2='1-6-7-02', json_path='./data/title_json/',
        creat_json=creat_json, json_name='摆这个图形用到了那些图片？请选出来'
    )


    # todo 1-6-7-03 摆对的拖入√，摆错的拖入O。
    CreatTitlesUnit6.SolidFigture().CombinationLoationSelectMid(
        url_name1='know-cube-drag3_1-6', url_name2='1-6-7-03', json_path='./data/title_json/',
        creat_json=creat_json, json_name='摆对的拖入√，摆错的拖入O'
    )


    #todo 1-6-7-04 连一连，找出相同积木搭起来的图形。
    CreatTitlesUnit6.SolidFigture().SplitFindCombineSelectMid(
        url_name1='know-cube-connect3_1-6', url_name2='1-6-7-04', json_path='./data/title_json/',
        creat_json=creat_json, json_name='连一连，找出相同积木搭起来的图形'
    )

    # todo 1-6-7-05 连一连，找出相同积木搭起来的图形。
    CreatTitlesUnit6.SolidFigture().BrickConstractSelectMid(
        url_name1='know-cube-connect3_1-6', url_name2='1-6-7-05', json_path='./data/title_json/',
        creat_json=creat_json, json_name='连一连，找出相同积木搭起来的图形'
    )

    # todo 1-6-7-06 那两堆可以拼成下面的图形？用线连起来。
    CreatTitlesUnit6.SolidFigture().PatchPictureSelectMid(
        url_name1='know-cube-connect4_1-6', url_name2='1-6-7-06', json_path='./data/title_json/',
        creat_json=creat_json, json_name='那两堆可以拼成下面的图形？用线连起来'
    )


    #todo 1-6-7-07  下面图形中分别有几个小正方形？
    CreatTitlesUnit6.SolidFigture().CalculationCubeMid(
        url_name1='know-cube-input4_1-6', url_name2='1-6-7-07', json_path='./data/title_json/',
        creat_json=creat_json, json_name='下面图形中分别有几个小正方形'
    )


    #todo 1-6-7-08  下面的大长方体是几个相同的小长方体组成吗?
    CreatTitlesUnit6.SolidFigture().ConstituteCuboidMid(
        url_name1='know-cube-input4_1-6', url_name2='1-6-7-08', json_path='./data/title_json/',
        creat_json=creat_json, json_name='下面的大长方体是几个相同的小长方体组成吗'
    )

    # todo 1-6-7-09 摆成一个长方体，最少要用多少个相同的正方体？
    CreatTitlesUnit6.SolidFigture().ConstituteCuboid2Mid(
        url_name1='know-cube-input5_1-6', url_name2='1-6-7-09', json_path='./data/title_json/',
        creat_json=creat_json, json_name='摆成一个长方体，最少要用多少个相同的正方体'
    )

    # todo 1-6-7-10 小亮和小红用正方体分别搭了一个立体图形，小亮给小红几块积木，两个人就一样多了
    CreatTitlesUnit6.SolidFigture().ThanHowMuchMid(
        url_name1='know-cube-input5_1-6', url_name2='1-6-7-10', json_path='./data/title_json/',
        creat_json=creat_json, json_name='小亮和小红用正方体分别搭了一个立体图形，小亮给小红几块积木，两个人就一样多了'
    )

    # todo 1-6-7-11 接着摆什么？选一选。
    CreatTitlesUnit6.SolidFigture().SequencingSelectMid(
        url_name1='know-cube-select3_1-6', url_name2='1-6-7-11', json_path='./data/title_json/',
        creat_json=creat_json, json_name='接着摆什么？选一选'
    )



main()