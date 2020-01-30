class Solution {
public:
    vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
        const int m = mat.size();
        const int n = mat[0].size();
        vector<deque<int>> diag(m+n);
        for(int i=0; i<m; ++i){
            for(int j=0; j<n; ++j){
                diag[i-j+n].push_back(mat[i][j]);
            }
        }
        for(auto& d: diag){
            sort(begin(d), end(d));
        }
        for(int i=0; i<m; ++i){
            for(int j=0; j<n; ++j){
                mat[i][j] = diag[i-j+n].front();
                diag[i-j+n].pop_front();
            }
        }
        return mat;
    }
};