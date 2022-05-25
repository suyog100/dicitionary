
'''
1)to get the smallest number in a list
'''

# list_one=[1,2,3,4]
# print (min(list_one))


'''
2)function to check if a list is empty
'''
# empty_list=[]
# def check_empty(my_list):
#     if len(my_list)==0:
#         return "empty"
#     else:
#         return " not empty"
# print(check_empty(empty_list))

'''
3)to select a random element form a list
'''
# print(random.choice(list_one))

'''
4)program to copy a list
'''
# to_be_copie=[1,2,3]
# copied_list=to_be_copied.copy()
# print(copied_list)

'''
5)find the second largest number in a list.
'''
# second_largest=[2,3,4,5,6]
# second_largest.sort()
# print(second_largest[-2])


'''
6)wap to print a specified list after removing the 3rd element
'''

# def my_lis(li):
#     a=[]
#     x=[li[3]]
#     for i in li:
#         if i not in x:
#             a.append(i)
#     return a
# print(my_list([1,2,3,'puttiing',5,7]))



'''
7)count the number of even and odds from a sequence of numbers
'''
# our_numbers=[1,2,3,4,5,6,7,8,9,10]
# even_count=0
# odd_count=0
#  for i in our_numbers:
#      if i%2==0:
#          even_count+=1
#     else:
#         odd_count+=1
# print(even_count)
# print(odd_count)


'''
8)add a element to a tuple
'''

# original_tuple={1,2,3}
# converted_tuple=list(original_tuple)
# converted_tuple.append(4)
# changed_tuple=tuple(converted_tuple)
# print(changed_tuple)


'''
9)covert a tuple to a list
'''

# tuple_to_convert={1,2,3}
# to_list=list(tuple_to_covert)


'''
10)convert fa tuple to string
'''
# to_string = str(tuple(to_list)


'''
11)convert a list to tuple
'''
# new_tuple=tuple(to_list)


'''
12)convert list of tuple to dictonary
'''

# user_list=[("name","john"),("age",25)]
# user_data_dict=dict(user_list)

'''
13)add a key to a dictionary
'''
# sample_dict={0:10,1:20}
# sampl_dict[2]=30

'''
14)concatenate the given dictionaries
'''
# dict_one={1:10,2:20}
# dict_one{3:30,4:40}
# dict_three={5:50,6:60}

# dict_one.update(dict_two)
# dict_one.update(dict_three)

'''
15)check if a  given key exist in a dictionary
'''
# key_check_dict={
#     'name' : 'Suyog'
#     'age' : 19
# }
# if 'name' in key_check_dict:
#     print('yes it is')
# else:
#     print ('no its not')

'''
16)print a dictionary where the keys are the numbrs from 1 to 15 and the values
are square of the keys
'''
# for i in range(1,16):
#     square_dict[i]=i**2

'''
17)merge two python dictionary
'''
# first_dict=[1,2]
# to_be_merged=[3,4]
# first_dict.extend(to_be_merged)

'''
18)find third largest number in a list 
'''

# third_largest_list=[4,5,6,7,8,9]
# third_largest_list.sort()
# print(third_largest_list[-3])


'''
19)write a python program to create a set
'''
'''
20)wap to iterations over sets
'''
'''
21)wap a program to add members() in a set.
'''
'''
23)wap to remove item form a set if it is present in the set
'''

# set_1={'a','b','c','d','e','f','g','h','i'}
# for j in set_1:
#     print(j)
# set_1.add("1")
# set_1.remove('a')
# set_1.discard('a')
# print(set_1)


'''
24)wap to create a intersection of sets
'''

# set_1={1,2,3,4,5}
# set_2={3,5,4,6,9}
# b=set_1.intersection(set_2)
# print(b)


'''
25)wap to check given key already exist in a dictionary 
'''

# d={1:10,2:20,3:30,4;40,5:50,6:60}
# def key_present(x):
#     print('key is present in the dictionary')
# else:
#     print('key is not present in the dictionary')
# key_present(5)
# key_present(9)


'''
26)
'''
a={1:11,2:22,3:33,4:44}
if 44 in a.values():
    print("present")
else:
    print("not prresent")
    