# -*- coding: utf-8 -*-
# import unittest
# from lib import actions
import actions

# class test_demo_api():
#     def test_login(self, login_obj):
#         print "Testing logging in. Loading the configurations from login object."
#         res = actions.login(login_obj.url, login_obj.account, login_obj.nickName)
#         print "Verifying the response with the expected output."
#         assert res["error_code"]                == login_obj.err_code
#         assert res["user"]["id"]                == login_obj.user_id
#         assert res["user"]["v5_id"]             == login_obj.user_v5_id     #"%s | %s" % (res["user"]["nickName"], login_obj.user_nickName)
#         assert res["user"]["account"]           == login_obj.user_account
#         assert len(res["user"]["sessionId"])    == 32
#         assert res["user"]["nickName"]          == login_obj.user_nickName #"%s | %s" % (res["user"]["nickName"], login_obj.user_nickName)
#         assert res["user"]["createTimeMillis"] is not None
#         assert res["user"]["avatar"]            == login_obj.user_avatar
#
#     def test_find_account(self, login_obj, find_account_obj):
#         print "Testing finding accounts... Trying to log in first."
#         getSeesion      = actions.login(login_obj.url, login_obj.account, login_obj.nickName)["user"]["sessionId"]
#         print "Login successful. Running the test."
#         res             = actions.findAccount(getSeesion, find_account_obj.url, find_account_obj.account)
#
#         print "Verifying the response with the expected output."
#         assert res["error_code"]            == find_account_obj.err_code
#         assert res["user"]["id"]            == find_account_obj.user_id
#         assert res["user"]["v5_id"]         == find_account_obj.user_v5_id
#         assert res["user"]["account"]       == find_account_obj.user_account
#         assert res["user"]["sessionId"] is None
#         assert res["user"]["nickName"]      == find_account_obj.user_nickName
#         assert res["user"]["createTimeMillis"] is not None
#         assert res["user"]["avatar"]        == find_account_obj.user_avatar
#
#     def test_create_group(self, login_obj, create_group_obj):
#         print "Testing creating a group... Trying to log in first."
#         res_login   = actions.login(login_obj.url, login_obj.account, login_obj.nickName)
#         get_session = res_login["user"]["sessionId"]
#         get_v5_id   = res_login["user"]["v5_id"]
#         print "Login successful. Running the test."
#
#         create_group_obj.result_creator         = get_v5_id
#         create_group_obj.result_member_v5_id    = create_group_obj.result_member_v5_id + "," + get_v5_id
#         create_group_obj.result_member_v5_id    = re.split(',', create_group_obj.result_member_v5_id)
#
#         res         = actions.createGroup(get_session, create_group_obj.url, create_group_obj.members_v5_id)
#         memberNum   = res["result"]["number"]
#
#         res_result_member_v5_id     = []
#         for count in (0, memberNum - 1):
#             res_result_member_v5_id.append(res["result"]["member"][count]["v5_id"])
#
#         for tmp in create_group_obj.result_member_v5_id:
#             if tmp in res_result_member_v5_id:
#                 res_result_member_v5_id.remove(tmp)
#
#         print "Verifying the response with the expected output."
#         assert res["error_code"]            == create_group_obj.err_code
#         assert res["result"]["id"] is not None
#         assert res["result"]["v5_id"] is not None
#         assert res["result"]["number"]      == 3
#         assert res["result"]["creator"]     == create_group_obj.result_creator
#         assert res["result"]["name"]        == create_group_obj.result_name
#         assert res["result"]["createTime"] is not None
#         assert res["result"]["updateTime"] is not None
#         assert res["result"]["desc"]        == create_group_obj.result_desc
#         assert res["result"]["avatar"]      == create_group_obj.result_avatar
#         assert res_result_member_v5_id      == []
#
#     def test_join_group(self, login_obj, join_group_obj):
#         print "Testing inviting people into a group... Trying to log in first."
#         res_login   = actions.login(login_obj.url, login_obj.account, login_obj.nickName)
#         getSeesion  = res_login["user"]["sessionId"]
#         print "Login successful. Running the test."
#
#         res                 = actions.joinGroup(getSeesion, join_group_obj.url, join_group_obj.groupId, join_group_obj.members_v5_id)
#         join_members_num    = len(res["result"]["join_members"])
#
#         print "Verifying the response with the expected output."
#         assert res["error_code"]        == join_group_obj.err_code
#         assert res["result"]["id"]      == join_group_obj.result_id
#         assert res["result"]["v5_id"]   == join_group_obj.result_v5_id
#
#         res_result_member_v5_id             = []
#         if res["result"]["join_members"]    == []:
#             assert res_result_member_v5_id == join_group_obj.join_members_v5_id
#         else:
#             for count in (0, join_members_num - 1):
#                 res_result_member_v5_id.append(res["result"]["join_members"][count]["v5_id"])
#             for tmp in join_group_obj.result_member_v5_id:
#                 if tmp in res_result_member_v5_id:
#                     res_result_member_v5_id.remove(tmp)
#                     assert res_result_member_v5_id == []

class test_core_server():
    def test_get_token_test(self, get_token_obj):
        print "Running test for getting the auth token..."
        res = actions.get_token_test(url=get_token_obj.url,
                                     client_id=get_token_obj.client_id,
                                     client_secret=get_token_obj.client_secret,
                                     grant_type=get_token_obj.grant_type)
        res_access_token    = res["access_token"]
        res_token_type      = res["token_type"]
        res_expires_in      = res["expires_in"]
        res_scope           = res["scope"]
        print "Verifying the response with the expected output."
        assert len(res_access_token)    == 36
        assert res_token_type           == get_token_obj.token_type
        assert res_expires_in is not None
        assert res_scope                == get_token_obj.scope

    def test_get_userId_sessionId_test(self, get_token_obj, get_UserId_SessionId_obj):
        print "Running test for getting user ID and session ID from CG Cloud..."
        token = actions.get_token_test(url=get_token_obj.url,
                                       client_id=get_token_obj.client_id,
                                       client_secret=get_token_obj.client_secret,
                                       grant_type=get_token_obj.grant_type,
                                       ret_type="header")
        res = actions.get_userId_sessionId_test(token, get_UserId_SessionId_obj.url, get_UserId_SessionId_obj.app_user_id,
                                                get_UserId_SessionId_obj.app_user_nick_name)
        print "Verifying the response with the expected output."
        assert res["error_code"]                == get_UserId_SessionId_obj.error_code
        assert res["user"]["id"]                == get_UserId_SessionId_obj.user_id
        assert len(res["user"]["session_id"])  == 32

    def test_get_sessionID_test(self, get_token_obj, get_sessionID_obj):
        print "Running the test for getting session ID..."
        token = actions.get_token_test(url=get_token_obj.url,
                                       client_id=get_token_obj.client_id,
                                       client_secret=get_token_obj.client_secret,
                                       grant_type=get_token_obj.grant_type,
                                       ret_type="header")
        res = actions.get_seesionId_test(token, get_sessionID_obj.url, get_sessionID_obj.app_user_id)
        print "Verifying the response with the expected output."
        #assert res["error_code"]                 == get_sessionID_obj.error_code
        # assert res["user"]["id"]                 == get_sessionID_obj.user_id
        # assert len(res["user"]["session_id"])   == 32



#########################################获取服务器地址----主逻辑####################################################
    def test_get_server_test(self, get_token_obj, get_sessionID_obj, get_server_test_obj):
        print "Testing getting server... Trying to log in first."
        token = actions.get_token_test(url=get_token_obj.url,
                                       client_id=get_token_obj.client_id,
                                       client_secret=get_token_obj.client_secret,
                                       grant_type=get_token_obj.grant_type,
                                       ret_type="header")
        sessionId = actions.get_seesionId_test(token, get_sessionID_obj.url, get_sessionID_obj.app_user_id)["user"]["session_id"]
        res = actions.get_server_test(token, sessionId, get_server_test_obj.url)
        print "Verifying the response with the expected output."
#        assert res["error_code"] == get_server_test_obj.error_code

#########################################获取服务器地址----模拟未登录################################################
    def test_get_server_test1(self, get_token_obj, get_sessionID_obj, get_server_test_obj):
        print "Testing getting server... Trying to log in first.——unauthorized"
        token = {}
        sessionId = "hfhhfhhfhfh"
        res = actions.get_server_test(token, sessionId, get_server_test_obj.url)
        print "Verifying the response with the expected output."
        # assert res["error_code"] == get_server_test_obj.error_code

#########################################更新token----主逻辑#########################################################
    def test_update_token_test(self, get_token_obj, get_sessionID_obj, update_token_test_obj):
        print "Testing updating token... Trying to log in first."
        token = actions.get_token_test(url=get_token_obj.url,
                                       client_id=get_token_obj.client_id,
                                       client_secret=get_token_obj.client_secret,
                                       grant_type=get_token_obj.grant_type,
                                       ret_type="header")
        sessionId = actions.get_seesionId_test(token, get_sessionID_obj.url, get_sessionID_obj.app_user_id)["user"]["session_id"]
        res = actions.update_token_test(token, sessionId, update_token_test_obj.url,
                                        update_token_test_obj.app_id,
                                        update_token_test_obj.device_type,
                                        update_token_test_obj.device_token,
                                        update_token_test_obj.provider)
        print "Verifying the response with the expected output."
#        assert res["error_code"] == update_token_test_obj.error_code

#########################################更新token----模拟未登录#####################################################
    def test_update_token_test1(self, get_token_obj, get_sessionID_obj, update_token_test_obj):
        print "Testing updating token... Trying to log in first.——unauthorized"
        token = {}
        sessionId = "hhfghhfghfghh"
        res = actions.update_token_test(token, sessionId, update_token_test_obj.url,
                                        update_token_test_obj.app_id,
                                        update_token_test_obj.device_type,
                                        update_token_test_obj.device_token,
                                        update_token_test_obj.provider)
        print "Verifying the response with the expected output."
        # assert res["error_code"] == update_token_test_obj.error_code

    def test_get_location_test(self, get_token_obj, get_sessionID_obj, get_location_test_obj):
        print "Testing getting member’s location... Trying to log in first."
        token = actions.get_token_test(url=get_token_obj.url,
                                       client_id=get_token_obj.client_id,
                                       client_secret=get_token_obj.client_secret,
                                       grant_type=get_token_obj.grant_type,
                                       ret_type="header")
        sessionId = actions.get_seesionId_test(token, get_sessionID_obj.url, get_sessionID_obj.app_user_id)["user"][
            "session_id"]
        res = actions.get_location_test(token, sessionId, get_location_test_obj.url)
        print "Verifying the response with the expected output."
#        assert res["error_code"] == get_location_test_obj.error_code


    def test_update_nickname_test(self, get_token_obj, get_sessionID_obj, update_nickname_obj):
        print "Running the test for updating nick name..."
        print "TEST**************************************"
        print update_nickname_obj.app_user_nick_name
        token       = actions.get_token_test(url=get_token_obj.url,
                                             client_id=get_token_obj.client_id,
                                             client_secret=get_token_obj.client_secret,
                                             grant_type=get_token_obj.grant_type,
                                             ret_type="header")
        sessionId   = actions.get_seesionId_test(token, get_sessionID_obj.url, get_sessionID_obj.app_user_id)["user"]["session_id"]
        res = actions.update_nickname_test(token, sessionId, update_nickname_obj.url, update_nickname_obj.app_user_id,
                                           update_nickname_obj.app_user_nick_name)
        print "Verifying the response with the expected output."
        assert res["error_code"] == update_nickname_obj.error_code


    def test_create_group_test(self, get_token_obj, get_sessionID_obj, create_group_test_obj):
        print "Testing creating a group... Trying to log in first."
        token = actions.get_token_test(url=get_token_obj.url,
                                       client_id=get_token_obj.client_id,
                                       client_secret=get_token_obj.client_secret,
                                       grant_type=get_token_obj.grant_type,
                                       ret_type="header")
        sessionId = actions.get_seesionId_test(token, get_sessionID_obj.url, get_sessionID_obj.app_user_id)["user"][
            "session_id"]
        res = actions.create_group_test(token, sessionId, create_group_test_obj.url,
                                        create_group_test_obj.groupInfo["members"],
                                        create_group_test_obj.groupInfo["group_name"],
                                        create_group_test_obj.groupInfo["group_desc"], )
#        assert res["error_code"] == create_group_test_obj.error_code
        return  res
#############创建群组缺少参数######
    def test_create_group_testQ(self, get_token_obj, get_sessionID_obj, create_group_test_obj):
        print "Testing creating a group... Trying to log in first."
        token = actions.get_token_test(url=get_token_obj.url,
                                        client_id=get_token_obj.client_id,
                                        client_secret=get_token_obj.client_secret,
                                        grant_type=get_token_obj.grant_type,
                                        ret_type="header")
        sessionId = actions.get_seesionId_test(token, get_sessionID_obj.url, get_sessionID_obj.app_user_id)["user"][
            "session_id"]
        res = actions.create_group_testQ(token, sessionId, create_group_test_obj.url,
                                        create_group_test_obj.groupInfo["group_name"],
                                        create_group_test_obj.groupInfo["group_desc"], )
        #        assert res["error_code"] == create_group_test_obj.error_code
        return res
#************账户未登录*************
#场景：#场景：token，sessionid传空
    def test_create_group_test1(self, get_token_obj, get_sessionID_obj, create_group_test_obj):
        print "Testing creating a group... Trying to log in first."
        token = {}

        sessionId = ""

        res = actions.create_group_test(token, sessionId, create_group_test_obj.url,
                                            create_group_test_obj.members_user_id,
                                            create_group_test_obj.groupInfo["group_name"],
                                            create_group_test_obj.groupInfo["group_desc"], )

#**************群成员超过限制****************
#场景：选择多个不同好友加入群组
    def test_create_group_test2(self, get_token_obj, get_sessionID_obj, create_group_test_obj):
        print "Testing creating a group... Trying to log in first."
        token = actions.get_token_test(url=get_token_obj.url,
                                           client_id=get_token_obj.client_id,
                                           client_secret=get_token_obj.client_secret,
                                           grant_type=get_token_obj.grant_type,
                                           ret_type="header")

        sessionId = actions.get_seesionId_test(token, get_sessionID_obj.url, get_sessionID_obj.app_user_id)["user"][
                "session_id"]

        user_id = ""
        for i in range(0, 500):
                user_id = user_id + "," + "chenying_%d" % i

        res = actions.create_group_test(token, sessionId, create_group_test_obj.url,
                                            user_id,
                                            create_group_test_obj.groupInfo["group_name"],
                                            create_group_test_obj.groupInfo["group_desc"] )

#########################################加入群组----主逻辑##########################################################
    def test_join_group_test(self, get_token_obj, get_sessionID_obj, join_group_test_obj):
        print "Testing joining  into a group... Trying to log in first."
        token = actions.get_token_test(url=get_token_obj.url,
                                       client_id=get_token_obj.client_id,
                                       client_secret=get_token_obj.client_secret,
                                       grant_type=get_token_obj.grant_type,
                                       ret_type="header")
        sessionId = actions.get_seesionId_test(token, get_sessionID_obj.url, get_sessionID_obj.app_user_id)["user"]["session_id"]
        res = actions.join_group_test(token, sessionId, join_group_test_obj.url, join_group_test_obj.groupInfo["group_id"],
                                      join_group_test_obj.join_members_user_id)
        print "Verifying the response with the expected output."
#        assert res["error_code"] == join_group_test_obj.error_code

#########################################加入群组----模拟未登录######################################################
    def test_join_group_test1(self, get_token_obj, get_sessionID_obj, join_group_test_obj):
        print "Testing joining  into a group... Trying to log in first.——unauthorized"
        token = {}
        sessionId = "hhfhfh"
        res = actions.join_group_test(token, sessionId, join_group_test_obj.url, join_group_test_obj.groupInfo["group_id"],
                                      join_group_test_obj.join_members_user_id)
        print "Verifying the response with the expected output."
        # assert res["error_code"] == join_group_test_obj.error_code

#########################################加入群组----模拟群组人数超限################################################
    def test_join_group_test2(self, get_token_obj, get_sessionID_obj, join_group_test_obj):
        print "Testing joining  into a group... Trying to log in first.——group member count over limit"
        token = actions.get_token_test(url=get_token_obj.url,
                                       client_id=get_token_obj.client_id,
                                       client_secret=get_token_obj.client_secret,
                                       grant_type=get_token_obj.grant_type,
                                       ret_type="header")

        sessionId = actions.get_seesionId_test(token, get_sessionID_obj.url, get_sessionID_obj.app_user_id)["user"]["session_id"]
        member_id = ""
        for i in range(0, 500):
            member_id = member_id + "," + "chenying_%d" % i
        res = actions.join_group_test(token, sessionId, join_group_test_obj.url, join_group_test_obj.groupInfo["group_id2"],
                                      member_id)
        print "Verifying the response with the expected output."
        # assert res["error_code"] == join_group_test_obj.error_code
###############################更新群组############################
    def test_update_group_test(self, get_token_obj, get_sessionID_obj, update_group_obj):
        print "Running the test for updating group..."
        token = actions.get_token_test(url=get_token_obj.url,
                                       client_id=get_token_obj.client_id,
                                       client_secret=get_token_obj.client_secret,
                                       grant_type=get_token_obj.grant_type,
                                       ret_type="header")
        sessionId = actions.get_seesionId_test(token, get_sessionID_obj.url, get_sessionID_obj.app_user_id)["user"]["session_id"]
        res = actions.update_group_test(token, sessionId, update_group_obj.url, update_group_obj.groupInfo["group_id"],
                                        update_group_obj.groupInfo["group_name"], update_group_obj.groupInfo["group_desc"])
        print "Verifying the response with the expected output."
#        assert res["error_code"] == update_group_obj.error_code

#*************账户未登录***************
#场景：#场景：token，sessionid传空
    def test_update_group_test1(self, get_token_obj, get_sessionID_obj, update_group_obj):
        print "Running the test for updating group..."
        token = {}
        sessionId = ""
        res = actions.update_group_test(token, sessionId, update_group_obj.url, update_group_obj.groupInfo["group_id"],
                                            update_group_obj.groupInfo["group_name"], update_group_obj.groupInfo["group_desc"])
        print "Verifying the response with the expected output."

#***********缺少参数*****************
#场景：不传group_id
    def test_update_group_test2(self, get_token_obj, get_sessionID_obj, update_group_obj):
        print "Running the test for updating group..."
        token = actions.get_token_test(url=get_token_obj.url,
                                       client_id=get_token_obj.client_id,
                                       client_secret=get_token_obj.client_secret,
                                       grant_type=get_token_obj.grant_type,
                                       ret_type="header")
        sessionId = actions.get_seesionId_test(token, get_sessionID_obj.url, get_sessionID_obj.app_user_id)["user"][
            "session_id"]
        res = actions.update_group_test2(token, sessionId, update_group_obj.url,
                                         update_group_obj.groupInfo["group_name"],
                                         update_group_obj.groupInfo["group_desc"])
        print "Verifying the response with the expected output."

###############################################获取群组信息主逻辑###################################################
    def test_get_group_infor_test(self, get_token_obj, get_sessionID_obj, get_group_infor_obj):
        print "Running the test for ask group information.."
        token = actions.get_token_test(url=get_token_obj.url,
                                       client_id=get_token_obj.client_id,
                                       client_secret=get_token_obj.client_secret,
                                       grant_type=get_token_obj.grant_type,
                                       ret_type="header")
        if (type(get_sessionID_obj) == type("")):
             sessionId = get_sessionID_obj
        else:
             sessionId = actions.get_seesionId_test(token, get_sessionID_obj.url, get_sessionID_obj.app_user_id)["user"][
            "session_id"]
        res = actions.get_group_infor_test(token, sessionId, get_group_infor_obj.url, get_group_infor_obj.groupInfo["group_id"],get_group_infor_obj.groupInfo["group_detail"])
        # print "Verifying the response with the expected output."
#        assert res["error_code"] == get_group_infor_obj.error_code
#########################################获取群组信息----模拟未登录#################################################
    def test_get_group_infor_testB(self, get_token_obj, get_sessionID_obj, get_group_infor_obj):
        print "Running the test for ask group information.."
        token = {}

        sessionId = ""
        res = actions.get_group_infor_test(token, sessionId, get_group_infor_obj.url, get_group_infor_obj.groupInfo["group_id"],
                                           get_group_infor_obj.groupInfo["group_detail"])
        # print "Verifying the response with the expected output."
        # assert res["creator"] == get_group_infor_obj.result_creator

#########################################拉取离线消息----主逻辑###################################################
    def test_get_offline_messages_test(self, get_token_obj, get_sessionID_obj, get_offline_messages_test_obj):
        print "Testing getting offline messages... Trying to log in first."
        token = actions.get_token_test(url=get_token_obj.url,
                                       client_id=get_token_obj.client_id,
                                       client_secret=get_token_obj.client_secret,
                                       grant_type=get_token_obj.grant_type,
                                       ret_type="header")
        sessionId = actions.get_seesionId_test(token, get_sessionID_obj.url, get_sessionID_obj.app_user_id)["user"]["session_id"]
        res = actions.get_offline_messages_test(token, sessionId, get_offline_messages_test_obj.url)
        print "Verifying the response with the expected output."
#        assert res["error_code"] == get_offline_messages_test_obj.error_code

#########################################拉取离线消息----模拟未登录#################################################
    def test_get_offline_messages_test1(self, get_token_obj, get_sessionID_obj, get_offline_messages_test_obj):
        print "Testing getting offline messages... Trying to log in first.——unauthorized"
        token = {}
        sessionId = "hfhfhhfdfhhfh"
        res = actions.get_offline_messages_test(token, sessionId, get_offline_messages_test_obj.url)
        print "Verifying the response with the expected output."
        # assert res["error_code"] == get_offline_messages_test_obj.error_code

    def test_upload_unread_mes_test(self, get_token_obj, get_sessionID_obj, upload_unread_mes_test_obj):
        print "Testing setting disturb... Trying to log in first."
        token = actions.get_token_test(url=get_token_obj.url,
                                       client_id=get_token_obj.client_id,
                                       client_secret=get_token_obj.client_secret,
                                       grant_type=get_token_obj.grant_type,
                                       ret_type="header")
        sessionId = actions.get_seesionId_test(token, get_sessionID_obj.url, get_sessionID_obj.app_user_id)["user"][
            "session_id"]
        res = actions.upload_unread_mes_test(token, sessionId, upload_unread_mes_test_obj.url, upload_unread_mes_test_obj.unread)
        print "Verifying the response with the expected output."
        assert res["error_code"] == upload_unread_mes_test_obj.error_code
#***********账户未登录***************
#场景：#场景：token，sessionid传空
    def test_upload_unread_mes_test1(self, get_token_obj, get_sessionID_obj, upload_unread_mes_test_obj):
        print "Testing setting disturb... Trying to log in first."
        token = {}
        sessionId = ""
        res = actions.upload_unread_mes_test(token, sessionId, upload_unread_mes_test_obj.url, upload_unread_mes_test_obj.unread)
        print "Verifying the response with the expected output."
        assert res["error_code"] == upload_unread_mes_test_obj.error_code
#############################################判断文件是否存在主逻辑################################################
    def test_is_file_exist(self, get_token_obj, get_sessionID_obj, is_file_exist_obj):
        print  "Testting checking file is exist......try to login first"
        token = actions.get_token_test(url=get_token_obj.url,
                                       client_id=get_token_obj.client_id,
                                       client_secret=get_token_obj.client_secret,
                                       grant_type=get_token_obj.grant_type,
                                       ret_type="header")

        sessionId = actions.get_seesionId_test(token, get_sessionID_obj.url, get_sessionID_obj.app_user_id)["user"][
            "session_id"]

        res = actions.is_file_exist(sessionId, is_file_exist_obj.url, is_file_exist_obj.md5,
                                    is_file_exist_obj.app_id, is_file_exist_obj.region_code)
####################################################################################################################
###########################################上传文件主逻辑###########################################################
    def test_upload_file_test(self, get_token_obj, get_sessionID_obj, upload_file_obj):
        print  "Testting uploading a file......try to login first"
        token = actions.get_token_test(url=get_token_obj.url,
                                       client_id=get_token_obj.client_id,
                                       client_secret=get_token_obj.client_secret,
                                       grant_type=get_token_obj.grant_type,
                                       ret_type="header")
        sessionId = actions.get_seesionId_test(token, get_sessionID_obj.url, get_sessionID_obj.app_user_id)["user"][
            "session_id"]
        res = actions.upload_file_test(sessionId, upload_file_obj.url, upload_file_obj.file,
                                       upload_file_obj.app_id, upload_file_obj.region_code)

    def test_set_disturb_test(self, get_token_obj, get_sessionID_obj, set_disturb_test_obj):
        print "Testing setting disturb... Trying to log in first."
        token = actions.get_token_test(url=get_token_obj.url,
                                       client_id=get_token_obj.client_id,
                                       client_secret=get_token_obj.client_secret,
                                       grant_type=get_token_obj.grant_type,
                                       ret_type="header")
        sessionId = actions.get_seesionId_test(token, get_sessionID_obj.url, get_sessionID_obj.app_user_id)["user"][
            "session_id"]
        res = actions.set_disturb_test(token, sessionId, set_disturb_test_obj.url, set_disturb_test_obj.disable)
        print "Verifying the response with the expected output."
        assert res["error_code"] == set_disturb_test_obj.error_code

#***********账户未登录*********
#场景：token，sessionid传空
    def test_set_disturb_test1(self, get_token_obj, get_sessionID_obj, set_disturb_test_obj):
        print "Testing setting disturb... Trying to log in first."
        token = {}
        sessionId = ""
        res = actions.set_disturb_test(token, sessionId, set_disturb_test_obj.url, set_disturb_test_obj.disable)
        print "Verifying the response with the expected output."
        assert res["error_code"] == set_disturb_test_obj.error_code


##########################################群组中踢人主逻辑#########################################################
    def test_remove_group_member_test(self, get_token_obj, get_sessionid_obj, get_group_obj):
        token = actions.get_token_test(get_token_obj.url,
                                       client_id=get_token_obj.client_id,
                                       client_secret=get_token_obj.client_secret,
                                       grant_type=get_token_obj.grant_type,
                                       ret_type="header")
        if (type(get_sessionid_obj) == type("")):
            sessionId = get_sessionid_obj

        else:
             sessionId = actions.get_seesionId_test(token, get_sessionid_obj.url, get_sessionid_obj.app_user_id)["user"][
             "session_id"]
        res = actions.remove_group_member_test(token,
                                               sessionId,
                                               get_group_obj.url,
                                               get_group_obj.groupInfo["group_id"],
                                               get_group_obj.member_v5_id)
#        assert res["error_code"]        == get_group_obj.err_code
        #assert res["error"]              == get_group_obj.error
##################################群组中踢人---模拟未登录###########################################################
    def test_remove_group_member_testB(self, get_token_obj, get_sessionid_obj, get_group_obj):
        token = {}
        sessionId = ""
        res = actions.remove_group_member_test(token,
                                               sessionId,
                                               get_group_obj.url,
                                               get_group_obj.groupInfo["group_id"],
                                               get_group_obj.member_v5_id)
        # assert res["error_code"]        == get_group_obj.err_code
        # assert res["error"]              == get_group_obj.error
####################################################################################################################
###################################群组中踢人--缺少参数#############################################################
    def test_remove_group_member_testC(self, get_token_obj, get_sessionid_obj, get_group_obj):
        token = actions.get_token_test(get_token_obj.url,
                                       client_id=get_token_obj.client_id,
                                       client_secret=get_token_obj.client_secret,
                                       grant_type=get_token_obj.grant_type,
                                       ret_type="header")
        if (type(get_sessionid_obj) == type("")):
            sessionId = get_sessionid_obj

        else:
            sessionId = actions.get_seesionId_test(token, get_sessionid_obj.url, get_sessionid_obj.app_user_id)["user"][
                "session_id"]
        res = actions.remove_group_member_testB(token,
                                               sessionId,
                                               get_group_obj.url,

                                               get_group_obj.member_v5_id)
        # assert res["error_code"]        == get_group_obj.err_code
        # assert res["error"]              == get_group_obj.error

#########################################解散群组----主逻辑##########################################################
    def test_dissolve_group_test(self, get_token_obj, get_sessionID_obj, dissolve_group_test_obj):
        print "Testing dissolving a group... Trying to log in first."
        token = actions.get_token_test(url=get_token_obj.url,
                                       client_id=get_token_obj.client_id,
                                       client_secret=get_token_obj.client_secret,
                                       grant_type=get_token_obj.grant_type,
                                       ret_type="header")
        sessionId = actions.get_seesionId_test(token, get_sessionID_obj.url, get_sessionID_obj.app_user_id)["user"]["session_id"]

        res = actions.dissolve_group_test(token, sessionId, dissolve_group_test_obj.url,
                                              dissolve_group_test_obj.groupInfo["group_id"])
        print "Verifying the response with the expected output."
#        assert res["error_code"] == dissolve_group_test_obj.error_code

#########################################解散群组----模拟未登录######################################################
    def test_dissolve_group_test1(self, get_token_obj, get_sessionID_obj, dissolve_group_test_obj):
        print "Testing dissolving a group... Trying to log in first.——unauthorized"
        token = {}
        sessionId = "hfhfhhfhhfhf"
        res = actions.dissolve_group_test(token, sessionId, dissolve_group_test_obj.url,
                                          dissolve_group_test_obj.groupInfo["group_id"])

        print "Verifying the response with the expected output."
        #assert res["error_code"] == dissolve_group_test_obj.error_code

#########################################解散群组----缺少参数########################################################
    def test_dissolve_group_test2(self, get_token_obj, get_sessionID_obj, dissolve_group_test_obj):
        print "Testing dissolving a group... Trying to log in first.—— illegalexception"
        token = actions.get_token_test(url=get_token_obj.url,
                                       client_id=get_token_obj.client_id,
                                       client_secret=get_token_obj.client_secret,
                                       grant_type=get_token_obj.grant_type,
                                       ret_type="header")
        sessionId = actions.get_seesionId_test(token, get_sessionID_obj.url, get_sessionID_obj.app_user_id)["user"]["session_id"]
        res = actions.dissolve_group_test1(token, sessionId, dissolve_group_test_obj.url)
        print "Verifying the response with the expected output."
        # assert res["error_code"] == dissolve_group_test_obj.error_code

###############################################退出群组################################################################
    def test_exit_group(self, get_token_obj, get_sessionID_obj, exit_group_test_obj):
        print "Testing dissolving a group... Trying to log in first.——unauthorized"
        token = actions.get_token_test(url=get_token_obj.url,
                                       client_id=get_token_obj.client_id,
                                       client_secret=get_token_obj.client_secret,
                                       grant_type=get_token_obj.grant_type,
                                       ret_type="header")

        sessionId = actions.get_seesionId_test(token, get_sessionID_obj.url, get_sessionID_obj.app_user_id)["user"][
        "session_id"]
        res = actions.dissolve_group_test(token, sessionId, exit_group_test_obj.url,
                                          exit_group_test_obj.groupInfo["group_id"])
        print "Verifying the response with the expected output."
###############################################退出群组---未登录################################################################
    def test_exit_group1(self, get_token_obj, get_sessionID_obj, exit_group_test_obj):
        print "Testing dissolving a group... Trying to log in first.——unauthorized"
        token = {}

        sessionId = ""
        res = actions.dissolve_group_test(token, sessionId, exit_group_test_obj.url,
                                          exit_group_test_obj.groupInfo["group_id"])
        print "Verifying the response with the expected output."
#########################################退出群组----缺少参数########################################################
    def test_exit_group2(self, get_token_obj, get_sessionID_obj, exit_group_test_obj):
        print "Testing dissolving a group... Trying to log in first.——unauthorized"
        token = actions.get_token_test(url=get_token_obj.url,
                                       client_id=get_token_obj.client_id,
                                       client_secret=get_token_obj.client_secret,
                                       grant_type=get_token_obj.grant_type,
                                       ret_type="header")

        sessionId = actions.get_seesionId_test(token, get_sessionID_obj.url, get_sessionID_obj.app_user_id)["user"][
        "session_id"]
        res = actions.exit_group_test1(token, sessionId, exit_group_test_obj.url)
        print "Verifying the response with the expected output."

    def test_creat_chatroom_test(self,get_token_obj,get_sessionID_obj,creat_chatroom_test_obj):
        token=actions.get_token_test(url=get_token_obj.url,
                                     client_id=get_token_obj.client_id,
                                     client_secret=get_token_obj.client_secret,
                                     grant_type=get_token_obj.grant_type,
                                     ret_type="header")
        sessionId=actions.get_userId_sessionId_test(token,get_sessionID_obj.url,get_sessionID_obj.app_user_id)["user"][
        "session_id"]
        res=actions.creat_chatroom_test(token,sessionId,creat_chatroom_test_obj.url,creat_chatroom_test_obj.chatroomInfo["desc"],creat_chatroom_test_obj.app_id)
        print "Verifying the response with the expected output."
        assert res["error_code"] == creat_chatroom_test_obj.error_code
        return  res

    def test_get_chatroom_list_test(self, get_token_obj, get_sessionID_obj, get_chatroom_list_test_obj):
       token = actions.get_token_test(url=get_token_obj.url,
                                   client_id=get_token_obj.client_id,
                                   client_secret=get_token_obj.client_secret,
                                   grant_type=get_token_obj.grant_type,
                                   ret_type="header")
       sessionId = actions.get_userId_sessionId_test(token, get_sessionID_obj.url, get_sessionID_obj.app_user_id)["user"][
        "session_id"]
       res = actions.get_chatroom_list_test(token, sessionId, get_chatroom_list_test_obj.url, get_chatroom_list_test_obj.chatroomInfo["live"],
                                      get_chatroom_list_test_obj.app_id,get_chatroom_list_test_obj.chatroomInfo["count"])
       print "Verifying the response with the expected output."
       assert res["error_code"] == get_chatroom_list_test_obj.error_code

    def test_get_chatroom_infor_test(self, get_token_obj, get_sessionID_obj, get_chatroom_infor_test_obj):
       token = actions.get_token_test(url=get_token_obj.url,
                                   client_id=get_token_obj.client_id,
                                   client_secret=get_token_obj.client_secret,
                                   grant_type=get_token_obj.grant_type,
                                   ret_type="header")
       sessionId = actions.get_userId_sessionId_test(token, get_sessionID_obj.url, get_sessionID_obj.app_user_id)["user"][
        "session_id"]
       res = actions.get_chatroom_infor_test(token, sessionId, get_chatroom_infor_test_obj.url,
                                      get_chatroom_infor_test_obj.chatroomInfo["id"],get_chatroom_infor_test_obj.app_id)
       print "Verifying the response with the expected output."
#       assert ["error_code"] == get_chatroom_infor_test_obj.error_code