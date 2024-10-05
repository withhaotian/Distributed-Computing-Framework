from collections import namedtuple

"""
    you can just define the message types here,
    and import them in other modules
"""

# Message Definition
""" Task request message from client to leader"""
RequestMsg = namedtuple(
    'RequestMsg',
    ['inputs']
)

""" Task result message from leader to client"""
ResultMsg = namedtuple(
    'ResultMsg',
    ['success', 'results']
)

""" Intermidiate message from leader to follower"""
Leader2FollowerMsg = namedtuple(
    'Leader2FollowerMsg',
    ['example']
)

""" Intermidiate message from follower to leader"""
Follower2LeaderMsg = namedtuple(
    'Follower2LeaderMsg',
    ['example']
)

""" Follower register with leader"""
class FollowerRegisterMsg(object):
    pass