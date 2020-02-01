class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& nums, int r, int c) {
        int m = nums.size();
        int n = nums[0].size();
        if(r*c != m*n) return nums;
        vector<vector<int>> ans(r, vector<int>(c, 0));
        for(int i=0; i<m*n; ++i){
            int org_x = i/n;
            int org_y = i%n;
            int new_x = i/c;
            int new_y = i%c;
            ans[new_x][new_y] = nums[org_x][org_y];
        }
        return ans;
    }
};