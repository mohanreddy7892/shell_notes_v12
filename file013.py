# some code

student = {'sam': 10, 'iran': 60, 'sunder': 90, 'sunder': 100}
print(student['sam'], student['sunder'])
list_last_key = list(student.keys())
print(list_last_key)
print(list_last_key[-1], "-->", student.get(list_last_key[-1]))
print("keys", student.keys())
print("values", student.values())
