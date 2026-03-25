# analytics.py

import matplotlib.pyplot as plt
from utils import load_data

# Function to show summary graph
def show_summary(file):
    data = load_data(file)

    if not data:
        print("No data to analyze.")
        return

    categories = {}
    
    # Calculate total per category
    for entry in data:
        cat = entry["category"]
        categories[cat] = categories.get(cat, 0) + entry["amount"]

    # Prepare data for graph
    labels = list(categories.keys())
    values = list(categories.values())

    # Plot graph
    plt.bar(labels, values)
    plt.title("Expense Summary")
    plt.xlabel("Category")
    plt.ylabel("Amount")

    plt.show()