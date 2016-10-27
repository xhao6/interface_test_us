# -*- coding: utf-8 -*-
from ApiClass import *

App_a = {
         "groups":
             {"group_01": {"members": "TEST_testAccount222" + "," + "TEST_testAccount333",
                           "creator": "TEST_testAccount111",
                           "group_name": "test_groupName",
                           "group_desc": "test_groupDesc",
                           "group_avatar": "http://new.image.chatgame.me/api/file/avatar/2015/11/24/8/9d6463ab-4083-4b01-a416-65e4e382ad00",
                           "group_id": "init",
                           "group_id1": "819bd16064f011e6bba7fb907fee57mm",
                           }
              },
         "correct_err_code1": 401,
         "correct_err_code2": 4019,
         "correct_err_code3": 4001
         }

CoreServer_url  = "https://cloudus.v5.cn"

############################解散群组——账号未登录#########################
##########modules里迅增一个方法——token为空，session随意赋一个值##########
#********** TESTCASE **********
CoreServer_DissolveGroupTest_01                 = DissolveGroupTest()
# input
CoreServer_DissolveGroupTest_01.url             = CoreServer_url + "/open/api/group/exit"
CoreServer_DissolveGroupTest_01.groupInfo         = App_a["groups"]["group_01"]

# expect
CoreServer_DissolveGroupTest_01.error_code            = App_a["correct_err_code1"]

##########解散群组——群组不存在##########
############传一个错的group_id1###########
#********** TESTCASE **********
CoreServer_DissolveGroupTest_02                 = DissolveGroupTest()
# input
CoreServer_DissolveGroupTest_02.url             = CoreServer_url + "/open/api/group/exit"
CoreServer_DissolveGroupTest_02.groupInfo         = App_a["groups"]["group_01"]

# expect
CoreServer_DissolveGroupTest_02.error_code            = App_a["correct_err_code2"]

##########解散群组——缺少参数# ##########
###############不传groupId# ##############
#********** TESTCASE **********
CoreServer_DissolveGroupTest_03                 = DissolveGroupTest()
# input
CoreServer_DissolveGroupTest_03.url             = CoreServer_url + "/open/api/group/exit"
#CoreServer_DissolveGroupTest_03.groupId         = ""

# expect
CoreServer_DissolveGroupTest_03.error_code            = App_a["correct_err_code3"]

