# coding: utf-8
'''
传输协议部分的实现, 包括上行帧处理; 下行数据解析
需求: bitstring
'''
from bitstring import BitArray


class AOS_Frame(object):
    def __init__(self):
        # 初始化一个帧
        self.__sync_code = b'\x1A\xCF\xFC\x1D'
        self.__frame_header = bytes(6)
        self.__data = bytes(208)
        self.__RS_code = bytes(32)

    def gen_frame_header(self, craft_id, virtual_channel_id,
                         virtual_channel_count, is_encrypt):
        # 输入类型检查
        # 范围检查, 首先定义了bit流的长度, 用overwrite函数时可保证长度(范围)安全
        h_craft_id = BitArray(8)
        h_virtual_channel_id = BitArray(6)
        h_virtual_channel_count = BitArray(24)
        h_is_encrypt = BitArray(1)

        h_craft_id.overwrite(craft_id, 0)
        h_virtual_channel_id.overwrite(virtual_channel_id, 0)
        h_virtual_channel_count.overwrite(virtual_channel_count, 0)
        h_is_encrypt.overwrite(is_encrypt, 0)
        header = BitArray()
        header.append('0b00')
        header.append(h_craft_id)
        header.append(h_virtual_channel_id)
        header.append(h_virtual_channel_count)
        header.append('0b00')
        header.append(h_is_encrypt)
        header.append('0b00000')
        self.__frame_header = header.tobytes()

    def gen_frame(self):
        # 得到整个帧
        frame_data = bytes()
        frame_data = (self.__sync_code + self.__frame_header + self.__data +
                      self.__RS_code)
        return frame_data


class Up_Link(object):
    pass


# WARN test code
if __name__ == '__main__':
    # WARN test code
    a_frame = AOS_Frame()
    # print(a_frame.gen_frame())
    print(a_frame.gen_frame_header('0xaa', '0b001100', '0x10f', '0b0'))
