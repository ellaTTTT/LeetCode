class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int wealth = 0;
        for(int m=0; m < accounts.size(); m++) {
            int num = accumulate(accounts[m].begin(), accounts[m].end(), 0);
            if(wealth < num) {
                wealth = num;
            }
        }
        return wealth;
    }
};