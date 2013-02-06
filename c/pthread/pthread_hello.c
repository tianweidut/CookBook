#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <pthread.h>

void * thread_function(void *arg);
char msg[]="hello world";

int main(){
    
    int res;
    pthread_t a_thread;
    void *thread_rst;

    res = pthread_create(&a_thread,NULL,thread_function,(void*)msg); //create!!!
    if(res != 0 )
    {
        perror("thread create failed");
        exit(EXIT_FAILURE);
    }

    printf("waiting for thread to finish...\n");
    res = pthread_join(a_thread,&thread_rst);
    if(res != 0 )
    {
        perror("thread join failed");
        exit(EXIT_FAILURE);
    }

    printf("thread joined, it returned %s\n",(char*)thread_rst);
    printf("Message is now %s\n",msg);

    exit(EXIT_SUCCESS);

}
void * thread_function(void *arg)
{
    printf("thread_function is running ,Arg was %s\n",(char*)msg);
    sleep(1);
    strcpy(msg,"Bye!");
    pthread_exit("Thank you for the CPU time");
}
