#include "ftp.h"
#include "crc32.h"
#include <stdio.h>
#include <inttypes.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

#define __GNU_RADIO_
//#include <math.h>
#ifdef __GNU_RADIO_
#include "c_socket.h"

int server_sockfd;
int client_sockfd;

#endif // __GNU_RADIO_

//#define DATA_LEN 256
#define _PATH_NAME_ "/home/lilac/Documents/transfile_test/tmp/rx.tmp"
#define N_ERRO 20
#define WAIT 0
#define PACK_LEN 256
#define MAX_DATA 300
//#define _NAME_LEN_ 20
//#define file_name 18121800


/*void ftp_new_packet(unsigned char *data, int len)
{
	remove(_PATH_NAME_);

	int ret = mkfifo(_PATH_NAME_,S_IFIFO | 0666);///
	//unsigned char buf[len];
	unsigned char trans_state;

	//memset(buf,'\0',sizeof(buf));
	trans_state = data[0];
	int fd = open(_PATH_NAME_,O_WRONLY);


	if(trans_state == 0xdd){
		ret = write(fd,data,len);
	}
	//else{
	//	ret = write(fd,,1);	//?????
	//}
	close(fd);
}*/

void ftp_packet_send(unsigned char *data, int len)
{

}

void new_trans(int dst, unsigned char *file_name, uint8_t filename_len, uint32_t f_number)
{
	unsigned char buf[100];
	memset(buf,'\0',sizeof(buf));
	_TX_START_ tx_start;
	_STATE_ trans_state;

	unsigned char frame_tx[30];
	unsigned char request_state[6];
	unsigned char data[12+DATA_LEN];
    uint8_t len = 0;
    extern int sockfd,new_fd;

		uint32_t ready_state;
		uint32_t rx_fnumber;

		int data_size;


		//filename_len = sizeof(file_name);////

		//frame_tx[0] = 0xaa;
//file NO.
    memset(&tx_start,0,sizeof(tx_start));
	tx_start.head = 0xaa;
	tx_start.f_number = f_number;
	tx_start.name_len = filename_len;
	memcpy((void*)tx_start.f_name, (void*)file_name, filename_len);
	tx_start.f_size = file_size(file_name, 1);
	tx_start.f_crc = file_size(file_name, 0);
	tx_start.b_len = DATA_LEN;
	//check(&tx_start, frame_tx);

    memcpy((void*)frame_tx, (void*)&(tx_start.head), 1);
	memcpy((void*)(frame_tx + 1), (void*)&(tx_start.f_number), 4);
	memcpy((void*)(frame_tx + 5), (void*)&(tx_start.name_len), 1);
	memcpy((void*)(frame_tx + 6), (void*)&(tx_start.f_name), tx_start.name_len);
	memcpy((void*)(frame_tx + 6 + tx_start.name_len), (void*)&(tx_start.f_size), 4);
	memcpy((void*)(frame_tx + 10 + tx_start.name_len), (void*)&(tx_start.f_crc), 4);
	memcpy((void*)(frame_tx + 14 + tx_start.name_len), (void*)&(tx_start.b_len), 2);
	uint8_t tx_len = tx_start.name_len + 16 + 1;
    frame_tx[tx_len - 1] = pack_crc(frame_tx, tx_len-1);



//request transmit state
	request_state[0] = 0xcc;
	memcpy((void*)(request_state + 1), (void*)&(tx_start.f_number), 4);
	request_state[5] = pack_crc(request_state, 5);

/////
	//FILE *fd = fopen(_PATH_NAME_, "wb");
	while(1)
	{
		////write(can_socket,frame_tx,filename_len+16+1);
		filewrite(dst, frame_tx, tx_len);
		printf("f_size: %x \n", tx_start.f_size);
		usleep(1000);
		////write(can_socket,request_state,sizeof(request_state));
		filewrite(dst, request_state, 6);

		sleep(1);
        #ifndef __GNU_RADIO_
		len = recv(sockfd, buf, MAX_DATA, 0);
		#else
		len = recv_from_client(client_sockfd, buf, MAX_DATA);
		#endif // __GNU_RADIO_
		printf("Received: ");
		for (int i = 0; i < len; i++ ){
            printf("%x, ", buf[i]);
        }
        printf("\n");

		if(pack_crc(buf, len) == 0){
           // trans_state.head = buf[0];
           if(buf[0] == 0xdd){
                memcpy((void*)&trans_state.f_number,(void*)(buf + 1), 4);
                memcpy((void*)&trans_state.rec_state,(void*)(buf + 5), 4);
                if(trans_state.f_number == tx_start.f_number){
                    if(trans_state.rec_state == 0xfffffffe){
                        break;
                    }else if(trans_state.rec_state == 0xffffffff){
                        continue;
                    }else{
                        memcpy((void*)&trans_state.fail_seq, (void*)(buf + 9), trans_state.rec_state);
                        break;
                    }
                }else
                    continue;
           }else
                continue;
		}
		else
			continue;
	}
//           ready state

	int N;
	if(tx_start.f_size%DATA_LEN == 0)
		N = tx_start.f_size/DATA_LEN;
	else
		N = tx_start.f_size/DATA_LEN + 1;
    printf("block_num: %d \n", N);

	unsigned char loss_data[FAIL_NUM];

	//for(int i = 0; i < N; i++){
    while(1){

        int i = 0;
        printf("i = : %d\n", i);

        if(i%10 == 0 || i == N - 1){
            filewrite(dst, request_state, 6);
          //  usleep(1000);
            #ifndef __GNU_RADIO_
            len = recv(sockfd, buf, MAX_DATA, 0);
            #else
            len = recv_from_client(client_sockfd, buf, MAX_DATA);
            #endif
            usleep(1000);
            printf("i = : %d\n", i);
        }

        usleep(100000);
       // len = recv(sockfd, buf, MAX_DATA, 0);
        if (pack_crc(buf, len) == 0){

            printf("rec_file:\n");
            for (int i = 0; i < len; i++ ){
                printf("%x, ", buf[i]);
            }
            printf("\n");

            if(buf[0] = 0xdd){
                memcpy((void*)&ready_state,(void*)(buf + 5), 4);
                if(ready_state == 0x00000000){
                    printf("send finished");
                    break;
                }else if(ready_state == 0xffffffff){
                    printf("error");
                }else{
                    uint32_t loss_N;
                    uint32_t loss_OR;
                    if(ready_state == 0xfffffffe){
                        loss_N = 10;
                    }else
                        loss_N = ready_state;
                    for(int j = 0; j < loss_N; j++){

                        memcpy((void*)&loss_OR, (void*)(buf+9+j*4), 4);
                        data_size = file_read(&tx_start, N, loss_OR, data);//loss number
                        filewrite(dst, data, data_size);
                        usleep(100000);
                    ////write(can_socket,&loss_data,sizeof(loss_data));
                    }

                }
            }
            i++;
        }

     //   usleep(1000000);

		//data_size = file_read(&tx_start, N, i, data);
		///write(can_socket,data,data_size);

		//printf("send_len: %d", data_size);

	}
}

int file_size(unsigned char *filename, int flag)
{
	//char fileDir[] = "/home/lilac/Documents/filename";
	unsigned char data[PACK_LEN];
	uint32_t crc = 0xFFFFFFFF;

	char name;
	FILE *fp = fopen((filename),"r");  // FILE *fp = fopen(fdir(filename),"r");
//	FILE *fp = fopen("/home/lilac/Documents/transfile_test/trans_file/20180623","rb+");
	uint32_t size;
	uint16_t len;
	uint16_t N;
	if(fp == NULL ){
		printf("\nerror on open file!");
		exit(1);
	}
	else{
            fseek(fp, 0, SEEK_END);
            size = ftell(fp);

		if (flag == 1){
            //fseek(fp, 0 , 0);
            //fread(data, 1, size, fp);
			fclose(fp);
			return size;

		}else{
		    if(size%PACK_LEN == 0)
                N = size/PACK_LEN;
            else
                N = size/PACK_LEN + 1;
		    //size/PACK_LEN
			//fseek(fp, 0, 0);
			for(int i = 0; i < N; i++){

			    if (size%PACK_LEN != 0 && i == N - 1){
                    len = size%PACK_LEN;
                }else
                    len = PACK_LEN;

                fseek(fp, i*PACK_LEN, 0);
                fread(data, 1, len, fp);

                crc = csp_crc32_memory(data, len, crc);
			}
			fclose(fp);
			return crc;
		}
	}
}

int file_read(_TX_START_ *tx, int N, int file_order, unsigned char *b_data)
{
	//char fileDir[] = "/home/lilac/Documents/filename";
	//_BLOCK_ data;
	int last_size;
	int b_size;
	//int read_data;

	last_size = tx->f_size - (N-1)*DATA_LEN;

	if(file_order < N){
        b_size = DATA_LEN;
	}else{
        b_size = last_size;
	}


	char buffer[DATA_LEN];

	//read_loc = file_order*DATA_LEN;

	FILE *fp = fopen(fdir(tx->f_name),"r");
	fseek(fp, file_order * tx->b_len, 0);
	fread(buffer, b_size, 1, fp);
	fclose(fp);

	printf("send data: %d \n", file_order);
	for(int i = 0; i < b_size; i++) {
            printf("%c", buffer[i]);
	}
	printf("\n");
    printf("b_size: %x \n", b_size);

	b_data[0] = 0xbb;
	memcpy((void*)(b_data + 1), (void*)&(tx->f_number), 4);
	memcpy((void*)(b_data + 5), (void*)&file_order, 4);
	memcpy((void*)(b_data + 9), (void*)&b_size, 2);
	memcpy((void*)(b_data + 11), (void*)buffer, b_size);
	b_data[11+b_size] = pack_crc(b_data, 11 + b_size);
	b_size = b_size + 12 ;
	return b_size;
}
#ifndef __GNU_RADIO_
void filewrite(int dst, unsigned char *data, int len)
{
	/*remove("/home/lilac/Documents/transfile_test/tmp/tx.tmp");
	int ret = mkfifo("/home/lilac/Documents/transfile_test/tmp/tx.tmp",S_IFIFO | 0666);
	int fp = open("/home/lilac/Documents/transfile_test/tmp/tx.tmp",O_WRONLY);
	ret = write(fp, data, len);
	close(fp);*/

   // recv(sockfd,buf,MAX_DATA,0);//œ«œÓÊÕÊýŸÝŽòÈëbuf£¬²ÎÊý·Ö±ðÊÇŸä±ú£¬Ž¢ŽæŽŠ£¬×îŽó³€¶È£¬ÆäËûÐÅÏ¢£šÉèÎª0ŒŽ¿É£©¡£
   // printf("Received: %s\n",buf);
     extern int sockfd,new_fd;/*cocket句柄和接受到连接后的句柄 */
     send(sockfd, data,len,0);

}
#else
void filewrite(int dst, unsigned char *data, int len){
	static char is_running;
	// static int server_sockfd;
    // static int client_sockfd;
	if(is_running != 'o'){
		// server not running
		// start server
		server_sockfd = start_tcpserver(9999);
		// waiting GNU Radio connect
		client_sockfd = wait_client_in(server_sockfd);
		is_running = 'o';
	}
	if(len != 0){
		//send something
		send_to_client(client_sockfd, data, len);
	}else{
		close_all(server_sockfd, client_sockfd);
	}
}
#endif
/*void check(_TX_START_ *tx_start, unsigned char *frame_tx)
{
	unsigned char num = 0;
	unsigned char crc;
	memcpy((void*)frame_tx, (void*)&(tx_start->head), 1);
	memcpy((void*)(frame_tx + 1), (void*)&(tx_start->f_number), 4);
	memcpy((void*)(frame_tx + 5), (void*)&(tx_start->name_len), 1);
	memcpy((void*)(frame_tx + 6), (void*)&(tx_start->f_name), tx_start->name_len);
	memcpy((void*)(frame_tx + 6 + tx_start->name_len), (void*)&(tx_start->f_size), 4);
	memcpy((void*)(frame_tx + 10 + tx_start->name_len), (void*)&(tx_start->f_crc), 4);
	memcpy((void*)(frame_tx + 14 + tx_start->name_len), (void*)&(tx_start->b_len), 2);

	for (int i = 0; i < 16 + tx_start->name_len; i++){
		num = num + frame_tx[i];
	}
	crc = ~(num % 256);
	memcpy((void*)(frame_tx + 16 + tx_start->name_len), (void*)&crc, 1);
	//return ~(num % 256);
}*/

unsigned char path_name[300];
char *fdir(char *fn)
{
	//char *path_name = (char*)malloc(300);
	strcpy(path_name, "/home/lilac/Documents/transfile_test/trans_file/");
	strcat(path_name, fn);
	return path_name;
}

/*void main()
{
	uint32_t file_flag;
	unsigned char file_name[20];
	uint8_t len;
    memset(file_name,"\0",20);

	printf("input file name:");
	scanf("%s",file_name);
	printf("input file number:");
	scanf("%d",&file_flag);
	len = strlen(file_name);
    int dst = 0;
	new_trans(dst, file_name, len, file_flag);

}*/
