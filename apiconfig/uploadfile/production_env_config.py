# -*- coding: utf-8 -*-
from api_class import *

App_a = {"app_id": "10000920",
         "app_secret": "7499453344773ceed176118398dcdcc9",
         "grant_type": "client_credentials",
         "file": "v5vcloud_api_uploadfile_tests.py",
         "file_1": "",
         "file_2": "init.apkqw",
         "region_code": "0001",
         "app_id": "10000920",
         "accounts":
             {"account_01": { "id": "TEST_testAccount111",
                                "nickName": "Iam_login_05",
                                "user_avatar": "http://cn.file.chatgame.me/api/file/download/2016/7/26/2/b999baff-45b4-4147-957e-8c05d2c55b16.jpg"
                              },
              "account_02": { "id": "TEST_testAccount222",
                                "nickName": "Iam_login_03",
                                "user_avatar": "http://cn.file.chatgame.me/api/file/download/2016/7/26/2/5c3d14cc-9fc0-40d5-8b04-9b02ca69f5ff.jpg"
                                },
              "account_03":{"id":"TEST_testAccount333",
                               "nickName": "Iam_login_33",
                                }
             },
         "correct_err_code":2000,
         "null_error_code": 4022,
         "fail_error_code": 4023,

        }
CoreServer_url  = "https://cloudus.v5.cn"
######上传文件-----文件为空#########
######请求参数中去掉file，另外一种方法可以给file传一个空值来实现#
CoreServer_UploadFileTest_01     =  UploadFileTest()
#input
CoreServer_UploadFileTest_01.url   = CoreServer_url + "/api/file/upload"
# CoreServer_UploadFileTest_01.file  = App_a["file_1"]
CoreServer_UploadFileTest_01.app_id = App_a["app_id"]
CoreServer_UploadFileTest_01.region_code = App_a["region_code"]
#expect
CoreServer_UploadFileTest_01.null_error_code = App_a["null_error_code"]

