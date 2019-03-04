#include <stdint.h>
#ifndef __FTP_H__
#define __FTP_H__
#define DATA_LEN 256
#define _NAME_LEN_ 20
#define FAIL_NUM 10




typedef struct _TX_START_
{
	uint8_t head;
	uint32_t f_number;
	uint8_t name_len;
	uint8_t f_name[_NAME_LEN_];
	uint32_t f_size;
	uint32_t f_crc;
	uint16_t b_len;
	uint8_t pack_crc;
}_TX_START_;

typedef struct _BLOCK_
{
	uint8_t head;
	uint32_t f_number;
	uint32_t f_seq;
	uint16_t b_len;
	//uint16_t b_size[DATA_LEN];
	uint8_t block[DATA_LEN];
	uint8_t b_crc;
}_BLOCK_;

typedef struct _STATE_
{
    uint8_t head;
    uint32_t f_number;
    uint32_t rec_state;
    uint32_t fail_seq[FAIL_NUM];
    uint8_t pack_crc;
}_STATE_;

//void ftp_new_packet(unsigned char *data, int len);
void new_trans(int dst, unsigned char* file_name, uint8_t filename_len, uint32_t f_number);
char *fdir(char *fn);
void check(_TX_START_ *tx_start, unsigned char *frame_tx);
void filewrite(int dst, unsigned char *data, int len);
int file_read(_TX_START_ *tx, int N, int file_order, unsigned char *b_data);
int file_size(unsigned char *filename, int flag);


#endif // __FTP_H__
