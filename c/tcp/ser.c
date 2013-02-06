#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>

#include <arpa/inet.h>  //AF_INET使用
#include <netinet/in.h>
#include <netdb.h>
#include <string.h>

#define MAXSIZE 100
#define PORT    5000
#define BLOCK   5

void main(int argc,char *argv[])
{
    int server_sockfd,client_sockfd;
    int server_len,client_len;
    struct sockaddr_in server_add;
    struct sockaddr_in client_add;
    int read_cnt;
    char tmp[4];    //控制字
    char file_name[MAXSIZE];    //文件名
    char send[MAXSIZE];         //发送文件
    char recv[MAXSIZE];         //接收文件
    int opt =1;
   
    memset(file_name,'\0',MAXSIZE);
    //step1:建立套接字
    if(-1==(server_sockfd=socket(AF_INET,SOCK_STREAM,0)))
    {
        perror("socket Err");
        exit(EXIT_FAILURE);
    }

    //step2:实名绑定
    bzero(&server_add,sizeof(struct sockaddr_in));
    server_add.sin_family = AF_INET;
    server_add.sin_addr.s_addr =htonl(INADDR_ANY);
    server_add.sin_port = htons(PORT);
    server_len = sizeof(server_add);

    setsockopt(server_sockfd,SOL_SOCKET,SO_REUSEADDR,&opt,sizeof(opt));    //避免垃圾socket

    if(bind(server_sockfd,(struct sockaddr *)&server_add,server_len)<0)
    {   
        perror("bind Err");
        exit(EXIT_FAILURE);
    }

    //Step3:建立listen队列
    if(listen(server_sockfd,BLOCK)<0)
    {
        perror("listen Err");
        exit(EXIT_FAILURE);
    }

    //step4:获取accpet+具体相应过程
    while(1)
    {
        client_len = sizeof(client_add);
        client_sockfd = accept(server_sockfd,(struct sockaddr *)&client_add,&client_len);
        if(-1 == client_sockfd)
        {
            perror("Accept  Err");
            exit(EXIT_FAILURE);
        }
        printf("now Build the accept!\n");
        //对具体控制字相应

        read(client_sockfd,tmp,4);
       // read(client_sockfd,file_name,MAXSIZE);
        read(client_sockfd,file_name,MAXSIZE);

        printf("Cnt_Flag:%s,file_name:%s\n",tmp,file_name); 

        //FILE *fd=fopen(file_name,"rb");
        FILE *fd=fopen(file_name,"a+b");
        if(fd == NULL)
        {
            perror("Get Fopen Err");
            exit(EXIT_FAILURE);
        }

        if(0==strcmp(tmp,"get"))
        {
            printf("Client get file from local server!\n");
            while(!feof(fd))
            {
                int len=fread(send,1,MAXSIZE,fd);   //在文件中读取字符串到缓冲区
                write(client_sockfd,send,len);      //从缓冲区向client_sockfd写入信息
                printf("->");
            }
            printf("Send Success!\n");
        }
        else
        {
            printf("client send file to local server!\n");
            while(1)
            {
                read_cnt = read(client_sockfd,recv,MAXSIZE); //套接字向缓冲区写入
                
                if(0==read_cnt)
                {
                    break;
                }
                
                fwrite(recv,1,read_cnt,fd);     //向文件写入缓冲区内容
                printf("->");
            }
            printf("receive success!\n");
        }
        
        close(client_sockfd);
        fclose(fd);
    }
        
    exit(EXIT_SUCCESS);
}
