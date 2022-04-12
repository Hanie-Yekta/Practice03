# taein tedad anasor araye
print("How many element does your list have?")
T_list = int(input())

my_list = []
flag = 1

# por kardn araye tavasot karbar
for i in range(0, T_list):
    print("Enter the element of your list:")
    my_list.append(int(input()))

for j in range(0,T_list-1):
    if my_list[j] < my_list[j+1]:
        pass
    else:
        flag = -1
        print("it's not sorted")
        break

if flag == 1:
    print("it's sorted")
