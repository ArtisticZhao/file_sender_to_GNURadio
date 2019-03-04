#include "c_socket.h"
#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int start_tcpserver(unsigned short port)
{
    int server_sockfd; //服务器端套接字
    struct sockaddr_in my_addr;
	my_addr.sin_family = AF_INET;         //设置为IP通信
    my_addr.sin_addr.s_addr = INADDR_ANY; //服务器IP地址--允许连接到所有本地地址上
    my_addr.sin_port = htons(port);       //服务器端口号

    /*创建服务器端套接字--IPv4协议，面向连接通信，TCP协议*/
    if ((server_sockfd = socket(PF_INET, SOCK_STREAM, 0)) < 0)

    {
        perror("socket");
        return 1;
    }
    // 设置端口复用!
    int reuse0=1;
    if (setsockopt(server_sockfd, SOL_SOCKET, SO_REUSEADDR, (char *)&reuse0, sizeof(reuse0))==-1){
        perror("reuse");
        return 1;
    }
    /*将套接字绑定到服务器的网络地址上*/
    if (bind(server_sockfd, (struct sockaddr *)&my_addr, sizeof(struct sockaddr)) < 0)

    {
        perror("bind");
        return 1;
    }

    /*监听连接请求--监听队列长度为5*/
    listen(server_sockfd, 5);

    return server_sockfd;
}

int wait_client_in(int server_sockfd){
    struct sockaddr_in remote_addr; //客户端网络地址结构体
    int client_sockfd; //客户端套接字
    int sin_size = sizeof(struct sockaddr_in);
    if ((client_sockfd = accept(server_sockfd, (struct sockaddr *)&remote_addr, (socklen_t *)&sin_size)) < 0)

    {
        perror("accept");
        return 1;
    }
    printf("accept client %s\n", inet_ntoa(remote_addr.sin_addr));
    return client_sockfd;
}

int send_to_client(int client_sockfd, unsigned char* message, int len){
    return send(client_sockfd, message, len, 0);
}

int recv_from_client(int client_sockfd, unsigned char* buf, int bufsize){
    return recv(client_sockfd, buf, bufsize, 0);
}

void close_all(int server_sockfd, int client_sockfd){
    close(client_sockfd);
    close(server_sockfd);
}
