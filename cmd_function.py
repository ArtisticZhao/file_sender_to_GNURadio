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
    print("[INFO]: 发送复位命令")
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
        print('[INFO]: 设置天线接收速率--12kbps')
        speed = cmd_code['sys_speed']['12kbps']
    else:
        print('[INFO]: 设置天线接收速率--100kbps')
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
        print('[INFO]: 缓存模式')
        mod = cmd_code['sys_mod']['buf_mod']
    elif index == 1:
        print('[INFO]: 实时转发模式')
        mod = cmd_code['sys_mod']['proxy_mod']
    elif index == 2:
        print('[INFO]: 数据注入模式')
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
        return
    print('[INFO]: 设置待操作文件: ', end="")
    print(' '.join(format(x, '02x') for x in b))

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
        return
    print('[INFO]: 删除文件: ', end="")
    print(' '.join(format(x, '02x') for x in b))

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
        return
    print("[INFO]: 设置nid: ", end="")
    print(' '.join(format(x, '02x') for x in b))
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
        return
    print("[INFO]: 设置星上包数: ", end="")
    print(' '.join(format(x, '02x') for x in b))

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
    print("[INFO]: FTP开始传输")
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

    print("[INFO]: FTP停止传输")
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
        return
    # save seed
    print("[INFO]: 设置seed: ", end="")
    print(' '.join(format(x, '02x') for x in b))

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


def cmd_send_hex(parent):
    # 这里利用了seed窗口进行hex发送, hex数据不经过数据包 直接进入数据帧
    seed = parent.ui.Seed.toPlainText()
    seed = re.sub(r'\s+', '', seed)  # 去除空白字符
    try:
        b = BitArray(hex=seed).bytes
    except CreationError:
        QMessageBox.warning(parent, "Warning", "请0~F的hex内容(可用空格分割)")
        return

    print("[INFO]: hex: ", end="")
    print(' '.join(format(x, '02x') for x in b))

    # 发前KISS
    k = KISS_Encoder_One_Frame()
    b_data = k.encode(b)
    # 发送
    kiss_frame.presend_cmd(b_data)


def cmd_get_status(parent):
    # 下传工参
    print("[INFO]: 下传工参")
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
        return
    print("[INFO]: 下传文件数据块: ", end="")
    print(' '.join(format(x, '02x') for x in b))

    aos_packet = AOS_Packet()
    b_data = aos_packet.gen_packet(cmd_code['get_file_block'], b'\x08', b)
    # 发前KISS
    k = KISS_Encoder_One_Frame()
    b_data = k.encode(b_data)
    # 发送
    kiss_frame.presend_cmd(b_data)


def cmd_switch_antenna(parent):
    # 切换天线至本机
    print("[INFO]: 切换天线至本机")
    aos_packet = AOS_Packet()
    b_data = aos_packet.gen_packet(cmd_code['switch_antenna'], b'\x00', None)
    # 发前KISS
    k = KISS_Encoder_One_Frame()
    b_data = k.encode(b_data)
    # 发送
    kiss_frame.presend_cmd(b_data)


def cmd_rf_ch_close(parent):
    # 射频通道关闭
    print("[INFO]: 射频通道关闭")
    aos_packet = AOS_Packet()
    b_data = aos_packet.gen_packet(cmd_code['rf_ch_close'], b'\x00', None)
    # 发前KISS
    k = KISS_Encoder_One_Frame()
    b_data = k.encode(b_data)
    # 发送
    kiss_frame.presend_cmd(b_data)


def cmd_gongcan_download_time(parent):
    # 30s工参下传
    aos_packet = AOS_Packet()
    index = parent.ui.gongcan_download_time_cb.currentIndex()

    if index == 0:
        print("[INFO]: 30s下传工参: 开")
        b_data = aos_packet.gen_packet(
            cmd_code['set_gongcan_download_time'], b'\x01',
            cmd_code['gongcan_download_time']['open'])
    elif index == 1:
        print("[INFO]: 30s下传工参: 关")
        b_data = aos_packet.gen_packet(
            cmd_code['set_gongcan_download_time'], b'\x01',
            cmd_code['gongcan_download_time']['close'])
    elif index == 2:
        cmd_rf_ch_close(None)
        return
    # 发前KISS
    k = KISS_Encoder_One_Frame()
    b_data = k.encode(b_data)
    # 发送
    kiss_frame.presend_cmd(b_data)
