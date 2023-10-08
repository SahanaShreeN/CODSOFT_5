import sqlite3

class ContactManager:
    def __init__(self):
        self.connection = sqlite3.connect('contacts.db')
        self.cursor = self.connection.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            email TEXT NOT NULL,
            address TEXT NOT NULL
        )''')

    def add_contact(self, name, phone_number, email, address):
        self.cursor.execute('''INSERT INTO contacts (name, phone_number, email, address) VALUES (?, ?, ?, ?)''', (name, phone_number, email, address))
        self.connection.commit()

    def view_contact_list(self):
        self.cursor.execute('SELECT name, phone_number FROM contacts')
        contacts = self.cursor.fetchall()

        return contacts

    def search_contact(self, name_or_phone_number):
        self.cursor.execute('SELECT name, phone_number FROM contacts WHERE name LIKE ? OR phone_number LIKE ?', ('%' + name_or_phone_number + '%', '%' + name_or_phone_number + '%'))
        contacts = self.cursor.fetchall()

        return contacts

    def update_contact(self, id, name, phone_number, email, address):
        self.cursor.execute('''UPDATE contacts SET name = ?, phone_number = ?, email = ?, address = ? WHERE id = ?''', (name, phone_number, email, address, id))
        self.connection.commit()

    def delete_contact(self, id):
        self.cursor.execute('DELETE FROM contacts WHERE id = ?', (id,))
        self.connection.commit()

def main():
    contact_manager = ContactManager()

    while True:
        print('Contact Management System')
        print('1. Add contact')
        print('2. View contact list')
        print('3. Search contact')
        print('4. Update contact')
        print('5. Delete contact')
        print('6. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            name = input('Enter contact name: ')
            phone_number = input('Enter contact phone number: ')
            email = input('Enter contact email: ')
            address = input('Enter contact address: ')

            contact_manager.add_contact(name, phone_number, email, address)

            print('Contact added successfully.')

        elif choice == '2':
            contacts = contact_manager.view_contact_list()

            print('Contact List:')
            for contact in contacts:
                print('Name:', contact[0])
                print('Phone number:', contact[1])

        elif choice == '3':
            name_or_phone_number = input('Enter contact name or phone number to search: ')

            contacts = contact_manager.search_contact(name_or_phone_number)

            print('Search results:')
            for contact in contacts:
                print('Name:', contact[0])
                print('Phone number:', contact[1])

        elif choice == '4':
            id = int(input('Enter contact ID to update: '))
            name = input('Enter contact name: ')
            phone_number = input('Enter contact phone number: ')
            email = input('Enter contact email: ')
            address = input('Enter contact address: ')

            contact_manager.update_contact(id, name, phone_number, email, address)

            print('Contact updated successfully.')

        elif choice == '5':
            id = int(input('Enter contact ID to delete: '))

            contact_manager.delete_contact(id)

            print('Contact deleted successfully.')

        elif choice == '6':
            break

        else:
            print('Invalid choice.')

if __name__ == '__main__':
    main()