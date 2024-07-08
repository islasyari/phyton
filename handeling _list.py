def replace_artist(top_artists):
    try: #ask the user for an index and a new artist name
        index = int(input("Enter the index of the artist to replace: "))
        new_artist = input("Enter the new artist name: ")
        top_artists[index] = new_artist
        print("Updated list:", top_artists)
    except (ValueError, IndexError): # function to block error.
        print("An input error occurred.")

def main(): 
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    replace_artist(top_artists)

main()
