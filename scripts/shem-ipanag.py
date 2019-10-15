size = input("Enter square size: ")

for x in range(size):
    dots_str = ''
    for y in range(size):
        dots_str += '*'
    print(dots_str)