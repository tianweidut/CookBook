#include <iostream>
#include <stack>
#include <BTNode.h>
using namespace std;


template<class T>
void postOrderTreeIteration(BTNode *pTree)
{
	stack<BTNode<T>*> st;
	BTNode<T> *cur =  pTree;
	BTNode<T> *pre = NULL;

	while(cur||st.size())
	{
		while(cur)
		{
			st.push(cur);
			cur= cur->left;
		}

		cur = st.top();

		if( cur->right==NULL || cur->right==pre)
		{
			visit(cur);
			st.pop();
			pre = cur;
			cur = NULL;
		}
		else
		{
			cur = cur->right;
		}

		
	}
}

template <class T>
void postOrderTree(BTNode *pTree)
{
	if(pTree)
	{
		postOrderTree(pTree->right);
		postOrderTree(pTree->left);
		visit(pTree);
	}
}
