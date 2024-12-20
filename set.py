a = {1,2,3,4,5}
a.add(6)
a.add("Nepal") #adds the given item to the set
print(a)
b = {6,7,8,9,10} 
a.update(b) #update the item of b in a
print(a)
a.remove(5) # removes given item from  the set
print(a)
b = a.copy() # makes copy of given set
print(b)
b.clear() #clear all the items from the set
print(b)
removed_element = a.pop() #removes random item from the list
print(removed_element)
y = {'a','b','c','d'}
removed_element_y = y.pop()