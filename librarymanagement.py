import datetime

# Dictionary to manage book records
books = {}  # book_name: {'available': bool, 'issued_to': str or None, 'issue_date': date or None, 'allotted_days': int or None}

def add_books():
    book_name = input("Enter the name of the book to add: ").strip()
    if not book_name:
        print("Book name cannot be empty.")
        return
    if book_name in books:
        print(f"'{book_name}' already exists in the library.")
    else:
        books[book_name] = {'available': True, 'issued_to': None, 'issue_date': None, 'allotted_days': None}
        print(f"'{book_name}' has been added to the library.")

def show_books():
    available_books = [book for book, details in books.items() if details['available']]
    if not available_books:
        print("No books are currently available in the library.")
    else:
        print("Available books in the library:")
        for book in available_books:
            print(f"  - {book}")

def issue_books():
    book_name = input("Enter the name of the book to issue: ").strip()
    if book_name not in books:
        print(f"'{book_name}' does not exist in the library.")
        return
    if not books[book_name]['available']:
        issued_to = books[book_name]['issued_to']
        print(f"'{book_name}' is already issued to {issued_to}.")
        return
    
    student_name = input("Enter the student's name: ").strip()
    if not student_name:
        print("Student name cannot be empty.")
        return
    
    try:
        allotted_days = int(input("Enter the number of days the book is allotted for: "))
        if allotted_days <= 0:
            print("Allotted days must be a positive number.")
            return
    except ValueError:
        print("Invalid number for allotted days.")
        return
    
    issue_date = datetime.date.today()
    books[book_name]['available'] = False
    books[book_name]['issued_to'] = student_name
    books[book_name]['issue_date'] = issue_date
    books[book_name]['allotted_days'] = allotted_days
    
    print(f"'{book_name}' has been issued to {student_name} for {allotted_days} days.")
    print("Note: Fines apply after the allotted period as follows:")
    print("  - 1st week overdue: Rs. 10/day")
    print("  - 2nd week overdue: Rs. 20/day")
    print("  - 3rd week overdue: Rs. 60/day")
    print("  - And so on, with rates increasing weekly.")

def return_books():
    book_name = input("Enter the name of the book to return: ").strip()
    if book_name not in books:
        print(f"'{book_name}' does not exist in the library.")
        return
    if books[book_name]['available']:
        print(f"'{book_name}' was not issued.")
        return
    
    issue_date = books[book_name]['issue_date']
    allotted_days = books[book_name]['allotted_days']
    return_date = datetime.date.today()
    days_passed = (return_date - issue_date).days
    
    if days_passed <= allotted_days:
        fine = 0
        fine_message = "No fine applied."
    else:
        overdue_days = days_passed - allotted_days
        fine = 0
        for day in range(1, overdue_days + 1):
            # Calculate the week for this overdue day
            total_day = allotted_days + day
            week = ((total_day - 1) // 7) + 1
            if week == 1:
                rate = 10
            else:
                rate = 10
                for i in range(2, week + 1):
                    rate *= i
            fine += rate
        fine_message = f"Fine applied: Rs. {fine} for {overdue_days} overdue days."
    
    # Return the book
    books[book_name]['available'] = True
    books[book_name]['issued_to'] = None
    books[book_name]['issue_date'] = None
    books[book_name]['allotted_days'] = None
    
    print(f"'{book_name}' has been returned successfully.")
    print(f"Days passed: {days_passed}, Allotted days: {allotted_days}.")
    print(fine_message)

def library():
    print("Welcome to the Library Management System")
    while True:
        print("\nMenu:")
        print("1. Add Books")
        print("2. Show Available Books")
        print("3. Issue Books")
        print("4. Return Books")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue
        
        if choice == 1:
            add_books()
        elif choice == 2:
            show_books()
        elif choice == 3:
            issue_books()
        elif choice == 4:
            return_books()
        elif choice == 5:
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    library()
