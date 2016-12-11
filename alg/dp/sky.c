#include <stdio.h>
#include <stdlib.h>

const int x[]={-1,0,1,0},y[]={0,1,0,-1};

int pos[101][101];		//position
int val[101][101];		//long distance
int row,col;			//row,col

int ok(int i,int j)
{
	return (i>=1&&i<=row&&j>=1&&j<=col)?1:0;
}
int dp(int i,int j)
{
    int k=0;
	if (val[i][j]>0)
	{
		return val[i][j];
	}
	for(k=0;k<4;k++)
	{
		if (ok(i+x[k],j+y[k]) == 1)
		{
		    if (pos[i][j]>pos[i+x[k]][j+y[k]])
		    {
                if (val[i][j]<dp(i+x[k],j+y[k])+1)
                {
                    val[i][j] = dp(i+x[k],j+y[k])+1;
                }
		    }

		}
	}
	return val[i][j];
}


int main()
{
	int max =0,i,j;
	scanf("%d%d",&row,&col);

	for (i=1;i<=row;i++)
	{
		for (j=1;j<=col;j++)
		{
			scanf("%d",&pos[i][j]);

		}
	}
    for (i=1;i<=row;i++)
	{
		for (j=1;j<=col;j++)
		{
			val[i][j] = 0;
		}
	}

	for (i=1;i<=row;i++)
	{
		for (j=1;j<=col;j++)
		{
			if (max < dp(i,j))
			{
				max = dp(i,j);
			}
		}
	}
	printf("%d",max+1);

	return;
}
