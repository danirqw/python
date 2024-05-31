# count = 0     
# word = "hello baby"
# for i in word:
#     if i == "l":
#         count +=1
# print(f"count:{count}")
# i = 5
# while i < 15:
#     print(i)
#     i +=2
    
# a = True
# while a:
#     if input("write:") == "stop":
#         a = False
# for i in range(1, 11):
#     if i ==5:
#         break
#     if i % 2 == 0:
#         continue
#     print(i)
# found = None
# for i in "hello":
#     if i == "l":
#         found = True
#         break
# else:
#     found = False
# print(found)





# nums = [5, 7, 4, 9, [5, 4]]
# nums[0] = 50
# print(nums[-1] [1])
# numbers = [1, 2, 3, 4]
# numbers.append(100)
# numbers.insert(0, True)
# numbers.extend([123,145])
# numbers.sort()
# # numbers.reverse()
# numbers.pop(1)
# numbers.remove(2)
# # numbers.clear()
# print(numbers.count(3))
# print(len(numbers))

# nums = [1, 2, 3, "4", False]
# for el in nums:
#      print(el)

n = int(input("enter length:"))
user_list =[]
i = 0
while i < n:
    string = "enter elemeny #"+ str(i + 1) + ":"
    user_list.append(input(string))
    i += 1
print(user_list)