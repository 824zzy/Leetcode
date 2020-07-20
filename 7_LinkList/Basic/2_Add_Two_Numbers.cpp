class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry=0;
        ListNode dummy(0);
        ListNode* curr = &dummy;
        while(l1 || l2 || carry) {
            int a = 0;
            int b = 0;
            if(l1) {
                a = l1->val;
                l1 = l1->next;
            }
            if(l2) {
                b = l2->val;
                l2 = l2->next;
            }
            carry += a + b;
            curr->next = new ListNode(carry%10);
            carry /= 10;
            curr = curr->next;
        }
        return dummy.next;
    }
};