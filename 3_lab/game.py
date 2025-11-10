import random

class CardGame:
    CARD_FIRST_NAMES = ["Dragon", "Knight", "Wizard", "Goblin", "Elf"]
    CARD_SECOND_NAMES = ["of Fire", "of Ice", "of Thunder", "of Shadows", "of Light"]
    def __init__(self):
        self.name = f"{random.choice(self.CARD_FIRST_NAMES)} {random.choice(self.CARD_SECOND_NAMES)}"
        self.attack_power = random.randint(5, 15)
        self.health = random.randint(20, 30)
    
    def attack(self, other_card): 
        other_card.health -= self.attack_power
        return f"{self.name} атакує {other_card.name}. {other_card.name} залишилось {other_card.health} здоров'я!"
    
    def defend(self):
        self.health += 2
        return f"{self.name} захищається, здоров'я відновилось до {self.health}!"
    
    def make_move(self, other_card):
        if random.choice([True, False]):
            return self.attack(other_card)
        else:
            return self.defend()

if __name__ == "__main__":
    player_1 = [CardGame(), CardGame(), CardGame()]
    player_2 = [CardGame(), CardGame(), CardGame()]

    for i in range(1, 100):
        print(f"{10*'-'} Раунд {i} {10*'-'}")
        card1 = random.choice(player_1)
        print(f"Наша карта: {card1.name} з атакою {card1.attack_power} та здоровям {card1.health}")
        
        card2 = random.choice(player_2)
        print(f"Ворожа карта: {card2.name} з атакою {card2.attack_power} та здоровям {card2.health}")

        print(card1.make_move(card2))
        print(card2.make_move(card1))

        if card1.health <= 0:
            print(f"*** {card1.name} програв!")
            player_1.remove(card1)
        print(f"Залишилось карт у гравця 1: {len(player_1)}")
        if card2.health <= 0:
            print(f"*** {card2.name} програв!")
            player_2.remove(card2)
        print(f"Залишилось карт у гравця 2: {len(player_2)}")

        if len(player_1) == 0:
            print("### Гравець 1 програв! Всі наші карти програли!")
            break
        elif len(player_2) == 0:
            print("### Гравець 2 програв! Всі ворожі карти програли!")
            break

        print(f"{10*'-'} Кінець раунду {i} {10*'-'}\n")
