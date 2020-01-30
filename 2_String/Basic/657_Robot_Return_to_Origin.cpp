""" Amazon
Basic simulation
"""
class Solution {
public:
    bool judgeCircle(string moves) {
        vector<int> coor{0, 0};
        for(char m: moves){
            if(m=='U'){
                coor[0] += 1;
            }
            if(m=='D'){
                coor[0] -= 1;
            }
            if(m=='L'){
                coor[1] += 1;
            }
            if(m=='R'){
                coor[1] -= 1;
            }
        }
        return coor[0]==0 && coor[1]==0;
    }
};