my_tuple = (1, ) # when one variable is set as a tuple, the , part should be included to specify that this variable will be a tuple, not an integer.
t = 1, 2, 3, 4
print (type(t)) # no need for ()

t = list(t) #change of formation
print(type(t))
print (t)

a = tuple(range(2,100,2))
print(a)