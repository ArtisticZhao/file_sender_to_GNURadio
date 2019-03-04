#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void load_parms(char **argv, int *port, char *path);  // 读取运行参数

int main(int argc, char **argv)
{
    int listen_port = 0;  // tcpserver 端口
    char path[100] = {0}; // 传输文件路径
    if (argc == 5)
    {
        load_parms(argv, &listen_port, path);
        printf("f_path = %s\n", path);
        printf("l_port = %d\n", listen_port);
        int dst = 0;
        int file_flag = 255;
        new_trans(dst, path, strlen(path), file_flag);
    }
    else
    {
        // 返回使用说明
        printf("[-f path of file] [-p tcp server listen port]\n");
    }
    return 0;
}


void load_parms(char **argv, int *port, char *path)
{
    /*
        从运行参数中读入文件名字, 和tcpserver 端口号
    */
    for (int i = 1; i < 5; i += 2)
    {
        if (strcmp(argv[i], "-f") == 0)
        {
            strcpy(path, argv[i + 1]);
        }
        else if (strcmp(argv[i], "-p") == 0)
        {
            *port = atoi(argv[i + 1]);
        }
    }
}
