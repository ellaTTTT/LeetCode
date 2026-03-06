class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        auto compareWealth = [](const vector<int>& a, const vector<int>& b) {
            return accumulate(a.begin(), a.end(), 0) < accumulate(b.begin(), b.end(), 0);
        };
        auto it = max_element(accounts.begin(), accounts.end(), compareWealth);
        return accumulate(it->begin(), (*it).end(), 0);
    }
};