import argparse
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.top.client import *
from src.top.leader import *
from src.top.follower import *

"""
    python3 run.py --mode client
    python3 run.py --mode leader
    python3 run.py --mode follower
"""

def parse_args():
    # Parse input arguments
    desc = 'Run Distributed Computing System'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--mode', default='client', type=str, help='Mode of the device (client, leader, follower)')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()

    if(args.mode == 'client'):
        print('Client Deivce!')
        start_client()
    elif(args.mode == 'leader'):
        print('Leader Node!')
        start_leader()
    elif(args.mode == 'follower'):
        print('Follower Node!')
        start_follower()
    else:
        raise Exception('Invalid Mode Argument!')