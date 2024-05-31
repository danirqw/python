def first_action():
    while True:
        answer = input("ты кушал обед? (да\нет)")
        if answer == "да":
            print("У тебя есть энергия")
            return True
        elif answer == "нет":
            print("У тебя нет энергии")
            return False    
def second_action():
    while True:
        answer = input('"пожар!", - услышал ты истерический щум своих соседей.Бежим на улицу?(да\нет)')
        if answer =="да":
            print("ты выбежал на улицу")
            return True
        elif answer == "нет":
            print("ты остался дома")
            return False     
def third_action(energy:bool, is_outside:bool):
    if energy and is_outside:
        print("вы увидили красивую девушку. Дом сгорел, но вы с ней познакомились и теперь живёте с ней")
    elif not energy and is_outside:
        print("У вас нет сил, вы упали вподъезде, сгорели, а вот девушка-пожарный потушила вашу квартиру и продала её")
    elif energy and not is_outside:
        print("вы плотно поели, но сгорели")   
    else:
        print("вы подошли к батарее, постучали по ней и соседи перестали кричать про жар.Вы легли на кровать и уснул") 
def game():
    energy = first_action()
    is_outside = second_action()
    third_action(energy, is_outside) 
if __name__ == "__main__":
    game()