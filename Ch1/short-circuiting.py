##>>> 1 / 0
##ZeroDivisionError

##>>> True or 1 / 0
##True

##>>> 1 / 0 or True
##Traceback (most recent call last):
##  File "<stdin>", line 1, in <module>
##ZeroDivisionError: division by zero
####所以遍历中先计算前面的，遇到1 / 0 直接短路，True在前面遇到or直接输出，同理，输出前面的

#>>> 4 or 6
#4
#>>> 4 and 6
#6
#>>> 6 and 4
#4
####如果都真，那么or前，and后
#>>> 0 and 4
#0
#>>> False and 4
#False
#>>> 0 or 3
#3
####and如果有假，就走假,or如果有真，先走真
#>>>False or 0
#选0，最后一个为假的