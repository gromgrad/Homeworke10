#Работа со словарем
my_dict={'Roman':16041984,'Alexander':22081999, 'Alena':18121983,}
print(my_dict)
print(my_dict['Roman'])
print(my_dict.get('Masha'))
my_dict.update({'Masha': 30021983,
                'Vasya': 18191989})
print(my_dict)
del my_dict['Roman']
print(my_dict)
                                 #print(my_dict.keys())
                                 #x=my_dict.pop('Masha')
                                 #print(x)
                                 #print(my_dict.values())
                                 #print(my_dict.items())

#Множества
my_set={1,2,3,4,5,1,2,3,4,}
print(my_set)
my_set.update({50,'Apple'})
                                 #my_set.add('Orange')
print(my_set)
                                 #print(my_set.discard(100))
print(my_set.remove(1))
print(my_set)