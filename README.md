# LeetCode
A space for coding from leetcode
Each folder contains the problem description and solutions in different languages.
Each folder is named after the problem number and topic, and include a README.md file which has the probelm description and constraints.
Each language folder contains at least 2 solutions in that language.
Each folder also contains a solution.md file which has the solution explanation.

### Before Start
C++ - LeetCode usually use `vector<int>&` in C++ to pass the array, which means the array is passed by reference.
So we can modify the array in place.
The `vector<int>` means that it is a dynamic array, which can be resized, while `&` here means that it is passed by reference.

Python - LeetCode usually use `List[int]` to pass the mutable objects(lists), they are passed by object reference, allowing for in-place modifications.
The `self` here is the instance of class, which is primary used to access other methods or stored data that needs to persist across different function calls.