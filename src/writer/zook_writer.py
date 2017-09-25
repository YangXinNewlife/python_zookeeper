# -*- coding:utf-8 -*-
from kazoo.client import KazooClient
__author__ = 'yangxin'


class ZookWriter(object):

    def __init__(self):

        self.ZK_ADDRESS = "localhost:2181"
        self.ZK = KazooClient(self.ZK_ADDRESS)
        self.ZK.start()
        with open("/data/apps/con_zoo.txt", "r") as zoo_config:
            self.FILE = zoo_config

    def set_data(self, value):
        self.ZK.set('/*****/prod', b'{}'.format(value))

    def create_node(self, node):
        self.ZK.ensure_path(node)


with open("/data/apps/con_zoo.txt", "r") as file_config:
    FILE = file_config
    data = FILE.read()
zk = ZookWriter()
zk.create_node("/*****/prod")
zk.set_data(data)
