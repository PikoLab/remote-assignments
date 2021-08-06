input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
input2 = [
{'key': 'a', 'value': 3},
{'key': 'b', 'value': 1},
{'key': 'c', 'value': 2},
{'key': 'a', 'value': 3},
{'key': 'c', 'value': 5}
]

def count(input):
    my_dict={}
    for i in input:
        if i not in my_dict:
            my_dict[i]=1
        else:
            my_dict[i]+=1
    return my_dict


def group_by_key(input):
    my_dict={}
    for i in input:
        if i["key"] not in my_dict:
            my_dict[i["key"]]=i["value"]
        else:
            my_dict[i["key"]]+=i["value"]
    return my_dict

print(count(input1)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}
print(group_by_key(input2)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}