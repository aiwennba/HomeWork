#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: Aiwen

import time
import sys
import os
import pickle
import json
import getpass

def User_Input_salary():
    '''
    定义一个函数,用于接收用户输入工资金额
    '''
    Flag = False
    while not Flag:
        User_salary = input('请输入您预消费的金额(元):').strip()
        if User_salary.isdigit():
            User_salary=int(User_salary)
            Flag = True
            if User_salary >= 200000:
                print('-'*50)
                print('\033[34;1m继续加油哦~!\033[0m')
                print('-'*50)
        else:
            print('抱歉,您输入的 \033[31;1m%s \033[0m不是一个合法的工资/金额'%User_salary)

    return User_salary

def Deny_user(username):
    '''定义一个写入用户信息到黑名单的函数,在后面的时候调用直接将锁定用户信息写入到锁文件中去'''
    with open('locked.db','a+') as f:
        print('\033[1;31m抱歉,用户 %s 输入次数太多, 已被锁定,请联系管理员解锁!' %username)
        f.write('%s\n' %username)

def loggin_out():
    # user_shopping[user].setdefault(user,User_salary)   #退出之前将用户名和用于余额信息写入字典用于下一次登录判断
    user_shopping[user].setdefault('salary', User_salary)
    with open(user_shopping_db, 'wb') as f:
         pickle.dump(user_shopping, f)

def digit_input(num):
    if str.isdigit(num):   # 对输入是否是数字进行判断
       num = int(num)      # 如果输出的是个数字，则转化为整数类型
    return (num)           # 返回输入字符



#定义一个字典,用于下面验证用户身份,账户名密码通过key:value的形式存储在字典中
user_list = {
    'test1':'123456',
    'test2':'123456',
    'test3':'123456',
}






def username():
    '''
    定义一个函数,用于接收用户输入用户名密码的验证
    如果用户名在锁定文件locked.db中,直接返回给用户已被锁定,退出程序
    判断用户输入是否是同一用户输入三次错误尝试,如果是,则锁定用户,否则三次之后退出程序;
    '''
    Flag = False
    Count = 0
    Lock_count = 1
    user_name = ''
    while Count < 3:
        User_input_name = input('请输入您的用户名: ').strip()
        if User_input_name:
            User_input_name = str(User_input_name)
            User_input_pass = input( '请输入您的密码: ').strip()
            with open('locked.db','r') as f:
                for i in f:
                    if User_input_name == i.strip():
                        print('\033[31;1m您的用户已经被锁定,请联系管理员解锁!\033[0m')
                        exit(0)
            if User_input_name == user_name:
                Lock_count += 1
            else:
                user_name = User_input_name
                Lock_count -= 1
            for user,passwd in user_list.items():
                if User_input_name == user and User_input_pass == passwd: #判断用户名和密码认证是否成功
                    print('\033[32;1m欢迎登陆 %s\033[0m'.center(50,'#') %User_input_name)
                    Flag = True
                    break
                if Flag:
                    break
            else:
                print('用户名或密码不正确,请重新输入')
                #print(User_input_name)
                #print(User_input_pass)

                Count += 1
                ##if User_input_name
        if Flag:
            break
    else:
        if Lock_count == 2:
            Deny_user(User_input_name)
        exit(0)
    #user_info.remove(User_input_name)
    #if len(data) != 0:
        #del user_info[User_input_name]
        #return User_input_name,user_info,User_salary
    #else:
        #return User_input_name
    return User_input_name


# 余额充值函#
def balance_recharge():
    recharge_flag = 1  # 充值循环参数###
    while recharge_flag:
        recharge_num = input('请输入充值金额 | 返回(b) | 退出(q):')
        if len(recharge_num) != 0:  # 如果输入非空，对输入进行判断并转化类型
           recharge_num = digit_input(recharge_num)
        if recharge_num == 'q':  # 如果输入为q,则退出程序
           sys.exit()
        elif recharge_num == 'b':  # 如果输入为b,则返回第一层循环，重新选择商品编号
             if len(recharge_num) == 0:
                 pass
             else:
               recharge_num = int(0)
               break
             break
        elif type(recharge_num) is int and recharge_num > 0:  # 输入要求充值金额
            recharge_flag = 0  # 改变充值循环参数
            print('充值成功，请查收'.center(80, ' '))  # 提示充值成功
        else:
            print('请输入正确的金额~!')
    return (recharge_num)

##定义商品列表
commodity_list = {
    "phone_list":
        {'Apple': 5000,
         'Xiaomi': 1000,
         'Sumsung': 4000,
         'Huawei': 10000,
         'Blackberry': 500},

    "close_list":
        {'duanxiu': 5000,
         'shirt': 100,
         'duanku': 4000,
         'changku': 10000,
         'waitao': 500},

    "car_list":
        {'Mercedes-Benz': 500000,
         'BMW X5': 1000000,
         'Tuguan': 400000,
         "Buick": 100000,
         "Chevrolet": 500000},

    "other_list":
        {'Apple': 5000,
         'Book': 100,
         'Bike': 4000,
         'Computer': 10000,
         'Coffer': 500}
}

user_shopping_db = 'user_shopping.db'
shopp_car = '{0}    {1}         {2}     {3}     {4}'
#user_file = open(user_shopping_db,'rb')
data = open(user_shopping_db,'rb').read()
if len(data) != 0:
    user_data = len(pickle.load(open(user_shopping_db,'rb')))
    user_info = pickle.load(open(user_shopping_db,'rb'))
else:
    user_data = 0

user_shopping = {}  #定义一个空字典,用于存储用户的购物车信息
Flag = False        #定义标志位,用于进入循环
User_flag = False   #定义一个用户标志位,用于判断用户是否有认证,防止后面循环会要求用户反复认证


while not Flag:     #进入循环主题
    if not User_flag:   #根据定义用户标志位来判断
        user = username()   #将上面定义函数实例化,并赋值给user变量
        if user_data != 0:  #判断变量非空进入下面验证,取出用户上一次登录程序
            for i in user_info.keys():
                if user == i:
                    id = 1
                    for k,v in user_info.items():
                        if user == k:
                            #shopp_car = '{0}    {1}         {2}     {3}     {4}'
                            print('\033[32;1m欢迎您, %s, 您上一次的余额为 %s\033[0m'%(k,user_info[user]['salary']))
                            print('购物车的内容如下'.center(70,'-'))
                            print('\033[34;1m|序列   |    物品名      |      数量   |   小计   |   购买时间|\033[0m') #先打印title
                            User_salary = user_info[user]['salary']
                            del user_info[user]['salary']

                        for k1,v1 in user_info[user].items():
                            if user != k1:
                                print('|','-'*70,'|')
                                print(shopp_car.format(id,k1,v1[0],v1[1],v1[2]))
                                id +=1
                                #continue
                        else:
                            print('-'*70)
                    #if input('按下任意键继续...'):pass
                    #del user_info[user]
                    user_shopping = user_info
                else:
                    User_salary = User_Input_salary()
                    pass
        else:
            User_salary = User_Input_salary()   #实例化用户输入消费金额函数并复制给变量

        print(' 欢迎 [ %s ] 来到购物商店,请选择您需要的物品以及数量'.center(70,'#')%user)

    for id,keys in enumerate(commodity_list.keys()):  #进入三级菜单
        print('|','-'*20,'|')
        print(id,keys)
    User_id = input('\033[33;1m请选择您的分类  Q/q(退出程序) C/c(检查购物车) R/r(金额充值):\033[0m').strip()
    if User_id == 'q' or User_id == 'Q':  #判断是Q/q,退出程序
        # user_shopping[user].setdefault('salary',User_salary)
        loggin_out()
        print('欢迎下次再来 [ %s ], bye!'%user)
        Flag = True
        break
    if User_id == 'c' or User_id == 'C':  #如果是c/C,检查用户购物车,如果购物车为空,提示用户为空
        if len(user_shopping) != 0:  #判断如果用户购物车不为空是显示购物车信息
            print('购物车'.center(70))
            print('-'*70)
            print('\033[34;1m|序列   |    物品名      |      数量   |   小计   |   购买时间|\033[0m') #先打印title
            product_index = 1 #定义一个序列ID
            user_consume = 0 #定义一个值为0的用户消费金额初始值,用于下面累加用户此次消费总金额
            #print(user_shopping)
            for value in user_shopping[user].keys():
                #print(value)
                #print(shopp_car.format(product_index,index,value[1][0],value[0][1],value[0][2],))
                print(shopp_car.format(product_index,value,user_shopping[user][value][0],user_shopping[user][value][1],user_shopping[user][value][2],))
                user_consume += user_shopping[user][value][1] #自增用户消费金额
                product_index += 1 #序列ID自增
                print('-'*70)
            print('-'*70)
            print('\033[34;1m尊敬的用户[ %s ], 共消费 [ %s ]元, 您的余额 [ %s ]元\033[0m'%(user,user_consume,User_salary))

            if input('\033[31;1m 按下任意键继续...\033[0m'):pass
        else: #如果购物车为空,提示用户购物车为空,并返回商品列表
            print('-'*50)
            print('抱歉,你还未购买任何物品~')
            print('-'*50)
    if User_id == 'R' or User_id == 'r':
       User_salary += balance_recharge()
       # loggin_out()

    if User_id.isdigit() and int(User_id) < len(commodity_list.keys()):
        product = list(commodity_list.keys())[int(User_id)]  #将字典转换为有序列表
        while not Flag:
            for id2,key2 in enumerate(commodity_list[product].items()):  #进入商品明细,供用户选择序号购买
                print('|', '-'*30, '|')
                print(id2,key2)
            print('#'*70)
            User_id2 = input('\033[33;1m请选择您需要的物品序列添加到购物车:  Q/q(退出程序) B/b(返回) C/c(检查购物车)\033[0m'.center(30,'#')).strip()
            if User_id2.isdigit() and int(User_id2) < len(commodity_list[product]):
                #print(commodity_list[product][int(User_id2)])
                product1 = list(commodity_list[product].keys())[int(User_id2)]
                price = int(commodity_list[product][product1])
                print('您已经选择了物品\033[32;1m %s \033[0m, 宝贝价格(元):\033[32;1m %s \033[0m'%(product1,price))
                product_num = input('请输入你购买的物品\033[32;1m %s \033[0m数量:'%product1).strip()
                if product_num.isdigit() and product_num and int(product_num) != 0:
                    product_num = int(product_num)
                    price *= product_num
                    if price <= User_salary:
                        User_salary -= price
                        product_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())  #返回当前购买时间给一个变量
                        #if product1 not in user_shopping.get(user): #判断如果用户购买的商品不在购物车中直接setdefault值为新商品信息
                        if not user_shopping.get(user):
                            #user_shopping[user]=
                            #user_shopping[user] = [{product1,[product_num,price,product_time,]}]
                            user_shopping[user] = {product1:[product_num,price,product_time,]}

                        else:  #如果存在购物车中,更新现有信息
                            #print(user_shopping[user][product1][0][0])
                            user_shopping[user].setdefault(product1,[product_num,price,product_time,])
                            # print(user_shopping)
                            product_num += user_shopping[user][product1][0] #累加商品数量
                            print(user_shopping[user][product1][0])
                            price += user_shopping[user][product1][1]  #累加商品金额
                            user_shopping[user][product1][0] = product_num  #重新修改购物车中的值
                            user_shopping[user][product1][1] = price
                            user_shopping[user][product1][2] = product_time
                        #user_shopping[product_id] = [product1,product_num,price,product_time]
                        #打印购买成功信息,包括用户购买商品\金额以及余额
                        print('恭喜你,成功购买物品\033[32;1m %s \033[0m数量\033[32;1m %s \033[0m,' \
                              '此次消费\033[32;1m %s (元) \033[0m, 余额:\033[32;1m %s \033[0m' \
                              %(product1,product_num,price,User_salary))
                        print('#'*70)
                        continue
                    else: #输入用户余额不足,提示用户充值
                        pay = input('\033[31;1m抱歉,您的余额[ %s ],宝贝价格[ %s ],余额不足,不能购买此物品,是否充值? (y/Y)\033[0m'%(User_salary,price)).strip()
                        if pay and pay == 'y' or pay == 'Y':  #输入y/Y为确认充值
                            pay_money = input('请输入要充值的金额:').strip()  #充值金额
                            if pay_money.isdigit() and int(pay_money) != 0: #如果是数字而且充值金额不能为0
                                User_salary += int(pay_money)  #用户余额+=新充值金额,并赋值给余额变量
                                time.sleep(1)
                                print('-'*50)
                                print('充值成功,账户最新余额:\033[31;1m [ %s ] 元\033[0m'%User_salary) #打印充值成功
                                if User_salary >= 200000:  #如果用户充值金额大于等于20W
                                    print('\033[34;1m不错继续加油~!\033[0m')
                                print('-'*50)
                                if input('按下任意键继续...'):pass
                                continue
                            else:  #如果输入一个非y/Y值,提示用户没有选择充值,而后进入商品详单列表
                                print('抱歉,您没有选择充值')
                                continue
                else:
                    #print('\033[31;1m输入数量不可用!\033[0m')
                    if input('\033[31;1m抱歉,您输入数量的不可用!按下任意键继续...\033[0m'):pass
                    continue
            if User_id2 == 'q' or User_id2 == 'Q': #输入Q/q,退出程式
                #user_shopping[user].setdefault(user,User_salary)   #退出之前将用户名和用于余额信息写入字典用于下一次登录判断
                # user_shopping[user].setdefault('salary',User_salary)
                # with open(user_shopping_db,'wb') as f:
                #     pickle.dump(user_shopping,f)
                loggin_out()
                print('欢迎下次再来 [ %s ], bye!'%user)
                time.sleep(1)
                Flag = True
                break
            if User_id2 == 'c' or User_id2 == 'C': #允许用户输入c/C查看购物车信息
                print('购物车'.center(70))
                print('-'*70)

                print('\033[34;1m|序列   |    物品名      |      数量   |   小计   |   购买时间|\033[0m') #先打印title
                print('*'*70)
                product_index = 1 #定义一个序列ID
                user_consume = 0 #定义一个值为0的用户消费金额初始值,用于下面累加用户此次消费总金额
                #print(user_shopping)
                for value in user_shopping[user].keys():
                    #print(value)
                    #print(shopp_car.format(product_index,index,value[1][0],value[0][1],value[0][2],))
                    print(shopp_car.format(product_index,value,user_shopping[user][value][0],user_shopping[user][value][1],user_shopping[user][value][2],))
                    user_consume += user_shopping[user][value][1] #自增用户消费金额
                    product_index += 1 #序列ID自增
                print('-'*70)
                print('\033[34;1m尊敬的用户[ %s ], 共消费 [ %s ]元, 您的余额 [ %s ]元\033[0m'%(user,user_consume,User_salary))

                if input('\033[32;1m 按下任意键继续...\033[0m'):pass
            if User_id2 == 'b' or User_id2 == 'B':  #输入b/B,返回上一级
                User_flag = True
                break
            else:
                #print('\033[31;1m您输入的物品序列不可用!!!\033[0m')
                print('\033[31;1m您输入的物品序列不可用!!!\033[0m')
                continue

                #pass
                #print(product1)
                #print(price)
    else:
        if not User_id:
            print('\033[31;1m您输入的物品序列不可用!!!\033[0m')
            User_flag = True
            continue
        else:
            User_flag = True