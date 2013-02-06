#include <iostream>

using namespace std;

int v[10000];
int w[10000];
int ret[10000];

int main()
{
    int caseCnt = 0;

    cin>>caseCnt;

    for(int i=0;i<caseCnt;i++)
    {
        int i,j;
        cin>>i>>j;

        ret[0] = 0;
        v[0] = 0;
        w[0] = 0;

        for(int k=1;k<=i;k++)
        {
            cin>>v[k];
            ret[k] = 0;
        }

        for(int k=1;k<=i;k++)
        {
            cin>>w[k];
        }

        for(int m=1;m<=i;m++)
        {
            for(int n=j;n>=0;n--)
            {
                ret[n] =(ret[n]>(ret[n-v[m]]+w[m])) ?(ret[n]):(ret[n-v[m]]+w[m]);
            }
        }

        cout<<ret[j];

    }

    return 0;
}
