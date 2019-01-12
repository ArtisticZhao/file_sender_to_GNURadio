/*
 * 文件传输协议
 * 版本 1.0 
 * 参考设计rsync协议
 * 功能 应用层传输协议， 传输文件
 * 物理层： 无线 CAN总线
 */

typedef struct{
}frame_main_header;


/*
 * 功能： 存储到介质
 */
uint8_t save_to_file(uint8_t* pdata){
    uint8_t is_success;
    return is_success;
}
uint8_t CRC_interface(uint8_t* pdata){

}
