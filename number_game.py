import random
def game(login:str):

    print("Компьютер загадал число от 1 до 100. Попробуй его угадать!")
    secret_number = random.randint(1, 100)
    tries = 0
    name = login.capitalize()
    while tries <= 10:
        tries +=1
        print(f"попытка №{tries}")
        person_number = input("Введите число:") 
        if not person_number.isdigit():
            print("неправильный ввод. вводите только числа")
            tries -=1
            continue
        person_number = int(person_number)
        if person_number > secret_number:
            print(f"{name}, вы вели число больше чем моё")
        elif person_number < secret_number:
            print(f"{name},вы вели число меньше чем моё")    
        elif person_number == secret_number:
            print(f"{name}, ты угадал, молодец") 
            break
        print()
        if tries ==10:
            print(f"вы не угадали, число было {secret_number}")
if __name__ == "__main__":
    game()
  
        
        

       
    

    
    