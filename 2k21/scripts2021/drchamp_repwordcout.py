# Code to count repeating word in the string

import collections
input_string=input(str())
output=collections.Counter(input_string)

values = output.values()
values_list = list(values)
ans=values_list.count(1)
print(ans)