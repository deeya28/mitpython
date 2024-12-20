# dictionary is used to store mutliple values in key:value pair
capital ={
    "Nepal":"Kathmandu",
    "India":"New Delhi",
    "China":"Beijing"
}
print(capital)
print(len(capital))
print(type(capital))


print(capital.keys()) # gives list of keys in the dictionary
print(capital.values()) # gives list of values in the dictionary

print(capital['Nepal']) # gives the value of given key
capital['Japan'] = "Tokyo" # adds the value in the dictionary
print(capital)

capital['Bhutan'] = 'Thimpu'
print(capital)

pop_element = capital.pop("Bhutan")
print(pop_element)
print(capital)

a = {1,2,3,4}
b = (1 ,2,3,4)

marks = {
    "Math":80,
    "Science": 80,
    "Nepali": 80
}
print(marks)
capital.update(marks) # adds the given dictionary value in first dictionary
print(capital)
copy_capital = capital.copy() # to copy all the values from the given dictionary
print("This is a copy capital : ",copy_capital)

copy_capital.clear() # to clear all the values from the dictionary
print(copy_capital)

# items() :> it will print tuples(comes inside small bracket) of all item
print(marks.items())

# Nesting with dictionary
# Dictionary nested inside a dictionary nested inside a dictionary

test={'key1':{'nestkey':{'subnestkey':'hello'}}}
print(test['key1']['nestkey']['subnestkey'])
print(test['key1']['nestkey'])
print(test['key1'])
print(test.values())

student = {}
print(type(student))
student["Name"] = "Ram Shrestha"
print(student)

student['age'] = 17
student['address']= 'Kathmandu'
student['education'] = 'SEE'
print(student)
student['hobby'] = ['Football', 'Volleyball', 'Basketball']
print(student)

print(student['hobby'][-1])