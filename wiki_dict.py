a,b,*c = range(1,100,1)
print(a, type(a))
print(b, type(b))
print(c, type(c)) #list


#append

ice = {'aa':1000,'bb':2000,'cc':3000}
ice['dd']= 4000
ice['ee']= 5000
ice['aa']= 2000 # not :, use =
print(ice)


# table

data = {
    'a': [300, 'A3124'],
    'b': [210, '2MVDI',303],
    'c': [190, '3FEED']
}

data2 = {
    'd': [200, '12324'],
    'e': [900, '1fega',303],
    'f': [110, '4hsda']
}
print(data.keys())
print(data.values())
print(data['b'][2]) #when calling specific data, dict_name[key][index] form >> 303

#update method
data.update(data2)
print(data)

#zip
#eg1
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)

#eg2
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)

