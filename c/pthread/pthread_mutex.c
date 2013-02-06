//用信号量进行同步
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <pthread.h>
#include <semaphore.h>

void * thread_function(void *arg);
#define WORK_SIZE 1024
char work_area[WORK_SIZE];
pthread_mutex_t work_mutex;     //对work_area和time_to_exit进行保护
int time_to_exit = 0;

int main(){
    
    int res;
    pthread_t a_thread;
    void *thread_rst;
    
    res = pthread_mutex_init(&work_mutex,NULL);
    if( res != 0 )
    {
        perror("pthread mutex init failed");
        exit(EXIT_FAILURE);
    }

    res = pthread_create(&a_thread,NULL,thread_function,NULL); //create!!!
    if(res != 0 )
    {
        perror("thread create failed");
        exit(EXIT_FAILURE);
    }

    //线程1：输入字符串
    pthread_mutex_lock(&work_mutex);
    printf("print some text ,Enter 'End' to finish\n");
    while(!time_to_exit)
    {
        fgets(work_area,WORK_SIZE,stdin);
        pthread_mutex_unlock(&work_mutex);
        while(1)
        {
            pthread_mutex_lock(&work_mutex);
            if(work_area[0]!='\0')
            {
                pthread_mutex_unlock(&work_mutex);
                sleep(1);
            }
            else
            {
                break;
            }
        }
    }
    pthread_mutex_unlock(&work_mutex);
    printf("\nwaiting for the thread to finish.....\n");

    //join 线程合并，收集信息
    res = pthread_join(a_thread,&thread_rst);
    if(res != 0 )
    {
        perror("thread join failed");
        exit(EXIT_FAILURE);
    }

    printf("thread joined, it returned %s\n",(char*)thread_rst);
    pthread_mutex_destroy(&work_mutex);

    exit(EXIT_SUCCESS);

}
void * thread_function(void *arg)
{
    sleep(1);
    pthread_mutex_lock(&work_mutex);

    while(strncmp("End",work_area,3)!=0)
    {
        printf("you input %d characters \n",strlen(work_area)-1);
        work_area[0]='\0';
        pthread_mutex_unlock(&work_mutex);
        sleep(1);
        pthread_mutex_lock(&work_mutex);
        while(work_area[0] == '\0')
        {
            pthread_mutex_unlock(&work_mutex);
            sleep(1);
            pthread_mutex_lock(&work_mutex);
        }
        pthread_mutex_unlock(&work_mutex);
    }
    time_to_exit = 1;
    work_area[0] = '\0';
    pthread_mutex_unlock(&work_mutex);
    pthread_exit("Thank you for the CPU time");
}
