import fight
import number_game
import magicall_ball
import textquest
import wishlist
import functions
import harry
import library
from colorama import Fore, Back, Style
def sign_up():
    login = input("введите логин:")
    password1 = input("введите пароль:")
    password2 = input("введите пароль:")
    many_logins = give_list("logins.txt")
    
    if login =="" or password1 =="" or password2=="":
        print("введены не полные данные")
    elif login in many_logins:
        print("такой логин уже существует")
    elif password1 == password2:
        with open("logins.txt", "a", encoding="UTF - 8") as file:
            file.write(login + "\n")
        with open("passwords.txt", "a", encoding="UTF - 8") as file:
            file.write(f"{password2}\n")
            print(f"Пользователь {login} добавлен в систему") 
    else:
        print("Пароли не совпадают") 
def give_list(filename):
    with open(filename, mode="r", encoding="UTF-8") as file:
        text = file.read().split("\n") 
        return text
def sign_in():
    login = input("введите логин:")  
    password = input("введите пароль:") 
    all_logins = give_list("logins.txt")
    all_passwords = give_list("passwords.txt")
    if login in all_logins:# если логин есть в базе данных
        login_line = all_logins.index(login) # беерём номер строки
        true_password = all_passwords[login_line] # взяли пароль с тойже  строки
        if true_password == password:
            print("вы вошли в систему")
            return True, login
        else:
            print("вы вели не тот пароль или не тот логин") 
    else:
        print("такого логина нет")           
    
go = False  
while True:
    if go == False:# если go выключен 
        print(Fore.MAGENTA + "добро пожаловать в  иной мир")
        print("меню:")
        print("1 - зарегистрироваться")
        print("2- войти")
        print("3 - выйти из программы" + Style.RESET_ALL)
        
        choise = input("ваш выбор:") 
        if choise == "1":
            sign_up()
        elif choise =="2":
            go, login = sign_in() #если мы вошли тогда go становиться True    
        elif choise == "3":
            print(" спасибо за использование программы")    
            break
        else:
            print("нет такого вариант")
        input("Нажмите Enter")
    else:# если go вллючен
        print(f"Приветствуем тебя {login}")
        print("меню:")
        print("1 - выйти из программы")
        print("2 - сыграть магическую битву")
        print("3 - сыграть number game")
        print("4 - сыграть magical ball")
        print("5 - сыграть textqwest")
        print("6 - сыграть список желаний")
        print("7 - сыграть тексткрафт")
        print("8 - мой проект")
        choise = input("ваш выбор:") 
        if choise == "1":
            print(" спасибо за использование программы")    
            break
        elif choise == "2":
            fight.game()
        elif choise =="3":
            number_game.game(login)
        elif choise =="4":
            magicall_ball.game()
        elif choise =="5":
            textquest.game()
        elif choise =="6":
            wishlist.game()
        elif choise =="7":
            functions.game()
        elif choise =="8":
            harry.game()
        else:
            print("нет такого вариант")
        input("Нажмите Enter") 

   
    
    
    
        