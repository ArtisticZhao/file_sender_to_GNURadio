# coding: utf-8
import time
import datetime
from bitstring import BitArray
from shared import cmd_code


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


class AOS_Telemetry_Packet(object):
    def __init__(self):
        self.gongcan = dict()

    def decode(self, b_data, sat):
        assert isinstance(b_data, bytes), \
            "ERROR TYPE at: AOS_Telemetry_Packet.decode"
        assert len(b_data) == 120, \
            "LEN ERROR at: AOS_Telemetry_Packet.decode"
        ba = BitArray(b_data[0:1])
        self.gongcan['配置状态'] = ba.hex
        ba = BitArray(b_data[1:2])
        if sat == cmd_code['cmd_A']:
            pass
        else:
            if ba.int == 1:
                self.gongcan['射频通道开关'] = '开'
            else:
                self.gongcan['射频通道开关'] = '关'
        ba = BitArray(b_data[2:3])
        self.gongcan['通道状态标识1'] = ba.hex
        ba = BitArray(b_data[3:4])
        if sat == cmd_code['cmd_A']:
            self.gongcan['通道状态标识2'] = ba.hex
        else:
            pass
        ba = BitArray(b_data[4:5])
        if sat == cmd_code['cmd_A']:
            self.gongcan['发射增益高字节'] = ba.hex
        else:
            self.gongcan['接收速率'] = ba.hex
        ba = BitArray(b_data[5:6])
        if sat == cmd_code['cmd_A']:
            self.gongcan['发射增益低字节'] = ba.hex
        else:
            pass
        ba = BitArray(b_data[6:7])
        if sat == cmd_code['cmd_A']:
            self.gongcan['+5V接收电流'] = str(ba.uint * 4) + 'mA'
        else:
            pass
        ba = BitArray(b_data[7:8])
        if sat == cmd_code['cmd_A']:
            self.gongcan['+5V接收电压'] = str(ba.uint / 32.0) + 'V'
        else:
            self.gongcan['+1V内核电压'] = str(ba.uint / 32.0) + 'V'
        ba = BitArray(b_data[8:9])
        if sat == cmd_code['cmd_A']:
            self.gongcan['+5V发射电流'] = str(ba.uint * 4) + 'mA'
        else:
            pass
        ba = BitArray(b_data[9:10])
        if sat == cmd_code['cmd_A']:
            self.gongcan['+5V发射电压'] = str(ba.uint / 32.0) + 'V'
        else:
            self.gongcan['+1.8V IO电压'] = str(ba.uint / 32.0) + 'V'

        ba = BitArray(b_data[10:11])
        if sat == cmd_code['cmd_A']:
            self.gongcan['+3.3V电流'] = str(ba.uint * 4) + 'mA'
        else:
            pass
        ba = BitArray(b_data[11:12])
        if sat == cmd_code['cmd_A']:
            self.gongcan['+3.3V电压'] = str(ba.uint / 32.0) + 'V'
        else:
            self.gongcan['+1.5V DDR3电压'] = str(ba.uint / 32.0) + 'V'
        ba = BitArray(b_data[12:16])
        self.gongcan['接收频偏1'] = str(ba.float) + 'Hz'
        ba = BitArray(b_data[16:20])
        self.gongcan['接收频偏2'] = str(ba.float) + 'Hz'

        ba = BitArray(b_data[20:24])
        self.gongcan['数字信号强度指示1'] = str(ba.float) + 'dB'
        ba = BitArray(b_data[24:28])
        self.gongcan['数字信号强度指示2'] = str(ba.float) + 'dB'

        ba = BitArray(b_data[28:29])
        if sat == cmd_code['cmd_A']:
            self.gongcan['模拟信号强度指示'] = ba.hex
        else:
            pass
        ba = BitArray(b_data[29:30])
        self.gongcan['PCB温度1'] = str(ba.int) + '℃'
        ba = BitArray(b_data[30:31])
        if sat == cmd_code['cmd_A']:
            self.gongcan['PCB温度2'] = str(ba.int) + '℃'
        else:
            pass
        ba = BitArray(b_data[31:32])
        if sat == cmd_code['cmd_A']:
            pass
        else:
            self.gongcan['剩余存储空间'] = str(ba.uint/128) + 'GB'
        ba = BitArray(b_data[32:33])
        if sat == cmd_code['cmd_A']:
            pass
        else:
            self.gongcan['CPU占用率'] = str(ba.int) + '%'

        ba = BitArray(b_data[33:34])
        self.gongcan['CAN发送包计数'] = ba.hex
        ba = BitArray(b_data[34:35])
        self.gongcan['CAN接收包计数'] = ba.hex
        ba = BitArray(b_data[35:36])
        self.gongcan['CAN错误包计数'] = ba.hex
        ba = BitArray(b_data[36:37])
        self.gongcan['CAN执行错误计数'] = ba.hex
        ba = BitArray(b_data[37:38])
        self.gongcan['CAN最近一条指令'] = ba.hex
        ba = BitArray(b_data[38:39])
        self.gongcan['CAN指令执行情况'] = ba.hex

        ba = BitArray(b_data[39:40])
        self.gongcan['RF发送包计数'] = ba.hex
        ba = BitArray(b_data[40:41])
        self.gongcan['RF发送抛弃包计数'] = ba.hex
        ba = BitArray(b_data[41:42])
        self.gongcan['RF接收包计数'] = ba.hex
        ba = BitArray(b_data[42:43])
        self.gongcan['RF接收错误包计数'] = ba.hex
        ba = BitArray(b_data[43:44])
        self.gongcan['RF接收执行错误计数'] = ba.hex
        ba = BitArray(b_data[44:45])
        if sat == cmd_code['cmd_A']:
            self.gongcan['RF接收纠错失败计数'] = ba.hex
        ba = BitArray(b_data[45:46])
        self.gongcan['RF最近一条指令'] = ba.hex
        ba = BitArray(b_data[46:47])
        self.gongcan['RF指令执行情况'] = ba.hex
        if sat == cmd_code['cmd_A']:
            ba = BitArray(b_data[47:51])
            self.gongcan['AGC寄存器'] = ba.uint
        else:
            ba = BitArray(b_data[47:49])
            self.gongcan['连续传输包数'] = ba.uint
            ba = BitArray(b_data[49:50])
            self.gongcan['信标使能标识'] = ba.uint
            ba = BitArray(b_data[50:51])
            self.gongcan['FTP当前接收文件号'] = ba.uint
        ba = BitArray(b_data[51:55])
        self.gongcan['FTP当前接收文件ID'] = ba.hex
        ba = BitArray(b_data[55:59])
        self.gongcan['FTP当前接收文件长度'] = str(ba.uint)
        ba = BitArray(b_data[59:63])
        self.gongcan['FTP当前接收文件校验值'] = ba.hex
        ba = BitArray(b_data[63:65])
        self.gongcan['FTP接收数据块大小'] = str(ba.uint)
        ba = BitArray(b_data[65:69])
        self.gongcan['FTP接收成功包数'] = str(ba.uint)
        ba = BitArray(b_data[69:73])
        self.gongcan['FTP接收缺失包数'] = str(ba.uint)

        ba = BitArray(b_data[73:74])
        self.gongcan['目标CAN节点地址'] = ba.hex
        ba = BitArray(b_data[74:75])
        self.gongcan['当前发送文件序号'] = ba.hex
        ba = BitArray(b_data[75:79])
        self.gongcan['当前发送文件长度'] = str(ba.uint)
        ba = BitArray(b_data[79:83])
        self.gongcan['当前发送文件校验值'] = ba.hex

        ba = BitArray(b_data[83:85])
        self.gongcan['FTP发送数据块大小'] = str(ba.uint)
        ba = BitArray(b_data[85:89])
        self.gongcan['FTP发送成功包数'] = str(ba.uint)
        ba = BitArray(b_data[89:93])
        self.gongcan['FTP发送缺失包数'] = str(ba.uint)
        ba = BitArray(b_data[93:97])
        self.gongcan['读取数据包计数'] = str(ba.uint)
        # ba = BitArray(b_data[97:101])
        # self.gongcan['注入数据计数'] = str(ba.uint)

        ba = BitArray(b_data[101:102])
        self.gongcan['复位计数'] = str(ba.uint)
        ba = BitArray(b_data[102:103])
        self.gongcan['复位标识'] = ba.hex
        if sat == cmd_code['cmd_A']:
            pass
        else:
            ba = BitArray(b_data[103:104])
            self.gongcan['接收文件备份状态'] = ba.hex

        ba = BitArray(b_data[104:108])
        self.gongcan['ARM运行时间'] = str(ba.uint) + 's'
        ba = BitArray(b_data[108:112])
        if sat == cmd_code['cmd_A']:
            self.gongcan['AVR运行时间'] = str(ba.uint) + 's'
        else:
            pass
        # 添加辅助信息
        self.gongcan['recv_time'] = datetime.datetime.now().strftime(
            '%Y-%m-%d %H:%M:%S.%f')
        self.gongcan['timestamp'] = int(time.time() * 1000)
        self.gongcan['sat'] = sat
        return self.gongcan


if __name__ == '__main__':
    import json
    b_data = b''
    atp = AOS_Telemetry_Packet()

    print(json.dumps(atp.decode(b_data), indent=2))
