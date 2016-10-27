# -*- coding: utf-8 -*-

#每一个接口动作写一个类
#……………………………………………………………… client to demoServer ………………………………………………………………
#登录类
class login():
    ''' request '''
    url                 = ""
    account             = ""
    nickName            = ""

    # expect
    err_code                    = None
    user_id                     = None
    user_v5_id                  = None
    user_account                = None
    user_sessionId              = None
    user_nickName               = None
    user_createTimeMillis       = None
    user_avatar                 = None

class FindAccountTest:
    '''request'''
    url                 = ""
    account             = ""
    #expect
    error_code          = 2000
    user_id             = None
    user_v5_id          = None
    user_account        = None
    user_sessionId      = None
    user_nickName       = None
    user_createTimeMillis  = None
    user_avatar         = None

class createGroup():
    ''' request '''
    url             = ""
    members_v5_id   = ""

    # expect
    err_code                    = None
    result_id                   = None
    result_v5_id                = None
    result_number               = None
    result_creator              = None
    result_name                 = None
    result_createTime           = None
    result_updateTime           = None
    result_desc                 = None
    result_avatar               = None
    result_member_v5_id         = None

class joinGroup:
    ''' request '''
    url             = ""
    groupId         = ""
    members_v5_id   = ""

    # expect
    err_code                        = None
    result_id                       = None
    result_v5_id                    = None
    join_members_v5_id              = None


#……………………………………………………………… client to demoServer ………………………………………………………………
class getToken:
    '''request'''
    url             = ""
    client_id       = None
    client_secret   = ""
    grant_type      = ""

    # expect
    access_token    = None
    token_type      = None
    expires_in      = None
    scope           = None

class getUserIdSessionId:
    '''request'''
    app_user_id         = ""
    app_user_nick_name  = ""
    url                 = ""
    header              = {}

    # expect
    error_code      = None
    user_id         = None
    user_session_id = None

class getSessionID:
    '''request'''
    app_user_id = ""
    url         = ""
    header      = {}

    # expect
    error_code      = None
    user_id         = None
    user_session_id = None


class GetServerTest:
    '''request'''
    url                         = ""

    # expect
    tcp_server                        = None
    file_server                       = None

class UpdateTokenTest:
    '''request'''
    url                         = ""
    app_id                      =""
    device_type                 =""
    device_token                =""
    provider                    =""

    # expect
    error_code                        = None

class GetLocationTest:
    ''':request'''
    url                   =""

    #expect
    lat                 =None
    lon                 =None


class UpdateNicknameTest:
    '''request'''
    app_user_id         = ""
    app_user_nick_name  = ""
    url                 = ""


    # expect
    error_code          = None

class CreatGroupTest:
    ''' request '''
    url                 = ""
    members_user_id     = ""
    result_name         = ""
    desc                = ""

    # expect
    result_id                   = None
    result_number               = None
    result_creator              = None
    result_name                 = None
    result_create_time          = None
    result_update_time          = None
    result_desc                 = None
    result_member_user_id       = None
    result_conversation         = None

class JoinGroupTest:
    ''' request '''
    url                   = ""
    groupId               = ""
    join_members_user_id  = ""

    # expect
    error_code                       = None
    result_join_members_user_id      = None
    #join_members_nickname           = None
    #join_members_createTime         = None


class UpdateGroupTest:
    '''request'''
    url                 =""
    groupId            =""
    result_name         =""
    desc                =""

    #expect
    error_code         =None

class GetGroupInforTest:
    """request"""
    url             = ""
    groupId         = ""

    #expect
    err_code                        = None
    result_id                       = None
    result_creator                  = None
    result_create_time              = None
    result_update_time              = None
    result_desc                     = None
    result_name                     = None
    result_number                   = None
    result_memeber_user_id          = None
    result_conversation             = None

class GetOfflineMessagesTest:
    '''request'''
    url                         = ""
    last_message_id             = ""
    length                      = ""

    # expect
    messages_id                        = None
    messages_content                   = None
    messages_type                      = None
    messages_create_time               = None
    messages_sender                    = None
    messages_receiver_type             = None
    messages_conversation_id           = None
    messages_meta_entity_format        = None
    messages_meta_cmsgid               = None
    messages_receiver                  = None
    messages_secret                    = None
    messages_room_id                   = None




class UploadUnreadMesTest:
    '''request'''
    url            =""
    unread         =None

    #expect
    error_code     =None

class IsFileExistTest:
    '''request'''
    url = ""
    md5 = ""
    app_id = ""
    region_code = ""
    #expect
    error_code = None
    is_exist  = None
    file_url = ""

class UploadFileTest:
    '''request'''
    url = ""
    file = ""
    app_id = ""
    region_code = ""
    # expect
    file_id = ""
    file_url = ""

class SetDisturbTest:
    '''request'''
    url               =""
    disable           =""

    #expect
    error_code        =None

class RemoveGroupMemberTest:
    '''request'''
    url                 = ""
    group_id            = ""
    member_v5_id        = ""

    #expect
    err_code            = None
    error               = ""
############解散群租
class DissolveGroupTest:
    ''' request '''
    url                   = ""
    groupId               = ""

    # expect
    error_code                       = None
##########退出群租
class ExitGroupTest:
    '''request'''
    url                   = ""
    group_id               = ""

    #expect
    error_code = None

##########创建聊天室############
class CreatChatroomTest:
    url                   =""
    desc                  =""
    app_id                 =""
    #expect
    error_code            =""
    id                    =""

#######获取直播室列表##########
class GetChatroomListTest:
    url                  =""
    live                 =""
    count                =""
    app_id               =""
    #expect
    error_code           =""
    number               =""
    id                   =""
    creator              =""
    desc                 =""
    observers            =""
    cover_url            =""
    rtmp_server          =""
    is_alive             =""

#######获取直播信息########
class GetChatroomInforTest:
    url           =""
    chatRoomId    =""
    app_id        =""
    #expect
    error_code       =""
    acc_number       =""
    number           =""
    cover_url        =""
    city             =""
    is_live          =""
    user_id          =""
    chat_room_id     =""
    room_id          =""
    rtmp_server      =""
    ssrc             =""
    udp_server_ip       =""
    horizontal       =""
    # app_id           =""