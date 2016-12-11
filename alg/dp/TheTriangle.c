//DP basic problem From:POJ 1163
//从底向上进行分析，然后填充每一个位置

#include <stdio.h>
#include <stdlib.h>

const int max = 1000;

int main()
{
    int a[max][max];
    int i,j,k;

    for(i=0;i<max;i++)
        for(j=0;j<max;j++)
        {
            a[i][j] = 0;
        }

    int level = 0;
    scanf("%d",&level);


    //input
    for(i=1;i<level+1;i++)
    {
        for(j=0;j<i;j++)
        {
            scanf("%d",&a[i][j]);
        }
    }

    //buttom -> top
    for(i=level-1;i>0;i--)
        for(j=0;j<i;j++)
        {
            a[i][j] += ((a[i+1][j]>a[i+1][j+1])?a[i+1][j]:a[i+1][j+1]);
        }

    //print max
    printf("%d\n",a[1][0]);
}
