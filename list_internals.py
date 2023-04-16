alist = []
print(alist.__sizeof__()) #40bytes is the overhead of an empty list
alist.append(1) #this creates an object whose value is 1 and the object's memory address is stored in the list instead of the value itself.
print(alist)
print(alist.__sizeof__())
alist.append(2)
alist.append(3)
alist.append(10)
print(alist) #for the first append statement, 32bytes i.e. 4 memory locations are reserved. After you use up the 4 locations, another 4 locations are reserved on the next append call.
print(alist.__sizeof__())
alist.append(5)
print(alist)
print(alist.__sizeof__())
#first 2 sets of append will reserve 4 locations each. then onwards it will reserve 8 locations till the 6th set. 7th-9th set will reserve 12 locations. 10th and 11th will reserve 16 locations. 12th and 13th will reserve 20 locations while 14th will reserve 24 and 15th will reserve 28 locations. then 16th will reserve 32 and 17th will reserve 36.

blist = [10, 100, 1000, 10000]
new_list = iter(blist)  #this creates am iterable object new_list.
print(next(new_list))  #next points the pointer to the value in the next location and returns the value present in the current location.
print(next(new_list))
print(next(new_list))
print(next(new_list))
