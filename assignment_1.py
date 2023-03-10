print("Please Enter the number of inputs:", end=" ")
count = int(input().strip())

user_list = []
for i in range(count):
    # print("Please Enter the input number {}".format(i+1))
    # print(f"Please Enter the input number {i+1}", end=" ")
    print('Please Enter the input number %s:' % (i+1), end=" ")
    user_list.append(int(input().strip()))

print("The Minimum number is:", min(user_list))
print("The Maximum number is:", max(user_list))
print("The Average of the inputs is:", sum(user_list)/len(user_list))
# print("Here is the sorted list in ascending order:", sorted(user_list))
# print("Here is the sorted list in descending order:", sorted(user_list, reverse=True))

user_list.sort()
print("Here is the sorted list in ascending order:", end=' ')
for i in range(len(user_list)):
    print(user_list[i], end=' ')
print("")

# user_list.sort(reverse=True)
# print("Here is the sorted list in descending order:", end=' ')
# for i in range(len(user_list)):
#    print(user_list[i], end=' ')
# print("")

print("Here is the sorted list in descending order:", end=' ')
for i in range(len(user_list)-1, -1, -1):
    print(user_list[i], end=' ')
print("")
