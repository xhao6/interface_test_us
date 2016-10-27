# -*- coding: utf-8 -*-
from ApiClass import *

App_a = {"accounts":
                     {"account_01": {"id": "TEST_testAccount111",
                                     "id1": "gggggg",
                                     "nickName": "Iam_login_05",
                                     "user_avatar": "http://cn.file.chatgame.me/api/file/download/2016/7/26/2/b999baff-45b4-4147-957e-8c05d2c55b16.jpg"
                                     },
                      },
         "groups":
             {"group_01": {"members": "TEST_testAccount222" + "," + "TEST_testAccount333",
                           "creator": "TEST_testAccount111",
                           "group_name": "test_groupName",
                           "group_desc": "test_groupDesc",
                           "group_avatar": "http://new.image.chatgame.me/api/file/avatar/2015/11/24/8/9d6463ab-4083-4b01-a416-65e4e382ad00",
                           "group_id": "80233c8073d511e69ce5fb907fee57ba",
                           "group_id1": "None",
                           "group_id2": "ffefd9d0701211e69ce5fb907fee57ba",
                           },
              },
         "correct_err_code1": 401,
         "correct_err_code2": 4019,
         "correct_err_code3": 4001,
         "correct_err_code4": 4042,
         }

CoreServer_url  = "https://cloudus.v5.cn"

#######################加入群组——账号未登录##############################
##########modules里迅增一个方法——token为空，session随意赋一个值##########
#********** TESTCASE **********
CoreServer_JoinGroupTest_01                 =JoinGroupTest()

# input
CoreServer_JoinGroupTest_01.url             = CoreServer_url + "/open/api/group/join"
CoreServer_JoinGroupTest_01.groupInfo         = App_a["groups"]["group_01"]
CoreServer_JoinGroupTest_01.members_user_id = App_a["accounts"]["account_01"]["id"]

# expect
CoreServer_JoinGroupTest_01.error_code            = App_a["correct_err_code1"]

##########加入群组——群组不存在###########
##########传一个错的群组group_id1##########
#********** TESTCASE **********
CoreServer_JoinGroupTest_02                 =JoinGroupTest()

# input
CoreServer_JoinGroupTest_02.url             = CoreServer_url + "/open/api/group/join"
CoreServer_JoinGroupTest_02.groupInfo         = App_a["groups"]["group_01"]
CoreServer_JoinGroupTest_02.members_user_id = App_a["accounts"]["account_01"]["id"]

# expect
CoreServer_JoinGroupTest_02.error_code            =  App_a["correct_err_code2"]
CoreServer_JoinGroupTest_02.join_members_user_id  = App_a["accounts"]["account_01"]["id"]

#############加入群组——非法参数############
##########加入群组的id传一个错的id1##########
#********** TESTCASE **********
CoreServer_JoinGroupTest_03                 =JoinGroupTest()

# input
CoreServer_JoinGroupTest_03.url             = CoreServer_url + "/open/api/group/join"
CoreServer_JoinGroupTest_03.groupInfo         = App_a["groups"]["group_01"]
CoreServer_JoinGroupTest_03.members_user_id = App_a["accounts"]["account_01"]["id1"]

# expect
CoreServer_JoinGroupTest_03.error_code            = App_a["correct_err_code3"]

##################加入群组——群组人数超限##############
##########modules里新增一个方法，加一个for循环##########
#********** TESTCASE **********
CoreServer_JoinGroupTest_04                 =JoinGroupTest()

# input
CoreServer_JoinGroupTest_04.url             = CoreServer_url + "/open/api/group/join"
CoreServer_JoinGroupTest_04.groupInfo         = App_a["groups"]["group_01"]#2
#CoreServer_JoinGroupTest_04.members_user_id = "402946405aeb11e6afa2819403d79ace"

# expect
CoreServer_JoinGroupTest_04.error_code            = App_a["correct_err_code4"]



