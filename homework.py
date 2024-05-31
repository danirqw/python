# number = 1
# while number < 10:
#     print("you are welcome")
#     number += 1

# number = int(input("введите число:"))
# word = "silence is golden"
# while number >= 1:
#     print(word)
#     number -= 1
# n = int(input(" введите число:"))
# while n >=1:
#     print("0"*5)
#     n -= 1
# counter = 0
# last = 26
# while counter < 26:
#     counter += 1
#     if counter % 2 ==1:
#         print("первый")
#     else:
#         print("второй")
#     if counter == last:
#         print("расчёт окончен")    
#         break


# mylist = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь","ноябрь", "декабрь" ]    
# for calendar in mylist:
#     print(f"месяц - {calendar}")
# for i in range(12):
#     print(f"{i + 1}. {mylist[i]}")  
# for number, mylist in enumerate(mylist, start=1) :
#     print(f"{number}. {mylist}")     


# menu = [
#     ["burger", "cola"],
#     ["pizza", "tarhun"],
#     ["nagets", " juice"],
# ]
# for food, drink  in menu:
#     print(f"покушать - {food}, попить - {drink}")

# num = input("ведите сисло:")
# summa = 0
# for digit in list (num):
#     summa += int(digit)
# if int (num) % 2 ==0 and summa % 3 == 0:
#     print("число делится на шесть")    
# else:
#     print(" не делится")    



# def find_max(a:int, b:int, c: int):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b 
#     else:
#         return c

# num = int(input("введите число больше 1 :"))
# factorial = 1
# while 0 < num :
#     factorial *= num
#     num -= 1
# print(f" факториал вашего числа равен {factorial}")    
