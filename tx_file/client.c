#include<stdio.h>
#include<stdlib.h>
#include<errno.h>
#include<string.h>
#include<sys/types.h>
#include<netinet/in.h>
#include<sys/socket.h>
#include<sys/wait.h>

#define DEST_PORT 1500//Ŀ���ַ�˿ں�
#define DEST_IP "192.168.2.236"/*Ŀ���ַIP��������Ϊ����*/
#define MAX_DATA 300//���յ����������̶�

int sockfd,new_fd;/*cocket����ͽ��ܵ����Ӻ�ľ�� */

void main()
{
	uint32_t file_flag;
	unsigned char file_name[20];
	uint8_t len;
        memset(file_name,"\0",20);


    struct sockaddr_in dest_addr;/*Ŀ���ַ��Ϣ*/
    char buf[MAX_DATA];//�����������

    sockfd=socket(AF_INET,SOCK_STREAM,0);/*����socket*/

    if(sockfd==-1)
    {
        printf("socket failed:%d",errno);
    }

    //��������������������
    dest_addr.sin_family=AF_INET;
    dest_addr.sin_port=htons(DEST_PORT);
    dest_addr.sin_addr.s_addr=inet_addr(DEST_IP);
    bzero(&(dest_addr.sin_zero),8);


    if(connect(sockfd,(struct sockaddr*)&dest_addr,sizeof(struct sockaddr))==-1) //���ӷ�������������Ŀ���ַ�ʹ�С
    {
        printf("connect failed:%d",errno);//ʧ��ʱ���Դ�ӡerrno
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

   // close(sockfd);//�ر�socket
    return 0;
}
