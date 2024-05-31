import time
import random
spells = { # словарь
    "Авада кедавра": 100,
    "экспелиармус": 15,
    "редукто":random.randint(30, 40),
    "круциатус":random.randint(35, 45),
    "cектум сепра":random.randint(40,45),
    "репаро":random.randint(15,35)
}
class Character:
    def __init__(self, name:str, power:int, defense:str):
        self.name = name
        self.power = power
        self.hp = 100
        self.lov = random.randint(1, 100)
        self.defence = defense
    def evade(self):
        if random.randint(self.lov,100) ==self.lov:
            print(f"{self.name} уклонился от атаки.Удачи!")
            return True
        return False
    def get_spell(self):
        zaklinaniya = list(spells.keys()) [:-1]
        return random.choice(zaklinaniya)
        
        
    def attack(self, attacted_character, spell):
        if attacted_character.evade(): # если мы уклонились
            return  None # выходим из метода без урона
        elif spell == attacted_character.defence:
            print(f"{attacted_character.name} обладает защитой от {spell} атака не прошла")
            return None
        attacted_character.hp -= spells[spell]
        print(f"{self.name} атаковал персонажа {attacted_character.name} заклинанием {spell}")
    def say_info(self):
        if self.hp < 0:
            self.hp = 0
        elif self.hp > 100:
            self.hp =100
        
        print(f"состояние у персонажа {self.name} : жизней {self.hp} ловкости: {self.lov} ")

class Player(Character):
    pass
    def heal(self):
        self.hp += spells["репаро"]
        print(f"{self.name} применил заклинанаие репаро. Да здраствует жизнь!")
def change(char:character):
    player.name = char.name
    player.power = char.power
    player.defence = char.defence   

player = Player("неподражаемый Данир", power=10,defense="Авада кедавра")
def game():    

    char1 = Character("Гарри Потер", power=8, defense="Авада кедавра")
    char2 = Character("Рон Уизли", power=6, defense=None)
    char3 = Character("Гермион Грайнджер", power=7, defense="cектум сепра")
    char4 = Character("волендеморт",  power=8, defense="Авада кедавра")
    char5 = Character("Белатриса Лестрайндж",  power=7, defense="круциатус")
    char6 = Character("северус снейп",  power=7, defense="cектум сепра")

    characters1 = [char1, char2, char3,]
    characters2 = [char4, char5, char6]
    player_choice = input(f"Выбери персонажа из списка:\n1-Гарри Потер\n2-Рон Уизли\n3Гермион Грайнджер\n4-{player.name}")
    enemy2 = random.choice(characters2)
    if player_choice == "1":
        change(char1)
    elif player_choice == "2":
        change(char2)
    elif player_choice == "3":
        change(char3)

        
    #characters.remove(char1)



    while True:
        action = input("выбири действия:\n1-лечиться\n2-атаковать\n")
        if action == "1":
            player.heal()
        elif action == "2":  
            player_spell = player.get_spell()
            time.sleep(1)
            player.attack(enemy2, player_spell)
        else:
            print("такого действия нет")
            continue
        player.say_info()
        enemy2.say_info()
        print()
        time.sleep(1)
        enemy2_spell = enemy2.get_spell()
        enemy2.attack(player, enemy2_spell)
        player.say_info()
        enemy2.say_info()
        print()
        if player.hp <= 0 and enemy2.hp <= 0:
            print("НИчья")
            break
        elif player.hp <= 0:
            print(f"{enemy2.name} победил")
            break
        elif enemy2.hp <= 0:
            print(f"{player.name} победил")
            break
if __name__ =="__main__":
    game()




