#include <bits/stdc++.h>
#include <cstddef>
#include <iostream>

using namespace std;
struct Node{
    int data;
    Node* right;
    Node* left;
    
};


// creation of a linked list tyoe of connection beteween the 
// nodes where in each node is divided in 3 parts 
// left->pointing to the left node and left part of the tree or the samller value 
// center-> It has the data 
// right ->pointing to the left node and left part of the tree or the samller value 
    Node* getanewNode(int val)
    {
        Node* newNode=new Node();
        newNode ->data=val;
        newNode->left=newNode->right=NULL;
        return newNode;
        
    }






//creating a node and inserting the value for 
//newly created node 
//greater value is pushed at right 
//while the smaller value than the previous node ios pushed at left side 
//it is recursive function and goes until the root parameter becomes zero 
//after that it creates a new node 
//which then followed by the link formation 
//and at the end of the recursive 
//function the last leaf is connected to the main root of the tree 

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









//the following function is used for searching in the tree 
//return true or false on finding the value 
bool search_value(Node* root ,int data)
{
    if(root == NULL)
        return false;
    else if (root->data==data) 
        return true;
    else if (data<=root->data)return search_value(root->left ,data);
    else return search_value(root->right, data);
    

}






//next is a function used for finding minimum and maximum of 
//a tree 
//in minimum we would only go through the left side as in a BST 
//all the value in the left subtree are small 
//and right subtree are big 
//
//int findMin(Node* root)
//{
//    Node* current=root;
//    if(root== NULL)
//    {
//        cout<<"does not exist";
//        return -1;
//    }
//    int temp=root->data;
//    int left_min=findMin(root->left);
//    int right_min=findMin(root->right);
//    if(left_min<temp)
//    {
//        temp=left_min;
//    }
//    else {
//    temp=right_min;
//
//    }
//    
//    return temp;
//
//        
//    }
//
//int findMax(Node* root)
//{
//    Node* current=root;
//    if(root== NULL)
//    {
//        cout<<"does not exist";
//        return -1;
//    }
//   int temp=root->data;
//   int left_max=findMax(root->left);
//   int right_max=findMax(root->right);
//   if(left_max>temp)
//   {
//       temp=left_max;
//   }
//
//   else {
//   temp=right_max;
//   }
//   return temp;
//}
//
//
//







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
    int number;
    cout<<"enter a number ";
        cin>>number;
    if (search_value(root,number)==true)
    {
        cout<<"found\n";
            
    }
    else {
    cout<<"Not found \n";
    }
    
    
//    cout << "Maximum element is " << findMax(root) << endl; 
//    
//    cout << "Minimum element is " << findMin(root) << endl; 
}


