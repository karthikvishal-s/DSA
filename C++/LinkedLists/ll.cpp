#include <iostream>
#include <vector>

using namespace std;

struct Node{
    int data;
    Node* next;

    Node(int data){
        this->data=data;
        this->next=nullptr;
    }
};

void traverseList(Node* head){
    while(head!=nullptr){
        cout <<head->data<<"\n";
        head=head->next;
    }
}
void searchList(Node* head,int target){
    int index=0;
    while(head!=nullptr){
        
        if(head->data==target){
            cout << "Element found at index: " << index << "\n";
            return;}
        
        head=head->next;
        index+=1;
    }

}

void lengthList(Node* head){
    int count=0;
    while(head!=nullptr){
        count+=1;
        head=head->next;

    }
    cout << "Length of the list is: " << count << "\n";
}

void insert(Node* head,int data,int pos){
    Node* newNode = new Node(data);
    
    if(pos == 0){
        newNode->next = head;
        head = newNode;
        return;
    }

    Node* curr = head;
    for(int i=0;i<pos-1 && curr!=nullptr;i++){
        curr=curr->next;
    }

    newNode->next = curr->next;
    curr->next=newNode;

}








int main(){
    Node* head = new Node(10);
    head->next = new Node(20);
    head->next->next = new Node(30);
    head->next->next->next = new Node(40);

    traverseList(head);
    searchList(head, 30);
    lengthList(head);
    insert(head, 25, 2);
    traverseList(head);

    return 0;
};