# Contact Book (Python CLI)

A simple command-line Contact Book application written in Python. Manage your contacts—add, view, search, and delete—right from the terminal!

---

## Features

- Add a new contact (name & phone number)
- View all contacts in a tabular format
- Search for a contact by name
- Delete contacts with confirmation
- User-friendly, interactive menu

---

## How It Works

Contacts are stored in-memory in a Python dictionary during each program run.

---

## Getting Started

### Prerequisites

- Python 3.13

### Installation

Clone the repository and navigate to the folder
https://github.com/pranav25bai11457/Contact-Book-Python-Project.git
cd contact-book


---

## Usage

Run the script in your terminal:
python contact_book.py


Follow the menu prompts:

- 1 – Add Contact
- 2 – View All Contacts
- 3 – Search for a Contact
- 4 – Delete a Contact
- 5 – Exit

Sample excerpt from contact_book.py:
def display_menu():
print("\n--- Contact Book Menu ---")
print("1. Add Contact")
print("2. View Contacts")
print("3. Search Contact")
print("4. Delete Contact")
print("5. Exit")

<img width="1142" height="365" alt="Screenshot 2025-11-23 193646" src="https://github.com/user-attachments/assets/af8adac3-972d-408e-860a-afae21dfb318" />



---

## File Structure

- contact_book.py – All functions and the main loop in one file

---

## Possible Improvements

- Save/load contacts from a file for persistence
- Edit/update existing contacts
- Add extra fields (email, address)
- Input validation (e.g., phone number format)
- Object-oriented design
