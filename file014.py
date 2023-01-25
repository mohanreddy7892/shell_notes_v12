# some code
list_data = [2025, 508, 607, 600, 788]
output = []
for i in list_data:
    output.append(''.join(str(i).split("0")))
print(output)
