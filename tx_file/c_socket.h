#ifndef C_SOCKET_H_INCLUDED
#define C_SOCKET_H_INCLUDED

int start_tcpserver(unsigned short port);
int wait_client_in(int server_sockfd);
int send_to_client(int client_sockfd, unsigned char* message, int len);
int recv_from_client(int client_sockfd, unsigned char* buf, int bufsize);
void close_all(int server_sockfd, int client_sockfd);
#endif // C_SOCKET_H_INCLUDED
