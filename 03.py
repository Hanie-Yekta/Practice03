import random

# taein tedad anasor araye
print("How many element does your list have?")
n = int(input())

my_list = []

# por kardn arraye be surat qeyrtekrari vatasadofi
for i in range(0,n):
    my_list.append(random.randint(0,1000))

print(my_list)