import random
basket = []
damage = 0
def attack():
    global damage
    damage += random.randint(100, 1000)
    print("Робот бьёт Землю")
    print(f"текущий уверень повреждения {damage}")
    if damage >= 10000:
        print("Земля уничтожена")
        exit()
def wash():
    print("машина стирает")
def robot_up():
    """робот пойдёт вперёд"""
    print("робот идёт вперёд")
def robot_down():
    print("робот идёт назад")
def robot_right():
    print("робот идёт на право") 
def robot_left():
    print("робот идёт на лево")
def robot_jump():
    print("робот прыгает")
def robot_grab(what_we_found:str):
    global basket
    print(f"робот взял алмаз {what_we_found}")
    basket.append(what_we_found)
def robot_search():
    items = ["уголь","уголь", "железо", "дерево","дерево","дерево",  "золото", "свинец", "палка", "палка" "палка", "топопр"]
    item = random.choice(items)
    print(f"найден предмет:{item}")
    return item
def show_basket():
    if len(basket) > 0:
        for index, element in enumerate(basket,start=1):
            print(f"{index}.{element}")
    else:
        print("в инвентаре нет ничего")
def crafting():
    recept1 = ["палка","железо"] # кирка железная
    recept2 = ["палка","золото"] # кирка золоотая
    recept3 = ["палка","свинец"] # кирка свинцовая
    recepts=[recept1, recept2, recept3]
    receptmeans = [" кирка железная","кирка золоотая","кирка свинцовая"]
    for index, recept in enumerate(receptmeans,start=1):
        print(f"{index}.{recept}")
    while not (choice:= input("выберите что крафтить:")).isdigit():
        print("нужно вводить число")
    if int(choice)<=len(recepts) :
        thing = recepts[int(choice) - 1]  
        while thing:
            show_basket()
            print(f"осталось :{thing}") 
            choice = input("что будем использовать ? ")
            if choice == "стоп":
                break
            elif choice.isdigit() ==True:
                if int(choice)<=len(basket):
                    used = basket[int(choice)-1]
                    if used in thing:
                        print(f"использованно :{used}")
                        basket.pop(int(choice)-1)
                        thing.remove(used)
                    else:
                        print("ой, так такого не надо")
            else:
                print("введите номер элемента или стоп")
        if not thing:
            basket.append(receptmeans[recepts.index(thing)])        
                
    
                   






def game():
    while True:
        key = input("введите клавишу (wasdepor):")
        if key == "w":
            robot_up()
        elif key == "a":
            robot_left()
        elif key == "s":
            robot_down()
        elif key == "d":
            robot_right() 
        elif key == " ":
            robot_jump()
        elif key =="r":
            attack()
        elif key == "e":
            if random.randint(1,2) ==1:
                predmet = robot_search()
                robot_grab(predmet)
            else:
                print("робот ничего не нашёл")
        elif key == "p":
            show_basket()
        elif key == "o":
            crafting()
                
        else:
            print("нет такой функции")
if __name__ == "__main__":
    game()           
    
    