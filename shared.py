# coding:utf-8
import queue

# shared object
KISS_encode_queue = queue.Queue()

status = {'GRC_Online': False, 'HCR_Online': False}

settings = {
    'craft_id': b'\x30',
    'virtual_channel_id': 1,
    'cmd_channel_id': 0,
    'is_encrypt': False,
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
    'set_speed': b'\xA1',
    'sys_speed': {
        '12kbps': b'\x55',
        '100kbps': b'\xAA'
    },
    'set_prefile_no': b'\x83',
    'del_file': b'\x84',
    'set_nid': b'\x85',
    'ftp_start': b'\x87',
    'ftp_stop': b'\x88',
    'set_seed': b'\x89',
    'get_status': b'\x91',
    'get_file_block': b'\x94',
    'switch_antenna': b'\xA0',
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
