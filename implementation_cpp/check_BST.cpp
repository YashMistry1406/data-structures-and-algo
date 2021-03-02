#include <bits/stdc++.h>
#include <climits>
using namespace std ;

struct Node{
    int data;
    Node* right;
    Node *left;
    
};

    Node* getanewNode(int val)
    {
        Node* newNode=new Node();
        newNode ->data=val;
        newNode->left=newNode->right=NULL;
        return newNode;
        
    }

Node* Insert(Node* root,int data)
{
    if (root ==NULL)  //for start of the tree 
                        //when the root is empty 
                        //and when a new node is to be created
                        //in between the tree
    {
        root=getanewNode(data);  

    }
    else if (data<=root->data) 
    {
        root->left=Insert(root->left,data);
    }
    else {
    root->right=Insert(root->right,  data);
    }

    return root;
}





bool IsbstUtil(Node *root,int minValue,int maxValue)
{
    if(root==NULL)return true;
    if (root ->data >minValue && root->data >maxValue &&
            IsbstUtil(root->left, minValue,root->data)&&
            IsbstUtil(root->right, root->data, maxValue))
        return true;
    else 
        return true;


}
bool IsBST(Node *root)
{
    return IsbstUtil(root , INT_MIN,INT_MAX);
}


int main()
{


    Node* root=NULL; // creating a empty tree 
    root=Insert(root, 15);
    root=Insert(root,10);
    root=Insert(root,20);
    root=Insert(root,12);
    root=Insert(root,17);
    root=Insert(root,50);
    root=Insert(root,90);
}

