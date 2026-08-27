number = 1
while number <= 10:
    print(number)
    number += 1

# library example
books = 5
while books > 0:
    print(f"There are {books} available in the library.")
    books -= 1
    if books == 0:
        print("There are no books available in the library.")

choice = ""
while choice != "5":
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Display Books")
    print("5. Exit")

    choice = input("Enter your choice: ")
    print(f"You selected option {choice}.")
    if choice == "5":
        print("Exiting the program.Goodbye!")

choice1 = ""
while choice1 != "4":
    print("\n LIBRARY MENU")
    print("1. Add book")
    print("2. Borrow book")
    print("3. Return Book")
    print("4. Exit")

    choice1 = input("Enter your choice: ")

    if choice1 == "1":
        print("Adding a book...")
    elif choice1 == "2":
        print("Borrowing a book...")
    elif choice1 == "3":
        print("Returning a book...")
    elif choice1 == "4":
        print("Exiting the Library Menu. Goodbye!")
    else:
        print("Invalid choice.Please Try Again")



#while loopwith break statetement
while True:
    book4 = input("Enter a book title: ").strip()
    if book4.lower() == "exit":
        break

    if book4 == "":
        print("The book title cannot be empty")
        continue

    print("Book added: ", book4)

#restaurant menu example
while True:
    order = input("Enter an order: ").strip()
    if order.lower() == "done":
        break

    if order == "":
        print("The Order cannot be empty")
        continue

    print(f"{order} added to Menu.")