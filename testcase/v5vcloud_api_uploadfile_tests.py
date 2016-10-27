# -*- coding: utf-8 -*-
import unittest
import datetime
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import apiconfig.uploadfile.production_env_config as apimgr1
import lib.modules as modules
import apiconfig.mainprocess.ProductionEnv_config as apimgr
class core_server_tests(unittest.TestCase):
    test = modules.test_core_server()
    def setUp(self):
        currentTime = str(datetime.datetime.now())[0:19]
        print "@@@@@@@@@@-- RUN TESTCASE --%s@@@@@@@@@@" % currentTime
        pass

    def tearDown(self):
        pass
###############################上传文件--文件为空（缺少参数）######################################################
    def test0101_test_upload_file_test(self):
        print "B----------------------------------test0101_test_upload_file_test-----------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr1.CoreServer_UploadFileTest_01
        self.test.test_upload_file_test(auth,session,info)
        print "E----------------------------------test0101_test_upload_file_test------------------------E"
#####################################################################################################################