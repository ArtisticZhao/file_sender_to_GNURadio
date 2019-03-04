#include <stdint.h>
#ifndef __CRC32_H__
#define __CRC32_H__

void csp_crc32_gentab(void);
uint32_t csp_crc32_memory(const uint8_t * data, uint32_t length, uint32_t crc);
uint8_t pack_crc(unsigned char *data, int len);

#endif
