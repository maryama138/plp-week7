shopping_list = []

while True:
    print("\nadd / remove / show / done")
    choice = input("What do you want to do? ").lower()

    if choice == "add":
        item = input("Enter an item: ")
        shopping_list.append(item)
        print(item, "was added to your list.")

    elif choice == "remove":
        item = input("Enter an item to remove: ")

        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "was removed from your list.")
        else:
            print("That item is not on your list.")

    elif choice == "show":
        print("Your shopping list:")

        for item in shopping_list:
            print("-", item)

    elif choice == "done":
        print("Goodbye!")
        break

    else:
        print("Please choose add, remove, show, or done.")
