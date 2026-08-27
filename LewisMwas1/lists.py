books = ["python","Java", "CSS", "Javascript"]

print(books[0])
print(books[1])
print(books[2])
print(books[3])

books[0] = "Django"
print(books[0])
print(books[1])

#append()/adding ite to a list
books.append("SQL")
print(books)

#removing an item from a list
books.remove("Javascript")
print(books)

#length of books
print(len(books))

for book in books:
    print(f"I have a book called {book}")

books_library =["Python basics", "Java", "CSS", "Python Crashcourse", "C++"]
for book in books_library:
    if "Python " in book:
        print(f"Python book found: {book}")