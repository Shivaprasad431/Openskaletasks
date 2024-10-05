import pandas as pd
import itertools

def find_minimum_price(file_path, food_items):
    # Load the CSV file
    df = pd.read_csv(file_path)

    # Split the input food items into a list
    food_items = food_items.split()

    # Initialize variables to track the minimum price and corresponding restaurant ID
    min_price = float('inf')
    best_restaurant_id = None

    # Create a dictionary to track food item prices by restaurant
    restaurant_food_prices = {}

    # Iterate through each row in the DataFrame
    for _, row in df.iterrows():
        restaurant_id = row['restaurant_id']
        food_price = row['price']

        # Initialize if the restaurant is not in the dictionary
        if restaurant_id not in restaurant_food_prices:
            restaurant_food_prices[restaurant_id] = {
                'rows': [],
                'food_item_prices': {}
            }

        # Store the row for processing later
        restaurant_food_prices[restaurant_id]['rows'].append(row)

        # Check each food item column
        for i in range(1, 6):  # Assuming there are 5 food item columns
            food_item_column = f'food_item_{i}'
            food_item = row[food_item_column]

            # If the food item matches one in the input list, store its price
            if food_item in food_items:
                restaurant_food_prices[restaurant_id]['food_item_prices'][food_item] = food_price

    # Now, check which restaurants have the requested food items
    for restaurant_id, data in restaurant_food_prices.items():
        total_prices = []  # List to hold possible total prices

        # Check for same row prices
        for row in data['rows']:
            found_items = set()
            row_price = 0

            # Calculate the total price if the food items are found in the same row
            for i in range(1, 6):
                food_item_column = f'food_item_{i}'
                food_item = row[food_item_column]

                if food_item in food_items:
                    found_items.add(food_item)
                    row_price += row['price']

            # If all requested food items are found in this row, add to total prices
            if found_items.issuperset(food_items):
                total_prices.append(row_price)

        # Check for different rows prices
        # Create combinations of prices for the required food items across different rows
        food_item_indices = {item: [] for item in food_items}

        # Populate the indices for each food item
        for row in data['rows']:
            for item in food_items:
                if item in row.values:
                    food_item_indices[item].append(row)

        # Now create combinations of prices
        if len(food_items) > 1:
            for combination in itertools.product(*[food_item_indices[item] for item in food_items]):
                # Check if the combination is from the same restaurant
                if len(set(r['restaurant_id'] for r in combination)) == 1:
                    total_price = sum(r['price'] for r in combination)
                    total_prices.append(total_price)

        # Find the minimum price for this restaurant if there are any valid total prices
        if total_prices:
            min_restaurant_price = min(total_prices)
            if min_restaurant_price < min_price:
                min_price = min_restaurant_price
                best_restaurant_id = restaurant_id

    # Output the result
    if best_restaurant_id is not None:
        return f"{best_restaurant_id}, {min_price:.2f}"
    else:
        return "No matching restaurant found"

# Main execution
if __name__ == "__main__":
  file_path = 'data.csv'  # Ensure the path to your CSV file is correct
  user_input = input("Enter food items separated by spaces: ")
  result = find_minimum_price(file_path, user_input)
  print(result)