# Fractional Knapsack Problem

# Thief can take fractions of items (Float?)
# Exhibits optimal substructure property
# Most valuable load weighs at most W pounds
# If item j is removed then most valuable load has at most weight W - w_j
# That thief can take of set size n - 1
# If we remove weight w of one item j from optimal load, the most valuable load is at most W - w
# That thief can take of set size n - 1 plus w_j - w pounds of item j

# Greedy algorithm
# Compute value per pound v_i / w_i for each item
# Thief takes as much of the item with the highest value per pound as possible
# If no more of that item can be taken, move on to the next highest value per pound item
# Repeat until the most valuable load is full


# function needs a map of items with their values and weights
# dict = {item1: (value1, weight1), item2: (value2, weight2), ...}
# function needs a weight limit
# function returns the maximum value of items that can be taken
def fractional_knapsack_problem(dict_items: dict, weight_limit: int) -> float:
    # dict_vpp = {item1: value_per_pound1, item2: value_per_pound2, ...}
    dict_vpp = {}
    # Calculate the value per pound for each item and append to dict_vpp
    for item, (value, weight) in dict_items.items():
        dict_vpp[item] = value / weight

    # Sort the items by value per pound in descending order
    sorted_items = sorted(dict_vpp, key=dict_vpp.get, reverse=True)

    # Take as much of the item with the highest value per pound as possible and add to the most valuable load
    # If no more of that item can be taken, move on to the next highest value per pound item
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
print(fractional_knapsack_problem({'A': (60, 10), 'B': (100, 20), 'C': (120, 30)}, 50))  # Output: 240.0
print(fractional_knapsack_problem({'A': (60, 10), 'B': (100, 20), 'C': (120, 30)}, 30))  # Output: 180.0
print(fractional_knapsack_problem({'A': (60, 10), 'B': (100, 20), 'C': (120, 30)}, 20))  # Output: 100.0


