#ifndef _DICT_INFO_H
#define _DICT_INFO_H

#define DICT_DEBUG   1   //调试开关
#define BUFSIZE 5000    //行缓冲区
#define IFO_EXT ".ifo"  //ifo文件后缀

typedef struct 
{
    char ver[100];      //版本信息
    int wordcnt;        //单词数量
    int idxFileSize;    //索引文件大小
    char bookname[100]; //词典名称
    char sameTypeSequence[10];  //
    char other[1000];   //其他信息

}DICT_INFO;

//词典解析，返回一个DICT_INFO结构体指针
DICT_INFO *getDictInfo(char *file);
//解析每行
static void parseLine(char *line,DICT_INFO *dict);

#endif  //end the _DICT_INFO_H
