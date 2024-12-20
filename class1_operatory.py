










# # True and False = False
# # False and True = False
# # False and false = False
# # print(data==4 and data ==5)

# # or gives false when all arguments are false
# # True or True = True
# # True or False = True
# # False or True = True
# # False or False = False
# print(data==4 or data ==5)

# # # not it make the true statement into false and vice versa.
# print(not(data==4 or data ==5))
# # # 5, Membership
# # # int, not in
# num_list = [1,2,3,4,5,6,7,8,9]
# x = 10
# print(x in num_list)
# print(X not in num_list)

# # 6. Identity operator 
# # is , is not
x = 10
print(id(x))
y = 10
print(id(y))
listx = [1,2,3]
print(id(listx))
listy=[1,2,3]
print(id(listy))
print("This is an identity operator output : ", x is y)
print("This is an identity operator output : ", listx is not listy)
