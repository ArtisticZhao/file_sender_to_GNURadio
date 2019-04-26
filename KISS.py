# coding:utf-8
'''
@ 用于KISS解码功能
KISS 协议 数据包以C0开头 ，以C0结尾
当数据中有C0时， 以 DB DC替换
当数据中有DB时， 以 DB DD替换
'''

import time
import queue
from copy import deepcopy
from threading import Thread

from core_frame_protocol import AOS_Frame

from shared import KISS_encode_queue
from shared import settings, counters

KISS_FEND = ord('\xC0')  # 192
KISS_FESC = ord('\xDB')  # 219
KISS_TFEND = ord('\xDC')  # 220
KISS_TFESC = ord('\xDD')  # 221


class KISS_frame(Thread):
    def __init__(self):
        super().__init__()
        self.__shutdown = False
        self.b_data = b''  # 起始一个标识符
        self.sender = None
        self.temp = None
        self.timer_count = 0  # 定时器计数, 当数据不来的时候就等来10ms, 并加1, 达到值之后强行发送
        self.cmd_queue = queue.Queue()

    def set_sender(self, sender):
        # 设置发送器
        self.sender = sender

    def presend_cmd(self, b_data):
        '''
        准备发送命令, 将命令放入队列中, 带文件传输的空闲时期发送
        '''
        if self.__shutdown is True:
            # 文件没有发送, 直接发送指令
            aos_frame = AOS_Frame()
            aos_frame.gen_frame_header(
                settings['craft_id'], settings['cmd_channel_id'],
                counters[settings['cmd_channel_id']], '0b0')
            counters[settings['cmd_channel_id']] += 1  # 计数器自加
            # 发前KISS
            k = KISS_Encoder_One_Frame()
            send_data = k.encode(aos_frame.gen_frame())
            if len(send_data) < 208:
                while True:
                    send_data += b'\xC0'
                    if len(send_data) == 208:
                        break
                assert len(
                    send_data) == 208, "len error in KISS_frame.presend_cmd"
                self.sender.send(send_data)
        else:
            # 文件正在发送
            pass

    def run(self):
        while not self.__shutdown:
            if not KISS_encode_queue.empty():
                self.timer_count = 0  # 清空计数器
                # 得到一个新Byte
                b = KISS_encode_queue.get()
                '''# 判断是否需要转换
                if b == 0xC0:
                    b = b'\xDB\xDC'
                elif b == 0xDB:
                    b = b'\xDB\xDD'
                else:'''
                b = bytes([b])  # convert to bytes
                # 插入到发送队列中
                self.put_in_buf(b)
            else:
                if len(self.b_data) > 0:  # 缓冲区中有数据
                    time.sleep(0.01)  # 等待10ms
                    self.timer_count += 1
                    if (self.timer_count == 20):
                        self.force_full_buf()
                        self.sender_send()
                        self.timer_count = 0  # 清空计数器

    def put_in_buf(self, b_data):
        '''
        插入数据到self.b_data, 如果满了就打包发送
        '''
        assert isinstance(b_data, bytes),\
            "not bytes! at: KISS_frame.put_in_buf"
        assert len(b_data) == 2 or len(b_data) == 1,\
            "len ERROR at: KISS_frame.put_in_buf"
        '''
        这里分的情况:
            1.如皋余下的地方可以放入b_data则放入
            2.如果余下的位置不足把当前的数据帧中(data区最大长度208字节), 则放入可以放入的部分, 并发送
        '''
        if (208 - len(self.b_data) > len(b_data)):
            self.b_data += b_data
        elif (208 - len(self.b_data)) == 1:
            self.b_data += b_data[:1]  # 截取第一字节
            self.temp = b_data[1:]  # 截取第二字节
        else:
            raise NameError("some strange ERROR at: KISS_frame.put_in_buf")

        if (len(self.b_data) == 208):
            # 满包发送
            self.sender_send()

    def sender_send(self):
        assert len(self.b_data) == 208, "len ERROR at sender_send"
        # 满包发送
        aos_f = AOS_Frame()
        aos_f.gen_frame_header(settings['craft_id'],
                               settings['virtual_channel_id'],
                               counters[settings['virtual_channel_id']], '0b0')
        counters[settings['virtual_channel_id']] += 1
        aos_f.set_data_area(self.b_data)
        # 发前KISS
        k = KISS_Encoder_One_Frame()
        self.sender.send(k.encode(aos_f.gen_frame()))

        # 新的缓存区
        self.b_data = b''
        if self.temp is not None:
            self.b_data += self.temp
            self.temp = None

    def force_full_buf(self):
        '''
        当一包长度不足208yte 用C0填充满并发送
        '''
        if len(self.b_data) < 208:
            while True:
                self.b_data += b'\xC0'
                if len(self.b_data) == 208:
                    break
        else:
            raise NameError("some strange ERROR :KISS_frame.put_in_buf")

    def shutdown(self):
        '''
        停止该线程
        '''
        self.__shutdown = True


class KISS_Decoder():
    '''
    @ KISS协议解码器
    每次解码之后，会将包数据放入packets中， 因为网络有可能有残废包，但残废包是不能通过解包程序，可以直接无视掉
    '''

    def __init__(self):
        self.in_esc_mode = False
        self.data_buf = bytes()
        self.decoded_len = 0

    def AppendStream(self, stream_data):
        '''
        @ stream_data : kiss 编码的数据，只需要讲KISS数据帧，按照顺序通过
        stream_data传入，当解码完毕后会自动返回数据包，并重置解码器等待下一次解码
        '''
        for b in stream_data:
            if not self.in_esc_mode:
                if b == KISS_FEND:
                    if self.decoded_len != 0:
                        remsg = deepcopy(self.data_buf)  # 解码出一个包！！！
                        self.reset_kiss()
                        return remsg

                elif b == KISS_FESC:
                    self.in_esc_mode = True

                else:
                    self.data_buf += bytes([b])
                    self.decoded_len += 1

            else:
                if b == KISS_TFEND:
                    self.data_buf += b'\xc0'  # (KISS_FEND)
                elif b == KISS_TFESC:
                    self.data_buf += b'\xdb'  # (KISS_FESC)

                self.decoded_len += 1
                self.in_esc_mode = False

    def reset_kiss(self):
        '''
        @ 重置decoder
        '''
        self.data_buf = bytes()
        self.decoded_len = 0


class KISS_Encoder_One_Frame():
    def __init__(self):
        self.encoded_bytes = bytes()

    def encode(self, msg_bytes):
        self.encoded_bytes = msg_bytes
        i = len(msg_bytes) - 1
        while True:
            if i == -1:
                break
            if self.encoded_bytes[i] == int(0xc0):
                self.encoded_bytes = self.encoded_bytes[:i] \
                    + b'\xdb\xdc' +  \
                    self.encoded_bytes[i+1:]
            elif self.encoded_bytes[i] == int(0xdb):
                self.encoded_bytes = self.encoded_bytes[:i] \
                    + b'\xdb\xdd' +  \
                    self.encoded_bytes[i+1:]
            i -= 1
        self.encoded_bytes = b'\xc0' + self.encoded_bytes + b'\xc0'
        return self.encoded_bytes


if __name__ == '__main__':
    # e = KISS_Encoder_One_Frame()
    # b = b'\xc0\xbe\x12\xdd\xdb'
    # b = e.encode(b)
    # print(b)

    d = KISS_Decoder()
    b = b'\xc0\xdb\xdc\xbe\x12\xdd\xdb\xdd\xc0'
    b = d.AppendStream(b)
    print(b)
