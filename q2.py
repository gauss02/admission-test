def count(input):
    counts = {}
    for char in input:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}


def group_by_key(input):
    result = {}
    for dictionary in input:
        key = dictionary['key']
        value = dictionary['value']
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result

input2 = [
{'key': 'a', 'value': 3},
{'key': 'b', 'value': 1},
{'key': 'c', 'value': 2},
{'key': 'a', 'value': 3},
{'key': 'c', 'value': 5}
]
print(group_by_key(input2)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}


