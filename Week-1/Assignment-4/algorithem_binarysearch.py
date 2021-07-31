array1=[1,2,5,6,7]

# hi=high, lo=low, mi=middle
def find_position_binarysearch(numbers,target):
    position=-1
    lo=0
    hi=len(numbers)-1
    while (lo <= hi):
        mi=(lo+hi)//2
        if numbers[mi] == target:
            position=mi
            break
        else: 
            if numbers[mi] > target:
                hi=mi-1
            else: 
                lo=mi+1
    return position


print('Find position of target {} in arry {}: The answer is {}.'.format(1,array1,find_position_binarysearch(array1,1)))
print('Find position of target {} in arry {}: The answer is {}.'.format(2,array1,find_position_binarysearch(array1,2)))
print('Find position of target {} in arry {}: The answer is {}.'.format(5,array1,find_position_binarysearch(array1,5)))
print('Find position of target {} in arry {}: The answer is {}.'.format(6,array1,find_position_binarysearch(array1,6)))
print('Find position of target {} in arry {}: The answer is {}.'.format(7,array1,find_position_binarysearch(array1,7)))
print('Find position of target {} in arry {}: The answer is {}.'.format(4,array1,find_position_binarysearch(array1,4)))
