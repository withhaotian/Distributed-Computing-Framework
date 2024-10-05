from http import client
from pydoc import cli
import struct
import pickle
import socket
from threading import local
import bluelet

# Some random bytes to separate messages.
SENTINEL = b'\xd10\xdc%?0C\xaf\xb4:\xacs\x9e\xd5\xe31'

def recv_msg(sock):
    # Read message length and unpack it into an integer
    msg = yield sock.readline(SENTINEL, bufsize=64*1024*1024)
    if msg is None or SENTINEL not in msg:
        # `msg` can be None because of a questionable decision in
        # bluelet to return None from a socket operation when it raises
        # an exception. I should fix this sometime.
        yield bluelet.end()  # Socket closed.
    msg = msg[:-len(SENTINEL)]
    msg = decode_msg(msg)
    # return msg
    yield bluelet.end(msg)      # Analogous to return in ordinary Python.

def decode_msg(msg):
    res = pickle.loads(msg)
    return res

def encode_msg(data):
    msg = pickle.dumps(data)
    # print('length: ', len(msg), '-------------------')
    return msg

def send_msg(sock, msg):
    yield sock.sendall(encode_msg(msg) + SENTINEL)

class ClientNetworking():
    def __init__(self, host, port):
        self.host = host        # server host
        self.port = port        # server post
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # build connection
        self.s.connect((self.host, self.port))

    def send_msg(self, msg):
        send_msg(self.s, msg)

    def receive_msg(self):
        received = recv_msg(self.s)
        return received

    def close_channel(self):
        self.s.close()

class ServerNetworking():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((self.host, self.port))
        self.s.listen()

    def send_msg(self, conn, msg):
        send_msg(conn, msg)

    def receive_msg(self, conn):
        received = recv_msg(conn)
        return received

    def accept_conn(self):
        conn = self.s.accept()
        return conn

    def close_channel(self):
        self.s.close()
