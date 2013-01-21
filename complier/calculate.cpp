// Calculator.cpp : Defines the entry point for the console application.
//


///////////////////////////////////////////////////////////////////////////////
//		对四则运算表达式的文法完善
//		E-->AE'
//		E'-->+AE'|e
//		A-->BA'
//		A'-->-BA'|e
//		B-->TB'
//		B-->/TB'|e
//		T-->FT'
//		T'-->*FT'|e
//		F-->(E)|num
///////////////////////////////////////////////////////////////////////////////

#include <iostream>
#include <stdlib.h>
#include <string>
#include <stdio.h>
using namespace std;

// 这一段是记号的定义
#define ADD 0
#define MUL 1
#define LBRACE 2
#define RBRACE 3
#define NUM 4
#define END 5
#define OTHER 6
//新添加
#define SUB 7
#define DIV 8

//char input[200];	// 输入串。
string input;

int lookahead;
int pCur;
int yylval;

// 函数声明
int yylex();
void Match(int t);
long T();
long E_();
long E();
long A();
long A_();
long B();
long B_();
long T_();
long F();

// 词法分析器，读入一个记号
int yylex()
{
	char num[20];
	int temp = 0;

	// 过滤掉空白
	while ( input[pCur]==' ' ) pCur++;

	// 如果是数字，那么把这个记号的数值计算出来放在 yylval 中
	while (input[pCur] >= '0' && input[pCur] <= '9'){
		num[temp++] = input[pCur++];
	}
	if (temp >0) 
	{
		sscanf(num, "%d", &yylval);
		return NUM;
	}

	// 其他记号的处理
	switch (input[pCur++])	// 注意：这里指针往前移了一位
	{
	case '+': return ADD;
	case '*':return MUL;
	case '(':return LBRACE;
	case ')':return RBRACE;
	case '\0': return END;
	case '-': return SUB;
	case '/': return DIV;
	default: return OTHER;
	}
}

// 匹配函数，若当前记号与参数相同，则读入下一个记号
void Match(int t)
{
	if (lookahead == t) lookahead = yylex();
	else 
	{
		printf("\n Error\n");

		exit(0);
	}
}

 
long E()
{
	switch (lookahead)
	{
	case LBRACE:	// FIRST(TE')={(,num}
	case NUM:
		return A() + E_();
	default:
		printf("\n Error\n");
		exit(0);
	}		
}

// 处理 E'-->+AE'|e
long E_()
{
	switch (lookahead)
	{
	case ADD:	// E'-->+TE' 的情况， FIRST(E')={+,e}
		Match(ADD); return A() + E_();

	case RBRACE:// E'-->e 的情况，这个时候需要处理 FOLLOW集合， FOLLOW(E')={), $}
	case SUB:
	case DIV:
	case END:
		return 0;
	default:
		printf("\n Error\n");

		exit(0);
	}	
}
long A()
{
	switch (lookahead)
	{
	case LBRACE:	// FIRST(TE')={(,num}
	case NUM:
		return B() - A_();
	default:
		printf("\n Error\n");

		exit(0);
	}		
}
long A_()
{
	switch (lookahead)
	{
	case SUB:	 
		Match(SUB); return B() - A_();

	case RBRACE: 
	case ADD:
	case DIV:
	case END:
		return 0;
	default:
		printf("\n Error\n");

		exit(0);
	}	
}
long B()
{
	switch (lookahead)
	{
	case LBRACE:	// FIRST(TE')={(,num}
	case NUM:
		return T() / B_();
 
	default:
		printf("\n Error\n");

		exit(0);
	}		
}
long B_()
{
	switch (lookahead)
	{
	case DIV:	// FIRST(*FT')={*}
		Match(DIV);
		return T() /B_();
	case ADD:	// T'-->e 的情况，这个时候需要处理 FOLLOW集合， FOLLOW(T')={+,),$}
	case SUB:
	case MUL:
	case RBRACE:
	case END:
		return 1;
	default:
		printf("\n Error\n");

		exit(0);
	}	
}
long T()
{
	switch (lookahead)
	{
	case LBRACE:	// FIRST(FT')={(,num}
	case NUM:
		return F()*T_();
	default:
		printf("\n Error\n");

		exit(0);
	}
}
// 处理 T'-->*FT'|e
long T_()
{
	switch (lookahead)
	{
	case MUL:	// FIRST(*FT')={*}
		Match(MUL);
		return F() * T_();
	case ADD:	// T'-->e 的情况，这个时候需要处理 FOLLOW集合， FOLLOW(T')={+,),$}
	case SUB:
	case DIV:
	case RBRACE:
	case END:
		return 1; 
	default:
		printf("\n Error\n");

		exit(0);
	}		
}

// 处理 F-->(E)|num
long F()
{
	int temp;

	switch(lookahead)
	{
	case LBRACE:	// FIRST((E))={(}
		Match(LBRACE);
		temp = E();
		Match(RBRACE);
		return temp;
	case NUM:		// FIRST(num) = {num}
		temp = yylval;
		Match(NUM);
		return temp;
	default:
		printf("\n Error\n");

		exit(0);		
	}
}


int main(int argc, char* argv[])
{
	bool again_ask=true;
	char a;

	while (again_ask)
	{
			pCur = 0;

			// 读入输入串
			cout<<"please input your expression:";
			cin>>input;

			// lookahead 赋初值
			lookahead = yylex();

			// 调用 开始符号E 对应的处理过程来处理输入串
			cout<<"the answer is "<<E()<<endl;

			cout<<"Y/N:";
			cin>>a;
			
			again_ask=((a=='Y'||a=='y')?1:0);

	}
	cout<<"welcome to the next!\n";
	return 0;
}



