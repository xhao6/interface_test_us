# -*- coding: utf-8 -*-
#移除群成员
###群组不存在###
class RemoveGroupMemberTest:
    #input
    url = ""
    group_id = ""
    member_v5_id = ""

    #expect
    noexist_error_code = None

#####缺少参数###
class RemoveGroupMemberTestB:
#input
    url = ""
    # group_id = ""
    member_v5_id = ""
#expect
    miss_error_code = None

#####账号未登录###
class RemoveGroupMemberTestC:
#input
    url = ""
    group_id = ""
    member_v5_id = ""
#expect
    nologin_error_code = None
