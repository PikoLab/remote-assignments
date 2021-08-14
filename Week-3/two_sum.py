arr = [2, 7, 11, 15]

def twoSum1(nums, target):
    index1=0
    index2=0
    for num1 in nums:
        for num2 in nums:
            total=num1+num2
            if num1 != num2 and total==target:
                return [index1, index2]
            else: 
                index2 +=1
        index1 +=1

def twoSum2(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j] == (target - nums[i]):
                return [i,j]


def twoSum3(nums, target):
    hashmap={}
    for i in range(len(nums)):
        hashmap[nums[i]]=i
    for i in range(len(nums)):
        ans=target-nums[i]
        if ans in hashmap and ans!=i:
            return[i,hashmap[ans]]

def twoSum4(nums, target):
    hashmap={}
    for i in range(len(nums)):
        ans=target-nums[i]
        if ans in hashmap:
            return [i, hashmap[ans]]
        hashmap[nums[i]]=i
            


print("Approach1: The result of two_sum in {} is {}".format(arr, twoSum1(arr,9)))
print("Approach2: The result of two_sum in {} is {}".format(arr, twoSum2(arr,9)))
print("Approach3: The result of two_sum in {} is {}".format(arr, twoSum3(arr,9)))
print("Approach4: The result of two_sum in {} is {}".format(arr, twoSum4(arr,9)))


print("""
Approach1: Brute Force
Time complexity: O(n^2). 
For each element, try to find its complement by looping 
through the rest of the array which takes O(n) time. 
Therefore, the time complexity is O(n^2).
""")



print("""
Approach2: Brute Force
Time complexity: O(n^2). 
For each element, try to find its complement by looping 
through the rest of the array which takes O(n) time. 
Therefore, the time complexity is O(n^2).
""")


print("""
Approach3: Using Hashmap
Time complexity: O(n). 
traverse the list containing n elements exactly twice. 
Since the hash table reduces the lookup time to O(1), 
the overall time complexity is O(n).
""")

print("""
Approach4: Using Hashmap 
Time complexity: O(n). 
traverse the list containing n elements only once. 
Each lookup in the table costs only O(1) time.
""")

