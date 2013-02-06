#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <ctype.h>   //tolower
#include <sys/types.h>
#include <sys/stat.h>

#include "dict_idx.h"   //不规则动词索引

#define DEBUG 1     //调试开关按钮
#define WORDNum     200     //文中单词数量
#define WORDLen     20      //每个单词最大长度

#define YES     1
#define NO      0

const char *filename = _IDX_NAME;
const char *dictname = _DICT_NAME;

struct wordFlag
{
    int pos;    //快排中所处位置
    int flag;   //是否被转化 
};

int explainWord(char *src,WORD_IDX *word);

int main(void)
{
    int c=0;
    char *cpBuffer=NULL;    //输入字符串,未指定大小（关键点）
    int num=0;
    FILE *inFile=NULL;      //原始写入文件指针
    FILE *outFile=NULL;     //读入文件指针
    FILE *writeFile=NULL;   //结果写入文件
    long FileSize=0;           //文件长度
    char *readBuffer=NULL;  //读取文件字符串指针
    int wordsum;            //预测单词长度
    int wordcnt=0;
    int alpha = 0;
    WORD_IDX idx[60];
    
    printf("===============words recongnize=====================\n");
    printf("Step1:-------->end the char:~\n");

    //step1:根据缓冲区大小，动态产生数组
    c=getchar();  
    for( num=0;num<BUFSIZ;num++)
    {
        if(*(stdin->_IO_buf_base+num)=='~')   //当遇到~时结束输入
        {
            break;
        }
    }
    
    //申请空间
    if((cpBuffer=(char*)malloc(num*sizeof(char)+1))==NULL)
    {
        perror("CpBuffer malloc address!\n");
        exit(EXIT_FAILURE);
    }
    //字符串填充
    memcpy(cpBuffer,stdin->_IO_buf_base,(num?num:1));   //
    *(cpBuffer+num)='\0';

#if DEBUG
    printf("<------------------------------------------>\n");
    printf("%s\n",cpBuffer);
#endif
    
    //step2:输入文件
   if((inFile=fopen("input.txt","a+"))==NULL)
   {
       printf("\n error in:input.txt create\n");
       perror("fopen error!");
       exit(EXIT_FAILURE);
   } 
   fwrite(cpBuffer,strlen(cpBuffer),1,inFile);
   fclose(inFile);

    //stpe3:文件中读取(基本处理)
    if((outFile=fopen("input.txt","r"))==NULL)
    {
        printf("\nerror in:input open\n");
        perror("foen error!2");
        exit(EXIT_FAILURE);
    }
    
   // fseek(outFile,0,SEEK_END);      //获取文件长度
   // FileSize = ftell(outFile);
   // rewind(outFile);                
    //FileSize --> 字符总数
  //  wordsum = FileSize;          

    //此处FileSize为文件中字符总数
    char *words[WORDNum+1];    //此处可以根据文中字符书目+单词长度进行计算，避免浪费不必要的空间
                               //存储每个合法单元 
    char *wordsTmp[WORDNum+1]; //变化之后的词形存储
    for(int i=0;i<=WORDNum;i++)
    {
        if((words[i]=(char *)malloc(sizeof((char*)WORDLen)))==NULL)
        {
            perror("get word!");
            exit(EXIT_FAILURE);
        }
        words[i][0]=0; //单词中字母数量
        if((wordsTmp[i]=(char*)malloc(sizeof((char*)WORDLen)))==NULL)
        {
            perror("get word!2");
            exit(EXIT_FAILURE);
        }
    } 
    
   //step3:合法单词提取
   //规则：过滤，数字，标点，空格，下划线等,但对'-'不过滤
   //补充：实现中文过滤
   wordcnt = 0;     //合法单词计数,上限为WORDNum, 以0开头，为了防止开头出现空格字符
   alpha = 0;       //每个单词
  
   c = fgetc(outFile);
   do
   {
    //过滤中文
    if(c&0x80)  //成立，非ASCII字符
    {
        c = fgetc(outFile);     //相当于过滤掉下一个字符
        c = fgetc(outFile);     //++过程,补充边界判断
    }
    //合法字母判断
    if(!(((c>='A')&&(c<='Z'))||   //A~Z
       ((c>='a')&&(c<='z'))||   //a~z
       (c=='-')))                //-
    {
        //非法单词,此时结束单词统计
        c = fgetc(outFile);     //递增判断
        if(c==EOF)
        {
             break; //防止，最后末尾处为仅出现一个非法字符就结束
        }
        while(1)
        {
            if(((c>='A')&&(c<='Z'))||   //A~Z
               ((c>='a')&&(c<='z'))||   //a~z
               (c=='-'))                //-    :此处存在Bug，-不能在单词开头位置，需要在以后处理中过滤
            {
               //此时，分割完成一个单词
               if(0==wordcnt)
               {
                   //文件开头遇到非法字符
                   wordcnt=1; //开始调整
                   break;
               }
               words[wordcnt][++alpha]='\0';    //补充边界条件判断 
               wordcnt++;  //单词数目
               alpha=0;    
               break; //下个单词获取
            }
            //此时，仍为非法字符,继续进行读取
            c = fgetc(outFile);
            if(c==EOF)
            {
                break; //防止，最后末尾处为连续非法字符
            }
        }//end of while

    }//end of if
    else
    {
        //字母合法,构成单词
        //bug:-开头处理
        while((0==alpha)&&(c=='-'))     //防止出现连续-开头
        {
            c = fgetc(outFile);
            if(c==EOF)
            {
                break;
            }
        }
        alpha++;                //记录每个单词所有的合法字符书目
        words[wordcnt][0]++;    //记录数量
        //words[wordcnt][alpha]=c;
        words[wordcnt][alpha]=tolower(c); //转换成小写字母
        c = fgetc(outFile);
    }//end of else

   }while(c != EOF);

   //收尾处理
    words[wordcnt][++alpha]='\0';
    printf("\n<------------------------------------------>\n");
    printf("the word numbers are %d\n",wordcnt);
    for(int i=1;i<=wordcnt;i++)
    {
       printf("num:%d\t",words[i][0]);
       printf("%s\n",(words[i]+1));       //第一个字符不要打印，否则出现不可见字符打印
    }
    printf("\ni!!!!\n");
    fclose(outFile);
   
    //此时完成字符串删减过程
    //step4:词性变化
    //step4.1 拷贝单词
    struct wordFlag *flagArr;
    if((flagArr=(struct wordFlag*)malloc(sizeof((struct wordFlag *)(wordcnt+1))))==NULL)
    {
        perror("flag Arr");
        exit(EXIT_FAILURE);
    }

    for(int i=1;i<=wordcnt;i++)
    {
        for(int j=0;j<=(words[i][0]+1);j++)  //不能忽略'\0'
        {
            wordsTmp[i][j]=words[i][j];
        }
        flagArr[i].flag = NO;   //未访问
        flagArr[i].pos = i;     //基本位置
    }
    //step4.2 甄别与变化
    int len=0;

    DICT_INFO dict;     //词典原结构体
    dict.wordcnt = WORDSUM;     //单词数量
    dict.idxFileSize = WORDIDXSIZE;     //idx文件大小
    
    //WORD_IDX *idx=(WORD_IDX*)malloc((sizeof(WORD_IDX))*(dict.wordcnt));
    
    WORD_IDX *word=NULL;     //词汇索引
    if(NULL==idx)
    {
        perror("idx malloc free");
        printf("!!!!\n");
       //exit(EXIT_FAILURE);
    }
    if(getWords(filename,&dict,idx)==NULL)   //索引重置
    {
        printf("Error!!! GetWords!\n");
        getchar();
    }

    for(int i=1;i<=wordcnt;i++)     //对每个单词字符串处理
    {
        len = wordsTmp[i][0];
        if((len>=4)                     //最短单词长度判断，防止之后的单词长度变成负
          &&(wordsTmp[i][len]=='d')
          &&(wordsTmp[i][len-1]=='e'))
        {
            //此时，表示已经为动词，过去时，过去分词
            flagArr[i].flag = YES;     //已检测
            if(wordsTmp[i][len-2]=='r')
            {
                //以-r结尾的词，双写r字母+ed
                wordsTmp[i][len-2]='\0';
                wordsTmp[i][0]-=3;
            }
            else if(wordsTmp[i][len-2]=='i')
            {
                //以辅音字母+y结尾的词，变y为i+ed
                wordsTmp[i][len-2]='y';
                wordsTmp[i][len-1]='\0';
                wordsTmp[i][0]-=2;
            }
            else if(wordsTmp[i][len-2]==words[i][len-3])
            {
                //末尾只有一个辅音字母结尾的重度闭音节,双写该辅音字母
                wordsTmp[i][len-2]='\0';
                wordsTmp[i][0]-=3;
            }
            else if((wordsTmp[i][len-3]=='a')//||(wordsTmp[i][len-3]=='')  //此处歧义较多
                    ||(wordsTmp[i][len-3]=='i')||(wordsTmp[i][len-3]=='o')
                    ||(wordsTmp[i][len-3]=='u'))
            {
                //以e结尾的+d:以倒数第三个字母是元音字母，e删除
                wordsTmp[i][len]='\0';
                wordsTmp[i][0]--;
            }
            else if(wordsTmp[i][len-2]=='e')
            {
                //以e结尾的+d:双写ee结尾的
                wordsTmp[i][len]='\0';
                wordsTmp[i][0]--;
            }
            else
            {
                //加入规则动词变化时产生歧义的:looked,hoped等词汇
                word=getIdx((wordsTmp[i]+1),idx,&dict);
                if(NULL!=word) //此类型，未检测
                {
                    if(0!=explainWord((wordsTmp[i]+1),word))
                    {
                        //成功返回
                        wordsTmp[i][0]=word->length;
                    }
                }
                else
                {
                    //以原音字母+y结尾的词，直接加+ed
                    //一般在动词原型+ed
                    wordsTmp[i][len-1]='\0';
                    wordsTmp[i][0]-=2;
                }

            }
        }//if
        else
        {
            //此处扩展，用于非标准型转化
            //考虑采用何种数据结构在字典中搜索
            word = getIdx((wordsTmp[i]+1),idx,&dict);
            if(NULL!=word)
            {
                if(0!=explainWord((wordsTmp[i]+1),word))
                {
                    //成功返回
                    wordsTmp[i][0]=word->length;
                }
            }
        }
    }    
    //step5:快排，统计分析部分
    printf("<-------------------------------------->\n");
    for(int i=1;i<=wordcnt;i++)
    {
       printf("num:%d\t",words[i][0]);
       printf("%s\t\t\t-->",(words[i]+1));       //第一个字符不要打印，否则出现不可见字符打印
       printf("num:%d\t",wordsTmp[i][0]);
       printf("%s\n",(wordsTmp[i]+1));
    }
    printf("\n");

    //清除工作
    free(readBuffer);       
    free(cpBuffer);
    //free(idx);
    
    exit(EXIT_SUCCESS);

}
int explainWord(char *src,WORD_IDX *word)
{
    FILE *dictfile = fopen(dictname,"r+");
    char explain[word->length+1];
    memset(explain,'\0',word->length+1);

    if(NULL==dictfile)
    {
        perror("dict open");
        return 0;   //fail
    }
    if(0!=fseek(dictfile,word->offset,SEEK_SET))
    {
        perror("fseek open");
        return 0;
    }
    fread(explain,word->length,1,dictfile);

#if DEBUG
    printf("TEST:---->%s\n",explain);
#endif 
    strncpy(src,explain,word->length+1);
    *(src+word->length+1)='\0';  //可能没有必要
    
    return 1;   //成功返回   
}

