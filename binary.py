a="1101"
b="100"


def add_binary_numbers(x,y):
    max_len=max(len(x),len(y))
    print(f"maxlength",max_len)

    x=x.zfill(max_len)
    y=y.zfill(max_len)
    print(f"x, y values ",x,y)


    result=''
    carry=0

    for i in range(4 - 1, -1, -1):
            r = carry
            #print("before" ,i,r)
            r += 1 if x[i] == '1' else 0
            #print("xr:",x[i],r)
            r += 1 if y[i] == '1' else 0
            #print("yr:",y[i],r)
            result = ('1' if r % 2 == 1 else '0') + result
            #print(f"r",r)
            #print(result)
            carry = 0 if r < 2 else 1
            #print(f"carry",carry)

    if carry !=0 : result = '1' + result
    print(result.zfill(max_len))
            



add_binary_numbers(a,b)
