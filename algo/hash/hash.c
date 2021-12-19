#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>

#define MAX     30  //��ϣ��洢�ռ�

typedef enum
{
    NULLKEY,    //û�м�¼
    HAVEKEY,    //�м�¼
    DELKEY      //�м�¼��ɾ��
}HAVEORNOT;

typedef struct
{
    int elem[MAX];              //������Ԫ��
    HAVEORNOT elemflag[MAX];    //Ԫ��״̬��־
    int count;                  //hash table��Ԫ�ظ���
}HashTable;
typedef struct
{
    int keynum;     //��¼�������򣬿��Խ�������
}Record;

void InitHash(HashTable *T);    //hash init
void CreateHash(HashTable *T);  //���봴��
void PrintHash(HashTable T);    //��ӡ
int  SearchHash(HashTable *T,int key ,int *pos);   //��hash�н��в���
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
        scanf(" %c",&ch); /*�������ѡ��*/

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
void CreateHash(HashTable *T)  //���봴��
{
    Record e;
    printf("��������������ϣ��:(-1����)");
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
void PrintHash(HashTable T)   //��ӡ
{
    for(int i=0;i<MAX;i++)
    {
        if(T.elemflag[i]==HAVEKEY)
        {
            printf("%4d\t%4d\n",i,T.elem[i])
        }
    }
}
int SearchHash(HashTable *T,int key ,int *pos)   //��hash�н��в���
{
    //���Ŷ�ַѰ��
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
