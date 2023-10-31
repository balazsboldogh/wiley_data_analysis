import json
from datetime import datetime
from functools import reduce

# Step 1: Read the entire dataset from a JSON file

def read_json_dataset(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            if not isinstance(data, list):
                raise ValueError("JSON file must contain a list of objects.")
        return data
    except FileNotFoundError:
        raise FileNotFoundError("File not found. Please provide a valid file path.")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format in the provided file.")

# Load the dataset
dataset = read_json_dataset('E:/Codebase/src/assignments/map_reduce/restaurant.json')

# Step 2: Convert timestamps to human-readable dates

def convert_timestamp_to_date(review):
    try:
        timestamp = int(review['timestamp'])
        review['date'] = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')
        return review
    except (KeyError, ValueError):
        raise ValueError("Invalid timestamp in review.")

dataset = list(map(lambda restaurant: {**restaurant, 'reviews': list(map(convert_timestamp_to_date, restaurant['reviews']))}, dataset))

# Step 3: Identify restaurants with at least 5 reviews

def has_at_least_5_reviews(restaurant):
    return len(restaurant['reviews']) >= 5

restaurants_with_5_reviews = list(filter(has_at_least_5_reviews, dataset))

# Step 4: Identify restaurants with at least 5 reviews in the most recent year

MOST_RECENT_YEAR = max(review['date'] for restaurant in dataset for review in restaurant['reviews']).split('-')[0]

def has_at_least_5_reviews_in_recent_year(restaurant):
    reviews_in_recent_year = list(filter(lambda review: review['date'].startswith(MOST_RECENT_YEAR), restaurant['reviews']))
    return len(reviews_in_recent_year) >= 5

restaurants_with_5_reviews_recent_year = list(filter(has_at_least_5_reviews_in_recent_year, dataset))

# Step 5: Compute the average number of reviews per restaurant

average_reviews_per_restaurant = reduce(lambda x, y: x + len(y['reviews']), dataset, 0) / len(dataset)

# Step 6: Identify restaurants with more reviews than the average

def has_more_reviews_than_average(restaurant):
    return len(restaurant['reviews']) > average_reviews_per_restaurant

restaurants_with_more_reviews_than_average = list(filter(has_more_reviews_than_average, dataset))

# Output
print(f"Number of restaurants in the dataset: {len(dataset)}")
print(f"Number of restaurants with at least 5 reviews: {len(restaurants_with_5_reviews)}")
print(f"Number of restaurants with at least 5 reviews in {MOST_RECENT_YEAR}: {len(restaurants_with_5_reviews_recent_year)}")
print(f"Average number of reviews per restaurant: {average_reviews_per_restaurant:.2f}")
print(f"Number of restaurants with more reviews than the average: {len(restaurants_with_more_reviews_than_average)}")
