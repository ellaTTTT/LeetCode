### iterative
使用迭代遍歷所有元素，將當前元素與前一個元素相加，得到當前元素的 running sum。  
`vector<int>`主要是想練習vector的用法，他是一個動態陣列，可以隨意調整大小，在範例中也使用`vector<int> res(n)`來初始化一個大小為n的vector，並將結果存入其中。

### partial_sum
使用`partial_sum`函式(一種STL函式)，將前一個元素的 running sum 與當前元素相加，得到當前元素的 running sum。他需要輸入3個值分別為輸入的開頭(.begin())、結尾(.end())以及輸出的開頭(.begin())。

