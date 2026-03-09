class Solution {
public:
    vector<string> fizzBuzz(int n) {
        map<int, string> num = {{3, "Fizz"}, {5, "Buzz"}};
        vector<string> answer(n);
        for(int i=1; i<=n; i++) {
            string curr = "";
            for (const auto &[key, value] : num){
                if (i%key == 0){
                    curr += value;
                }
            }
            if(curr.empty()){
                answer[i-1] = to_string(i);
            } else {
                answer[i-1] = curr;
            }
        }
        return answer;
    }
};