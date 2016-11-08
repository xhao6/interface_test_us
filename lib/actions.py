# -*- coding: utf-8 -*-
import urllib
import urllib2
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import time

#PART 1------------------------- 功能性函数包括 http处理，字符串处理等-------------------------
# 用于连接的超时重试机制，默认允许超时两次后重试，重试前等待3秒
def allow_retry(req, total=3):
    trial = 0
    res = None
    while trial < total:
        try:
            res = urllib2.urlopen(req)
            break
        except:
            print "Failed to connect required URL"
            trial = trial + 1
            time.sleep(3)
    return res

def get(url, header):
    # request headers
    req = urllib2.Request(url, None, header)
    req_header_get = req.header_items()
    print "***request header_get = ***\n%s" % req_header_get

    # send request and get response handle
    print "Connecting to URL" + url
    res = allow_retry(req)

    # response code
    res_code = res.getcode()
    print "***response code = ***\n%s" % res_code
    # response header
    res_header = res.info()
    print "***response header = ***\n%s" % res_header
    # response body
    res_body = res.read()
    print "***response body = ***\n%s" % res_body
    res.close()

    return res_body

def post(url, data, header):
    #request headers
    req_header = header

    #request body
    data = urllib.urlencode(data)
    print "bbbbBBBBBBBBBBBBBB",data
    #pre--request
    req = urllib2.Request(url, data, req_header)

    #req_header_tmp = req.get_header("User-agent")
    #print "***request header_tmp = *** %s" % req_header_tmp

    req_header_get = req.header_items()
    print "***request header_get = ***\n%s" % req_header_get

    req_body = req.get_data()
    print "***request body = ***\n%s" % req_body
    #send request and get response handle
    print "Connecting to URL" + url
    res = allow_retry(req)

    #response code
    res_code = res.getcode()
    print "***response code = ***\n%s" % res_code
    #response header
    res_header = res.info()
    print "***response header = ***\n%s" % res_header
    #response body
    res_body =  res.read()
    print "***response body = ***\n%s" % res_body
    res.close()

    return res_body

def post_upload_file(url, file, header):
    #此方法用于上传文件接口的post形式
    # request headers
    print "@@@ header input is", header

    # 在 urllib2 上注册 http 流处理句柄
    register_openers()
    ######判断上传的文件是否为空（在异常逻辑中--文件为空接口中用到）######################
    if(file == ""):
        data,header_ext = multipart_encode({"file":""})
    else:
        data, header_ext = multipart_encode({"file":open(file,"rb")})

    header.update(header_ext)

    # pre--request
    req = urllib2.Request(url, data, header)

    req_header_get = req.header_items()
    print "***request header_get = ***\n%s" % req_header_get

    # send request and get response handle
    print "Connecting to URL" + url
    res = allow_retry(req)

    # response code
    res_code = res.getcode()
    print "***response code = ***\n%s" % res_code
    # response header
    res_header = res.info()
    print "***response header = ***\n%s" % res_header
    # response body
    res_body = res.read()
    print "***response body = ***\n%s" % res_body
    res.close()

    return res_body

def null2None2dict(res=""):
    res = res.replace("null", "None")
    res = res.replace("false", "False")
    res = res.replace("true", "True")
    return eval(res)


# PART 2------------------------- CLIENT -----> SERVER -------------------------
# def login(url="", account="", nick_name=None):
#     # PARAMETER:        url和account不可以为空  nick_name可以为空(不传)   3个都是string类型
#     # OUTPUT:           http response body----->dict类型输出
#     login_url               = url
#     data                    = {}
#     data["account"]         = account
#     if nick_name:
#         data["nickName"]    = nick_name
#     header                  = {}
#
#     response = post(login_url, data, header)
#     return null2None2dict(response)
#
#
# def findAccount(sessionID="", url="", account=""):
#     # PARAMETER:        3个string类型参数，都不可以为空
#     # OUTPUT:           http response body----->dict类型输出
#     header          = {"session": sessionID}
#     full_url        = url + "?account=" + account
#
#     response        = get(full_url, header)
#     return null2None2dict(response)
#
# def createGroup(sessionID="", url="", members=""):
#     # PARAMETER:        3个string类型参数，都不可以为空
#     # OUTPUT:           http response body----->dict类型输出
#     header          = {"session": sessionID}
#     data            = {"members": members}
#
#     response        = post(url, data, header)
#     return null2None2dict(response)
#
# def joinGroup(sessionID="", url="",groupId="", members=""):
#     # PARAMETER:        4个string类型参数，都不可以为空
#     # OUTPUT:           http response body----->dict类型输出
#     header          = {"session": sessionID}
#     data            = {"groupId":groupId, "members": members}
#
#     response        = post(url, data, header)
#     return null2None2dict(response)


# PART 3------------------------- SERVER -----> SERVER -------------------------
def get_token_test(url="", client_id=0, client_secret="",grant_type="", ret_type=""):
    # PARAMETER:        4个参数（string,int,string,string,string），只有最后一个可以为空
    # 特别说明:         ret_type 为header时，return 鉴权头
    # OUTPUT:           http response body----->dict类型输出
    url         = url
    data        = {"client_id":client_id, "client_secret":client_secret, "grant_type":grant_type}
    header      = {}

    res         = post(url, data, header)

    if ret_type == "header":
        res             = null2None2dict(res)
        access_token    = res["access_token"]
        token_type      = res["token_type"].capitalize()
        return {"Authorization": token_type + " " + access_token}
    else:
        return  null2None2dict(res)

def get_userId_sessionId_test(token={}, url="", app_user_id="", app_user_nick_name=""):
    # PARAMETER:        token -- dict类型，其他3个string类型参数，只有最后一个可以为空
    #  OUTPUT:           http response body----->dict类型输出
    url_pre         = url
    if app_user_nick_name:
        url_full    = url_pre + "app_user_id=%s&app_user_nick_name=%s" %(app_user_id,app_user_nick_name)
    else:
        url_full    = url_pre + "app_user_id=%s" % app_user_id

    header = token

    res             = get(url_full, header)
    return null2None2dict(res)

def get_seesionId_test(token={}, url="", app_user_id=""):
    # PARAMETER:        token -- dict类型，其他2个string类型参数
    # OUTPUT:           http response body----->dict类型输出
    url_pre         = url
    url_full        = url_pre + "app_user_id=%s" % app_user_id
    header          = token

    res             = get(url_full, header)
    return null2None2dict(res)

def get_server_test(token={}, sessionID="", url=""):
    header     = token
    header_ext ={"client-session":sessionID}
    header.update(header_ext)
    res        =get(url, header)
    return null2None2dict(res)

def update_token_test(token={}, getSession="", url="",app_id="", device_type="", device_token="", provider=""):
    header          = token
    header_ext      = {"client-session": getSession}
    header.update(header_ext)
    data            = {"app_id": app_id, "device_type": device_type, "device_token": device_token,"provider": provider}
    res             = post(url, data, header)
    return null2None2dict(res)

def get_location_test(token={}, getsession="", url=""):
    header         = token
    header_ext     = {"client-session": getsession}
    #url=url+"/api/user/location"
    header.update(header_ext)
    res = get(url, header)
    return null2None2dict(res)

def update_nickname_test(token={}, getSession="", url="",app_user_id="", app_user_nick_name=""):
    # PARAMETER:        token -- dict类型，其他4个string类型参数
    #  OUTPUT:           http response body----->dict类型输出
    data        = {"app_user_id":app_user_id,"app_user_nick_name":app_user_nick_name}
    header      = token
    header_ext  = {"client-session":getSession}
    header.update(header_ext)
    res         = post(url, data, header)
    return null2None2dict(res)

def create_group_test(token={}, sessionID="", url="", members="", name="", desc=""):
    # PARAMETER:        3个string类型参数，都不可以为空
    # OUTPUT:           http response body----->dict类型输出
    header      = token
    header_ext  = {"client-session":sessionID}
    header.update(header_ext)
    #header          = {"session": sessionID}
    data            = {"member": members, "name":name, "desc":desc}
    response        = post(url, data, header)
    return null2None2dict(response)
#########创建群组缺少参数######
def create_group_testQ(token={}, sessionID="", url="",  name="", desc=""):
    # PARAMETER:        3个string类型参数，都不可以为空
    # OUTPUT:           http response body----->dict类型输出
    header      = token
    header_ext  = {"client-session":sessionID}
    header.update(header_ext)
    #header          = {"session": sessionID}
    data            = { "name":name, "desc":desc}
    response        = post(url, data, header)
    return null2None2dict(response)

def join_group_test(token={}, getSession="", url="",groupId="", members=""):
    # PARAMETER:        4个string类型参数，都不可以为空
    # OUTPUT:           http response body----->dict类型输出
    header          = token
    header_ext      = {"client-session": getSession}
    header.update(header_ext)
    data            = {"group_id": groupId, "member": members}
    res             = post(url, data, header)
    return null2None2dict(res)

def update_group_test(token={}, sessionID="", url="", groupId="",name="", desc=""):
    # PARAMETER:        token -- dict类型，其他4个string类型参数
    #  OUTPUT:           http response body----->dict类型输出
    header      = token
    data        = {"group_id":groupId,"name":name,"desc":desc}
    header_ext  = {"client-session":sessionID}
    header.update(header_ext)
    res         = post(url, data, header)
    return null2None2dict(res)

#**********缺少参数***********
#场景：不传group_id
def update_group_test2(token={}, sessionID="", url="",name="", desc=""):
    # PARAMETER:        token -- dict类型，其他4个string类型参数
    #  OUTPUT:           http response body----->dict类型输出
    header      = token
    data        = {"name":name,"desc":desc}
    header_ext  = {"client-session":sessionID}
    header.update(header_ext)
    res         = post(url, data, header)
    return null2None2dict(res)

def get_group_infor_test(token={}, sessionID="", url="",groupId="",detail=0):
    # PARAMETER:        4个string类型参数，都不可以为空
    # OUTPUT:           http response body----->dict类型输出
    header     = token
    url        = url+"group_id=%s&&detail=%s" %(groupId,detail)
    header_ext ={"client-session":sessionID}
    header.update(header_ext)
    res        =get(url, header)
    return null2None2dict(res)



def get_offline_messages_test(token={}, sessionID="", url=""):
    header     = token
    #url        = url+"last_message_id=%s&length=%s" %(last_message_id&length)
    header_ext ={"client-session":sessionID}
    header.update(header_ext)
    res        =get(url, header)
    return null2None2dict(res)

def upload_unread_mes_test(token={}, getsession="", url="", unread=""):
    header          = token
    header_ext      = {"client-session": getsession}
    header.update(header_ext)
    data            = {"unread": unread}
    res             = post(url, data, header)
    return null2None2dict(res)

def is_file_exist(sessionID="",url = "", md5= "",app_id="",region_code=""):
    header = {"client-session":sessionID,"app-id":app_id,"region-code":region_code}
    url  = url +"md5=%s" % md5
    print"TTTTTTTTT",url
    header.update(header)
    res = get(url, header)
    return null2None2dict(res)

def upload_file_test( sessionID ="",url="", file = "", app_id = "", region_code= ""):
    header = {"client-session": sessionID,"app-id":app_id,"region-code":region_code}
    header.update(header)
    data = file
    res = post_upload_file(url, data, header)
    return null2None2dict(res)


def set_disturb_test(token={}, getsession="", url="", disable=""):
    header          = token
    header_ext      = {"client-session": getsession}
    header.update(header_ext)
    data            = {"disable": disable}
    res             = post(url, data, header)
    return null2None2dict(res)

# changed by AndrewXU
def remove_group_member_test(token={}, sessionid="", url="", groupID="", members="", ):
    header          = token
    header_ext      = {"client-session":sessionid}
    header.update(header_ext)
    data            = {"group_id": groupID, "member": members}
    response        = post(url, data, header)
    return null2None2dict(response)
#########################群组中踢人------增加了一个方法：模拟缺少参数的场景#######################
def remove_group_member_testB(token={}, sessionid="", url="", members="", ):
    # PARAMETER:        3个string类型参数，都不可以为空
    # OUTPUT:           http response body----->dict类型输出
    header          = token
    header_ext      = {"client-session":sessionid}
    header.update(header_ext)
    data            = {"member": members}
    response        = post(url, data, header)
    return null2None2dict(response)
###################################################################################################
###########################解散群组###############################################################
def dissolve_group_test(token={}, getSession="", url="",groupId=""):
    # PARAMETER:       2个string类型参数，都不可以为空
    # OUTPUT:           http response body----->dict类型输出
    header          = token
    header_ext      = {"client-session": getSession}
    header.update(header_ext)
    data            = {"group_id": groupId}
    res             = post(url, data, header)
    return null2None2dict(res)
####################################################################################################

#########################解散群组------增加了一个方法：模拟缺少参数的场景###########################
def dissolve_group_test1(token={}, getSession="", url=""):
    # PARAMETER:        2个string类型参数，都不可以为空
    # OUTPUT:           http response body----->dict类型输出
    header          = token
    header_ext      = {"client-session": getSession}
    header.update(header_ext)
    data            = {}
    res             = post(url, data, header)
    return null2None2dict(res)
#######################################################################################################
################################退出群组###############################################################
def exit_group_test(token= {}, getSession = "", url = "", group_id = ""):
    header = token
    header_ext = {"client-session":getSession}
    header.update(header_ext)
    data  = {"group_id":group_id}
    res                 = post(url, data, header)
    return  null2None2dict(res)

###########################退出群组---缺少参数###############################################################
def exit_group_test1(token={}, getSession="", url=""):
    # PARAMETER:       2个string类型参数，都不可以为空
    # OUTPUT:           http response body----->dict类型输出
    header          = token
    header_ext      = {"client-session": getSession}
    header.update(header_ext)
    data            = {}
    res             = post(url, data, header)
    return null2None2dict(res)
####################################################################################################

def creat_chatroom_test(token={},getSession="",url="",desc="",app_id=""):
    header          =token
    header_ext      ={"client-session":getSession,"app-id":app_id}
    header.update(header_ext)
    data            ={"desc":desc}
    res             =post(url,data,header)
    return null2None2dict(res)

def get_chatroom_list_test(token={},getSession="",url="",live="",app_id="",count=""):
    header          =token
    url = url + "live=%s&&count=%s" % (live, count)
    print "BBBBBBBBBBBBB",url
    header_ext      ={"client-session":getSession,"app-id":app_id}
    header.update(header_ext)
    res             =get(url,header)
    return null2None2dict(res)

def get_chatroom_infor_test(token={},getSession="",url="",chatRoomId="",app_id=""):
    header          =token
    url = url + "chatRoomId=%s" %chatRoomId
    print "BBBBBBBBBBBBB",url
    header_ext      ={"client-session":getSession,"app-id":app_id}
    header.update(header_ext)
    res             =get(url,header)
    return null2None2dict(res)
