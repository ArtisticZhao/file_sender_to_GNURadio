# coding: utf-8
'''
传输协议部分的实现, 包括上行帧处理; 下行数据解析
需求: bitstring
'''
from bitstring import BitArray
from call_c_lib import AES_C_Lib


class AOS_Frame(object):
    def __init__(self):
        # 初始化一个帧
        self.__frame_header = bytes(6)
        self.__data = bytes(208)
        self.__is_encrypt = False
        self.__aes = AES_C_Lib()

    def gen_frame_header(self, craft_id, virtual_channel_id,
                         virtual_channel_count, is_encrypt):
        # 输入类型检查
        # 范围检查, 首先定义了bit流的长度, 用overwrite函数时可保证长度(范围)安全
        h_craft_id = BitArray(8)
        h_virtual_channel_id = BitArray(6)
        h_virtual_channel_count = BitArray(24)
        h_is_encrypt = BitArray(1)

        h_craft_id.overwrite(craft_id, 0)
        h_virtual_channel_id.overwrite(
            BitArray(uint=virtual_channel_id, length=6), 0)
        h_virtual_channel_count.overwrite(
            BitArray(uint=virtual_channel_count, length=24), 0)
        h_is_encrypt.overwrite(is_encrypt, 0)
        header = BitArray()
        header.append('0b00')
        header.append(h_craft_id)
        header.append(h_virtual_channel_id)
        header.append(h_virtual_channel_count)
        header.append('0b00')
        header.append(h_is_encrypt)
        header.append('0b00000')
        if is_encrypt == '0b0':
            self.__is_encrypt = False
        else:
            self.__is_encrypt = True
        self.__frame_header = header.tobytes()

    def gen_frame(self):
        # 得到整个帧
        frame_data = bytes()
        encrypted_data = None
        if self.__is_encrypt:
            # 加密
            encrypted_data = self.__aes.encrypt(self.__data)
            frame_data = (self.__frame_header + encrypted_data)
        else:
            # 不加密
            frame_data = (self.__frame_header + self.__data)
        return frame_data

    def set_data_area(self, b_data):
        assert isinstance(b_data, bytes), \
            "type ERROR at: AOS_Frame.set_data_area"
        assert len(b_data) == 208, \
            "len ERROR at: AOS_Frame.set_data_area"
        self.__data = b_data

    def decode_frame(self, b_data):
        assert isinstance(b_data, bytes), \
            "type ERROR at: AOS_Frame.decode_frame"
        assert len(b_data) == 214, \
            "len ERROR at: AOS_Frame.decode_frame"
        f_data = dict()
        f_data['frame_header'] = self.decode_header(b_data[0:6])
        f_data['data'] = b_data[6:214]
        if f_data['frame_header']['is_encrypt'] == 1:
            # 加密 需解密
            f_data['data'] = self.__aes.decrypt(f_data['data'])

        return f_data

    def decode_header(self, b_header):
        assert isinstance(b_header, bytes), \
            "type ERROR at: AOS_Frame.decode_header"
        assert len(b_header) == 6, \
            "len ERROR at: AOS_Frame.decode_header"
        bit_header = BitArray(b_header)
        f_header = dict()
        f_header['version'] = BitArray(bin=bit_header.bin[0:2]).uint
        f_header['craft_id'] = BitArray(bin=bit_header.bin[2:10]).uint
        f_header['virtual_channel_id'] = BitArray(
            bin=bit_header.bin[10:16]).uint
        f_header['virtual_channel_count'] = BitArray(
            bin=bit_header.bin[16:40]).uint
        f_header['is_encrypt'] = BitArray(bin=bit_header.bin[42:43]).uint
        return f_header


class Up_Link(object):
    pass


# WARN test code
if __name__ == '__main__':
    # WARN test code
    a_frame = AOS_Frame()
    # print(a_frame.gen_frame())
    print(a_frame.gen_frame_header('0xaa', '0b001100', '0x10f', '0b0'))
