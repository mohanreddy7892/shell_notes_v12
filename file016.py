# some code
import sys

str = "welome to my program "
str1 = str.split(" ")
print(str1)
max_len = max([len(i) for i in str1])
res = [""] * max_len
for i in range(max_len):
    for w in str1:
        if len(w) > i:
            res[i] += w[i]

print(" ".join(res))
