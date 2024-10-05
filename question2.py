import pandas as pd

def find_minimum_price(file_path, food_items):
    # Load the CSV file
    df = pd.read_csv(file_path)

    # Split the input food items into a list
    food_items = food_items.split()

    # Initialize variables to track the minimum price and corresponding restaurant ID
    min_price = float('inf')
    best_restaurant_id = None

    # Create a dictionary to track food items and their prices for each restaurant
    restaurant_food_prices = {}

    # Iterate through each row in the DataFrame
    for _, row in df.iterrows():
        restaurant_id = row['restaurant_id']
        food_price = row['price']

        # Initialize if the restaurant is not in the dictionary
        if restaurant_id not in restaurant_food_prices:
            restaurant_food_prices[restaurant_id] = {
                'prices': [],
                'food_items_found': set()
            }

        # Check each food item column
        for i in range(1, 6):  # Assuming there are 5 food item columns
            food_item_column = f'food_item_{i}'
            food_item = row[food_item_column]

            # If the food item matches one in the input list, add it to the set
            if food_item in food_items:
                restaurant_food_prices[restaurant_id]['food_items_found'].add(food_item)
                restaurant_food_prices[restaurant_id]['prices'].append(food_price)

    # Now, check which restaurants have all the requested food items
    for restaurant_id, data in restaurant_food_prices.items():
        # Check if all requested food items are found in this restaurant
        if all(item in data['food_items_found'] for item in food_items):
            # Calculate total price for the food items
            total_price = sum(data['prices'])
            print(f"Restaurant {restaurant_id}: Total Price {total_price}, Food Items Found: {data['food_items_found']}")  # Debugging output
            # Ensure we consider the minimum price across valid combinations
            if total_price < min_price:
                min_price = total_price
                best_restaurant_id = restaurant_id

    # Output the result
    if best_restaurant_id is not None:
        return f"{best_restaurant_id}, {min_price:.2f}"
    else:
        return "No matching restaurant found"

# Example usage
file_path = 'data.csv'  # Ensure the path to your CSV file is correct
print(find_minimum_price(file_path, 'burger tofu_log'))  # Expected Output: "7, 10.50"
print(find_minimum_price(file_path, 'chef_salad wine_spritzer'))  # Expected Output: "No matching restaurant found"
print(find_minimum_price(file_path, 'extreme_fajita jalapeno_poppers'))  # Expected Output: "6, 10.50"
