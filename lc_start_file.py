'''List comprehensions provide a concise way to create lists. 

It consists of brackets containing an expression followed by a for clause, then
zero or more for or if clauses. The expressions can be anything, meaning you can
put in all kinds of objects in lists.

The result will be a new list resulting from evaluating the expression in the
context of the for and if clauses which follow it. 

The list comprehension always returns a result list. '''


'''
new_list = []
for i in original_list:
    if filter(i):
        new_list.append(expressions(i))  '''

#You can obtain the same thing using list comprehension:

# new_list = [expression(i) for i in original_list if filter(i)]


#The list comprehension starts with a '[' and ']', to help you remember that the
#result is going to be a list.

	
# A short way to remember LC is:

#result  = [*transform/expression*    *iteration*         *filter/condition*     ]

list1 = list(range(1,11))
list2 = []

for x in list1:
    if x > 5:
        list2.append(x)

print(list2)

list2 = [x * 20 for x in list1 if x > 5]

print(list2)

squares = [x**2 for x in range(1,11)]
print(squares)






infile = open("test.txt", "r")
result = [i.rstrip('\n') for i in infile if "line3" in i]
print(result)


