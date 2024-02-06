from functools import cache

# Function to calculate the minimum number of scalar multiplications
# required to multiply a chain of matrices with given dimensions
def calculate_min_scalar_multiplications(dimensions: list[int]) -> int:
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

# Test the function with some sample inputs
print(calculate_min_scalar_multiplications([10, 30, 5, 60]))  # Output: 4500
print(calculate_min_scalar_multiplications([40, 20, 30, 10, 30]))  # Output: 26000
print(calculate_min_scalar_multiplications([10, 20, 30, 40, 30]))  # Output: 30000
