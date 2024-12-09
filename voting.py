def majority_number(numbers):
    count = 0
    candidate = None

    for num in numbers:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    return candidate

##当遍历到一个新数字时：
##如果 count 为 0，我们就将当前数字设为候选数字，并将 count 设为 1。
##如果当前数字与候选数字相同，就增加 count 的值。
##如果当前数字与候选数字不同，就减少 count 的值。
##由于要找的数字出现次数超过一半，所以即使其他数字不断 “抵消” 它的计数，最终这个数字的计数也不会被减到 0 。
##当遍历完数组后，最后的候选数字就可能是出现次数超过一半的数字。但由于可能存在一些特殊情况（例如没有数字出现次数超过一半，或者有多个数字出现次数都接近一半）导致结果不准确，所以通常还需要再遍历一遍数组来验证这个候选数字是否真的出现次数超过一半。