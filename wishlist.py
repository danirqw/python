import random
import os
def read_list():
    if not os.path.exists("whishlist.txt"):
        return[]
    file = open("whishlist.txt", "r", encoding="UTF-8")
    text = file.read().split("\n")
    file.close()
    return
def write_list(wish):
    file = open("whishlist.txt", "a", encoding="UTF-8")
    file.write(wish + "\n")
    file.close()
def game():
    print("Здраствуйте! Вы открыли приложение список желании")
    whishlist = read_list()
    while True:
        print(f" в этом приложение вы можете добавить желание.\n1 - добавить желание\n2 - вывести желании\n3 - выйти из программы")
        if random.randint(1,2) == 1 and len(whishlist) > 0:
            wish = random.choice(whishlist)
            print(f"не забудь ты своё желание исполнить: {wish}") 
        option = input("ваш выбор:")
        if option == "1":
            wish = input("Введите ваше желание:")
            if wish not in whishlist:
                whishlist.append(wish)
                write_list(wish)
        elif option == "2":
            if len(whishlist) == 0:
                print("у вас пока в спмске нет желании")
            else:    
                for number, desire in enumerate(whishlist, start=1):
                    print(f"{number}.{desire}")
        elif option == "3":
            print("спасибо за пользование программой")       
            break      
        else:
            print("в меню нет больше варинтов")
        input("для продолжения нажмите Enter")
if __name__ == "__main__":
    game()       
                
        
