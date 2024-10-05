from sre_constants import SUCCESS
from string import whitespace
import sys
import os
from tkinter.messagebox import NO
import torch
import bluelet

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from top import *
from config.configs import Config
from communication.networking import *

class Leader(object):
    def __init__(self):
        # configs
        self.conf = Config()

        # list of clients
        self.client_all = []
        # list of followers
        self.follower_all = []
    
    def init_leader(self):
        listener = bluelet.Listener(self.conf.leader_host, self.conf.leader_port)
        
        while True:
            conn = yield listener.accept()
            
            print(conn.sock)
            
            yield bluelet.spawn(self.handle_req(conn))
    
    def send2follower(self, conn, msg):
        yield send_msg(conn, msg)
    
    def handle_req(self, conn):

        while True:

            msg = yield recv_msg(conn)

            if msg is None:
                break

            if isinstance(msg, RequestMsg):
                """
                received msg from client
                """
                # add client to list
                if conn not in self.client_all:
                    self.client_all.append(conn)
                
                # receive client request,
                # and do some preprocessing,
                # then send jobs to followers
                # example:
                # yield bluelet.spawn(self.send2follower(conn, msg))

            elif isinstance(msg, Follower2LeaderMsg):
                """
                received msg from follower
                """
                
                # if results are ready, back results to client
                # example:
                # result_msg = ResultMsg()
                # yield bluelet.spawn(send_msg(conn, msg))
                
                pass

            elif isinstance(msg, FollowerRegisterMsg):
                """
                received msg from follower to register
                """
                # add follower to list
                if conn not in self.follower_all:
                    self.follower_all.append(conn)
                    print('add to follower list from', conn)
            
            else:
                raise Exception('Error Msg Type in Leader!')
    
    def run(self):
        try:
            bluelet.run(self.init_leader())
        except KeyboardInterrupt:
            pass

def start_leader():
    Leader().run()