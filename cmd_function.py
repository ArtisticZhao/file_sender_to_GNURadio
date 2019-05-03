# coding: utf-8
from core_packet_protocol import AOS_Packet
from shared import cmd_code
from tcp_core import kiss_frame
from KISS import KISS_Encoder_One_Frame


def cmd_reset(parent):
    '''
    发送复位命令
    '''
    aos_packet = AOS_Packet()
    b_data = aos_packet.gen_packet(cmd_code['reset'], b'\x00', None)
    # 发前KISS
    k = KISS_Encoder_One_Frame()
    b_data = k.encode(b_data)
    # 发送
    kiss_frame.presend_cmd(b_data)


def cmd_set_mod(parent):
    '''
    设置工作模式
    '''
    aos_packet = AOS_Packet()
    index = parent.ui.comboBox_mode.currentIndex()
    mod = None
    if index == 0:
        print('[DEBUG]: 缓存模式')
        mod = cmd_code['sys_mod']['buf_mod']
    elif index == 1:
        print('[DEBUG]: 实时转发模式')
        mod = cmd_code['sys_mod']['proxy_mod']
    elif index == 2:
        print('[DEBUG]: 数据注入模式')
        mod = cmd_code['sys_mod']['data_mod']
    else:
        print('[ERROR]: index ERROR')
    b_data = aos_packet.gen_packet(cmd_code['set_mod'], b'\x01', mod)
    # 发前KISS
    k = KISS_Encoder_One_Frame()
    b_data = k.encode(b_data)
    # 发送
    kiss_frame.presend_cmd(b_data)
