import random
def redookto(hp):
    hp -=30
    return hp

def episkey(hp):
    hp +=20
    return hp

def stupify(hp):
    hp -= 10
    return hp
def reparo(hp):
    hp += 10
    return hp

def change_malfoy(zaklinanie):
    print(f"У Малфоя было {malfloy_hp}")
    malfloy_hp = zaklinanie(malfloy_hp)
    print(f"У Малфоя стало {malfloy_hp}")
    return malfloy_hp
def change_me(zaklinanie):
    print(f"У вас было {my_hp}")
    my_hp = zaklinanie(my_hp)
    print(f"У вас стало {my_hp}")
    return malfloy_hp

def game():
    print("здраствуйте вы находитесь в игре HARRY POTTER")
    print("вы играете с персонажем Гарри потер" )
    my_hp = 100
    malfloy_hp = 100
    list_attack = ["redookto", "episkey","stupify"]
    while True:
        print("вы можете использовать заклинания такие как: redookto, episkey, protect, stupify")
        magic = input("введите заклинание:")
        malfloy_attack = random.choice(list_attack )   
        if magic == "stupify":
            malfloy_hp = change_malfoy(stupify)
        elif magic == "redookto":
            malfloy_hp = change_malfoy(redookto)
        elif magic == "episkey":
            malfloy_hp = change_me(episkey) 
        elif magic == "reparo":
            malfloy_hp = change_me(episkey)   
            
            
        if malfloy_attack == "reparo":
            malfloy_hp = change_malfoy(reparo)
        elif malfloy_attack == "episkey":
            malfloy_hp = change_malfoy(episkey)
if __name__ == "__main__":
    game()    
    

      
