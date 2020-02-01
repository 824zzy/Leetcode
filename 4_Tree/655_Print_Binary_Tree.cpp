class Solution {
public:
    vector<vector<string>> printTree(TreeNode* root) {
        int h = getHeight(root);
        int w = (1<<h) - 1; //power trick
        vector<vector<string>> ans(h, vector<string>(w, ""));
        dfs(ans, root, 0, w-1, 0);
        return ans;
    }
private:
    int getHeight(TreeNode* node) {
        if(!node) return 0;
        return 1+max(getHeight(node->left), getHeight(node->right));
    }
    void dfs(vector<vector<string>>& ans, TreeNode* node, int l, int r, int d) {
        if(!node) return;
        int m = (l+r)/2;
        ans[d][m] = std::to_string(node->val);
        dfs(ans, node->left, l, m-1, d+1);
        dfs(ans, node->right, m+1, r, d+1);
    }
};