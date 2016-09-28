#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: Aiwen

city_dict = {
    "北京市": {"北京": ["东城区", "西城区", "崇文区", "宣武区", "朝阳区", "海淀区",
                   "丰台区", "石景山区", "房山区", "通州区", "顺义区", "昌平区", "大兴区", "怀柔区",
                   "平谷区", "门头沟区", "密云县", "延庆县", "其他"]},
    "上海市": {"上海": ["浦东新区", "徐汇区", "长宁区", "普陀区", "闸北区", "虹口区", "杨浦区", "黄浦区", "南市区", "卢湾区",
                   "静安区", "宝山区", "闵行区", "嘉定区", "南汇县", "奉贤县", "松江县", "金山县", "青浦县", "崇明县"]},
    "江苏省": {"南京": ["玄武区", "秦淮区", "鼓楼区", "建邺区", "雨花台区", "栖霞区", "浦口区",
                   "六合区", "江宁区", "溧水区", "高淳区"],
            "苏州": ["姑苏区", "园区", "吴中区", "相城区", "吴江区", "常熟市", "昆山市", "张家港市", "太仓市"]},
    "浙江省": {"杭州": ["上城区", "下城区", "江干区", "拱墅区", "西湖区", "滨江区", "萧山区", "余杭区", "富阳区",
                   "桐庐县", "淳安县", "建德市", "临安市"]}
}
dict_key = {}


def search_menu():
    print('+++++++Sarching-City-Menu-System-*Level-One*+++++++')
    for city_index, city_key in enumerate(city_dict.keys(), 1):
        print(city_index, city_key)
        dict_key[str(city_index)]=city_key
    select = input("Input Num Display Menu:1！Input Quit:q ,Input Back:b :")
    if select == 'q':
        quit()
    elif select == 'b':
        print("Is Level One Menu，Can't ！Plase Try Again ！")
        return
    elif dict_key.get(select, 0):
        search_menu_1(dict_key[select])
    else:
        print('')
        print('Your Input ERROR，Please Try Aagin！')


def search_menu_1(select1):
    while True:
        print('')
        print('+++++++Sarching-City-Menu-System-*Level-Two*+++++++')
        for city_index, city_key in enumerate(city_dict[select1].keys(), 1):
            print(city_index, city_key)
            dict_key[str(city_index)] = city_key
        select2 = input("Input Num Display Menu:1！Input Quit:q ,Input Back:b :")
        if select2 == 'q':
            quit()
        elif select2 == 'b':
            search_menu()
        elif dict_key.get(select2, 0):
            search_menu_2(select1, dict_key[select2])
        else:
            print('')
            print('Your Input ERROR，Please Try Aagin！')


def search_menu_2(select1, select2):
    while True:
        print('')
        print('+++++++Sarching-City-Menu-System-*Level-Three*+++++++')
        for city_index, city_key in enumerate(city_dict[select1][select2], 1):
            print(city_index, city_key)
            dict_key[str(city_index)] = city_key
        select3 = input("Input Num Display Menu:1！Input Quit:q ,Input Back:b :")
        if select3 == 'q':
            quit()
        elif select3 == 'b':
            search_menu_1(select1)
        else:
            print('')
            print('Your Input ERROR，Please Try Aagin！')


search_menu()
