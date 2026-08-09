# Contact Book Manager

A simple command-line **Contact Book Manager** built in Python. It allows users to add, view, search, update, and delete contacts, with data stored persistently in a local JSON file.

## Features

- Add new contacts (name, phone, email, address)
- View all saved contacts in a formatted table
- Search contacts by name or phone number
- Update existing contact details
- Delete a contact by ID
- Input validation for phone numbers and email addresses
- Data persistence using `contacts.json` (auto-created on first run)

## Requirements

- Python 3.7+
- No external dependencies (uses only the Python standard library)

## How to Run

```bash
python contact_book.py
```

Follow the on-screen menu to add, view, search, update, or delete contacts.

## Running Tests

```bash
python -m unittest test_contact_book.py
```

## Project Structure

```
contact_book_manager/
├── contact_book.py       # Main application logic and CLI
├── test_contact_book.py  # Unit tests
├── contacts.json         # Auto-generated data file (created on first run)
└── README.md
```

## Example Usage

```
===== CONTACT BOOK MANAGER =====
1. Add Contact
2. View All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice (1-6): 1
Name: John Doe
Phone: 9876543210
Email (optional): john@example.com
Address (optional): Delhi, India
Contact 'John Doe' added successfully.
```

## Notes

- Data is stored locally in `contacts.json` in the same directory as the script.
- Deleting the JSON file will reset the contact book.
