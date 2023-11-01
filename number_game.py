import random
print("Компьютер загадал число от 1 до 100. Попробуй его угадать!")
secret_number = random.randint(1, 100)
tries = 0
while tries <= 10:
    tries +=1
    print(f"попытка №{tries}")
    person_number = int(input("Введите число:") )
    if person_number > secret_number:
        print("вы вели число больше чем моё")
    elif person_number < secret_number:
        print("вы вели число меньше чем моё")    
    elif person_number == secret_number:
        print("ты угадал, молодец") 
        break
    print()
       
    

    
    