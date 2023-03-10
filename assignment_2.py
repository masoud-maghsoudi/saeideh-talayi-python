def my_max(u_list):
    result = u_list[0]
    for i in range(len(u_list)):
        if u_list[i] > result:
            result = u_list[i]
    return result


def my_min(u_list):
    result = u_list[0]
    for i in range(len(u_list)):
        if u_list[i] < result:
            result = u_list[i]
    return result


def my_avg(u_list):
    result = 0
    for i in range(len(u_list)):
        result += u_list[i]
    return result/len(u_list)


def my_sort(u_list, reverse=False):
    for i in range(len(u_list)):
        for j in range(0, len(u_list) - i - 1):
            if u_list[j] > u_list[j + 1]:
                temp = u_list[j]
                u_list[j] = u_list[j+1]
                u_list[j+1] = temp
    if reverse is False:
        return u_list
    else:
        reversed_u_list = []
        for i in range(len(u_list)-1, -1, -1):
            reversed_u_list.append(u_list[i])
        return reversed_u_list


print("Please Enter the number of inputs:", end=" ")
count = int(input().strip())

user_list = []
for i in range(count):
    # print("Please Enter the input number {}".format(i+1))
    # print(f"Please Enter the input number {i+1}", end=" ")
    print('Please Enter the input number %s:' % (i+1), end=" ")
    user_list.append(int(input().strip()))


print("The Minimum number is:", my_min(user_list))
print("The Maximum number is:", my_max(user_list))
print("The Average of the inputs is:", '%.2f' % (my_avg(user_list)))

user_list = my_sort(user_list)
print("Here is the sorted list in ascending order:", end=' ')
for i in range(len(user_list)):
    print(user_list[i], end=' ')
print("")

# user_list=my_sort(user_list,reverse=True)
# print("Here is the sorted list in descending order:", end=' ')
# for i in range(len(user_list)):
#    print(user_list[i], end=' ')
# print("")

print("Here is the sorted list in descending order:", end=' ')
for i in range(len(user_list)-1, -1, -1):
    print(user_list[i], end=' ')
print("")
