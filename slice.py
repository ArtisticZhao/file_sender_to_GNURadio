# coding:utf-8

# writen by yaojia@hit

# 将传入文件指针fp按block_length参数读出的迭代器,返回值为bytes类型

# 若剩下部分不足block_length长度，则由tail来补足


def slice(fp, block_length, tail):

    while 1:

        k = fp.read(block_length)

        # 够长就yield

        if block_length - len(k) == 0:

            yield k

        # 不够长则补足长度，并且结束这个迭代器

        else:

            for j in range(0, block_length - len(k)):

                k = k + bytes.fromhex(str(hex(tail))[2:])

                yield k

                return k


def main():  # 进行测试

    path = './test.bin'

    fp = open(path, 'rb')

    for n in slice(fp, 2, 0xc0):

        print(n)

    fp.close()


if __name__ == '__main__':

    main()
