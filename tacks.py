# def  season(month:int):
#     if month in [1, 2, 12]:
#         return" зима"
#     if month in [3, 4, 5]:
#         return" весна"    
#     if month in [6, 7, 8]:
#         return" лето"
#     if month in [9, 10, 11]:
#         return" осень"
    
# print(season(month=6))

# def cel_to_far(cel:int):
#     far = cel *1.8 + 32
#     return far
# cel = int(input("введите число:"))
# far = cel_to_far(cel)
# print(far)

import random
def robot_scan():
    things_to_find = ['алмаз', 'рубин']
    thing = random.choice(things_to_find)
    if random.randint(1,2) ==1:
        return thing
    else:
        return 'ничего'
what_r_f = robot_scan()
print(f"Робот нашёл {what_r_f}")    