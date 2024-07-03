def main():
    book_titles = []
    
    # Collect Book Titles
    while len(book_titles) < 10:
        title = input("Enter a book title: ")
        book_titles.append(title.title())
    
    # Create a Sorted List
    sorted_titles = sorted(book_titles)
    
    # Display the Titles
    for title in sorted_titles:
        print(title)
        
# Call the main function
main()
