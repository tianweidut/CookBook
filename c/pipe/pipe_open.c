#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main()
{
    FILE *read_fp = NULL;
    char buf[BUFSIZ+1];
    int chars_int;
    memset(buf,'\0',sizeof(buf));

    read_fp = popen("uname -a","r");
    if(read_fp != NULL)
    {
        chars_int = fread(buf,sizeof(char),BUFSIZ,read_fp);
        if(chars_int>0)
        {
            printf("Output was -\n%s\n",buf);
        }
        pclose(read_fp);
        exit(EXIT_SUCCESS);
    }
    exit(EXIT_FAILURE);

}
