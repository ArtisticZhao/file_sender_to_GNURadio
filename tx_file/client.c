#include<stdio.h>
#include<stdlib.h>
#include<errno.h>
#include<string.h>
#include<sys/types.h>
#include<netinet/in.h>
#include<sys/socket.h>
#include<sys/wait.h>

#define DEST_PORT 1500//目标地址端口号
#define DEST_IP "192.168.2.236"/*目标地址IP，这里设为本机*/
#define MAX_DATA 300//接收到的数据最大程度

int sockfd,new_fd;/*cocket句柄和接受到连接后的句柄 */

void main()
{
	uint32_t file_flag;
	unsigned char file_name[20];
	uint8_t len;
        memset(file_name,"\0",20);


    struct sockaddr_in dest_addr;/*目标地址信息*/
    char buf[MAX_DATA];//储存接收数据

    sockfd=socket(AF_INET,SOCK_STREAM,0);/*建立socket*/

    if(sockfd==-1)
    {
        printf("socket failed:%d",errno);
    }

    //参数意义见上面服务器端
    dest_addr.sin_family=AF_INET;
    dest_addr.sin_port=htons(DEST_PORT);
    dest_addr.sin_addr.s_addr=inet_addr(DEST_IP);
    bzero(&(dest_addr.sin_zero),8);


    if(connect(sockfd,(struct sockaddr*)&dest_addr,sizeof(struct sockaddr))==-1) //连接方法，传入句柄，目标地址和大小
    {
        printf("connect failed:%d",errno);//失败时可以打印errno
    }
    else
    {
        printf("connect success\n");
    }


	printf("input file name:");
	scanf("%s",file_name);
	printf("input file number:");
	scanf("%d",&file_flag);
	len = strlen(file_name);
        int dst = 0;
	new_trans(dst, file_name, len, file_flag);

   // close(sockfd);//关闭socket
    return 0;
}
