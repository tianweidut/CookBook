#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main()
{
    FILE *write_fp = NULL;
    char buf[BUFSIZ+1];
    int chars_int;
    memset(buf,'\0',sizeof(buf));

    sprintf(buf,"once upon ...");
    write_fp = popen("od -c","w");
    if(write_fp != NULL)
    {
        chars_int = fwrite(buf,sizeof(char),BUFSIZ,write_fp);
        if(chars_int>0)
        {
            printf("Output was -\n%s\n",buf);
        }
        pclose(write_fp);
        exit(EXIT_SUCCESS);
    }
    exit(EXIT_FAILURE);

}
