class Contact:
    def __init__(self, name, phone, email, address): 
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):  
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f"Contact for {name} added successfully.\n")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.\n")
        else:
            print("Contact List:")
            for idx, contact in enumerate(self.contacts, 1):
                print(f"{idx}. {contact.name} - {contact.phone}")
            print()

    def search_contact(self, search_term):
        found = False
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
                found = True
        if not found:
            print("No matching contact found.\n")

    def update_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(f"Updating contact for {contact.name}. Leave blank if no change.")
                new_phone = input(f"New phone number (current: {contact.phone}): ")
                new_email = input(f"New email (current: {contact.email}): ")
                new_address = input(f"New address (current: {contact.address}): ")

                contact.phone = new_phone if new_phone else contact.phone
                contact.email = new_email if new_email else contact.email
                contact.address = new_address if new_address else contact.address

                print(f"Contact for {contact.name} updated.\n")
                return
        print(f"Contact with name {name} not found.\n")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact for {name} deleted.\n")
                return
        print(f"Contact with name {name} not found.\n")

def display_menu():
    print("Contact Book Details:")
    print("1. Add Contact :")
    print("2. View Contact Details :")
    print("3. Search Contact :")
    print("4. Update Contact :")
    print("5. Delete Contact :")
    print("6. Exit")

def main():
    contact_book = ContactBook()

    while True:
        display_menu()
        choice = input("Choose an option from (1-6): ")

        if choice == '1':
            name = input("Enter name : ")
            phone = input("Enter phone number : ")
            email = input("Enter email : ")
            address = input("Enter address : ")
            contact_book.add_contact(name, phone, email, address)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            contact_book.update_contact(name)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting the Contact Book. Goodbye!")
            break

        else:
            print("Invalid option. Please choose again.\n")

if __name__ == "__main__":  
    main()
