//��̬�滮�������⣺�ڽ�������
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>

#define maxGold     100     //���֧�ֽ������
#define maxPeo      1000    //���֧����Ա����

#define BUF         50      //ÿһ�л���
#define DEBUG       1       //���Կ���

int goldNum;      //�����Ŀ
int peopleNum;  //�������
int Max=0;      //�ڳ������ӣ���Ҫ������

int gold[maxGold];          //ÿ����󣬶�Ӧ�ɼ��Ľ�������
int people[maxGold];        //ÿ�������Ҫ������

int maxMine[maxPeo][maxGold];            //����¼��i������ǰj���󿪲��������

void init();
int  goldMax(int p,int n);

int main()
{
    init();     //��������
    printf("Max:%d\n",goldMax(peopleNum,goldNum-1));
    exit(EXIT_SUCCESS);
}
void init()
{
    FILE *input=NULL;
    char tmp[BUF];      //�洢ÿ�����
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

    while((line=fgets(tmp,BUF,input))!=NULL)    //��ȡ�д�
    {
        idx=strchr(line,' ');
        *idx='\0';
        people[i]=atoi(line);
        gold[i++]=atoi(idx+1);
    }

    for(int m=0;m<=maxPeo;m++)  //�˴����׳��� 
    {
        for(int n=0;n<maxGold;n++)
        {
            maxMine[m][n]=-1;   //��ʼ����ʾλ������   
        }
    }
}
int  goldMax(int p,int n)
{
    int ret;
    if(maxMine[p][n]!=-1)
    {
        //�Ѿ������������ 
        ret = maxMine[p][n];   //����¼
    }
    else if(0==n) //���һ�����
    {
        ret = (p>=people[n])?(gold[n]):(0);
#if DEBUG
        if(ret!=0)
        {
            //printf("����%d�����Ҫ%d�ˣ������ھ�%d���ӣ���ʣ%d��\n",n,people[n],gold[n],p-people[n]);
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
    maxMine[p][n]=ret;  //����¼
    return ret;
}


