#include <stdio.h>
#include <stdlib.h>

//The common subquence

enum Dire {Kinit=0,KUp,KLeft,KUpLeft};

void PrintLCS(int **A,int m,int n,char *pStr1,char *pStr2)
{
    if(pStr1 == NULL || pStr2 == NULL)
    {
        return;
    }

    int len1 = strlen(pStr1);
    int len2 = strlen(pStr2);

    if(A[m][n] == KUpLeft)
    {
        if(m>0&&n>0)
        {
            PrintLCS(A,m-1,n-1,pStr1,pStr2);
        }
        printf("%c",pStr1[m]);
    }
    else if(A[m][n] == KUp)
    {
        if(m>0)
        {
            PrintLCS(A,m-1,n,pStr1,pStr2);
        }
    }
    else
    {
        if(n>0)
        {
            PrintLCS(A,m,n-1,pStr1,pStr2);
        }
    }
}


int CalCommonSub(char* s1,char* s2)
{
    int ret = 0;
    int la = strlen(s1);
    int lb = strlen(s2);

    int i,j,k;

    int A[200][200];

    for( i=0;i<=la+1;i++)
        A[i][0] = 0;
    for(  i=0;i<=lb+1;i++)
        A[0][i] = 0;

    int dir[200][200];

    for(  i=1;i<=la;i++)
    {
        for(  j=1;j<=lb;j++)
        {
            if(s1[i-1] == s2[j-1])
            {
                A[i][j] = 1+ A[i-1][j-1];
                dir[i][j] = KUpLeft;
            }
            else
            {
                if(A[i-1][j]>A[i][j-1])
                {
                    A[i][j] = A[i-1][j];
                    dir[i][j] = KLeft;
                }
                else
                {
                    A[i][j] = A[i][j-1];
                    dir[i][j] = KUp;
                }

            }
        }
    }

    ret = A[la][lb];

    return ret;
}

int main()
{
    char a[200];
    char b[200];
    int ret = 0;
    while(scanf("%s %s",a,b)!=EOF)
    {
        ret = CalCommonSub(a,b);
        printf("%d\n",ret);
    }

    return 0;
}
