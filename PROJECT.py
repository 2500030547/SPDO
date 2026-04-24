import os
import pandas as pd
import matplotlib.pyplot as plt

FILE_NAME = "records.txt"

class Record:
    def __init__(self, name, phone, email, category):
        self.name = name
        self.phone = phone
        self.email = email
        self.category = category

    def __str__(self):
        return f"{self.name},{self.phone},{self.email},{self.category}"

def load_records():
    records = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, phone, email, category = line.strip().split(",")
                records.append(Record(name, phone, email, category))
    return records

def save_records(records):
    with open(FILE_NAME, "w") as file:
        for record in records:
            file.write(str(record) + "\n")

def add_record(records):
    try:
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        category = input("Enter Category (Friend/Family/Work): ")
        records.append(Record(name, phone, email, category))
        print("Record Added!")
    except:
        print("Error adding record")

def view_records(records):
    if not records:
        print("No records found")
        return
    print("\n--- Records ---")
    for i, r in enumerate(records):
        print(f"{i + 1}. {r.name} | {r.phone} | {r.email} | {r.category}")

def search_record(records):
    key = input("Enter name to search: ").lower()
    found = False
    for r in records:
        if key in r.name.lower():
            print(r.name, r.phone, r.email, r.category)
            found = True
    if not found:
        print("Record not found")

def delete_record(records):
    view_records(records)
    try:
        index = int(input("Enter record number to delete: ")) - 1
        if 0 <= index < len(records):
            records.pop(index)
            print("Record deleted")
        else:
            print("Invalid index")
    except:
        print("Error deleting record")

def update_record(records):
    view_records(records)
    try:
        index = int(input("Enter record number to update: ")) - 1
        if 0 <= index < len(records):
            records[index].name = input("New Name: ")
            records[index].phone = input("New Phone: ")
            records[index].email = input("New Email: ")
            records[index].category = input("New Category: ")
            print("Record updated")
        else:
            print("Invalid index")
    except:
        print("Error updating record")

def analyze_data():
    try:
        df = pd.read_csv(FILE_NAME, names=["Name", "Phone", "Email", "Category"])
        print("\nCategory Count:")
        print(df["Category"].value_counts())
    except:
        print("No data available")

def show_chart():
    try:
        df = pd.read_csv(FILE_NAME, names=["Name", "Phone", "Email", "Category"])
        df["Category"].value_counts().plot(kind="bar")
        plt.title("Category Distribution")
        plt.xlabel("Category")
        plt.ylabel("Count")
        plt.show()
    except:
        print("No data to visualize")

def main():
    records = load_records()
    while True:
        print("\n===== SPDO MENU =====")
        print("1. Add Record")
        print("2. View Records")
        print("3. Search Record")
        print("4. Delete Record")
        print("5. Update Record")
        print("6. Analyze Data")
        print("7. Show Chart")
        print("8. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_record(records)
        elif choice == "2":
            view_records(records)
        elif choice == "3":
            search_record(records)
        elif choice == "4":
            delete_record(records)
        elif choice == "5":
            update_record(records)
        elif choice == "6":
            analyze_data()
        elif choice == "7":
            show_chart()
        elif choice == "8":
            save_records(records)
            print("Data Saved. Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()