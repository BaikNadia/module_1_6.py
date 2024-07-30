my_dict = {'Anna':1993, 'Max':2002, 'Ira':2005}
print(my_dict)

print(my_dict['Max'])

my_dict.update({'Den':2001, 'Maria':2004})
print(my_dict)

a = my_dict.pop('Ira')
print(a)
print(my_dict)

my_set = {1,2,3,1,3,'big','big',(10,20,30)}
print(my_set)

my_set.update({4,5,True})
print(my_set)

my_set.discard(4)
print(my_set)
