# -*- coding: utf-8 -*-
#获取群组信息
###缺少参数###
class GetGroupInforTest:
    #input
    url = ""
    groupId= ""
    detail = ""

    #expect
    miss_error_code = None
    error = ""

###账户未登录###
class GetGroupInforTestB:
    # input
    url = ""
    groupId = ""
    detail = ""

    # expect
    nologin_error_code = None


###群组不存在###
class GetGroupInforTestC:
    # input
    url = ""
    groupId = ""
    detail = ""

    # expect
    notexist_error_code = None
    error = ""