# -*- coding: utf-8 -*-
from ApiClass import *

App_a = {
         "correct_err_code1": 401,
         "messages":
             {"last_message_id": 6167584608000294912,
              "messages_id": "6166846405551210496",
              "messages_type": "SYSTEM_NOTIFY",
              "messages_create_time": "1470290757551",
              "messages_sender": "643a2d6059f611e6afa2819403d79ace",
              "messages_conversation_id": "defaultGroupName：Iam_login_03 invites  to join the group chat",
              "messages_meta_push_content": "Iam_login_05",
              "messages_meta_cmsgid": "826a30ce-1cc6-4c8b-a243-61f944e173e6",
              "messages_receiver": "b3d590c0595c11e6afa2819403d79ace"
              }
         }

CoreServer_url  = "https://cloudus.v5.cn"


########################拉取用户的离线消息——账号未登录###################
##########modules里迅增一个方法——token为空，session随意赋一个值##########
#********** TESTCASE **********
CoreServer_GetOfflineMessagesTest_01                 = GetOfflineMessagesTest()
# input
CoreServer_GetOfflineMessagesTest_01.url                = CoreServer_url + "/api/user/message/msg_snap?"
CoreServer_GetOfflineMessagesTest_01.last_message_id    = App_a["messages"]["last_message_id"]
CoreServer_GetOfflineMessagesTest_01.length             = "1"

# expect
CoreServer_GetOfflineMessagesTest_01.error_code                  = App_a["correct_err_code1"]