# coding:utf-8
'''
@ 用于KISS解码功能
KISS 协议 数据包以C0开头 ，以C0结尾
当数据中有C0时， 以 DB DC替换
当数据中有DB时， 以 DB DD替换
'''
from copy import deepcopy

KISS_FEND = ord('\xC0')  # 192
KISS_FESC = ord('\xDB')  # 219
KISS_TFEND = ord('\xDC')  # 220
KISS_TFESC = ord('\xDD')  # 221


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
