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


def check_number_valid(contact_number):
    if contact_number.count("-") == 1:
        if "+" not in contact_number or contact_number.count("+") == 1 and "+" in contact_number[0]:
            cleared_contact_number = contact_number.replace("+", "").replace("-", "")
            if cleared_contact_number.isdigit():
                if 5 < len(cleared_contact_number) < 12:
                    return True
    print(f"{contact_number} is not a valid phone number. It should contain only digits, one optional hyphen (-), or a plus sign (+) at the start. It must contain 6 to 11 digits.")
    return False


def add_contact(phone_book):
    number_valid = False
    contact_name = input("Enter the name of the contact: ").strip().lower().capitalize()
    while number_valid == False:
        contact_number = input(f"Enter the phone number of {contact_name}: ").strip()
        number_valid = check_number_valid(contact_number)
        if number_valid == True:
            phone_book[contact_name] = contact_number
            print()
            print(f"Contact {contact_name}: {contact_number} has been added")


def remove_contact(phone_book):
    contact_to_be_removed = input("Enter the name of the contact to remove: ").strip().lower().capitalize()
    if contact_to_be_removed in phone_book:
        del phone_book[contact_to_be_removed]
        print()
        print(f"Contact {contact_to_be_removed} has been removed.")
    else:
        print()
        print("this contact does not exist.")


def search_contact(phone_book):
    searching_for_contact = input("Enter the name of the contact to search for: ").strip().lower().capitalize()
    print()
    if searching_for_contact in phone_book:
        print(f"{searching_for_contact}'s phone number is {phone_book[searching_for_contact]}.")
    else:
        print(f"{searching_for_contact} does not exist.")


def sort_copy(copied_phone_book):
    sorted_copied_phone_book = []
    while len(copied_phone_book) > 0:
        smallest_contact = None
        for contact, number in copied_phone_book.items():
            if smallest_contact is None or contact < smallest_contact[0]:
                smallest_contact = contact, number
        sorted_copied_phone_book.append(smallest_contact)
        del copied_phone_book[smallest_contact[0]]
    return sorted_copied_phone_book


def print_sorted_phone_book(sorted_copied_phone_book):
    print()
    for contact, number in sorted_copied_phone_book:
        print(f"- {contact}: {number}")


def view_contact(phone_book):
    copied_phone_book = phone_book.copy()
    sorted_copied_phone_book = sort_copy(copied_phone_book)
    print_sorted_phone_book(sorted_copied_phone_book)


def main():
    print("Welcome to the phone book app!")
    while True:
        main_menu()
        choice_menu = input("Enter your choice (1-5): ").strip()
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
        else:
            print(f"{choice_menu} is not a valid choice. Please select a number between 1 and 5.")


if __name__ == "__main__":
    main()