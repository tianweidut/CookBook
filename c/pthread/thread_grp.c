#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

#define NUM_THREADS 6
void *thread_function(void *arg);

int main()
{
    int res=0;
    pthread_t a_thread[NUM_THREADS];
    void *thread_rst=NULL;
    int i=0;

    for(i=0;i<NUM_THREADS;i++)
    {
        res = pthread_create(&(a_thread[i]),NULL,thread_function,(void*)&i);
        if(res!=0)
        {
            perror("Thread create failed");
            exit(EXIT_FAILURE);
        }

        sleep(1);
    }
    printf("waiting to finish...\n");
    for(i=NUM_THREADS-1;i>=0;i--)
    {
        res = pthread_join(a_thread[i],&thread_rst);
        if(res == 0)
        {
            printf("pick up the thread\n");
        }
        else
        {
            perror("pick up the thread error!");
        }
    }
    printf("\n--EOF--\n");
    exit(EXIT_SUCCESS);

}
void *thread_function(void *arg)
{
    int my_i = *((int *)arg);
    int rand_num;
    printf("thread_function is running ,Argure is %d\n",my_i);
    rand_num = 1+(9.0*rand()/(RAND_MAX+1.0));
    sleep(rand_num);
    printf("%d,says bye\n",my_i);
    pthread_exit(NULL);
}

