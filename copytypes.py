import copy

list1 = [1, 2, 3, 4]
list2 = copy.copy(list1)
list2[1] = 100
print("Shallow copy starts here")
print(list1)
print(list2)
list1.append(75)
print(list1)
print(list2)
print("Deep copy starts here") #instead of copying the reference, a new set of objects with their own reference is being created. So changes made in either of the object, will not affect the other one.
list3 = [10, 20, 30, 60]
list4 = copy.deepcopy(list3) #deep copy is costlier cause a new set of objects is being created.
list3[2] = 890
list4.append(100)
print(list3)
print(list4)
