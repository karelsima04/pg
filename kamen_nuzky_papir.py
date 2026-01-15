import random

rock = "👊"
scissors = "✌️"
paper = "🫱"

all_list = [rock, scissors, paper]

choose = int(input("Vyberte 0 pro kámen, 1 pro nůžky, 2 pro papír:\n"))
pc_choose = random.randint(0, 2)

user_picture = all_list[choose]
pc_picture = all_list[pc_choose]


print(user_picture)
print(pc_picture)

if pc_choose == 0 and choose == 0:
    print("Remíza")
if pc_choose == 1 and choose == 0:
    print("Vyhrál jsi")
if pc_choose == 2 and choose == 0:
    print("Prohrál jsi")   

if pc_choose == 0 and choose == 1:
    print("Prohrál jsi")
if pc_choose == 1 and choose == 1:
    print("Remíza")
if pc_choose == 2 and choose == 1:
    print("Vyhrál jsi")   

if pc_choose == 0 and choose == 2:
    print("Vyhrál jsi")
if pc_choose == 1 and choose == 2:
    print("Prohrál jsi")
if pc_choose == 2 and choose == 2:
    print("Remíza")   
