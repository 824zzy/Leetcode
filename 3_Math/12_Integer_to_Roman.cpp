class Solution {
public:
    const map<int, string, std::greater<>> nums2str = {{1,"I"}, {4,"IV"}, {9,"IX"}, {500,"D"}, {100, "C"}, {50, "L"}, {10, "X"}, {5, "V"},{900, "CM"}, {400, "CD"}, {90, "XC"}, {40, "XL"}, {1000, "M"}};
    
    string intToRoman(int num) {
        string ans;
        for(const auto& item: nums2str) {
            while(num/item.first!=0) {
                num -= item.first;
                ans += item.second;
            }
        }
        return ans;
    }
};