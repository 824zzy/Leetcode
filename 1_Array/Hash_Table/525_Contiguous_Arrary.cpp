class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        unordered_map<int, int> prefix;
        prefix[0] = -1;
        int currSum = 0;
        int ans = 0;
        for(int i=0; i<nums.size(); ++i) {
            currSum += nums[i] ? 1 : -1;
            if(prefix.count(currSum)) {
                ans = max(ans, i-prefix[currSum]);
            } else {
                prefix[currSum] = i;
            }
        }
        return ans;
    }
};