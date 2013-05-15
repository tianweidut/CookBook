#include <stdio.h>

typedef struct NameVal NameVal;
struct NameVal{
    char *name;
    int value;
};

typedef void (*FUNC)(int);
void print(int i){
    printf("%d\n",i);
}

int main(){
    int i;
    NameVal htmlchars[] = {
        "TEST", 1,
        "hello", 2,
    };

    for(i=0;i<2;i++){
        printf("%s \t %d \n",htmlchars[i].name, htmlchars[i].value);
    }

    //结构体数组
    NameVal test = {"hello world", 1};
    printf("%s\t %d \n",test.name, test.value);

    //定义函数指针
    FUNC pFunc = print;
    (*pFunc)(25);

    //定义数组
    typedef int Array [100];
    Array a;
    a[0]=1;
    printf("%d\n",a[0]);

    return 0;
}
