# suggestions.py

from utils import load_data

# Simple AI-like suggestion system
def give_suggestion(file):
    data = load_data(file)

    if not data:
        print("No data available.")
        return

    total = sum(entry["amount"] for entry in data)
    moods = [entry["mood"] for entry in data]

    # Basic logic
    if total > 5000:
        print("⚠️ You are spending a lot! Try to save more.")
    
    if moods.count("sad") > moods.count("happy"):
        print("💡 You seem stressed. Take a break or go out!")

    if moods.count("happy") > moods.count("sad"):
        print("😄 Great! Keep maintaining your lifestyle.")