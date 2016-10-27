# -*- coding: utf-8 -*-
########更新群组#######
class UpdateGroupTest:
    '''request'''
    url                 =""
    groupId            =""
    result_name         =""
    desc                =""

    #expect
    error_code         =None

#####缺少参数######
#场景：不传groupid
class UpdateGroupTest1:
    '''request'''
    url                 =""
   # groupId            =""
    result_name         =""
    desc                =""

    #expect
    error_code         =None