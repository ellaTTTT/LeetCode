class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        def evenOrOdd(x):
            if x != 0:
                nonlocal steps
                steps += 1
                numReduce = lambda x : (x//2) if (x % 2 == 0) else (x-1)
                numbers = numReduce(x)
                evenOrOdd(numbers)
            return steps
        return evenOrOdd(num)       