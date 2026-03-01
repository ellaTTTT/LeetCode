class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        evenOrOdd = lambda num : (num//2) if (num % 2 == 0) else (num-1)
        add = lambda steps : steps+1
        while(num!=0):
            num = evenOrOdd(num)
            steps = add(steps)
        return steps