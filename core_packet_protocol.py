# coding: utf-8
from bitstring import BitArray


class AOS_Packet(object):
    def __init__(self):
        self.__cmd_code = None
        self.__length = None
        self.__data = None
        self.__checksum = None

    def gen_packet(self, cmd_code, length, data):
        self.__cmd_code = cmd_code
        if length is not None:
            self.__length = length
        else:
            self.__length = b''
        if data is not None:
            self.__data = data
        else:
            self.__data = b''
        self.checksum()
        return self.__cmd_code + self.__length + self.__data + self.__checksum

    def checksum(self):
        assert isinstance(self.__cmd_code, bytes), \
            "type ERROR at: AOS_Packet.checksum"
        assert isinstance(self.__length, bytes), \
            "type ERROR at: AOS_Packet.checksum"
        assert isinstance(self.__data, bytes), \
            "type ERROR at: AOS_Packet.checksum"
        assert len(self.__cmd_code) == 1, \
            "len ERROR at: AOS_Packet.checksum"

        all_data = self.__cmd_code + self.__length + self.__data
        sum = 0
        for bit in all_data:
            sum += bit
        sum = sum % 256
        b = BitArray(uint=sum, length=8)
        b = ~b
        self.__checksum = b.tobytes()
