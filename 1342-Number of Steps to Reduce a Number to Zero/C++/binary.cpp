class Solution {
public:
    int numberOfSteps(int num) {   
        if (num!=0) {
            return 1 + numberOfSteps(num & 0x01 ? num-1 : num>>1 );
        } else {
            return 0;
        }
    }
};