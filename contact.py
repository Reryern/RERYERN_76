contacts = {
    "name":{"Ryan":{"phone": "0700206427", "email": "ryan@gmail.com", "address": "kibuli"}},
    "name":{"Khassim":{"phone": "0704707970", "email": "khassim@gmail.com", "address": "kawempe"}},
    "name":{"Ali":{"phone": "0772363835", "email": "ali@gmail.com", "address": "kabalagala"}},
    "name":{"Faizan":{"phone": "0776278155", "email": "faizan@gmail.com", "address": "muyenga"}}
}

def search_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None

def view_contact():
    contact_name = input("Enter the name to search for: ").strip()
    name = search_contact(name)
    if name:
        print("\nContact found")
        print(name)

        

'''def main():
    while True:
        print("\nContact book")
        print("1. Search for a contact")
        print("2. View contacts")
        print("3. Add a contact")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            search_contact()'''
