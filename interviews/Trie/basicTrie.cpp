#include <iostream>
#include <algorithm>

using namespace std;

const int sumson = 26;
const int base = 'a';

//trie struct
struct Trie
{
    int num;        //the numner of the prefix
    bool leafNode;   //leaf node
    struct Trie *son[sumson];   //the following node
};
/*create a new tree*/
Trie * newTrie()
{
    Trie * tmp = new Trie;      //build in the heap!
    tmp->num = 1;
    tmp->leafNode = false;
    for(int i=0;i<sumson;i++)
    {
        tmp->son[i] = NULL;
    }
    return tmp;                 // ok
}
/*insert produce: insert a word into the trie*/
void Insert(Trie *pTree,char *s)
{
    if(NULL == s) return;

    int len = strlen(s);
    Trie * tmp = pTree;

    for(int i =0 ;i<len; i++)
    {
        if(tmp->son[s[i]-base] == NULL)
        {
            tmp->son[s[i]-base] = newTrie();
        }
        else
        {
            tmp->son[s[i]-base]->num++;
        }
        tmp = tmp->son[s[i]-base];
    }
    tmp->leafNode = true;
}
/*delete the trie*/
void deleteTrie(Trie *pTree)
{
    if(NULL != pTree)
    {
        for(int i=0;i<sumson;i++)
        {
            if(pTree->son[i] != NULL)
            {
                deleteTrie(pTree->son[i]);
            }
        }
        delete pTree;   //释放空间
        pTree = NULL;   //指针归0
    }
}
/*Trie find*/
Trie * FindInTrie(Trie *pTree,char *s)
{
    if(NULL == s) return NULL;

    int len = strlen(s);
    Trie *tmp = pTree;

    for(int i=0;i<len;++i)
    {
        if(tmp->son[s[i]-base]!=NULL)
        {
            tmp = tmp->son[s[i]-base];
        }
        else
        {
            return NULL;
        }
    }
    return tmp;
}

int main()
{
    cout << "Hello world!" << endl;
    return 0;
}
