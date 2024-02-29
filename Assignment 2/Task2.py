import random

# 0-1 Knapsack Problem
# The 0-1 knapsack problem is the following. A thief robbing a store wants to
# take the most valuable load that can be carried in a knapsack capable of carrying
# at most W kgs of loot. The thief can choose to take any subset of n items in
# the store. The ith item is worth vi dollars and weighs wi kgs, where vi and wi
# are integers. Which items should the thief take? (We call this the 0-1 knapsack
# problem because for each item, the thief must either take it or leave it behind. The
# thief cannot take a fractional amount of an item or take an item more than once.)

def zero_one_knapsack_problem(dict_items: dict, weight_limit: int) -> int:
    # dict_vpkg = {item1: value_per_kg1, item2: value_per_kg2, ...}
    dict_vpkg = {}
    # Calculate the value per kg for each item and append to dict_vpkg
    for item, (value, weight) in dict_items.items():
        dict_vpkg[item] = value / weight

    # Sort the items by value per kg in descending order
    sorted_items = sorted(dict_vpkg, key=dict_vpkg.get, reverse=True)

    # Take as much of the item with the highest value per kg as possible and add to the most valuable load
    # If no more of that item can be taken, move on to the next highest value per kg item
    # Repeat until the most valuable load is full
    most_valuable_load = 0
    for item in sorted_items:
        value, weight = dict_items[item]
        if weight_limit >= weight:
            most_valuable_load += value
            weight_limit -= weight
        elif weight_limit == 0:
            break

    return most_valuable_load

# Fractional Knapsack Problem

# Thief can take fractions of items (Float?)
# Exhibits optimal substructure property
# Most valuable load weighs at most W kgs
# If item j is removed then most valuable load has at most weight W - w_j
# That thief can take of set size n - 1
# If we remove weight w of one item j from optimal load, the most valuable load is at most W - w
# That thief can take of set size n - 1 plus w_j - w kgs of item j

# Greedy algorithm
# Compute value per kg v_i / w_i for each item
# Thief takes as much of the item with the highest value per kg as possible
# If no more of that item can be taken, move on to the next highest value per kg item
# Repeat until the most valuable load is full


# function needs a map of items with their values and weights
# dict = {item1: (value1, weight1), item2: (value2, weight2), ...}
# function needs a weight limit
# function returns the maximum value of items that can be taken
def fractional_knapsack_problem(dict_items: dict, weight_limit: int) -> float:
    # dict_vpkg = {item1: value_per_kg1, item2: value_per_kg2, ...}
    dict_vpkg = {}
    # Calculate the value per kg for each item and append to dict_vpkg
    for item, (value, weight) in dict_items.items():
        dict_vpkg[item] = value / weight

    # Sort the items by value per kg in descending order
    sorted_items = sorted(dict_vpkg, key=dict_vpkg.get, reverse=True)

    # Take as much of the item with the highest value per kg as possible and add to the most valuable load
    # If no more of that item can be taken, move on to the next highest value per kg item
    # Repeat until the most valuable load is full
    most_valuable_load = 0
    for item in sorted_items:
        value, weight = dict_items[item]
        if weight_limit >= weight:
            most_valuable_load += value
            weight_limit -= weight
        else:
            most_valuable_load += value * (weight_limit / weight)
            break

    return most_valuable_load


# Test the function with some sample inputs
# Make an automation of the test cases
def generate_knapsack_problem(num_items, max_weight, max_value, max_capacity):
    items = {}
    for i in range(1, num_items + 1):
        weight = random.randint(1, max_weight)
        value = random.randint(1, max_value)
        items[f'item{i}'] = (value, weight)
    capacity = random.randint(num_items, max_capacity)
    return items, capacity

# Test 1
items1, capacity1 = generate_knapsack_problem(10, 100, 100, 1000)
print(f"Items: {items1}\nCapacity: {capacity1}")
print(f"0-1 Knapsack Problem: {zero_one_knapsack_problem(items1, capacity1)} is the most value to gain for the weight capacity.")
print(f"Fractional Knapsack Problem: {fractional_knapsack_problem(items1, capacity1)} is the most value to gain for the weight capacity")

# Test 2
items2, capacity2 = generate_knapsack_problem(10, 100, 100, 1000)
print(f"Items: {items2}\nCapacity: {capacity2}")
print(f"0-1 Knapsack Problem: {zero_one_knapsack_problem(items2, capacity2)} is the most value to gain for the weight capacity")
print(f"Fractional Knapsack Problem: {fractional_knapsack_problem(items2, capacity2)} is the most value to gain for the weight capacity")

# Test3
items3, capacity3 = generate_knapsack_problem(10, 100, 100, 1000)
print(f"Items: {items3}\nCapacity: {capacity3}")
print(f"0-1 Knapsack Problem: {zero_one_knapsack_problem(items3, capacity3)} is the most value to gain for the weight capacity")
print(f"Fractional Knapsack Problem: {fractional_knapsack_problem(items3, capacity3)} is the most value to gain for the weight capacity")


