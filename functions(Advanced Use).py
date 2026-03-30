def find(nums):
    min_num = nums[0]
    max_num = nums[0]
    for n in nums:
        if n < min_num:
            min_num=n
        if n > max_num:
            max_num=n
    return min_num, max_num

min_value,max_value=find([1,8,3,6])
print("min_value:",min_value)
print("max_value:",max_value)



