import json
import os

FILE_NAME = "contacts.json"

# Load contacts
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        contacts = json.load(file)
else:
    contacts = {}

def save_contacts():
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

while True:
    print("\n" + "=" * 40)
    print("         CONTACT BOOK")
    print("=" * 40)
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Contact Summary")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        name = input("Enter Name: ")

        if name in contacts:
            print("❌ Contact already exists.")
        else:
            phone = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")

            contacts[name] = {
                "Phone": phone,
                "Email": email,
                "Address": address
            }

            save_contacts()
            print("✅ Contact added successfully!")

    elif choice == "2":
        if not contacts:
            print("📒 No contacts available.")
        else:
            print("\n===== CONTACT LIST =====")
            for name, details in contacts.items():
                print(f"\n👤 Name    : {name}")
                print(f"📞 Phone   : {details['Phone']}")
                print(f"📧 Email   : {details['Email']}")
                print(f"🏠 Address : {details['Address']}")

    elif choice == "3":
        search = input("Enter contact name: ")

        if search in contacts:
            details = contacts[search]
            print(f"\n👤 Name    : {search}")
            print(f"📞 Phone   : {details['Phone']}")
            print(f"📧 Email   : {details['Email']}")
            print(f"🏠 Address : {details['Address']}")
        else:
            print("❌ Contact not found.")

    elif choice == "4":
        name = input("Enter contact name to update: ")

        if name in contacts:
            phone = input("New Phone: ")
            email = input("New Email: ")
            address = input("New Address: ")

            contacts[name] = {
                "Phone": phone,
                "Email": email,
                "Address": address
            }

            save_contacts()
            print("✅ Contact updated successfully!")
        else:
            print("❌ Contact not found.")

    elif choice == "5":
        name = input("Enter contact name to delete: ")

        if name in contacts:
            del contacts[name]
            save_contacts()
            print("🗑️ Contact deleted successfully!")
        else:
            print("❌ Contact not found.")

    elif choice == "6":
        print("\n===== CONTACT SUMMARY =====")
        print(f"📒 Total Contacts : {len(contacts)}")

    elif choice == "7":
        print("👋 Thank you for using Contact Book!")
        break

    else:
        print("❌ Invalid choice! Please enter a number between 1 and 7.")
