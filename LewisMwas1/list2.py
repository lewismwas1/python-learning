fruit_list = ["apple", "mango", "banana", "appricot", "orange", "avocado"]
fruits1 =[fruit.upper() for fruit in fruit_list]
print(fruits1)

#ifword starts with 'a'
new_fruits = [fruit for fruit in fruit_list if fruit[0] == "a"]
print(new_fruits)

#positive and negative values in a list
numbers = [1,-2,-5,-10,15,20,12,-3]
positive_numbers = [number for number in numbers if number > 0]
negative_numbers = [number for number in numbers if number < 0]
print(positive_numbers)
print(negative_numbers)
new_numbers = [0 if number < 0 else number for number in numbers]
print(new_numbers)


#input library books
library_books = [
    "Python Basics",
    "Advanced Python",
    "Java Basics",
    "Python Fundamentals",
    "C++",
    "Python Data science"
]
search = input("What book are you looking for ? : ").lower()

found_books = [book for book in library_books if search in book.lower()]
if found_books:
    print("Books found in library: ")
    for books in found_books:
        print(books)
else:
    print("Books not Found! ")