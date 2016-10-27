# -*- coding: utf-8 -*-
import unittest
import datetime
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import apiconfig.isfileexist.production_env_config as apimgr1
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
##############################判断文件是否上传------缺少参数#####################################################
    def test0101_is_file_exist_test(self):
        print "B----------------------------------test0101_is_file_exist_test----------------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr1.CoreServer_IsFileExistTest_01
        self.test.test_is_file_exist(auth, session, info)
        print "E-----------------------------------test0101_is_file_exist_test----------------------------------E"
