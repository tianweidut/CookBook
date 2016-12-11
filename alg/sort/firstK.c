#include <stdio.h>
#include <stdlib.h>


int binary_search(int *array,int length, int s, int e,int k)
{
    int end = e;
    int mid = s;
    while(s<=e)
    {
        mid = s + (e-s)/2;
        
        if(array[mid]==k)
        {
            if(mid==end)
            {
                if(mid == length-1)
                    return -1;
                else
                    return binary_search(array,length,mid+1,e,k);

            }
            return binary_search(array,length,mid+1,e,k); 
        }
        else if(array[mid] > k)
        {
            e = mid-1;
        }
        else
        {
            s = mid+1;
        }
    }

    return (array[s]>k)?array[s]:(((s+1)>end)?-1:array[s+1]);

}


int  main()
{
    //int input[] = {1,2,3,4,5,6,7,7,7,7,7,9,9,10,20,40,45};
    int input[] = {1,2,3,4,5,6,7,7,7,7,8,9,10,11};
    
    int l = sizeof(input)/sizeof(input[0]);

    int result = 0,k=0;

    printf("%d\n",l);
    
    k = 7; 
    result = binary_search(input,l,0,l-1,k);
    printf("%d -> %d\n",k,result);

    k = 9; 
    result = binary_search(input,l,0,l-1,k);
    printf("%d -> %d\n",k,result);

    k = 4; 
    result = binary_search(input,l,0,l-1,k);
    printf("%d -> %d\n",k,result);
    
    k = 11; 
    result = binary_search(input,l,0,l-1,k);
    printf("%d -> %d\n",k,result);




    return 0;
}
