# Facebook
class Solution {
public:
    int hammingDistance(int x, int y) {
        int t = x ^ y;
        int ans = 0;
        while(t>0){
            ans += t & 1; // check lowest bit
            t >>= 1;
        }
        return ans;
    }
};