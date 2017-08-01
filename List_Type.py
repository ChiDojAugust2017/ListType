some_list =  ['magical unicorns', 19, 'hello', 98.98, 'world']

total = 0
string = ''
is_string_only = True
is_number_only = True

for item in some_list:
    if type(item) is int or type(item) is float:
        total += item
        is_string_only = False
    elif type(item) is str:
        string += item + ' '
        is_number_only = False

print total
print string

if is_string_only:
    print 'the list consists of strings only'
elif is_number_only:
    print 'the list consists of numbers only'
else:
    print 'the list is mixed'










    
