
# # numbers=[1,2,3,4,5,6,7,89,2]
# # max=numbers[0] #assume 1st number is greatest 
# # for i in numbers:
# #     if i>max:
# #         max=i
# # print(max)
# print(True == 1)
# print(True is 1)

new=[1,2,3,4,5,6,7,7,8,9,9,0,0]
filter=[]
for numbers in new:
    if numbers not in filter:
        filter.append(numbers)

print(f'The sorted list is\n{filter}')
