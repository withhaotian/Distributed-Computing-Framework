from __future__ import print_function
from calendar import c
import sys
import os
import bluelet

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.config.configs import Config
from src.communication.networking import *

class Leader(object):
    def __init__(self):
        self.conf = Config()
        self.client_all = []
        self.follower_all = []
        # self.sock = ServerNetworking(self.conf.leader_host, self.conf.leader_port)

        self.msg_type = 'LEADER'

        print('hello leader')

    def init_conn(self, conn):
        # print('Connected: %s' % conn.addr[0])

        while(True):
            
            msg = yield recv_msg(conn)

            if msg is None:
                break

            print(msg)


            self.print_yy()
    
    def print_yy(self):
        print('Test******')

            # if(msg[0] == 'MSG_CLIENT'):
            #     if(conn not in self.client_all):
            #         self.client_all.append(conn)
            # elif(msg[0] == 'MSG_FOLLOWER'):
            #     if(conn not in self.follower_all):
            #         self.follower_all.append(conn)
    
    def release_leader(self):
        listener = bluelet.Listener(self.conf.leader_host, self.conf.leader_port)
        
        while True:
            conn = yield listener.accept()
            
            print(conn.sock)
            
            yield bluelet.spawn(self.init_conn(conn))
    
    def run_bluelet(self):
        try:
            bluelet.run(self.release_leader())
        except KeyboardInterrupt:
            pass

class Follower(object):
    def __init__(self):
        self.conf = Config()
        self.msg_type = 'MSG_FOLLOWER'
        print(self.conf.leader_host)

        # self.sock = ClientNetworking(self.conf.leader_host, self.conf.leader_port)

    def processing(self):
        conn = yield bluelet.connect(self.conf.leader_host, self.conf.leader_port)
        print(conn.sock)
        
        while True:
            yield bluelet.sleep(3)
            msg = [self.msg_type, 'hello']
            yield send_msg(conn, msg)

    def run_bluelet(self):
        try:
            bluelet.run(self.processing())
        except KeyboardInterrupt:
            pass

class Client(object):
    def __init__(self):
        self.conf = Config()
        self.msg_type = 'MSG_CLIENT'

        # self.sock = ClientNetworking(self.conf.leader_host, self.conf.leader_port)
    
    def send_req(self):
        conn = yield bluelet.connect(self.conf.leader_host, self.conf.leader_port)
        print(conn.sock)

        while(True):
            yield bluelet.sleep(3)
            msg = [self.msg_type, 'hello']
            yield send_msg(conn, msg)

    def run_bluelet(self):
        try:
            bluelet.run(self.send_req())
        except KeyboardInterrupt:
            pass

def start_leader():
    leader = Leader()
    
    leader.run_bluelet()

def start_follower():
    follower = Follower()
    
    follower.run_bluelet()

def start_client():
    client = Client()
    
    client.run_bluelet()

if __name__ == '__main__':
    
    if(sys.argv[1] == 'leader'):
        print('leader')
        start_leader()
    elif(sys.argv[1] == 'client'):
        print('client')
        start_client()
    elif(sys.argv[1] == 'follower'):
        print('follower')
        start_follower()