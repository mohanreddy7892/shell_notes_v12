#some code
import time
start = time.time()
def my_func():
    count=0
    for i in range(1000000001):
        for j in range(1000000001):
            for k in range(1000000001):
                if (i*j*k == 9959749959 and i*j*k <=9959749959):
                    count+=1
                    print("combationset is :",count,"->","[",i,j,k,"]")

my_func()

end = time.time()

print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")

                          
               