"""
Contact Book Manager
---------------------
A simple command-line Contact Book Manager built in Python.
Allows users to add, view, search, update, and delete contacts.
Data is persisted locally in a JSON file (contacts.json).
"""

import json
import os
import re

DATA_FILE = "contacts.json"


class ContactBook:
    def __init__(self, data_file=DATA_FILE):
        self.data_file = data_file
        self.contacts = self.load_contacts()

    # ---------- Data Persistence ----------

    def load_contacts(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                print("Warning: Could not read existing data file. Starting fresh.")
                return []
        return []

    def save_contacts(self):
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(self.contacts, f, indent=4)

    # ---------- Validation ----------

    @staticmethod
    def is_valid_phone(phone):
        return bool(re.fullmatch(r"[0-9+\-\s]{7,15}", phone))

    @staticmethod
    def is_valid_email(email):
        if not email:
            return True  # email is optional
        return bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email))

    # ---------- Core Operations ----------

    def add_contact(self, name, phone, email="", address=""):
        if not name.strip():
            print("Error: Name cannot be empty.")
            return False
        if not self.is_valid_phone(phone):
            print("Error: Invalid phone number format.")
            return False
        if not self.is_valid_email(email):
            print("Error: Invalid email format.")
            return False

        contact = {
            "id": self._next_id(),
            "name": name.strip(),
            "phone": phone.strip(),
            "email": email.strip(),
            "address": address.strip(),
        }
        self.contacts.append(contact)
        self.save_contacts()
        print(f"Contact '{name}' added successfully.")
        return True

    def _next_id(self):
        if not self.contacts:
            return 1
        return max(c["id"] for c in self.contacts) + 1

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        print("\n{:<4} {:<20} {:<15} {:<25} {:<20}".format(
            "ID", "Name", "Phone", "Email", "Address"))
        print("-" * 90)
        for c in self.contacts:
            print("{:<4} {:<20} {:<15} {:<25} {:<20}".format(
                c["id"], c["name"], c["phone"], c["email"], c["address"]))
        print()

    def search_contact(self, keyword):
        keyword = keyword.lower().strip()
        results = [
            c for c in self.contacts
            if keyword in c["name"].lower() or keyword in c["phone"]
        ]
        if not results:
            print("No matching contacts found.")
            return []
        for c in results:
            print(f"[{c['id']}] {c['name']} - {c['phone']} - {c['email']} - {c['address']}")
        return results

    def update_contact(self, contact_id, name=None, phone=None, email=None, address=None):
        contact = self._find_by_id(contact_id)
        if not contact:
            print(f"Error: No contact found with ID {contact_id}.")
            return False

        if name:
            contact["name"] = name.strip()
        if phone:
            if not self.is_valid_phone(phone):
                print("Error: Invalid phone number format.")
                return False
            contact["phone"] = phone.strip()
        if email is not None:
            if not self.is_valid_email(email):
                print("Error: Invalid email format.")
                return False
            contact["email"] = email.strip()
        if address is not None:
            contact["address"] = address.strip()

        self.save_contacts()
        print(f"Contact ID {contact_id} updated successfully.")
        return True

    def delete_contact(self, contact_id):
        contact = self._find_by_id(contact_id)
        if not contact:
            print(f"Error: No contact found with ID {contact_id}.")
            return False
        self.contacts.remove(contact)
        self.save_contacts()
        print(f"Contact ID {contact_id} deleted successfully.")
        return True

    def _find_by_id(self, contact_id):
        for c in self.contacts:
            if c["id"] == contact_id:
                return c
        return None


# ---------- CLI Menu ----------

def print_menu():
    print("\n===== CONTACT BOOK MANAGER =====")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")


def main():
    book = ContactBook()

    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email (optional): ")
            address = input("Address (optional): ")
            book.add_contact(name, phone, email, address)

        elif choice == "2":
            book.view_contacts()

        elif choice == "3":
            keyword = input("Enter name or phone to search: ")
            book.search_contact(keyword)

        elif choice == "4":
            try:
                cid = int(input("Enter contact ID to update: "))
            except ValueError:
                print("Error: ID must be a number.")
                continue
            print("Leave field blank to keep it unchanged.")
            name = input("New name: ") or None
            phone = input("New phone: ") or None
            email = input("New email: ")
            email = email if email != "" else None
            address = input("New address: ")
            address = address if address != "" else None
            book.update_contact(cid, name, phone, email, address)

        elif choice == "5":
            try:
                cid = int(input("Enter contact ID to delete: "))
            except ValueError:
                print("Error: ID must be a number.")
                continue
            confirm = input(f"Are you sure you want to delete contact {cid}? (y/n): ")
            if confirm.lower() == "y":
                book.delete_contact(cid)

        elif choice == "6":
            print("Exiting Contact Book Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 6.")


if __name__ == "__main__":
    main()
