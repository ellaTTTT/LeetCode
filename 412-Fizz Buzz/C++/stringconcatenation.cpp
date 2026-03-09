class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> answer(n);
        for(int i=1; i <= n; i++) {
            string num = "";
            if (i%3 == 0){
                num += "Fizz";
            }
            if(i%5 == 0){
                num += "Buzz";
            } 
            if(num.empty()){
                answer[i-1] = to_string(i);
            } else {
                answer[i-1] = num;
            }
        }
        return answer;
    }
};