# class Operators and expressions
name = 'Alice'
print(f"Hello, {name}!")

a = 15
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

score = 85
score -=5

print(score)
score *=2

print(score)

available_books = 100
borrowed_books = 55
print(f"The number of available books is: {available_books - borrowed_books}")

member_name = "Trevor"
title_book = "God of War"
message = member_name + " borrowed " + title_book
print(message)
print(f"{member_name} borrowed {title_book}")

fine_per_day = 20
overdue_days = 5
print(f" Your total fine is {fine_per_day * overdue_days} kenya shillings)")

book_status = "available"
book_status == "available"
if book_status == "available":
    print("The book is available for borrowing.")

book_status = "borrowed"
book_status != "available"
if book_status != "available":
    print("The book is not available for borrowing.")

copies_available = 25
books_borrowed = 30
if copies_available > 10 and books_borrowed > 20:
    print("There are  enough copies available for borrowing.") 
else: 
    print("There are not enough copies available for borrowing.") 

member_age = 18
membership_status = True
if member_age >= 18 or membership_status  != True:
    print("The member is eligible for borrowing books.")
else:
    print("The member is not eligible for borrowing books.")

# is and is not operators
shelf1 = ["python", "java", "c#", "c++"]
shelf2 = shelf1
print(shelf1 is shelf2)

#in and not in operators
book_in_library = ["python","java", "c#", "c++"]
if "python" in book_in_library:
    print("Python is available in the library")
if "html" not in book_in_library:
    print("HTML is not available in the library") 

# string methods
search = "PYTHON"
if search.lower() == "python":
    print("Search matched.")