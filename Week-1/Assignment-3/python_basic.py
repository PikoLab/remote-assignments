array1=[1,2,4,5]
array2=[5,2,7,1,6]
array3=[5,2,7,1,6]
array4=[5,2,7,7,7,1,6]

def find_max(numbers):
    max_num=0
    for i in range (0,len(numbers)): 
        if numbers[i] > max_num:
            max_num=numbers[i]
        else: 
            continue
    return max_num


def find_position(numbers,target):
    position=-1
    for i in range (0,len(numbers)):
        if numbers[i]==target:
            position=i
            break
    return position


print('Find max number in {}: The answer is {}.'.format(array1,find_max(array1)))
print('Find max number in {}: The answer is {}.'.format(array2,find_max(array2)))
print('Find position of target {} in arry {}: The answer is {}.'.format(5,array3,find_position(array3,5)))
print('Find position of target {} in arry {}: The answer is {}.'.format(7,array3,find_position(array3,7)))
print('Find position of target {} in arry {}: The answer is {}.'.format(7,array4,find_position(array4,7)))
print('Find position of target {} in arry {}: The answer is {}.'.format(3,array3,find_position(array3,3)))