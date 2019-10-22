# Finds the median of a list of numbers.
def median(list):
  list.sort()
  list_length = len(list)
    if list_length%2==0:
  return (list[int(list_length/2)-1] + list[int(list_length/2)])/2
  else:
    return list[int(list_length/2)]
