import random

# Pozdrav a pravidla
print("Ahoj, vítej ve hře Kámen, nůžky, papír!")
print("Pravidla: Kámen porazí nůžky, nůžky porazí papír, a papír porazí kámen.")

# Seznam možností
options = ["kámen", "nůžky", "papír"]

while True:
    # Uživatelská volba
    user_choice = input("Vyber si: kámen, nůžky, nebo papír? ").lower()
    if user_choice not in options:
        print("Neplatná volba. Zkus to znovu!")
        continue

    # Počítačova volba
    pc_choice = random.choice(options)
    print(f"Počítač si vybral: {pc_choice}")

    # Vyhodnocení
    if user_choice == pc_choice:
        print("Je to remíza!")
    elif (user_choice == "kámen" and pc_choice == "nůžky") or \
         (user_choice == "nůžky" and pc_choice == "papír") or \
         (user_choice == "papír" and pc_choice == "kámen"):
        print("Vyhrál/a jsi!")
    else:
        print("Prohrál/a jsi!")

    # Hrát znovu?
    play_again = input("Chceš hrát znovu? (ano/ne) ").lower()
    if play_again != "ano":
        print("Díky za hru! Měj se krásně!")
        break
