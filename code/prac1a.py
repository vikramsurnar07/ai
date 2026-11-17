# Vacuum Cleaner Reflex Agent

rooms = {
    "A": "Dirty",
    "B": "Dirty"
}
current_room = "A"

print("Initial Room Status")
print(rooms)

while True:
    print("\nAgent is in Room", current_room)
    if rooms[current_room] == "Dirty":
        print("Room is Dirty.")
        print("Action: Cleaning Room", current_room)
        rooms[current_room] = "Clean"
    else:
        print("Room is Clean.")
        if current_room == "A":
            current_room = "B"
        else:
            current_room = "A"
        print("Moving to Room", current_room)

    if rooms["A"] == "Clean" and rooms["B"] == "Clean":
        break

print("\nFinal Room Status")
print(rooms)
print("\nAll rooms are clean.")
