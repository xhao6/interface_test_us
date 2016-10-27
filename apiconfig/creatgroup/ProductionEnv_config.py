# -*- coding: utf-8 -*-
from ApiClass import *

# xuchaoxuan version 2.0
# yanglei    version 1.0  2.1

App_a = {
         "groups":
             {"group_01": {"members": "TEST_testAccount222" + "," + "TEST_testAccount333",
                            "members111": "",
                            "group_name": "test_groupName",
                            "group_desc": "test_groupDesc",
                            "group_id":"init",
                           }
             },
         "correct_err_code": 2000,
         "correct_err1_code": 4001,
         "correct_err2_code": 401,
         "correct_err3_code": 4042,
        }
CoreServer_url  = "https://cloudus.v5.cn"

##########创建群组##########
#********** TESTCASE 缺少参数**********
#场景：传错menbers_user_id或者menbers_user_id为空
CoreServer_CreatGroupTest1_02                    = CreatGroupTest1()
# input
CoreServer_CreatGroupTest1_02.url                = CoreServer_url + "/open/api/group/create"
CoreServer_CreatGroupTest1_02.groupInfo          = App_a["groups"]["group_01"]
# CoreServer_CreatGroupTest1_02.members_user_id    =App_a["groups"]["group_01"]["members111"]
# CoreServer_CreatGroupTest1_02.name               = App_a["groups"]["group_01"]["group_name"]
# CoreServer_CreatGroupTest1_02.desc               = App_a["groups"]["group_01"]["group_desc"]

# expect
CoreServer_CreatGroupTest1_02.error_code            = App_a["correct_err1_code"]

##########创建群组##########
#********** TESTCASE 账户未登录**********
#场景：token，sessionid传空
CoreServer_CreatGroupTest2_02                    = CreatGroupTest1()
# input
CoreServer_CreatGroupTest2_02.url                = CoreServer_url + "/open/api/group/create"
CoreServer_CreatGroupTest2_02.groupInfo         = App_a["groups"]["group_01"]

# expect
CoreServer_CreatGroupTest2_02.error_code            = App_a["correct_err2_code"]

##########创建群组##########
#********** TESTCASE 群成员超过限制**********
#场景：加入多个不同联系人
CoreServer_CreatGroupTest3_02                    = CreatGroupTest1()
# input
CoreServer_CreatGroupTest3_02.url                = CoreServer_url + "/open/api/group/create"
CoreServer_CreatGroupTest3_02.groupInfo   =App_a["groups"]["group_01"]
#

# expect
CoreServer_CreatGroupTest3_02.error_code            = App_a["correct_err3_code"]
