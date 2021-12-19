//动态规划初步问题：挖金子问题
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>

#define maxGold     100     //最大支持金矿数量
#define maxPeo      1000    //最大支持人员数量

#define BUF         50      //每一行缓冲
#define DEBUG       1       //调试开关

int goldNum;      //金矿数目
int peopleNum;  //最大人数
int Max=0;      //挖出最多金子，所要求解的量

int gold[maxGold];          //每个金矿，对应采集的金子数量
int people[maxGold];        //每个金矿，需要矿工数量

int maxMine[maxPeo][maxGold];            //备忘录，i个人挖前j个矿开采最大数量

void init();
int  goldMax(int p,int n);

int main()
{
    init();     //变量输入
    printf("Max:%d\n",goldMax(peopleNum,goldNum-1));
    exit(EXIT_SUCCESS);
}
void init()
{
    FILE *input=NULL;
    char tmp[BUF];      //存储每行情况
    char *line=NULL;
    char *idx=NULL;
    int i=0;

    if((input=fopen("beibao.in","r"))==NULL)
    {
        perror("file open");
        exit(EXIT_FAILURE);
    }
    line = fgets(tmp,BUF,input);
    if((idx = strchr(line,' '))==NULL)
    {
        printf("the input txt is error!!!\n");
        exit(EXIT_FAILURE);
    }
    *idx='\0';
    peopleNum = atoi(line);
    goldNum=atoi(idx+1);

    while((line=fgets(tmp,BUF,input))!=NULL)    //获取行串
    {
        idx=strchr(line,' ');
        *idx='\0';
        people[i]=atoi(line);
        gold[i++]=atoi(idx+1);
    }

    for(int m=0;m<=maxPeo;m++)  //此处容易出错 
    {
        for(int n=0;n<maxGold;n++)
        {
            maxMine[m][n]=-1;   //初始，表示位置数量   
        }
    }
}
int  goldMax(int p,int n)
{
    int ret;
    if(maxMine[p][n]!=-1)
    {
        //已经计算过的问题 
        ret = maxMine[p][n];   //备忘录
    }
    else if(0==n) //最后一个金矿
    {
        ret = (p>=people[n])?(gold[n]):(0);
#if DEBUG
        if(ret!=0)
        {
            //printf("开采%d金矿，需要%d人，可以挖掘%d金子，还剩%d人\n",n,people[n],gold[n],p-people[n]);
            printf("No:%d,NeedPeople:%d,Gold:%d,RePeople:%d\n",n,people[n],gold[n],p-people[n]);
        }
#endif
    }
    else if(p>=people[n])
    {
        ret = ((goldMax(p-people[n],n-1)+gold[n])>goldMax(p,n-1))?
            (goldMax(p-people[n],n-1)+gold[n]):
            (goldMax(p,n-1));
#if DEBUG
        if((goldMax(p-people[n],n-1)+gold[n])>goldMax(p,n-1))
        {
            printf("choice:: %d,in!!\n",n);
            printf("---------------->No:%d,NeedPeople:%d,Gold:%d,RePeople:%d\n",n,people[n],gold[n],p-people[n]);
        }
        else
        {
            printf("choice::%d,in!!\n",n-1);
        }
#endif
    }
    else
    {
        ret = goldMax(p,n-1);
#if DEBUG
        //printf("choice::%d,in!!\n",n-1);
       // printf("---------------->No:%d,NeedPeople:%d,Gold:%d,RePeople:%d\n",n,people[n],gold[n],p-people[n]);
#endif
    }
    maxMine[p][n]=ret;  //备忘录
    return ret;
}


