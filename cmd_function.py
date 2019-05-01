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
