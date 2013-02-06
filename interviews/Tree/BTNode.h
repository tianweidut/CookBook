#ifndef __BTNode__
#define __BTNode__
#include <iostream>
#include <stack>
using namespace std;

template<class T>
class BTNode
{
	public:
		T data;
		BTNode<T> *lChild;
		BTNode<T> *rChild;

		TreeNode():left(NULL),right(NULL){}
		TreeNode(const T& t):data(t),left(NULL),right(NULL){}
		TreeNode(const T& t,BTNode<T *> left,BTNode<T *> right):data(t),left(left),right(right){}

};

#endif
