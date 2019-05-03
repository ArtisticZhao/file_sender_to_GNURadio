# coding:utf-8
import queue

# shared object
KISS_encode_queue = queue.Queue()

settings = {
    'craft_id': b'\x30',
    'virtual_channel_id': 1,
    'cmd_channel_id': 0,
}

cmd_code = {
    # 指令代码
    'reset': b'\x80',
    'set_mod': b'\x82',
    'sys_mod': {
        'buf_mod': b'\x00',
        'proxy_mod': b'\x55',
        'data_mod': b'\xAA'
    },
    # 信道代码
    'cmd_AB': 0,
    'cmd_A': 1,
    'cmd_B': 2,
}

# 不同信道的计数器
counters = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
}