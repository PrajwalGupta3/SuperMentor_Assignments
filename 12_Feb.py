#Assignment Name : Smart Input Program
#Description : Build a Python program that takes name, age, hobby and prints a personalized message while categorizing age using conditionals.
# Assignment Name : Smart Input Program

try:
    name = input("Enter your name: ").strip()
    age = int(input("Enter your age: "))
    original_hobby = input("Enter your hobby: ").strip()

    if age < 13:
        age_group = "child"
    elif 13 <= age < 20:
        age_group = "teenager"
    elif 20 <= age < 60:
        age_group = "adult"
    else:
        age_group = "senior"

    hobby_lower = original_hobby.lower()
    if hobby_lower in ["reading", "writing", "painting"]:
        category = "creative"
    elif hobby_lower in ["sports", "gaming", "traveling"]:
        category = "active"
    else:
        category = "unique"

    if age_group == "adult":
        print(f"\nHello {name}! As an {age_group}, it's cool that you enjoy {original_hobby}.")
    else:
        print(f"\nHello {name}! As a {age_group}, it's cool that you enjoy {original_hobby}.")
        
    print(f"That sounds like a very {category} way to spend your time!")

except ValueError:
    print("Oops! Please enter a valid number for your age.")
