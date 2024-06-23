def main():
    programming_classes = ('Intro to Python', 'Advanced Python', 'Database Essentials', 'Web Development Basics', 'Data Structures in Python', 'Web Design Fundamentals')

    for course in programming_classes:
        print(course)

    number_of_classes = len(programming_classes)
    print(f'Total classes: {number_of_classes}')

if __name__ == '__main__':
    main()
