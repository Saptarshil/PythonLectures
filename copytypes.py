import copy

alist = [1, 2, 3, 4, [11, 21]]
blist = copy.copy(alist)#This is shallow copy where a new object is created and the reference of the earlier object is stored here.
alist[2] = 65
#blist[0] = 100 #any changes made either in the existing list or a new list will be reflected in both.
#blist.append(11) but addition of new elements will not be reflected in the other list.
print(alist)
print(blist)
clist = [10, 20, 30]
dlist = clist
print(id(clist))
print(id(dlist))
dlist[2] = 100
print(clist)
