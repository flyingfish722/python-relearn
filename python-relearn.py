# python复健
print("hello i come back!")
a = 1
print(type(a))
b = 2
print(isinstance(a,int))

array = list(range(10))

array.append(11)
array.insert(5, 12)
for i in array:
    print(i)
arr2 = [101, 102, 103]
array.extend(arr2)
print(array)
print(array.pop())
print(array)
array.reverse()
print(array)
