bond_actors = {
    "Sean Connery": "From Russia With Love",
    "Roger Moore": "Live and Let Die",
    "Pierce Brosnan": "Die Another Day",
    "Daniel Craig": "Skyfall"
}

# Initialize a score variable
score = 0

print("Try and name 4 actors who have played James Bond.")
for i in range(1, 5):
    #test=input("Attempt",i,"- Name an actor: ")

    actor_name = input(f"Attempt {i} - Name an actor: ").title()  # Convert input to title case

    if actor_name in bond_actors:
        print(f"Well done: {actor_name} was Bond in {bond_actors[actor_name]}.")
        score += 1
    else: 
        print(f"Sorry. {actor_name} hasn’t played Bond as far as I know.")

print(f"\nYou got {score} out of 4.")