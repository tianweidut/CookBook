#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>
#include "dict_info.h"

//词典解析，返回一个DICT_INFO结构体指针
//正确返回信息文件结构体，错误返回NULL
DICT_INFO *getDictInfo(char *file)
{
    FILE *ifo;
    char *line;
    char buffer[BUFSIZE];
    DICT_INFO *dict =(DICT_INFO *)malloc(sizeof(DICT_INFO));
    if(dict==NULL)
    {
        perror("error Dict");
        exit(EXIT_FAILURE);
    }
    if((ifo = fopen(file,"r+"))==NULL)
    {
        perror("fopen ifo!");
        exit(EXIT_FAILURE);
    }
    
    while((line=fgets(buffer,BUFSIZE,ifo))!=NULL)
    {
        parseLine(line,dict);
    }
    fclose(ifo);
    
    return dict;    
}
//解析每行,将信息装入特定字段
static void parseLine(char *line,DICT_INFO *dict)
{
    char *idx;
    if((idx=strchr(line,'='))!=NULL) //返回搜索开始的特定字符串
    {
        if(strstr(line,"version")!=NULL)
        {
            strcpy(dict->ver,idx+1);
        }
        else if(strstr(line,"wordcount")!=NULL)
        {
            dict->wordcnt = atoi(idx+1);
        }
        else if(strstr(line,"idxfilesize")!=NULL)
        {
            dict->idxFileSize=atoi(idx+1);
        }
        else if(strstr(line,"bookname")!=NULL)
        {
            strcpy(dict->bookname,idx+1);
        }
        else if(strstr(line,"sametypesequence")!=NULL)
        {
            strcpy(dict->sameTypeSequence,idx+1);
        }
        else
        {
            strcat(dict->other,line);
        }
    }
}

#if  DICT_DEBUG
int main(int argc,char **argv)
{
    DICT_INFO *tmp=getDictInfo("powerword2007_pwdnnjsj.ifo");
    if(tmp==NULL)
    {
        perror("get info err(main)");
        exit(EXIT_FAILURE);
    }
    
    
    printf("version:%s",tmp->ver);
    printf("bookname:%s",tmp->bookname);
    printf("wordcount:%d\n",tmp->wordcnt);
    printf("idxfilesize:%d\n",tmp->idxFileSize);
    printf("sts:%s\n",tmp->sameTypeSequence);
    printf("%s",tmp->other);
    free(tmp);

    exit(EXIT_SUCCESS);

}

#endif



