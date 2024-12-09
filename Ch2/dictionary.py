##键序列或值或键值对的访问可以使用 .keys() 或 .values() 或 .items() 
numerals = {'I': 1.0, 'V': 5, 'X': 10}

numerals['X']
10

numerals['I'] = 1
numerals['L'] = 50
numerals
{'I': 1, 'X': 10, 'L': 50, 'V': 5}
    
##注意， 'L' 没有添加到上述输出的末尾。字典是无序的键值对集合。
##当我们打印字典时，键和值会以某种顺序呈现，但作为语言的使用者，我们无法预测这个顺序会是什么。
##当程序多次运行时，顺序可能会改变。