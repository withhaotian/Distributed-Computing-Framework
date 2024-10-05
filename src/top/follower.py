from pyexpat import model
import socket
import argparse
import sys
import os
import torch
import bluelet

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from top import *
from config.configs import Config
from communication.networking import *

class Follower(object):
    def __init__(self):
        self.conf = Config()
    
    def processing(self):
        conn = yield bluelet.connect(self.conf.leader_host, self.conf.leader_port)

        # register with the leader
        yield send_msg(conn, FollowerRegisterMsg())
        
        while True:
            msg = yield recv_msg(conn)

            if msg is None:
                break

            if isinstance(msg, Leader2FollowerMsg):
                # do something with the msg
                pass
            else:
                raise Exception('Error Msg Type from Leader to Follower!')
            
            # send back the response
            result_msg = Follower2LeaderMsg()
            yield send_msg(conn, result_msg)
    
    def run(self):
        bluelet.run(self.processing())

def start_follower():
    Follower().run()
