my_list = []
my_list2 = [109,45,2,13,33,10, 70, 30, 40]
my_list.append(my_list2)
my_list.insert(2,15)
my_list3 = [50, 60, 70]
my_list.extend(my_list3)
print(my_list)

my_list.pop()
print(my_list)

my_list2.sort()
print(my_list2)

index_of_30 = my_list2.index(30)
print("Index of value 30:", index_of_30)

