# coding: utf-8
import re
from protocol.core_packet_protocol import AOS_Packet
from shared import cmd_code, settings
from tcp_core import kiss_frame
from protocol.KISS import KISS_Encoder_One_Frame
from PyQt5.QtWidgets import QMessageBox
from bitstring import BitArray, CreationError
from functions import save_aes_key


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


def cmd_set_speed(parent):
    '''
    设置天线接收速率
    '''
    aos_packet = AOS_Packet()
    index = parent.ui.comboBox_speed.currentIndex()
    speed = None
    if index == 0:
        print('[DEBUG]: 12kbps')
        speed = cmd_code['sys_speed']['12kbps']
    else:
        print('[DEBUG]: 100kbps')
        speed = cmd_code['sys_speed']['100kbps']
    b_data = aos_packet.gen_packet(cmd_code['set_speed'], b'\x01', speed)
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


def cmd_set_pre_file(parent):
    # 设置待操作文件
    prefile_no = parent.ui.prefile_no.text()
    if len(prefile_no) > 2 or len(prefile_no) == 0:
        QMessageBox.warning(parent, "Warning", "请输入00~0F之间的内容")
        return
    try:
        b = BitArray(hex=prefile_no).bytes
    except CreationError:
        QMessageBox.warning(parent, "Warning", "请输入00~0F之间的内容")

    aos_packet = AOS_Packet()
    b_data = aos_packet.gen_packet(cmd_code['set_prefile_no'], b'\x01', b)
    # 发前KISS
    k = KISS_Encoder_One_Frame()
    b_data = k.encode(b_data)
    # 发送
    kiss_frame.presend_cmd(b_data)


def cmd_del_file(parent):
    # 删除文件
    del_file_no = parent.ui.del_file_no.text()
    if len(del_file_no) > 2 or len(del_file_no) == 0:
        QMessageBox.warning(parent, "Warning", "请输入00~0F之间的内容")
        return
    try:
        b = BitArray(hex=del_file_no).bytes
    except CreationError:
        QMessageBox.warning(parent, "Warning", "请输入00~0F之间的内容")

    aos_packet = AOS_Packet()
    b_data = aos_packet.gen_packet(cmd_code['del_file'], b'\x01', b)
    # 发前KISS
    k = KISS_Encoder_One_Frame()
    b_data = k.encode(b_data)
    # 发送
    kiss_frame.presend_cmd(b_data)


def cmd_set_nid(parent):
    # 设置nid
    nid = parent.ui.nid.text()
    if len(nid) > 2 or len(nid) == 0:
        QMessageBox.warning(parent, "Warning", "请输入00~0F之间的内容")
        return
    try:
        b = BitArray(hex=nid).bytes
    except CreationError:
        QMessageBox.warning(parent, "Warning", "请输入00~0F之间的内容")

    aos_packet = AOS_Packet()
    b_data = aos_packet.gen_packet(cmd_code['set_nid'], b'\x01', b)
    # 发前KISS
    k = KISS_Encoder_One_Frame()
    b_data = k.encode(b_data)
    # 发送
    kiss_frame.presend_cmd(b_data)


def cmd_set_sat_block_num(parent):
    block_num = parent.ui.sat_block_num.text()
    try:
        block_num = int(block_num)
        b = BitArray(uint=block_num, length=16).bytes
    except (CreationError, ValueError):
        QMessageBox.warning(parent, "Warning", "请输入0~65535之间的内容")
    aos_packet = AOS_Packet()
    b_data = aos_packet.gen_packet(cmd_code['set_block_num'], b'\x02', b)
    # 发前KISS
    k = KISS_Encoder_One_Frame()
    b_data = k.encode(b_data)
    # 发送
    kiss_frame.presend_cmd(b_data)


def cmd_ftp_start(parent):
    '''
    FTP 开始传输
    '''
    aos_packet = AOS_Packet()
    b_data = aos_packet.gen_packet(cmd_code['ftp_start'], b'\x00', None)
    # 发前KISS
    k = KISS_Encoder_One_Frame()
    b_data = k.encode(b_data)
    # 发送
    kiss_frame.presend_cmd(b_data)


def cmd_ftp_stop(parent):
    '''
    FTP 停止传输
    '''
    aos_packet = AOS_Packet()
    b_data = aos_packet.gen_packet(cmd_code['ftp_stop'], b'\x00', None)
    # 发前KISS
    k = KISS_Encoder_One_Frame()
    b_data = k.encode(b_data)
    # 发送
    kiss_frame.presend_cmd(b_data)


def cmd_set_seed(parent):
    # 设置seed
    seed = parent.ui.Seed.toPlainText()
    seed = re.sub(r'\s+', '', seed)  # 去除空白字符
    if len(seed) != 32:
        QMessageBox.warning(parent, "Warning", "请输入16位hex的内容(可用空格分割)")
        return
    try:
        b = BitArray(hex=seed).bytes
    except CreationError:
        QMessageBox.warning(parent, "Warning", "请输入16位hex的内容(可用空格分割)")
    # save seed
    save_aes_key(parent)
    # update seed
    settings['aes_seed'] = b
    aos_packet = AOS_Packet()
    b_data = aos_packet.gen_packet(cmd_code['set_seed'], b'\x10', b)
    # 发前KISS
    k = KISS_Encoder_One_Frame()
    b_data = k.encode(b_data)
    # 发送
    kiss_frame.presend_cmd(b_data)


def cmd_get_status(parent):
    # 下传工参
    aos_packet = AOS_Packet()
    b_data = aos_packet.gen_packet(cmd_code['get_status'], b'\x00', None)
    # 发前KISS
    k = KISS_Encoder_One_Frame()
    b_data = k.encode(b_data)
    # 发送
    kiss_frame.presend_cmd(b_data)


def cmd_get_file_block(parent):
    # 下传文件数据块
    file_block = parent.ui.file_block.text()
    file_block = re.sub(r'\s+', '', file_block)  # 去除空白字符
    if len(file_block) != 16:
        QMessageBox.warning(parent, "Warning", "请输入8位hex的内容(可用空格分割)")
        return
    try:
        b = BitArray(hex=file_block).bytes
    except CreationError:
        QMessageBox.warning(parent, "Warning", "请输入8位hex的内容(可用空格分割)")

    aos_packet = AOS_Packet()
    b_data = aos_packet.gen_packet(cmd_code['get_file_block'], b'\x08', b)
    # 发前KISS
    k = KISS_Encoder_One_Frame()
    b_data = k.encode(b_data)
    # 发送
    kiss_frame.presend_cmd(b_data)


def cmd_switch_antenna(parent):
    # 切换天线至本机
    aos_packet = AOS_Packet()
    b_data = aos_packet.gen_packet(cmd_code['switch_antenna'], b'\x00', None)
    # 发前KISS
    k = KISS_Encoder_One_Frame()
    b_data = k.encode(b_data)
    # 发送
    kiss_frame.presend_cmd(b_data)
