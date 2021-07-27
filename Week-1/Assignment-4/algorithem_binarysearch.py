array1=[1,2,5,6,7]

# hi=high, lo=low, mi=middle
def find_position_binarysearch(numbers,target):
    position=-1
    lo=0
    hi=len(numbers)-1
    while (lo < hi):
        mi=(lo+hi)//2
        if numbers[mi] == target:
            position=mi
            break
        else: 
            if numbers[mi] > target:
                hi=mi
            else: 
                lo=mi
    return position


print('Find position of target {} in arry {}: The answer is {}.'.format(1,array1,find_position_binarysearch(array1,1)))
print('Find position of target {} in arry {}: The answer is {}.'.format(6,array1,find_position_binarysearch(array1,6)))