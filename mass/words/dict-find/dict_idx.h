#ifndef __DICT_IDX_
#define __DICT_IDX_

#include "dict_info.h"

#define IDX_DEBUG   1
#define IDX_EXT     "idx"

#define WORDSUM     60      //单词数目
#define WORDIDXSIZE 799     //索引长度
#define MaxSearch   (6+2)   //单词总数的对数求解

//描述词典信息
typedef struct 
{
    char word[100];     //单词
    int offset;         //偏移值
    int length;         //长度
}WORD_IDX;

//获取偏移值
static void *getWords(char *file,DICT_INFO *dict,WORD_IDX *idx);
//二分法搜索
WORD_IDX *getIdx(char *word,WORD_IDX *idx,DICT_INFO *dict);

inline static int toInt(unsigned char * fromInt);

#endif  //__DICT_IDX_ end
