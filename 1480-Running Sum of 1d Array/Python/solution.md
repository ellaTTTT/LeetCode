### append
使用`append()`函式將元素放入`res`中(置於最末端)。

### iterative
使用迭代遍歷所有元素，將當前元素與前一個元素相加，得到當前元素的 running sum。  
另一個嘗試使用`accumulate`函式，他會產生新的迭代器(iterator, 是 Iterable 的一種，具備「一次性」且「記住目前位置」的特性)，根據index計算index=0~index=當前位置的總和並依序給值，最後使用`list()`函式將這些值(存在nums中)轉換為list。

### map, lambda
