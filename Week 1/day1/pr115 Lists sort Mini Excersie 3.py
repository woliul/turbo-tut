# Create an empty list
books = []

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
    books.append(book)
    count += 1

# Print the final list
print("\nHere is Your favorite books Lists:")
for book in books:
    print("-", book)

# Search a book
# Search confirmation
search_conf = input("\nWould you like to search a book? (y/n): ").strip().lower()

# Search book from list using conditionals
if search_conf == "y":

    # Input for search book from list
    search_in = input("Enter the book name to search: ").strip().title()

    # search conditionals
    if search_in in books:
        print(f"'{search_in}' is in your book list.")
    else:
        print(f"'{search_in}' was not found in your list.")

# Remove a book
# Remove confirmation
remove_conf = input("\nWould you like to remove a book? (y/n): ").strip().lower()

# Remove book from list using conditionals
if remove_conf == "y":

    # Input for remove book from list
    remove_in = input("Enter the book name to remove: ").strip().title()

    # Remove conditionals
    if remove_in in books:
        books.remove(remove_in)
        print(f"'{remove_in}' has been removed from your list.")
    else:
        print(f"'{remove_in}' was not found in your list.")

    # Show updated list
    print("\nUpdated Book List:")
    for book in books:
        print("-", book)


# sort and sorted

# sort confirmation
sort_conf = input("\nWould you like to sort the list? (y/n): ").strip().lower()

# sort book from list
if sort_conf == "y":
    books.sort()  # Try sort without key
    print("Sort (case-sensitive):", books)

    books.sort(key=str.lower)  # Try sort with key
    print("Sort (case-insensitive):", books)

    sorted_books = sorted(books)  # Try sorted without key
    print("Sorted (case-sensitive):", sorted_books)

    sorted_books.sort(key=str.lower)  # Try sorted with key
    print("Sorted (case-insensitive):", sorted_books)