import random
import time

#Character Creation - Value Returning
def create_character():
    name = input("Enter your Warrior's Name: ")
    health = int(input("Enter your Starting Health: "))
    attack_points =int(input("Enter your Starting Strength: "))

    character = {
        "name": name,
        "health": health,
        "attack_points": attack_points
    }
    print('Welcome', name)
    return character

#See Your Character - Non Returning
def display_character(character):
    print("Character Info:")
    print(f"Name: {character['name']}")
    print(f"Health: {character['health']}")
    print(f"Damage: {character['attack_points']}")
    
#Adventuring
def adventure(character):
    event = random.choice(["healing_potion", "trap_damage", "strength_upgrade"])
    if event == "healing_potion":
        heal = random.randint(5, 20)
        character["health"] += heal
        print(f"Thata a fine looking potion, it boosts {character['name']}'s health by {heal} points!")
    elif event == "trap_damage":
        damage = random.randint(5, 30)
        character["health"] -= damage
        print(f"You should be more careful on your journey, that fall cost {character['name']}'s {damage} points of health!")
    elif event == "strength_upgrade":
        power_increase = random.randint(5, 40)
        character['attack_points'] += power_increase
        print(f"Looks like that side quest was worth it, {character['name']}'s got a strength potion and gained {power_increase} points of damage!")

#Boss Battle
boss_list = [
    {"name": "Dou no Senshi, Bronze Warrior of the Ancient Glades", "health": 150, "attack_points": 35, "reward": "Bronze Tsuka"},
    {"name": "Gin no Senshi, Silver Warrior of the Ancient Glades", "health": 250, "attack_points": 55, "reward": "Silver Fuchi"},
    {"name": "Ougon no Senshi, Golden Warrior of the Ancient Glades", "health": 350, "attack_points": 75, "reward": "Golden Ba"}
]

def boss_battle(character):
    global boss_list

    if not boss_list:
        print("All bosses have been vanquished and the Ancient Glades have been returned to peace, you forge their remains into the fabled 'Henkei Suru Kinzoku no Katana'!")
        return character

    boss = random.choice(boss_list)
    print(f"A Boss Appears: {boss['name']} (Health: {boss['health']}, Attack: {boss['attack_points']})!")
    time.sleep(2)

#Turn Sequence      
    for turn in range(100):
        if turn % 2 == 0:  
            damage = (character["attack_points"])
            boss["health"] -= damage
            boss["health"] = max(boss["health"], 0)
            print(f"{character['name']} attacks for {damage} damage! {boss['name']} has {boss['health']} health left.")
            time.sleep(2)
        else:  
            damage = (boss["attack_points"])
            character["health"] -= damage
            character["health"] = max(character["health"], 0)
            print(f"{boss['name']} attacks for {damage} damage! {character['name']} has {character['health']} health left.")
            time.sleep(2)


        if boss["health"] == 0:
            boss_list.remove(boss)
            print(f"{character['name']} defeated {boss['name']} and obtained the {boss['reward']}!")
            time.sleep(2)
            return character

        if character["health"] == 0:
            print(f"{character['name']} was defeated by {boss['name']}...")
            time.sleep(2)
            return character

#Main Menu
def main():
    character = None
    running = True  

    while running:
        print("\n--- Protector of Ancient Glade Demo ---")
        print("1. Create a character")
        print("2. View character info")
        print("3. Go on an adventure")
        print("4. Fight a boss")
        print("5. Exit game")

        if not boss_list:
            print("All bosses have been vanquished and the Ancient Glades have been returned to peace, you forge their remains into the fabled 'Henkei Suru Kinzoku no Katana'!")

        choice = input("Choose an option: ")

        if choice == '1':
            character = create_character()
        elif choice == '2':
            if character:
                display_character(character)
            else:
                print("You need to create a character first!")
        elif choice == '3':
            if character and character["health"] > 0:
                adventure(character)
            else:
                print("Hard to adventure when your dead, isn't it?")
        elif choice == '4':
            if character and character["health"] > 0:
                character = boss_battle(character)
            else:
                print("Hard to fight when your dead, isn't it?")
        elif choice == '5':
            print("Exiting game. Thanks for playing!")
            running = False  # Set running to False to exit the loop
        else:
            print("Invalid choice. Please choose a valid option.")

main()
    













            
