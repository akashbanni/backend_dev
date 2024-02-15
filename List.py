# list_1 = [10,20,30,40,50,60]
# print(list_1)
# #Output : [10, 20, 30, 40, 50, 60]
# list_2 = [70,80,90]
# list_12=list_1 + list_2
# print("List after extending: ",list_12)


list_1 = [10,20,30,40,50,60,70,80,90]

# the methods in list are  as follows:
# append()   add an element to the end of a list.
# extend()   adds elements from an iterable (like lists or tuples) to the end of a list.
# insert()   inserts an element at a specific position in a list.
# remove()   removes the first occurrence of an element from a list.
# pop()      removes and returns the last item in a list. If you provide a number it will return that index value.
# copy()     It  returns a shallow copy of the original object.
# sort(key)  sorts the list. If key is provided, it uses this one-arg function on each item in the list prior to making comparisons.
# sort()     sorts the list in ascending order.
# reverse()  reverses the list.
# index(x)   gives the index of the specified value x in the list.
# count(x)   counts how many times the specified value appears in the list.
# min(), max() find the minimum and maximum values in the list.

list_1.append(100) #appends 100 to the last index of list_1

print(list_1)
list_2 = [110,120]

list_1.extend(list_2) #extends list_1 with list_2
print(list_1)

list_1.insert(12,130)
print(list_1)
a=list_1.index(120)
print(a)
b=list_1.count(110)
print(b)
c=min(list_1)
d=max(list_1)
print("Smallest element: ",c)
print("Largest element: ",d)
list_1.remove(110)
print(list_1)
list_1.sort()
print(list_1)
list_1.reverse()
print(list_1)

