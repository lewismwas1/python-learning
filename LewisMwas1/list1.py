books = ["Python Basics", "Java", "CSS", "Python Crash Course", "C++"]
search = input("Enter the book you are searching for: ")
if search.lower() in [book.lower() for book in books]:
    print("book found! ")
else:
    print("Book not found! ")

#list comprehensions
numbers = [1,2,3,4,5,6,7,8,9,10]
new_list = [number for number in numbers if number > 5]
print(new_list)

#square listcomprehension
number_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
squares = [number ** 2 for number in number_list]
print(squares)

#evennumbers
even_numbers = [number for number in  number_list if number % 2 == 0]
print(even_numbers)

#oddnumbers
odd_numbers = [number for number in number_list if number % 2 != 0]
print(odd_numbers)

#doublingnumbers
double_number = [number * 2 for number in number_list]
print(double_number)

#greaterthan 10
greater = [number for number in number_list if number > 10]
print(greater)