# coding: utf-8
from core_packet_protocol import AOS_Packet
from shared import cmd_code
from tcp_core import kiss_frame


def cmd_reset(parent):
    '''
    发送复位命令
    '''
    aos_packet = AOS_Packet()
    b_data = aos_packet.gen_packet(cmd_code['reset'], None, None)
    # 发送
    kiss_frame.presend_cmd(b_data)
