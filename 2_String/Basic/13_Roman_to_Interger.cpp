class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> m{{'I', 1}, {'V', 5}, 
                                   {'X', 10},{'L', 50},
                                   {'C', 100}, {'D', 500},
                                   {'M', 1000}};
        int ans = 0;
        for(int i=0; i<s.size();i++){
            ans += m[s[i]];
            if(i>0 and m[s[i]]>m[s[i-1]]){
                ans -= 2 * m[s[i-1]];
            }
        }
        return ans;
    }
};