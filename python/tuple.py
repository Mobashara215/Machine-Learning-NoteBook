#Tuples are used to store multiple items in a single variable.
#A tuple is a collection which is ordered and unchangeable.
#Tuples are written with round brackets.
#Tuple items are ordered, unchangeable, and allow duplicate values.
#When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
#Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
#Since tuples are indexed, they can have items with the same value
tup=(2,3,45,6)
print(type(tup))
#tup[0]=5# eta hbe na karon #does not support item assignment 
##now tuple method
tup=(2,1,3,1)
print(tup[1:3])
#tuple method #index #count 
 #element er index ta jde pete cai tahole
tup=(2,3,4,5)
print(tup.index(2))
# jde jante cai 3 koibar ache
tup=(2,3,3,4,3)
print(tup.count(3))