import random
def game():
    print("Здраствуйте! Вы открыли приложение магический шар")
    answers = ["да", "возможно", "без сомнений", "мне кажеться нет", "конечно", "очень вероятно", "ответ не ясен", "не могу сказать", "не надейтесь"  "категорический нет", "нет", "духи говорят да"]
    while True:
        print(f"1 - в этом приложение вы можете спросить что нибудь .\n2 - выйти из программы")
        option = input("ваш выбор:")
        if option == "1":
            accidents = input("спросите что-нибудь:")
            ansmer = random.choice(answers)
            print(ansmer)
        elif option == "2":
            print("спасибо за пользование программой")       
            break  
        else:
            print("в меню нет больше варинтов")   
        input("для продолжения нажмите Enter")       
if __name__ == "__main__":
    game()