class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(begin(g), end(g));
        sort(begin(s), end(s));
        int ans = 0;
        int j = 0;
        for(int i: g){
            while(j<s.size() and i>s[j]){
                ++j;
            }
            if(j<s.size()){
                ++j;
                ++ans;
            }
        }
        return ans;
    }
};