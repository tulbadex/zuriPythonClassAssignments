# register

# login


# dictinary
# use key pairs
dictionary1 = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3',
}

print(dictionary1)

dictionary2 = {}
dictionary2['key4'] = 'value4'
dictionary2['key5'] = 'value5'
dictionary2['key6'] = 'value6'

''' print(dictionary2)

del dictionary2['key6']

print(dictionary2)

dictionary2.pop('key4')

print(dictionary2) '''

# loop thru dictionary
for key,value in dictionary2.items():
    # print(key, value)
    print('I have '+ key + ' relating to ' + value)