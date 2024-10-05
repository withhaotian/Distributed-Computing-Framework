import socket
import argparse
import sys
import os
import torch
import bluelet
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from top import *
from config.configs import Config
from communication.networking import *

def setup_seed(seed):
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
# 设置随机数种子
setup_seed(20)

class Client(object):
    def __init__(self):
        self.conf = Config()
        
    def send_req(self):
        conn = yield bluelet.connect(self.conf.leader_host, self.conf.leader_port)
        
        start = time.time()

        # msg = top.RequestMsg()
        
        yield send_msg(conn, msg)

        print('waiting for results...')

        msg = yield recv_msg(conn)

        if msg is None:
            yield bluelet.end()
            
        if not msg.success:
            print('Job failed!')
            yield bluelet.end()

        print(msg.results)
        
        end = time.time()
        print('Latency: ', '%.5f' % ((end - start)*1000), ' ms')
    
    def run(self):
        try:
            bluelet.run(self.send_req())
        except KeyboardInterrupt:
            pass

def start_client():
    Client().run()