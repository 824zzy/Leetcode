# Facebook
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> num2id;
        for(int i;i<nums.size(); i++){
            int res = target - nums[i];
            if(num2id.count(res)){
                return {num2id[res], i};
            }
            num2id[nums[i]] = i;
        }
        return {};
    }
};