chinese = ['coin', 'string', 'myriad']  # A list literal
suits = chinese                         # Two names refer to the same list

suits.pop()             # Remove and return the final element（pop里面是索引）
'myriad'
suits.remove('string')  # Remove the first element that equals the argument(String是被移出的元素)

suits.append('cup')              # Add an element to the end
suits.extend(['sword', 'club'])  # Add all elements of a sequence to the end
##########
suits is ['heart', 'diamond', 'spade', 'club']
False
suits == ['heart', 'diamond', 'spade', 'club']
True
#身份是一个比相等更强的条件
##最后两个比较说明了 is 和 == 之间的区别。前者检查身份，而后者检查内容的相等性。