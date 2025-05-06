# Create an empty list

book_list = []

# Input the list size
list_size = input("Enter the Book list size: ")
# Check list size input validation
try:
    list_size = int(list_size)
except (
        ValueError):
        print("Invalid list size input, Please enter a number")
        exit()
# Ask the user for 3 favorite books
count =0
while count < list_size:
    book = input(f"Enter the name of favorite book #{count+1}: ").strip().title()
    # Input validation: make sure the book name is not empty
    if not book: # If input is empty
        print("Book name can't be empty. Try again.")
        continue

    # Add to the list
    book_list.append(book)
    count += 1

# Print the final list
print("\nHere is Your favorite books Lists:")
for book in book_list:
    print("-", book)

# Remove a book
# Remove confirmation
remove_conf = input("\nWould you like to remove a book? (y/n): ").strip().lower()

# Remove book from list using conditionals
if remove_conf == "y":

    # Input for remove book from list
    remove_in = input("Enter the book name to remove: ").strip().title()

    # Remove conditionals
    if remove_in in book_list:
        book_list.remove(remove_in)
        print(f"'{remove_in}' has been removed from your list.")
    else:
        print(f"'{remove_in}' was not found in your list.")

    # Show updated list
    print("\nUpdated Book List:")
    for book in book_list:
        print("-", book)
