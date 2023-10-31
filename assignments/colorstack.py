import pandas as pd
import matplotlib.pyplot as plt

class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        return not bool(self.items)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def empty_stack(self):
        self.items = []

    def __str__(self):
        res = ""
        for item in self.items:
            res += str(item) + " "
        return res[:-1]

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def empty_stack(self):
        self.items = []

# Create a stack to manage colors for stacked bars
color_stack = stack()

# Read dataset
data = pd.read_csv('E:/Codebase/src/assignments/autoscout24-germany-dataset.csv')


# EXAMPLE 8 FUEL TYPE BY YEAR
top_4_fuel_types = data['fuel'].value_counts().index[:4]
filtered_data = data[data['fuel'].isin(top_4_fuel_types)]
pivot_table = filtered_data.pivot_table(index='year', columns='fuel', values='mileage', aggfunc='count', fill_value=0)

# Stacked bar chart
plt.figure(figsize=(14, 6))
for fuel_type in pivot_table.columns:
    color = color_stack.pop() if not color_stack.is_empty() else None
    pivot_table[year].plot(kind='bar', stacked=True, label=fuel_type, color=color)

plt.title('Car Fuel Types by Year (Top 4 Fuel Types)')
plt.xlabel('Year')
plt.ylabel('Number of Cars')
plt.legend(title='Fuel Type', bbox_to_anchor=(0.9, 1), loc='upper left')
plt.xticks(rotation=45)
plt.show()