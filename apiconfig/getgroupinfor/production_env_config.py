# -*- coding: utf-8 -*-
from  api_class import  *

App_a = {"app_id": "203228",
         "app_secret": "fbe54068c5eafd5262ff169a1682cca2",
         "grant_type": "client_credentials",
         "accounts":
             {"account_01": {"id": "TEST_testAccount11",
                             "nickName": "Iam_login_05",
                             "user_avatar": "http://cn.file.chatgame.me/api/file/download/2016/7/26/2/b999baff-45b4-4147-957e-8c05d2c55b16.jpg"
                             },
              "account_02": {"id": "TEST_testAccount222",
                             "nickName": "Iam_login_03",
                             "user_avatar": "http://cn.file.chatgame.me/api/file/download/2016/7/26/2/5c3d14cc-9fc0-40d5-8b04-9b02ca69f5ff.jpg"
                             },
              "account_03": {"id": "TEST_testAccount333",
                             "nickName": "Iam_login_33",
                             }
              },
         "groups":
             {"group_01": {"members": "TEST_testAccount222" + "," + "TEST_testAccount333",
                           "creator": "TEST_testAccount111",
                           "group_name": "test_groupName",
                           "group_desc": "test_groupDesc",
                           "group_avatar": "http://new.image.chatgame.me/api/file/avatar/2015/11/24/8/9d6463ab-4083-4b01-a416-65e4e382ad00",
                           "group_id": "80233c8073d511e69ce5fb907fee57ba",
                           "group_id_1": "",
                           "group_id_2": "39cbc09065b111e6bba7fb907fee57ab",
                           "group_detail":1,
                           }
              },
         "correct_err_code": 2000,
         "miss_error_code" :4001,
         "nologin_error_code": 401,
         "notexist_error_code":4019
         }
CoreServer_url  = "https://cloudus.v5.cn"

####获取群组信息——缺少参数#####
####将groupId设置成为一个空值####
#********** TESTCASE **********
CoreServer_GetGroupInforTest_01  = GetGroupInforTest()
#input
CoreServer_GetGroupInforTest_01.url = CoreServer_url + "/open/api/group/get?"
CoreServer_GetGroupInforTest_01.groupInfo = App_a["groups"]["group_01"]
CoreServer_GetGroupInforTest_01.detail = 1

#expect
CoreServer_GetGroupInforTest_01.miss_error_code = App_a["miss_error_code"]

####获取群组信息——账户未登录#####
####这个方法里 把token都设置成为空值，进而获取不到sessionID从而模拟未登录的情况######
#********** TESTCASE **********
CoreServer_GetGroupInforTest_02  = GetGroupInforTestB()
#input
CoreServer_GetGroupInforTest_02.url = CoreServer_url + "/open/api/group/get?"
CoreServer_GetGroupInforTest_02.groupInfo = App_a["groups"]["group_01"]
CoreServer_GetGroupInforTest_02.detail = 1

#expect
CoreServer_GetGroupInforTest_02.nologin_error_code = App_a["nologin_error_code"]

####获取群组信息——群组不存在##############################################
####给groupId传一个错误的值
#********** TESTCASE **********
CoreServer_GetGroupInforTest_03 = GetGroupInforTestC()
#input
CoreServer_GetGroupInforTest_03.url = CoreServer_url + "/open/api/group/get?"
CoreServer_GetGroupInforTest_03.groupInfo = App_a["groups"]["group_01"]
CoreServer_GetGroupInforTest_03.detail = 1
#expect
CoreServer_GetGroupInforTest_03.notexist_error_code = App_a["notexist_error_code"]
