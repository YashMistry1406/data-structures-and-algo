#include <bits/stdc++.h>
#include <cstddef>
using namespace std;

struct Node
{
    int data;
    struct Node* left;
    struct Node* right ;
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

Node * findMin(Node* root )
{
    Node* temp=root;
    while(temp->left!=NULL)
    {
        temp=temp->left;
    }
    return temp;
}





//struct Node* findMin(struct Node* node)
//{
//    struct Node* current = node;
// 
//    /* loop down to find the leftmost leaf */
//    while (current && current->right != NULL)
//        current = current->right;
// 
//    return current;
//}
struct Node* Delete(struct Node* root,int data)
{
    if(root==NULL) return root;
    else if (data <root->data) root->left= Delete(root->left, data);
    else if(data > root->data) root->right=Delete(root->right, data);
    else {
    if (root->left ==NULL && root->right==NULL)
    {
        delete root;
        root =NULL;

    }
    else if (root->left==NULL)
    {
        struct Node *temp =root;
        root=root->right ;
        delete temp;
    }
    else if(root->right==NULL)
    {

        struct Node *temp =root;
        root=root->left;
        delete temp;
    }
    else
    {
        struct Node *temp=findMin(root->right);
        root->data=temp->data;
        root->right=Delete(root->right, temp->data);
    }
    }
    return root;
}

void inorder(Node *root)
{
    if (root==NULL) return;
    inorder(root->left);
    cout<<root->data<<" ";
    inorder(root->right);
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
//    root=Delete(root, 50);
    root=Delete(root,10);
        
    inorder(root);
}


        
