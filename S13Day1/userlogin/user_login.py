#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: Aiwen
import sys

username = 'liuping'
password = int('0498')

counter = 0
while True:
       user_login = input("Enter Your Name:")
       password_login = int(input("Enter Your Password:"))
       # print(counter)
       with open("user_db",'r') as userdb:
            for userdb_list in userdb.readlines():
                userdb_list = userdb_list.strip().split()
                # print (userdb_list[0])
                if user_login in userdb_list[0]:
                   sys.exit("Sorry Your Name Is Locket~!")
       if counter < 2:
           # print(counter)
           if user_login == username and password_login == password:
              print("Welcome To Our System~!")
              counter = 0
              break
           else:
               print("Sorry Your Username/Password is Worng~!")
               counter +=1
               continue
       else:
           with open("user_db",'a+',) as userlogin_item:
                userlogin_item.writelines(user_login)
                userlogin_item.write("\n")
                userlogin_item.close()
           print("Your Input Too Many times~!")
           break