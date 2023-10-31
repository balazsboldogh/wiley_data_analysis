import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
data = pd.read_csv('E:/Codebase/src/assignments/autoscout24-germany-dataset.csv')


# _____________________________________________________________________________
# EXAMPLE 1 TOTAL NUMBER OF MANUAL AND AUTOMATIC CARS
# _____________________________________________________________________________


# Count the total number of manual and automatic cars
total_manual_cars = (data['gear'] == 'Manual').sum()
total_automatic_cars = (data['gear'] == 'Automatic').sum()

# Plot manual and automatic cars
plt.figure(figsize=(8, 6))
plt.bar(['Manual', 'Automatic'], [total_manual_cars, total_automatic_cars], color=['blue', 'red'],width=0.4)
plt.title('Total Number of Manual and Automatic Cars')
plt.xlabel('Transmission Type')
plt.ylabel('Count')

plt.show()


# _____________________________________________________________________________
# EXAMPLE 2 MANUAL AND AUTOMATIC CARS BY MANUFACTURER
# _____________________________________________________________________________


# Filter for manual and automatic cars
manual_cars = data[data['gear'] == 'Manual']
automatic_cars = data[data['gear'] == 'Automatic']

# Count the number of manual and automatic cars by manufacturer
manual_counts = manual_cars['make'].value_counts()
automatic_counts = automatic_cars['make'].value_counts()

# Only show manufacturers with over 200 cars for sale
manual_counts_filtered = manual_counts[manual_counts > 200]
automatic_counts_filtered = automatic_counts[automatic_counts > 200]

# Plot manual cars
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
manual_counts_filtered.plot(kind='bar', color='blue')
plt.title('Number of Manual Cars by Manufacturer (Over 200 Cars)')
plt.xlabel('Manufacturer')
plt.ylabel('Count')

# Plot automatic cars
plt.subplot(1, 2, 2)
automatic_counts_filtered.plot(kind='bar', color='red')
plt.title('Number of Automatic Cars by Manufacturer (Over 200 Cars)')
plt.xlabel('Manufacturer')
plt.ylabel('Count')

plt.tight_layout()
plt.show()


# _____________________________________________________________________________
# EXAMPLE 3 MANUAL AND AUTOMATIC CARS BY YEAR
# _____________________________________________________________________________


# Count the number of manual and automatic cars by year
manual_counts_by_year = manual_cars['year'].value_counts().sort_index()
automatic_counts_by_year = automatic_cars['year'].value_counts().sort_index()

# Plot manual and automatic cars by year
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(manual_counts_by_year.index, manual_counts_by_year, marker='o', color='blue')
plt.title('Number of Manual Cars by Year')
plt.xlabel('Year')
plt.ylabel('Count')

plt.subplot(1, 2, 2)
plt.plot(automatic_counts_by_year.index, automatic_counts_by_year, marker='o', color='red')
plt.title('Number of Automatic Cars by Year')
plt.xlabel('Year')
plt.ylabel('Count')

plt.tight_layout()
plt.show()


# _____________________________________________________________________________
# EXAMPLE 4 AVERAGE CAR PRICE BY MANUFACTURER
# _____________________________________________________________________________


# Average car price per manufacturer
average_price_by_manufacturer = data.groupby('make')['price'].mean()

# Count the number of cars by manufacturer
car_counts_by_manufacturer = data['make'].value_counts()

# Filter for manufacturers with more than 200 cars
filtered_manufacturers = car_counts_by_manufacturer[car_counts_by_manufacturer > 200]

# Filter the average prices for the selected manufacturers
average_price_by_manufacturer = average_price_by_manufacturer.loc[filtered_manufacturers.index]

# Sort the data by average price in ascending order
average_price_by_manufacturer = average_price_by_manufacturer.sort_values(ascending=False)

# Create a bar plot for average car price per manufacturer
plt.figure(figsize=(12, 6))
plt.bar(average_price_by_manufacturer.index, average_price_by_manufacturer, color='green')
plt.title('Average Car Price by Manufacturer (Manufacturers with > 200 Cars)')
plt.xlabel('Manufacturer')
plt.ylabel('Average Price')
plt.xticks(rotation=90)  # Rotate x-axis labels for readability

plt.tight_layout()
plt.show()


# _____________________________________________________________________________
# EXAMPLE 5 AVERAGE HORSEPOWER BY MANUFACTURER
# _____________________________________________________________________________


# Average horsepower per manufacturer
average_horsepower_by_manufacturer = data.groupby('make')['hp'].mean()

# Count the number of cars by manufacturer
car_counts_by_manufacturer = data['make'].value_counts()

# Filter for manufacturers with more than 200 cars
filtered_manufacturers = car_counts_by_manufacturer[car_counts_by_manufacturer > 200]

# Filter the average horsepower for the selected manufacturers
average_horsepower_by_manufacturer = average_horsepower_by_manufacturer.loc[filtered_manufacturers.index]

# Sort the data by average horsepower in ascending order
average_horsepower_by_manufacturer = average_horsepower_by_manufacturer.sort_values(ascending=False)

# Create a bar plot for average horsepower per manufacturer
plt.figure(figsize=(12, 6))
plt.bar(average_horsepower_by_manufacturer.index, average_horsepower_by_manufacturer, color='purple')
plt.title('Average Horsepower by Manufacturer (Manufacturers with > 200 Cars)')
plt.xlabel('Manufacturer')
plt.ylabel('Average Horsepower')
plt.xticks(rotation=90)  # Rotate x-axis labels for readability

plt.tight_layout()
plt.show()


# _____________________________________________________________________________
# EXAMPLE 6 MANUFACTURER MARKET SHARE
# _____________________________________________________________________________


# Count the number of cars by manufacturer
car_counts_by_manufacturer = data['make'].value_counts()

# Select the top 10 best selling manufacturers
top_10_manufacturers = car_counts_by_manufacturer.head(10)

# Create a pie chart for the top ten best-selling manufacturers
plt.figure(figsize=(8, 8))
plt.pie(top_10_manufacturers, labels=top_10_manufacturers.index, autopct='%1.1f%%', startangle=140)
plt.title('Top 10 Best Selling Car Manufacturers')

plt.show()


# _____________________________________________________________________________
# EXAMPLE 7 FUEL TYPE MARKET SHARE
# _____________________________________________________________________________


# Count the number of cars by fuel type
fuel_counts = data['fuel'].value_counts()

# Filter fuel types with a distribution above 1%
filtered_fuel_counts = fuel_counts[fuel_counts / fuel_counts.sum() > 0.01]

# Create a pie chart for car fuel types
plt.figure(figsize=(8, 8))
plt.pie(filtered_fuel_counts, labels=filtered_fuel_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Car Fuel Types (Above 1%)')

plt.show()


# _____________________________________________________________________________
# EXAMPLE 8 FUEL TYPE BY YEAR
# _____________________________________________________________________________


# Get the 4 most common fuel types
top_4_fuel_types = data['fuel'].value_counts().index[:4]

# Filter the data to include only the top 4 fuel types
filtered_data = data[data['fuel'].isin(top_4_fuel_types)]

# Pivot table to count the number of cars for each fuel type by year
pivot_table = filtered_data.pivot_table(index='year', columns='fuel', values='mileage', aggfunc='count', fill_value=0)

# Stacked bar chart
pivot_table.plot(kind='bar', stacked=True, figsize=(14, 6))
plt.title('Car Fuel Types by Year (Top 4 Fuel Types)')
plt.xlabel('Year')
plt.ylabel('Number of Cars')
plt.legend(title='Fuel Type', bbox_to_anchor=(0.9, 1), loc='upper left')

plt.xticks(rotation=45)
plt.show()




