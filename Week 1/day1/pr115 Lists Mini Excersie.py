# Create an empty list

book_list = []

# Input the list size
list_size = input("Enter the Book list size: ")
# Check list size input validation
try:
    list_in = int(list_size)
except (
        ValueError):
        print("Invalid list size input, Please enter a number")
        exit()
# Ask the user for 3 favorite books
count =0
while count < list_in:
    book = input(f"Enter the name of favorite book #{count+1}: ")
    # Input validation: make sure the book name is not empty
    if book == "":
        print("Book name can't be empty. Try again.")
        continue

    # Add to the list
    book_list.append(book)
    count += 1

# Print the final list
print("\nHere is Your favorite books Lists:")
for book in book_list:
    print("-", book)
