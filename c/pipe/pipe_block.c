#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main()
{
    FILE *read_fp = NULL;
    char buf[BUFSIZ+1];
    int chars_read;
    memset(buf,'\0',sizeof(buf));

    sprintf(buf,"once upon ...");
    read_fp = popen("uname -a","w");
    if(read_fp != NULL)
    {
        chars_read = fread(buf,sizeof(char),BUFSIZ,read_fp);
        if(chars_read>0)
        {
            buf[chars_read-1]='\0';
            printf("Reading %d-\n %s \n",BUFSIZ,buf);
            chars_read = fread(buf,sizeof(char),BUFSIZ,read_fp);
        }
        pclose(read_fp);
        exit(EXIT_SUCCESS);
    }
    exit(EXIT_FAILURE);

}
