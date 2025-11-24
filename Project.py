def display_menu():
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search for a Contact")
    print("4. Delete a Contact")
    print("5. Exit")


def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    if name in contacts:
        print(f"Contact '{name}' already exists. Try updating instead.")
    else:
        contacts[name] = phone
        print(f"Contact '{name}' added successfully!")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found. Your contact book is empty.")
    else:
        print("\n--- All Contacts ---")
        for name, phone in contacts.items():
            print(f"  {name}: {phone}")


def search_contact(contacts):
    name = input("Enter contact name to search: ").strip()
    if name in contacts:
        print(f"Found: {name} - {contacts[name]}")
    else:
        print(f"Sorry, '{name}' not found in your contacts.")


def delete_contact(contacts):
    name = input("Enter contact name to delete: ").strip()
    if name in contacts:
        confirm = input(f"Are you sure you want to delete '{name}'? (yes/no): ").strip().lower()
        if confirm == 'yes':
            del contacts[name]
            print(f"Contact '{name}' deleted.")
        else:
            print("Deletion cancelled.")
    else:
        print(f"Contact '{name}' not found.")


def main():
    contacts = {}
    print("Welcome to your Contact Book!")
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Thanks for using Contact Book. See you next time!")
            break
        else:
            print("Oops! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()