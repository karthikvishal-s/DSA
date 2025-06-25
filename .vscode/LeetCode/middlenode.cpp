/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };

class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        int count=0;
        ListNode *curr =head;
        while(curr!=nullptr){
            count+=1;
            curr=curr->next;
        }

        ListNode *ptr =head;
        if (count%2==0){
            for(int i=0;i<(count/2);i++){
                ptr=ptr->next;
            }

        }
        else{
            for(int i=0;i<floor(count/2);i++){
                ptr=ptr->next;
            }

        


        }
        return ptr;
        
    }
};

 */