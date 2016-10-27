# -*- coding: utf-8 -*-
from  api_class import  *

App_a = {"app_id": "203228",
         "app_secret": "fbe54068c5eafd5262ff169a1682cca2",
         "grant_type": "client_credentials",
         "accounts":
             {"account_01": {"id": "TEST_testAccount111",
                             "nickName": "Iam_login_05",
                             "user_avatar": "http://cn.file.chatgame.me/api/file/download/2016/7/26/2/b999baff-45b4-4147-957e-8c05d2c55b16.jpg"
                             },
              "account_02": {"id": "TEST_testAccount222",
                             "nickName": "Iam_login_03",
                             "user_avatar": "http://cn.file.chatgame.me/api/file/download/2016/7/26/2/5c3d14cc-9fc0-40d5-8b04-9b02ca69f5ff.jpg"
                             },
              "account_03": {"id": "TEST_testAccount333",
                             "nickName": "Iam_login_33",
                             },
              "account_04": { "id":"",
                             }
              },
         "groups":
             {"group_01": {"members": "TEST_testAccount222" + "," + "TEST_testAccount333",
                           "creator": "TEST_testAccount111",
                           "group_name": "test_groupName",
                           "group_desc": "test_groupDesc",
                           "group_avatar": "http://new.image.chatgame.me/api/file/avatar/2015/11/24/8/9d6463ab-4083-4b01-a416-65e4e382ad00.jpg",
                           "group_id": "80233c8073d511e69ce5fb907fee57ba",
                           "group_id_1": "",
                           "group_id_2": "39cbc09065b111e6bba7fb907fee57ab",
                           }
              },
         "correct_err_code": 2000,
         "miss_error_code" : 4001,
         "nologin_error_code": 401,
         "notexist_error_code":4019,

         }
CoreServer_url  = "https://cloudus.v5.cn"

####移除群成员——群组不存在#####
######传给一个错误的值给groupId########
#********** TESTCASE **********
CoreServer_RemoveGroupMemberTest_01 = RemoveGroupMemberTest()

#input
CoreServer_RemoveGroupMemberTest_01.url = CoreServer_url + "/open/api/group/remove"
CoreServer_RemoveGroupMemberTest_01.groupInfo = App_a["groups"]["group_01"]
CoreServer_RemoveGroupMemberTest_01.member_v5_id = App_a["accounts"]["account_03"]["id"]
#expect
CoreServer_RemoveGroupMemberTest_01.noexist_error_code = App_a["notexist_error_code"]

####移除群成员——缺少参数#####
########请求参数中，不传groupId######
#********** TESTCASE **********
CoreServer_RemoveGroupMemberTest_02 = RemoveGroupMemberTestB()

#input
CoreServer_RemoveGroupMemberTest_02.url = CoreServer_url + "/open/api/group/remove"
# CoreServer_RemoveGroupMemberTest_02.group_id = App_a["groups"]["group_01"]["group_id"]
CoreServer_RemoveGroupMemberTest_02.member_v5_id = App_a["accounts"]["account_04"]["id"]
#expect
CoreServer_RemoveGroupMemberTest_02.miss_error_code = App_a["miss_error_code"]

####移除群成员——账号未登录#####
####这个方法里 把token都设置成为空值，进而获取不到sessionID从而模拟未登录的情况######
#********** TESTCASE **********
CoreServer_RemoveGroupMemberTest_03 = RemoveGroupMemberTestC()

#input
CoreServer_RemoveGroupMemberTest_03.url = CoreServer_url + "/open/api/group/remove"
CoreServer_RemoveGroupMemberTest_03.groupInfo= App_a["groups"]["group_01"]
CoreServer_RemoveGroupMemberTest_03.member_v5_id = App_a["accounts"]["account_04"]["id"]
#expect
CoreServer_RemoveGroupMemberTest_03.nologin_error_code = App_a["nologin_error_code"]




