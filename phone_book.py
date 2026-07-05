phone_book = {
    "John": "555-1234",
    "Alice": "555-1234",
    "Bob": "555-2345",
    "Charlie": "555-3456",
    "Diana": "555-4567",
    "Eve": "555-5678"
}


def main_menu():
    print()
    print(
    "Select an action:\n"
    "1. Add a contact\n"
    "2. Remove a contact\n"
    "3. Search for a contact\n"
    "4. View the phone book\n"
    "5. Exit\n"
    )


def add_contact(phone_book):
    contact_name = input("Enter the name of the contact: ")
    contact_number = input(f"Enter the phone number of {contact_name}: ")
    phone_book[contact_name] = contact_number
    print()
    print(f"Contact {contact_name}: {contact_number} has been added")


def remove_contact(phone_book):
    contact_to_be_removed = input("Enter the name of the contact to remove: ")
    if contact_to_be_removed in phone_book:
        del phone_book[contact_to_be_removed]
        print()
        print(f"Contact {contact_to_be_removed} has been removed.")
    else:
        print()
        print("this contact does not exist.")


def search_contact(phone_book):
    searching_for_contact = input("Enter the name of the contact to search for: ")
    print()
    print(f"{searching_for_contact}'s phone number is {phone_book[searching_for_contact]}.")


def sort_copy(copied_phone_book):
    sorted_copied_phone_book = []
    while len(copied_phone_book) > 0:
        smallest_contact = None
        for contact, number in copied_phone_book.items():
            if smallest_contact == None or contact < smallest_contact[0]:
                smallest_contact = contact, number
        sorted_copied_phone_book.append(smallest_contact)
        del copied_phone_book[smallest_contact[0]]
    return sorted_copied_phone_book


def print_sorted_phon_book(sorted_copied_phone_book):
    print()
    for contact, number in sorted_copied_phone_book:
        print(f"- {contact}: {number}")


def view_contact(phone_book):
    copied_phone_book = phone_book.copy()
    sorted_copied_phone_book = sort_copy(copied_phone_book)
    print_sorted_phon_book(sorted_copied_phone_book)


def main():
    print("Welcome to the phone book app!")
    while True:
        main_menu()
        choice_menu = input("Enter your choice (1-5): ")
        print()
        if choice_menu == "1":
            add_contact(phone_book)
        elif choice_menu == "2":
            remove_contact(phone_book)
        elif choice_menu == "3":
            search_contact(phone_book)
        elif choice_menu == "4":
            view_contact(phone_book)
        elif choice_menu == "5":
            print()
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()