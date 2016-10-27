# -*- coding: utf-8 -*-
from ApiClass import *

# xuchaoxuan version 2.0
# yanglei    version 1.0  2.1

App_a = {
         "groups":
             {"group_01": {
                            "group_name": "test_groupName",
                            "group_desc": "test_groupDesc",
                            "group_id": "80233c8073d511e69ce5fb907fee57ba",
                            "group_id1":"",
                            }
             },
         "correct_err_code": 2000,
         "correct_err2_code":4001,
         "correct_err3_code":401,
         "correct_err4_code":4019,
         }
CoreServer_url  = "https://cloudus.v5.cn"

##########更新群组##########
#********** TESTCASE 群组不存在**********
#场景：不传groupid或者groupid传空
CoreServer_UpdateGroupTest_01                = UpdateGroupTest()
#input
CoreServer_UpdateGroupTest_01.url          =CoreServer_url + "/open/api/group/update"
CoreServer_UpdateGroupTest_01.groupInfo     = App_a["groups"]["group_01"]

#expect
CoreServer_UpdateGroupTest_01.error_code   = App_a["correct_err4_code"]


#********** TESTCASE 账户未登录**********
#场景：token，sessionid传空
CoreServer_UpdateGroupTest1_01                = UpdateGroupTest()
#input
CoreServer_UpdateGroupTest1_01.url          =CoreServer_url + "/open/api/group/update"
CoreServer_UpdateGroupTest1_01.groupInfo     =App_a["groups"]["group_01"]


#expect
CoreServer_UpdateGroupTest1_01.error_code   = App_a["correct_err3_code"]

#********** TESTCASE 缺少参数**********
#场景：不传groupid
CoreServer_UpdateGroupTest2_01                = UpdateGroupTest1()
#input
CoreServer_UpdateGroupTest2_01.url          =CoreServer_url + "/open/api/group/update"
CoreServer_UpdateGroupTest2_01.groupInfo    = App_a["groups"]["group_01"]

#expect
CoreServer_UpdateGroupTest2_01.error_code   = App_a["correct_err2_code"]
