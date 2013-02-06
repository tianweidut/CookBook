#include <stdlib.h>
#include <stdio.h>
#include <string.h>
//#include "dict_info.h"
#include "dict_idx.h"

//获取偏移值
static void *getWords(char *file,DICT_INFO *dict,WORD_IDX *idx)
{
    FILE *fs;
    size_t nread=0;
    if(dict==NULL)
    {
        return NULL;
    }
    
    if((fs=fopen(file,"rb"))==NULL)
    {
        perror("getwords open!");
        exit(EXIT_FAILURE);
    }
    unsigned char buffer[dict->idxFileSize];
    nread = fread(buffer,dict->idxFileSize,1,fs);   //获取索引文件大小-->buffer

    unsigned char *head;
    unsigned char *tail;
    head=tail=buffer;

    int it=0;
    int total=1;
    for(it=0;it<dict->idxFileSize;it++)
    {
        if((*head)=='\0')
        {
            strncpy((idx+total)->word,tail,head-tail+1);
            (idx+total)->offset=toInt(head+1);
            (idx+total)->length=toInt(head+5);
            total++;
            head+=9;
            tail=head;
            
            if(total==dict->wordcnt)
            {
                break;
            }
        }
        else
        {
            head++;
            continue;
        }
    }

}
//二分法搜索
WORD_IDX *getIdx(char *word,WORD_IDX *idx,DICT_INFO *dict)
{
    if((word==NULL)||(idx==NULL)||(dict==NULL))
    {
        return NULL;
    }
    int head=0;
    int tail=dict->wordcnt;
    int cur=tail/2;
    int cnt = 0;        //二分法，查找次数

    while(1)
    {
        int cmp = strcasecmp(word,idx[cur].word); //
        if(0==cmp)
        {
            return &idx[cur];
        }
        else if(0>cmp)
        {
            tail = cur;
        }
        else
        {
            head = cur;
        }
        cnt ++;

        cur = (tail+head)>>1;

        //根据二分法的分析情况，若搜索不到，最后会停留在cmp=1时，此时寻找的次数超过了二分法查找最大次数
        if(cnt>MaxSearch)
        {
            printf("对不起，此词未收录\n");
            return NULL;
        }
    }
}

inline static int toInt(unsigned char * i)
{
    return *(i+3)+(*(i+2)<<8)+(*(i+1)<<16)+(*(i)<<24);
}

#if IDX_DEBUG
int main(int argc,char **argv)
{
    //char *filename = "test.idx";
    //char *dictname = "test.dict";
    char *filename = "source.idx";
    char *dictname = "source.dict";

    DICT_INFO dict;
    dict.wordcnt =WORDSUM;//452185 ;
    dict.idxFileSize =WORDIDXSIZE;// 10106758;

    WORD_IDX *idx=(WORD_IDX*)malloc((sizeof(WORD_IDX))*(dict.wordcnt));
    if(idx==NULL)
    {
        perror("idx malloc free");
        exit(EXIT_FAILURE);
    }
    getWords(filename,&dict,idx);
   // WORD_IDX *word=getIdx(argv[1],idx,&dict);
    char im[80];
    printf("input:");
    scanf("%s",im);
    WORD_IDX *word=getIdx(im,idx,&dict);

    if(word==NULL)
    {
        //此时未收录此单词
        exit(EXIT_SUCCESS);
    }
    printf("%s,%d,%d\n",word->word,word->offset,word->length);

    FILE *dictfile = fopen(dictname,"r+");
    if(dictfile==NULL)
    {
        perror("dict open");
        exit(EXIT_FAILURE);
    }

    if(0 != fseek(dictfile,word->offset,SEEK_SET))  //词典文件开始
    {
        perror("fseek open");
        exit(EXIT_FAILURE);
    }

    char explain[word->length+1];
    memset(explain,'\0',word->length+1);
    fread(explain,word->length,1,dictfile);
    printf("%s\n",explain);
    free(idx);

    exit(EXIT_SUCCESS);
}

#endif

