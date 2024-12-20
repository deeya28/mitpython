#function is a block of code, we used function to reuse the code. Two type of function
# 1. Build-in function
# 2. User defined function

#syntax of function
#def function_name():
#    function body

# function_name()

#simple program in user defined function
#def helloworld():
 #   print("Hello, world!")

#helloworld()

# #positional arguments - takes value according to proper positional orders.
#def hello(name, course_name): #parameters
#    print("Hello", name, "Welcome to Python Training")
#    print(course_name)

#hello('Ram', 'Python with django') #arguments

# # # #keywords arguments - takes value according to keyword
# def hello(name, course_name): #parameter
#     print("Hello", name, "Welcome to Web development Training")
#     print(course_name)
#     print("I live in")
#     print("I am studying at ")

# hello(course_name='Python with django', name='Ram') #arguments

# #default arguments
#def hello(name, course_name='Python with django'): #parameter
 #   print("Hello", name, "Welcome to Web development Training")
#    print(course_name)

#hello(name='Ram', course_name='python with data science') #arguments

# #arbitrary arguments - *args

#def sum(*args):
 #   total = 0
 #   print(args[0]+args[1]+args[2])
 #   for n in args:
 #       total+=n
  #  total=0+2=2
   #  total=2+3=5
 #   return total  #return gives result of function and stop the excution of function

#resutlt = sum(2,3,5,4,5,6)
#print(resutlt)


# #arbitrary keyword arguments - **kwargs which contain data in key:value pairs
#def hello(**kwargs): #parameter
#    print("Hello", kwargs['name'], "Welcome to Web development Training")
#    print(kwargs['course_name'])

#hello(name='Ram', course_name='Python with Data Science', another_course='Python with Data Science')