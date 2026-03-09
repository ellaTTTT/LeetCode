class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        self.d = {3:'Fizz', 5:'Buzz', 15:'FizzBuzz'}
        self.answer = []
        for i in range(1, n+1):
            self.word = ''
            for key, value in self.d.items():
                if(i%key == 0):
                    self.word = value
            if not self.word:
                self.answer.append(str(i))
            else:
                self.answer.append(self.word)
        return self.answer

        