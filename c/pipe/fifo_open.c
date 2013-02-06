#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>
#include <unistd.h>

#define FIFO_NAME "./my_fifo"

int main(int argc,char *argv[])
{
    int res = 0;
    int open_mode = 0;
    int i = 0;

    if(argc<2)
    {
        fprintf(stderr,"Usage:%s <attr>",*argv);
        exit(EXIT_FAILURE);
    }

    for(i=1;i<argc;i++)
    {
        if(strncmp(*(++argv),"O_RDONLY",8)==0)
        {
            open_mode |= O_RDONLY;
        }
        if(strncmp(*(argv),"O_WRONLY",8)==0)
        {
            open_mode |= O_WRONLY;
        }
        if(strncmp(*(argv),"O_NONBLOCK",10)==0)
        {
            open_mode |= O_NONBLOCK;
        }
    }

    if(-1 == access(FIFO_NAME,F_OK))
    {
        res = mkfifo(FIFO_NAME,0777);
        if(0 == res)
        {
            printf("FIFO created\n");
            printf("Process %d \n",getpid());
            res = open(FIFO_NAME,open_mode);
            printf("Process %d result %d\n",getpid(),res);
            sleep(5);
            if(res != -1)
            {
                close(res);
            }
            printf("Process %d closed \n",getpid());
            exit(EXIT_FAILURE);
        }
    }
    exit(EXIT_FAILURE);
}
