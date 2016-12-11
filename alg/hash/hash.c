#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>

#define MAX     30  //哈希表存储空间

typedef enum
{
    NULLKEY,    //没有记录
    HAVEKEY,    //有记录
    DELKEY      //有记录被删除
}HAVEORNOT;

typedef struct
{
    int elem[MAX];              //数据体元素
    HAVEORNOT elemflag[MAX];    //元素状态标志
    int count;                  //hash table中元素个数
}HashTable;
typedef struct
{
    int keynum;     //记录的数据域，可以进行扩充
}Record;

void InitHash(HashTable *T);    //hash init
void CreateHash(HashTable *T);  //输入创建
void PrintHash(HashTable T);    //打印
int  SearchHash(HashTable *T,int key ,int *pos);   //在hash中进行查找
int  InsertHash(HashTable *T,Record inRecord);
int  DelHash(HashTable *T,Record delRe);
int  Hash(int num);

void main()
{
    HashTable HT;
    char ch,j='y';
    int pos;
    Record Re;


    initHash(&HT);
    CreateHash(&HT);
    printf("the hash table!!!\n");
    while(j!='n')
    {
        printf("1.display\n");
        printf("2.search\n");
        printf("3.insert\n");
        printf("4.delete\n");
        printf("5.exit\n");
        scanf(" %c",&ch); /*输入操作选项*/

        switch(ch)
        {
            case '1':
                {
                    if(0!=HT.count)
                    {
                        PrintHash(HT);
                    }
                    else
                    {
                        printf("the hash table is empty\n");
                    }
                    break;
                }
            case '2':
                {
                    if(0==HT.count)
                    {
                        printf("the hash table is not delete\n");
                    }
                    else
                    {
                        printf("input you key of search:");
                        scanf("%d",&Re.keynum);
                        if(SearchHash(HT,Re.keynum,&pos))
                        {
                            printf("\nexist:%d\n",pos);
                        }
                        else
                        {
                            printf("\nthe element is not exist\n");
                        }
                    }
                    break;
                }
            case '3':
                {
                    if(HT.count==MAX)
                    {
                        printf("the hash is full\n");
                    }
                    else
                    {
                        printf("insert your element:");
                        scanf("%d",Re.keynum);
                        if(InsertHash(&HT,Re))
                        {
                            printf("success insert\n");
                        }
                        else
                        {
                            printf("fail to insert\n");
                        }
                    }
                    break;
                }
            case '4':
                {
                    printf("delete the element\n");
                    scanf("%d",&Re.keynum);
                    if(DelHash(&HT,Re))
                    {
                        printf("delete success\n");
                    }
                    else
                    {
                        printf("fail to del\n")
                    }
                    break;
                }
        default:
                {
                    j='n';
                    break;
                }
        }
    }
    printf("the program is over\n");
    getchar();
    exit(EXIT_SUCCESS);
}
void InitHash(HashTable *T)   //hash init
{
    T->count =0;
    for(int i=0;i<MAX;i++)
    {
        T->elemflag[i] = NULLKEY;
    }
}
void CreateHash(HashTable *T)  //输入创建
{
    Record e;
    printf("输入整数构建哈希表:(-1结束)");
    scanf("%d",&e.keynum);
    while(e.keynum!=-1)
    {
        if(InsertHash(T,e))
        {
            scanf("%d",&e.keynum);
        }
        else
        {
            printf("nonono\n");
            return;
        }
    }

}
void PrintHash(HashTable T)   //打印
{
    for(int i=0;i<MAX;i++)
    {
        if(T.elemflag[i]==HAVEKEY)
        {
            printf("%4d\t%4d\n",i,T.elem[i])
        }
    }
}
int SearchHash(HashTable *T,int key ,int *pos)   //在hash中进行查找
{
    //开放定址寻找
    *pos = hash(k);
    int p1=(*pos);
    while((T.elemflag[(*p)]==HAVEKEY)&&(k!=T.elem[(*p)]))
    {
        (*p)++;
        if((*p)>=MAX)
        {
            (*p)=(*p)%MAX;
        }
        if((*p)==p1)return 0;
    }
    if((k==T.elem[(*p)])&&(T.elemflag[(*p)]==HAVEKEY))
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
int  InsertHash(HashTable *T,Record inRecord)
{
    int p;
    if(SearchHash((*T),inRecord.keynum,&p))
    {
        return 0;
    }
    else
    {
        (*T).elemflag[p]=HAVEKEY;
        (*T).elem[p]=inRecord.keynum;
        (*T).count++;
        return 1;
    }
}
int DelHash(HashTable *T,Record delRe)
{
    int p;
    if(!SearchHash((*T),delRe.keynum,&p))
    {
        return 0;
    }
    else
    {
        (*T).elemflag[p]=DELKEY;
        (*T).count--;
        return 1;
    }

}
int  Hash(int num)
{
    return (num%11);
}
