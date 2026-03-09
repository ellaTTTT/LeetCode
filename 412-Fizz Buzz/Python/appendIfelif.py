class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        self.answer = []
        for i in range(1, n+1):
            self.word = ''
            if(i%15 == 0):
                self.word = 'FizzBuzz'
            elif(i%3 == 0):
                self.word = 'Fizz'
            elif(i%5 == 0):
                self.word = 'Buzz'
            if not self.word:
                self.answer.append(str(i))
            else:
                self.answer.append(self.word)
        return self.answer

        