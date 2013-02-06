//取消一个线程
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

    sleep(4);
    printf("canceling thread...\n");
    res = pthread_cancel(a_thread);
    if(res != 0)
    {
        perror("pthread cancel error!!\n");
        exit(EXIT_FAILURE);
    }
    printf("waiting for thread to finish...\n");
    res = pthread_join(a_thread,&thread_rst);
    if(res != 0 )
    {
        perror("thread join failed");
        exit(EXIT_FAILURE);
    }

    //printf("thread joined, it returned %s\n",(char*)thread_rst);//如果要打印，thread_rst为空，出现段错误
    printf("Message is now %s\n",msg);

    exit(EXIT_SUCCESS);

}
void * thread_function(void *arg)
{
    int i,res;
    res = pthread_setcancelstate(PTHREAD_CANCEL_ENABLE,NULL);
    if(res != 0 )
    {
        perror("thread set failed");
        exit(EXIT_FAILURE);
    }

    res = pthread_setcanceltype(PTHREAD_CANCEL_DEFERRED,NULL);
    if(res != 0 )
    {
        perror("thread cancel type failed");
        exit(EXIT_FAILURE);
    }

    printf("thread_function is running ,Arg was %s\n",(char*)msg);
    
    for(i=0;i<10;i++)
    {
        printf("thread is still running(%d)....\n",i);
        sleep(1);
    }
    
    sleep(1);
    strcpy(msg,"Bye!");//此时后面不会运行
    pthread_exit("Thank you for the CPU time");
    //pthread_exit(0);
}
