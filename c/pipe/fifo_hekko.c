#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>

int main()
{
    int res = mkfifo("tianwei003",0777);
    if(0 == res)
    {
        printf("FIFO created\n");
    }
    exit(EXIT_FAILURE);
}
