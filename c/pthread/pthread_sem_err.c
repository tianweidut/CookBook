//用信号量进行同步
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <pthread.h>
#include <semaphore.h>

void * thread_function(void *arg);
sem_t bin_sem;
#define WORK_SIZE 1024
char work_area[WORK_SIZE];

int main(){
    
    int res;
    pthread_t a_thread;
    void *thread_rst;
    
    res = sem_init(&bin_sem,0,0);   //初始化信号量:注意初始值设置 
    if( res != 0 )
    {
        perror("sem init failed");
        exit(EXIT_FAILURE);
    }

    res = pthread_create(&a_thread,NULL,thread_function,NULL); //create!!!
    if(res != 0 )
    {
        perror("thread create failed");
        exit(EXIT_FAILURE);
    }

    //线程1：输入字符串
    printf("print some text ,Enter 'End' to finish\n");
    while(strncmp("End",work_area,3)!=0)
    {
        if(strncmp("Fast",work_area,4)==0)
        {
            //sleep(1); 当对输入加上延时之后，统计线程有足够的时间完成统计
            sem_post(&bin_sem);
            strcpy(work_area,"tianwei....");
        }
        else
        {
            fgets(work_area,WORK_SIZE,stdin);
        }
        sem_post(&bin_sem);     //注意sem_post返回int型,软件中要进行返回值检验
    }
    printf("waiting for the thread to finish.....\n");

    //join 线程合并，收集信息
    res = pthread_join(a_thread,&thread_rst);
    if(res != 0 )
    {
        perror("thread join failed");
        exit(EXIT_FAILURE);
    }

    printf("thread joined, it returned %s\n",(char*)thread_rst);
    
    sem_destroy(&bin_sem);  //清理信号量占有的资源，如果试图清除被其他线程等待的信号量，则发生错误

    exit(EXIT_SUCCESS);

}
void * thread_function(void *arg)
{
    sem_wait(&bin_sem);
    
    while(strncmp("End",work_area,3)!=0)
    {
        printf("you input %d characters \n",strlen(work_area)-1);
        sem_wait(&bin_sem);
    }

    pthread_exit("Thank you for the CPU time");
}
