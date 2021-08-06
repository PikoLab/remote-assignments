import bisect 

arr=[1, 2, 5, 5, 5, 6, 7]

def binary_search_first(numbers,target):
    lo=0
    hi=len(numbers)-1
    while (lo <= hi):
        mi=(lo+hi)//2
        if (numbers[mi] == target and numbers[mi]>numbers[mi-1]) or hi==lo:
            return mi
        elif numbers[mi] >= target:
            hi=mi-1
        elif numbers[mi] < target: 
            lo=mi+1


print(binary_search_first(arr, 2)) # should print 1 (the index of the target number ‘2’)
print(binary_search_first(arr, 5)) # should print 2 (the index of the ‘first’ target number ‘5’ shows up)
print(binary_search_first(arr, 3)) # should print 2 (since it can’t find number 3, return the index of ‘the smallest number larger then 3', that is, the index of the ‘first’ number 5)
print(binary_search_first(arr, 1))
print(binary_search_first(arr, 4))
print(binary_search_first(arr, 6))
print(binary_search_first(arr, 7))
print("-"*30)
print(bisect.bisect_left(arr,2))
print(bisect.bisect_left(arr,5))
print(bisect.bisect_left(arr,3))
print(bisect.bisect_left(arr,1))
print(bisect.bisect_left(arr,4))
print(bisect.bisect_left(arr,6))
print(bisect.bisect_left(arr,7))