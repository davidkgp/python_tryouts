list=[1,2,3,4,5,6,7,8,9,10,11]
print("Original List")
print(list)

new_list = [x*2 for x in list]
print(new_list)

new_even_list = [x for x in list if x%2==0 ]
print(new_even_list)

#inner loop
list_same=[10,100]
combine_add = [x+y for x in list for y in list_same]
print(combine_add)