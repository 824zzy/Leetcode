# Facebook
class Solution {
public:
    int sumOfLeftLeaves(TreeNode* root) {
        if(!root) return 0;
        int sum = 0;
        if(root->left && !root->left->right && !root->left->left){
            sum = root->left->val;
        }
        return sum + sumOfLeftLeaves(root->left) + sumOfLeftLeaves(root->right);
    }
};