import json
from datetime import datetime
import os

FILE = "curator_data.json"

# ------------------ Load & Save ------------------
def load_data():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


# ------------------ Auto Categorization ------------------
def auto_category(text):
    text = text.lower()
    if "python" in text or "code" in text:
        return "Programming"
    elif "money" in text or "expense" in text:
        return "Finance"
    elif "study" in text or "exam" in text:
        return "Education"
    elif "idea" in text:
        return "Ideas"
    else:
        return "General"


# ------------------ Add Entry ------------------
def add_entry(data):
    user = input("Enter your name: ")
    content = input("Enter your note/link/idea: ")

    category = auto_category(content)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    entry = {
        "user": user,
        "content": content,
        "category": category,
        "time": timestamp
    }

    data.append(entry)
    save_data(data)

    print(f"\n✅ Entry added under category: {category}\n")


# ------------------ View Entries ------------------
def view_entries(data):
    if not data:
        print("No entries found.\n")
        return

    print("\n📚 All Entries:\n")
    for i, entry in enumerate(data, 1):
        print(f"{i}. [{entry['time']}] ({entry['user']})")
        print(f"   → {entry['content']}")
        print(f"   📂 Category: {entry['category']}\n")


# ------------------ Search ------------------
def search_entries(data):
    keyword = input("Enter keyword to search: ").lower()

    results = [e for e in data if keyword in e["content"].lower()]

    if not results:
        print("❌ No matching entries.\n")
        return

    print("\n🔍 Search Results:\n")
    for entry in results:
        print(f"[{entry['time']}] ({entry['user']})")
        print(f"→ {entry['content']}")
        print(f"📂 {entry['category']}\n")


# ------------------ Filter by Category ------------------
def filter_category(data):
    cat = input("Enter category: ").capitalize()

    results = [e for e in data if e["category"] == cat]

    if not results:
        print("❌ No entries found.\n")
        return

    print(f"\n📂 {cat} Entries:\n")
    for entry in results:
        print(f"[{entry['time']}] {entry['content']}\n")


# ------------------ Insights ------------------
def show_insights(data):
    if not data:
        print("No data for insights.\n")
        return

    category_count = {}

    for entry in data:
        cat = entry["category"]
        category_count[cat] = category_count.get(cat, 0) + 1

    print("\n📊 Insights:\n")
    for cat, count in category_count.items():
        print(f"{cat}: {count} entries")

    most_used = max(category_count, key=category_count.get)
    print(f"\n🔥 Most used category: {most_used}\n")


# ------------------ Delete Entry ------------------
def delete_entry(data):
    view_entries(data)
    try:
        index = int(input("Enter entry number to delete: ")) - 1
        removed = data.pop(index)
        save_data(data)
        print("🗑️ Entry deleted!\n")
    except:
        print("❌ Invalid input.\n")


# ------------------ Export CSV ------------------
def export_csv(data):
    with open("curator_export.csv", "w") as f:
        f.write("User,Time,Category,Content\n")
        for e in data:
            f.write(f"{e['user']},{e['time']},{e['category']},{e['content']}\n")

    print("📁 Exported to curator_export.csv\n")


# ------------------ Menu ------------------
def menu():
    data = load_data()

    while True:
        print("====== 🧠 THE CURATOR ======")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Search")
        print("4. Filter by Category")
        print("5. Insights")
        print("6. Delete Entry")
        print("7. Export CSV")
        print("8. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_entry(data)
        elif choice == "2":
            view_entries(data)
        elif choice == "3":
            search_entries(data)
        elif choice == "4":
            filter_category(data)
        elif choice == "5":
            show_insights(data)
        elif choice == "6":
            delete_entry(data)
        elif choice == "7":
            export_csv(data)
        elif choice == "8":
            print("👋 Goodbye, Curator!")
            break
        else:
            print("❌ Invalid choice\n")


# ------------------ Run ------------------
if __name__ == "__main__":
    menu()