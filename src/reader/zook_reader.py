# -*- coding:utf-8 -*-
from kazoo.client import KazooClient
import os
__author__ = 'yangxin'


class ZookReader(object):

    def __init__(self):
        self.ZK_ADDRESS = os.environ.get("ZOOKEEPER_ADDRESS")
        self.ZK = KazooClient(self.ZK_ADDRESS)
        self.ZK.start()

    def get_data(self):
        key = "/*****/prod"
        result = self.ZK.get(key)
        result = result[0]
        list_param = result.split("\n")
        list_param1 = []
        dict_param = {}
        for i in range(len(list_param)):
            if list_param[i].startswith("dw.") is True:
                list_param1.append(list_param[i])
        for j in range(len(list_param1)):
            key = list_param1[j].split("=")[0]
            value = list_param1[j].split("=")[1]
            dict_param[key] = value
        return dict_param
