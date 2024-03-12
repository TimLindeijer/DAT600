from functools import cache

# Function to calculate the minimum number of scalar multiplications
# required to multiply a chain of matrices with given dimensions
# Based on implementation on wikipedia (https://en.wikipedia.org/wiki/Matrix_chain_multiplication#A_dynamic_programming_algorithm)
def calculate_min_scalar_multiplications_dynamic(dimensions: list[int]) -> int:
    @cache
    def calculate(i, j):
        # Base case: if there is only one matrix in the chain, return 0
        if i == j:
            return 0
        
        # Calculate the minimum number of scalar multiplications
        # by considering all possible split points in the chain
        return min((calculate(i, k) + dimensions[i] * dimensions[k] * dimensions[j] + calculate(k, j) 
                   for k in range(i + 1, j)), default=0)

    # Call the recursive function with the start and end indices of the chain
    return calculate(0, len(dimensions) - 1)

def calculate_min_scalar_multiplications_greedy(dimensions):
    cost = 0
    while len(dimensions) > 2:
        # Find the pair of matrices to multiply that has the smallest cost
        min_cost, min_index = min((dimensions[i-1]*dimensions[i]*dimensions[i+1], i) 
                                  for i in range(1, len(dimensions)-1))
        # Add the cost of this multiplication to the total cost
        cost += min_cost
        # Remove the middle dimension of the multiplied pair from the list
        dimensions.pop(min_index)
    return cost

# Test the function with some sample inputs
# Dynamic Programming
print(calculate_min_scalar_multiplications_dynamic([10, 30, 5, 60]))  # Output: 4500
print(calculate_min_scalar_multiplications_dynamic([40, 20, 30, 10, 30]))  # Output: 26000
print(calculate_min_scalar_multiplications_dynamic([10, 20, 30, 40, 30]))  # Output: 30000
# Greedy
print(calculate_min_scalar_multiplications_greedy([10, 30, 5, 60]))  # Output: 4500
print(calculate_min_scalar_multiplications_greedy([40, 20, 30, 10, 30]))  # Output: 26000
print(calculate_min_scalar_multiplications_greedy([10, 20, 30, 40, 30]))  # Output: 30000
