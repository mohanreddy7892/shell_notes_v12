str = input()
len_str = len(str)
#print(len_str)
if len_str != 1:
    mylist = list(str.strip())
    first_digit = mylist[0]
    last_digit = mylist[-1]
    sum_digits = int(first_digit) + int(last_digit)
    print(sum_digits)
else:
    print(str)
